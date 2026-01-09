"""Example 9: PATCH request."""

from spicycrab_reqwest import Client, Response


async def patch_resource(url: str, data: str) -> str:
    """Send a PATCH request with data."""
    client: Client = Client.new()
    response: Response = await client.patch(url).body(data).send()
    text: str = await response.text()
    return text


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/patch"
    data: str = '{"field": "patched_value"}'
    body: str = await patch_resource(url, data)
    print(f"Response: {body}")
