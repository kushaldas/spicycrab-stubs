"""Base64 roundtrip encode/decode example.

Demonstrates:
- Encoding and decoding strings
- Verifying data integrity by checking decoded length
"""

from spicycrab_base64 import encode, decode


def main() -> None:
    """Encode and then decode data."""
    original: str = "The quick brown fox"

    # Encode
    encoded: str = encode(original)
    print(f"Original: {original}")
    print(f"Encoded: {encoded}")

    # Decode and check length matches original
    decoded = decode(encoded)
    print(f"Decoded {len(decoded)} bytes (original was {len(original)} bytes)")
