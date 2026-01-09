"""Example 2: Using Client for GET request."""

from spicycrab_reqwest import Client, Response


async def fetch_with_client(url: str) -> str:
    """Fetch a URL using a Client instance."""
    client: Client = Client.new()
    response: Response = await client.get(url).send()
    text: str = await response.text()
    return text


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/get"
    body: str = await fetch_with_client(url)
    print(f"Response: {body}")
