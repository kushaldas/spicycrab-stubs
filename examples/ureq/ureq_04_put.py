"""PUT request example.

Demonstrates:
- Making a PUT request
"""

from spicycrab_ureq import put


def main() -> None:
    """Make a PUT request builder."""
    req = put("https://httpbin.org/put")
    print("Created PUT request builder")
