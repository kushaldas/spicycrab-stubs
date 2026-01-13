"""Calculate base64 encoded length.

Demonstrates:
- Calculating the length of base64 encoded output
"""

from spicycrab_base64 import encode


def main() -> None:
    """Calculate encoded lengths for different input sizes."""
    # Encode strings of different lengths and show output length
    s1: str = "abc"
    e1: str = encode(s1)
    print(f"Input '{s1}' ({len(s1)} bytes) -> encoded length {len(e1)}")

    s2: str = "Hello World!"
    e2: str = encode(s2)
    print(f"Input '{s2}' ({len(s2)} bytes) -> encoded length {len(e2)}")

    s3: str = "The quick brown fox jumps over the lazy dog"
    e3: str = encode(s3)
    print(f"Input 43 bytes -> encoded length {len(e3)}")
