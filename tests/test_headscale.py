import os
import unittest
from unittest import mock
import requests
from src.headscale import get_routes, HeadscaleError, Route

class TestHeadscale(unittest.TestCase):

    def setUp(self):
        # Save original environment
        self.original_env = os.environ.copy()
        # Set up mock environment variables
        os.environ['HEADSCALE_API_URL'] = 'http://example.com/api/v1'
        os.environ['HEADSCALE_API_KEY'] = 'test_api_key'

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

    @mock.patch('src.headscale.requests.get')
    def test_get_routes_success(self, mock_get):
        mock_response = mock.Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "routes": [
                {
                    "id": "1",
                    "machine": {"name": "node1"},
                    "prefix": "10.0.0.0/24",
                    "advertised": True,
                    "enabled": True
                }
            ]
        }
        mock_get.return_value = mock_response

        routes = get_routes()
        self.assertEqual(len(routes), 1)
        self.assertIsInstance(routes[0], Route)
        self.assertEqual(routes[0].route_id, "1")
        self.assertEqual(routes[0].node, "node1")
        self.assertEqual(routes[0].prefix, "10.0.0.0/24")
        self.assertTrue(routes[0].advertised)
        self.assertTrue(routes[0].enabled)

    @mock.patch('src.headscale.requests.get')
    def test_get_routes_request_exception(self, mock_get):
        mock_get.side_effect = requests.RequestException("Connection error")
        with self.assertRaises(HeadscaleError) as context:
            get_routes()
        self.assertIn("Failed to fetch routes", str(context.exception))
        self.assertIn("Connection error", str(context.exception))

    @mock.patch('src.headscale.requests.get')
    def test_get_routes_bad_response(self, mock_get):
        mock_response = mock.Mock()
        mock_response.ok = False
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_get.return_value = mock_response

        with self.assertRaises(HeadscaleError) as context:
            get_routes()
        self.assertIn("Failed to fetch routes", str(context.exception))
        self.assertIn("Status Code: 400", str(context.exception))
        self.assertIn("Bad Request", str(context.exception))

    @mock.patch('src.headscale.requests.get')
    def test_get_routes_invalid_response_structure(self, mock_get):
        mock_response = mock.Mock()
        mock_response.ok = True
        mock_response.json.return_value = {"invalid": "structure"}
        mock_get.return_value = mock_response

        with self.assertRaises(HeadscaleError) as context:
            get_routes()
        self.assertEqual(str(context.exception), "Invalid response structure.")

    def test_headscale_api_url_from_config(self):
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_URL, 'http://example.com/api/v1')

    def test_headscale_api_key_from_config(self):
        config = self.reload_config()
        self.assertEqual(config.HEADSCALE_API_KEY, 'test_api_key')

if __name__ == '__main__':
    unittest.main()
