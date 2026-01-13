"""Basic base64 decoding example.

Demonstrates:
- Decoding base64 strings back to bytes
- Getting the length of decoded data
"""

from spicycrab_base64 import decode


def main() -> None:
    """Decode a base64 string."""
    encoded: str = "SGVsbG8sIFdvcmxkIQ=="
    decoded = decode(encoded)
    # Print the length of decoded bytes
    print(f"Encoded: {encoded}")
    print(f"Decoded {len(decoded)} bytes")
