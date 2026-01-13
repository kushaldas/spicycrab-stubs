"""Basic base64 encoding example.

Demonstrates:
- Encoding strings to base64
"""

from spicycrab_base64 import encode


def main() -> None:
    """Encode a string to base64."""
    original: str = "Hello, World!"
    encoded: str = encode(original)
    print(f"Original: {original}")
    print(f"Encoded: {encoded}")
