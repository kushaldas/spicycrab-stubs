"""Base64 roundtrip encode/decode example.

Demonstrates:
- Encoding and decoding strings using the STANDARD engine
- Verifying data integrity by checking decoded length
"""

from spicycrab_base64 import STANDARD


def main() -> None:
    """Encode and then decode data."""
    original: str = "The quick brown fox"

    # Encode - print before encoding to avoid move
    print(f"Original: {original} ({len(original)} bytes)")
    encoded: str = STANDARD.encode(original)
    print(f"Encoded: {encoded}")

    # Decode and check length
    decoded = STANDARD.decode(encoded)
    print(f"Decoded {len(decoded)} bytes")
