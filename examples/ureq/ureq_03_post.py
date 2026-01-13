"""POST request example.

Demonstrates:
- Making a POST request
"""

from spicycrab_ureq import post


def main() -> None:
    """Make a POST request builder."""
    req = post("https://httpbin.org/post")
    print("Created POST request builder")
