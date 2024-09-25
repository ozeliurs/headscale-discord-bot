import os

HEADSCALE_API_URL = os.environ.get("HEADSCALE_API_URL")
if HEADSCALE_API_URL:

    if not HEADSCALE_API_URL.startswith(("http://", "https://")):
        HEADSCALE_API_URL = "http://" + HEADSCALE_API_URL

    HEADSCALE_API_URL = HEADSCALE_API_URL.rstrip('/')
    if not HEADSCALE_API_URL.endswith('/api/v1'):
        HEADSCALE_API_URL += '/api/v1'

HEADSCALE_API_KEY = os.environ.get("HEADSCALE_API_KEY")
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
