"""DELETE request example.

Demonstrates:
- Making a DELETE request
"""

from spicycrab_ureq import delete


def main() -> None:
    """Make a DELETE request builder."""
    req = delete("https://httpbin.org/delete")
    print("Created DELETE request builder")
