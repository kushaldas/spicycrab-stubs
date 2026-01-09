"""Example 5: Using ClientBuilder for configuration."""

from spicycrab_reqwest import Client, ClientBuilder, Response


async def fetch_with_configured_client(url: str) -> str:
    """Fetch a URL with a configured client."""
    client: Client = ClientBuilder.new().user_agent("spicycrab/1.0").build()
    response: Response = await client.get(url).send()
    text: str = await response.text()
    return text


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/user-agent"
    body: str = await fetch_with_configured_client(url)
    print(f"Response: {body}")
