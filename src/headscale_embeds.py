from typing import List

import discord

from src.headscale import Route
from src.constants import EMOJI_ADVERTISED, EMOJI_FAILURE, EMOJI_NOT_ADVERTISED, EMOJI_WARNING, EMOJI_SUCCESS, EMOJI_ID


class RoutesEmbed(discord.Embed):
    def __init__(self, routes: List[Route], **kwargs):
        super().__init__(**kwargs)
        self.title = "🛣️ Routes List"
        self.description = "📋 Displaying all available routes"
        self.color = discord.Color.blurple()

        # Group routes by node
        nodes = {}

        for route in routes:
            if route.node not in nodes:
                nodes[route.node] = []
            nodes[route.node].append(route)

        for node in nodes:
            # Group routes by prefix
            prefixes = {}
            for route in nodes[node]:
                if route.prefix not in prefixes:
                    prefixes[route.prefix] = route
                elif route.enabled:
                    prefixes[route.prefix] = route

            status = EMOJI_SUCCESS if all(route.enabled for route in prefixes.values()) else (EMOJI_WARNING if any(route.enabled for route in prefixes.values()) else EMOJI_FAILURE)

            self.add_field(
                name=f"{status} {node}",
                value="\n".join(f"{EMOJI_ADVERTISED if route.advertised else EMOJI_NOT_ADVERTISED}{EMOJI_SUCCESS if route.enabled else EMOJI_FAILURE} {route.prefix}" for route in prefixes.values()),
                inline=False
            )

class RouteEmbed(discord.Embed):
    def __init__(self, routes: List[Route], node: str, **kwargs):
        super().__init__(**kwargs)
        self.title = f"🛣️ Routes for {node}"
        self.description = f"📋 Displaying all routes for node: {node}"
        self.color = discord.Color.blurple()

        for route in routes:
            self.add_field(
                name=f"▶ {route.prefix}",
                value=f"{EMOJI_ID + ' ' + route.route_id}\n{(EMOJI_SUCCESS + ' Enabled') if route.enabled else (EMOJI_FAILURE + ' Disabled')}\n{(EMOJI_ADVERTISED + ' Advertised') if route.advertised else (EMOJI_NOT_ADVERTISED + ' Not Advertised')}",
                inline=False
            )


class ErrorEmbed(discord.Embed):
    def __init__(self, error: str, **kwargs):
        super().__init__(**kwargs)
        self.title = f"{EMOJI_FAILURE} Error"
        self.description = error
        self.color = discord.Color.red()
