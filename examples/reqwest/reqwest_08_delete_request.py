"""Example 8: DELETE request."""

from spicycrab_reqwest import Client, Response


async def delete_resource(url: str) -> bool:
    """Send a DELETE request and return success status."""
    client: Client = Client.new()
    response: Response = await client.delete(url).send()
    is_success: bool = response.status().is_success()
    return is_success


async def main() -> None:
    """Main entry point."""
    url: str = "https://httpbin.org/delete"
    success: bool = await delete_resource(url)
    print(f"Delete successful: {success}")
