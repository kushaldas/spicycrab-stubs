"""Example 1: Simple async GET request with reqwest."""

from spicycrab_reqwest import get, Response


async def fetch_url(url: str) -> str:
    """Fetch a URL and return the response text."""
    response: Response = await get(url)
    text: str = await response.text()
    return text


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/get"
    body: str = await fetch_url(url)
    print(f"Response: {body}")
