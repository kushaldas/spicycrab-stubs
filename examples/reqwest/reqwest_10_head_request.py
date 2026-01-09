"""Example 10: HEAD request to check if URL is accessible."""

from spicycrab_reqwest import Client, Response


async def check_url_accessible(url: str) -> bool:
    """Check if a URL is accessible using HEAD request."""
    client: Client = Client.new()
    response: Response = await client.head(url).send()
    is_success: bool = response.status().is_success()
    return is_success


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/bytes/1024"
    accessible: bool = await check_url_accessible(url)
    print(f"URL accessible: {accessible}")
