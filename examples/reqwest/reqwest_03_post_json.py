"""Example 3: POST request with JSON body."""

from spicycrab_reqwest import Client, Response


async def post_json(url: str, data: str) -> str:
    """Send a POST request with JSON body."""
    client: Client = Client.new()
    response: Response = await client.post(url).body(data).send()
    text: str = await response.text()
    return text


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/post"
    json_data: str = '{"name": "test", "value": 42}'
    body: str = await post_json(url, json_data)
    print(f"Response: {body}")
