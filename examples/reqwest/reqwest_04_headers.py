"""Example 4: GET request with custom headers."""

from spicycrab_reqwest import Client, Response


async def fetch_with_headers(url: str) -> str:
    """Fetch a URL with custom headers."""
    client: Client = Client.new()
    response: Response = await client.get(url).header("User-Agent", "spicycrab/1.0").header("Accept", "application/json").send()
    text: str = await response.text()
    return text


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/headers"
    body: str = await fetch_with_headers(url)
    print(f"Response: {body}")
