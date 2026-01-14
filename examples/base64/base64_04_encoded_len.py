"""Calculate base64 encoded length.

Demonstrates:
- Calculating the length of base64 encoded output using the STANDARD engine
"""

from spicycrab_base64 import STANDARD


def main() -> None:
    """Calculate encoded lengths for different input sizes."""
    # Encode strings of different lengths and show output length
    # Print input first, then encode to avoid ownership issues
    s1: str = "abc"
    print(f"Input '{s1}' ({len(s1)} bytes)", end="")
    e1: str = STANDARD.encode(s1)
    print(f" -> encoded length {len(e1)}")

    s2: str = "Hello World!"
    print(f"Input '{s2}' ({len(s2)} bytes)", end="")
    e2: str = STANDARD.encode(s2)
    print(f" -> encoded length {len(e2)}")

    s3: str = "The quick brown fox jumps over the lazy dog"
    e3: str = STANDARD.encode(s3)
    print(f"Input 43 bytes -> encoded length {len(e3)}")
