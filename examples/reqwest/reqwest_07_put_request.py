"""Example 7: PUT request."""

from spicycrab_reqwest import Client, Response


async def put_data(url: str, data: str) -> str:
    """Send a PUT request with data."""
    client: Client = Client.new()
    response: Response = await client.put(url).body(data).send()
    text: str = await response.text()
    return text


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/put"
    data: str = "updated data"
    body: str = await put_data(url, data)
    print(f"Response: {body}")
