"""Example 6: Checking response status code."""

from spicycrab_reqwest import Client, Response


async def check_url_success(url: str) -> bool:
    """Check if a URL returns a success status."""
    client: Client = Client.new()
    response: Response = await client.get(url).send()
    is_success: bool = response.status().is_success()
    return is_success


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/status/200"
    is_success: bool = await check_url_success(url)
    print(f"URL returned success: {is_success}")
