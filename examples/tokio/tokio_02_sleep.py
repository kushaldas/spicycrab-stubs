"""Example 02: Async sleep with tokio.

Demonstrates:
- Using tokio::time::sleep
- Duration from std::time
- Multiple awaits in sequence

Usage:
    ./tokio_sleep
"""

from spicycrab_tokio import sleep, Duration


async def delay_print(msg: str, secs: int) -> None:
    """Print a message after a delay."""
    await sleep(Duration.from_secs(secs))
    print(msg)


async def main() -> None:
    print("Starting...")
    await delay_print("After 1 second", 1)
    await delay_print("After 2 more seconds", 2)
    print("Done!")
