"""Basic base64 decoding example.

Demonstrates:
- Decoding base64 strings back to bytes using the STANDARD engine
- Getting the length of decoded data
"""

from spicycrab_base64 import STANDARD


def main() -> None:
    """Decode a base64 string."""
    encoded: str = "SGVsbG8sIFdvcmxkIQ=="
    # Print the encoded string first before decoding
    print(f"Encoded: {encoded}")
    decoded = STANDARD.decode(encoded)
    print(f"Decoded {len(decoded)} bytes")
