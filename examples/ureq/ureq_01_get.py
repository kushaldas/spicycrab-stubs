"""Basic GET request example.

Demonstrates:
- Creating a GET request builder
"""

from spicycrab_ureq import get


def main() -> None:
    """Create a GET request builder."""
    req = get("https://httpbin.org/get")
    print("Created GET request builder")
