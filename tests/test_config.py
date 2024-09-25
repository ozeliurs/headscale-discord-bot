import os
import unittest
from unittest import mock

class TestConfig(unittest.TestCase):

    def setUp(self):
        # Save original environment
        self.original_env = os.environ.copy()

    def tearDown(self):
        # Restore original environment
        os.environ.clear()
        os.environ.update(self.original_env)

    def reload_config(self):
        # Reload the config module to reflect env changes
        import importlib
        import src.config
        importlib.reload(src.config)
        return src.config

    def test_headscale_api_url_not_set(self):
        os.environ.pop("HEADSCALE_API_URL", None)
        config = self.reload_config()
        self.assertIsNone(config.HEADSCALE_API_URL)

    def test_headscale_api_url_with_http(self):
        os.environ["HEADSCALE_API_URL"] = "http://example.com"
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_URL, "http://example.com/api/v1")

    def test_headscale_api_url_with_https(self):
        os.environ["HEADSCALE_API_URL"] = "https://example.com"
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_URL, "https://example.com/api/v1")

    def test_headscale_api_url_without_protocol(self):
        os.environ["HEADSCALE_API_URL"] = "example.com"
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_URL, "http://example.com/api/v1")

    def test_headscale_api_url_with_trailing_slash(self):
        os.environ["HEADSCALE_API_URL"] = "https://example.com/"
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_URL, "https://example.com/api/v1")

    def test_headscale_api_url_with_api_v1(self):
        os.environ["HEADSCALE_API_URL"] = "https://example.com/api/v1"
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_URL, "https://example.com/api/v1")

    def test_headscale_api_key(self):
        os.environ["HEADSCALE_API_KEY"] = "test_api_key"
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_KEY, "test_api_key")

    def test_headscale_api_key_not_set(self):
        os.environ.pop("HEADSCALE_API_KEY", None)
        config = self.reload_config()
        self.assertIsNone(config.HEADSCALE_API_KEY)

    def test_discord_bot_token(self):
        os.environ["DISCORD_BOT_TOKEN"] = "test_token"
        config = self.reload_config()
        self.assertEqual(config.DISCORD_BOT_TOKEN, "test_token")

    def test_discord_bot_token_not_set(self):
        os.environ.pop("DISCORD_BOT_TOKEN", None)
        config = self.reload_config()
        self.assertIsNone(config.DISCORD_BOT_TOKEN)

if __name__ == '__main__':
    unittest.main()
