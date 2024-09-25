from dataclasses import dataclass
from typing import List

import requests

from src.config import HEADSCALE_API_URL, HEADSCALE_API_KEY

class HeadscaleError(Exception):
    pass

@dataclass
class Route:
    route_id: str
    node: str
    prefix: str
    advertised: bool
    enabled: bool


headers = {
    "Authorization": f"Bearer {HEADSCALE_API_KEY}"
}


def get_routes():
    try:
        response = requests.get(f"{HEADSCALE_API_URL}/routes", headers=headers, timeout=2.5)
    except requests.RequestException as e:
        raise HeadscaleError(f"Failed to fetch routes.\nError: {str(e)}")

    if not response.ok:
        raise HeadscaleError(f"Failed to fetch routes.\nStatus Code: {response.status_code}\nResponse: {response.text}")

    try:
        return [Route(
            route_id=route['id'],
            node=route['node']['name'],
            prefix=route['prefix'],
            advertised=route['advertised'],
            enabled=route['enabled']
        ) for route in response.json()["routes"] if route['node']['name']]
    except KeyError:
        raise HeadscaleError("Invalid response structure.")
