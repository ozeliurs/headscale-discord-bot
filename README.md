# Headscale Discord Bot

[![Quality Gate Status](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=alert_status&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)
[![Maintainability Rating](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=sqale_rating&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)
[![Reliability Rating](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=reliability_rating&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)
[![Security Rating](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=security_rating&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)

[![Coverage](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=coverage&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)
[![Technical Debt](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=sqale_index&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)
[![Lines of Code](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=ncloc&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)
[![Duplicated Lines (%)](https://sonarqube.devops-tools.apoorva64.com/api/project_badges/measure?project=Headscale-Discord-Bot&metric=duplicated_lines_density&token=sqb_9dbdf90089215fa53405ff59992aee727c428a40)](https://sonarqube.devops-tools.apoorva64.com/dashboard?id=Headscale-Discord-Bot)

This Docker image contains a Discord bot that integrates with Headscale for management and monitoring purposes.

## Running the Docker Image

To run this Docker image, follow these steps:

1. Pull the image from GitHub Container Registry:
   ```
   docker pull ghcr.io/ozeliurs/headscale-discord-bot:latest
   ```

2. Run the container with the required environment variables:
   ```
   docker run -d \
     -e HEADSCALE_API_URL=<your_headscale_api_url> \
     -e HEADSCALE_API_KEY=<your_headscale_api_key> \
     -e DISCORD_BOT_TOKEN=<your_discord_bot_token> \
     ghcr.io/ozeliurs/headscale-discord-bot:latest
   ```

   Replace `<your_headscale_api_url>`, `<your_headscale_api_key>`, and `<your_discord_bot_token>` with your respective values.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `HEADSCALE_API_URL` | The URL of your Headscale API (will be automatically formatted) |
| `HEADSCALE_API_KEY` | Your Headscale API key |
| `DISCORD_BOT_TOKEN` | Your Discord bot token |

## Notes

- The `HEADSCALE_API_URL` will be automatically formatted to ensure it starts with `http://` or `https://` and ends with `/api/v1`.
- Make sure you have Docker installed on your system.
- The bot will run continuously in the background. Use `docker logs` to view its output.
- To stop the bot, use `docker stop` with the container ID or name.

For more information on using this bot or contributing to the project, please refer to the full documentation or contact the repository maintainer.
