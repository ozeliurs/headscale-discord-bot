import unittest
from unittest.mock import Mock, patch
import discord

from src.headscale_embeds import RoutesEmbed, RouteEmbed, ErrorEmbed
from src.headscale import Route
from src.constants import EMOJI_ADVERTISED, EMOJI_FAILURE, EMOJI_NOT_ADVERTISED, EMOJI_WARNING, EMOJI_SUCCESS, EMOJI_ID

class TestHeadscaleEmbeds(unittest.TestCase):

    def setUp(self):
        self.mock_route = Mock(spec=Route)
        self.mock_route.route_id = "1"
        self.mock_route.node = "test_node"
        self.mock_route.prefix = "10.0.0.0/24"
        self.mock_route.advertised = True
        self.mock_route.enabled = True

    def test_routes_embed_init(self):
        routes = [self.mock_route]
        embed = RoutesEmbed(routes)
        self.assertEqual(embed.title, "🛣️ Routes List")
        self.assertEqual(embed.description, "📋 Displaying all available routes")
        self.assertEqual(embed.color, discord.Color.blurple())

    def test_routes_embed_add_field(self):
        routes = [self.mock_route]
        embed = RoutesEmbed(routes)
        self.assertEqual(len(embed.fields), 1)
        self.assertEqual(embed.fields[0].name, f"{EMOJI_SUCCESS} test_node")
        self.assertEqual(embed.fields[0].value, f"{EMOJI_ADVERTISED}{EMOJI_SUCCESS} 10.0.0.0/24")

    def test_routes_embed_multiple_routes(self):
        route2 = Mock(spec=Route)
        route2.route_id = "2"
        route2.node = "test_node"
        route2.prefix = "10.0.1.0/24"
        route2.advertised = False
        route2.enabled = False
        routes = [self.mock_route, route2]
        embed = RoutesEmbed(routes)
        self.assertEqual(len(embed.fields), 1)
        self.assertEqual(embed.fields[0].name, f"{EMOJI_WARNING} test_node")
        self.assertIn("10.0.0.0/24", embed.fields[0].value)
        self.assertIn("10.0.1.0/24", embed.fields[0].value)

    def test_route_embed_init(self):
        routes = [self.mock_route]
        embed = RouteEmbed(routes, "test_node")
        self.assertEqual(embed.title, "🛣️ Routes for test_node")
        self.assertEqual(embed.description, "📋 Displaying all routes for node: test_node")
        self.assertEqual(embed.color, discord.Color.blurple())

    def test_route_embed_add_field(self):
        routes = [self.mock_route]
        embed = RouteEmbed(routes, "test_node")
        self.assertEqual(len(embed.fields), 1)
        self.assertEqual(embed.fields[0].name, "▶ 10.0.0.0/24")
        self.assertIn(EMOJI_ID + " 1", embed.fields[0].value)
        self.assertIn(EMOJI_SUCCESS + " Enabled", embed.fields[0].value)
        self.assertIn(EMOJI_ADVERTISED + " Advertised", embed.fields[0].value)

    def test_error_embed_init(self):
        error_message = "Test error message"
        embed = ErrorEmbed(error_message)
        self.assertEqual(embed.title, f"{EMOJI_FAILURE} Error")
        self.assertEqual(embed.description, error_message)
        self.assertEqual(embed.color, discord.Color.red())

if __name__ == '__main__':
    unittest.main()
