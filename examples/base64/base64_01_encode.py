"""Basic base64 encoding example.

Demonstrates:
- Encoding strings to base64 using the STANDARD engine
"""

from spicycrab_base64 import STANDARD


def main() -> None:
    """Encode a string to base64."""
    original: str = "Hello, World!"
    print(f"Original: {original}")
    encoded: str = STANDARD.encode(original)
    print(f"Encoded: {encoded}")
