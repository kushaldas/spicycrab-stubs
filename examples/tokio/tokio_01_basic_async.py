"""Example 01: Basic async function.

Demonstrates:
- Defining async functions
- Using await keyword
- Async main with #[tokio::main]

Usage:
    ./tokio_basic_async
"""


async def greet(name: str) -> str:
    """Greet someone asynchronously."""
    return f"Hello, {name}!"


async def main() -> None:
    message: str = await greet("World")
    print(message)
