import discord
from discord import app_commands
import requests
from src.config import DISCORD_BOT_TOKEN
from src.headscale import get_routes, HeadscaleError
from src.headscale_embeds import RouteEmbed, RoutesEmbed, ErrorEmbed

bot = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(bot)


@tree.command(name="routes", description="List all available routes")
async def routes(interaction: discord.Interaction):
    try:
        routes = get_routes()
        embed = RoutesEmbed(routes)
        await interaction.response.send_message(embed=embed)
    except HeadscaleError as e:
        await interaction.response.send_message(embed=ErrorEmbed(str(e)))

@tree.command(name="route", description="List all routes for a specific node")
async def route(interaction: discord.Interaction, node: str):
    try:
        routes = get_routes()
        embed = RouteEmbed([route for route in routes if route.node == node], node)
        await interaction.response.send_message(embed=embed)
    except HeadscaleError as e:
        await interaction.response.send_message(embed=ErrorEmbed(str(e)))


@bot.event
async def on_ready():
    await tree.sync()
    print("Ready!")

@bot.event
async def on_guild_join(guild):
    await tree.sync(guild=guild)
    print(f"Synced commands to guild: {guild.name}")


if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
