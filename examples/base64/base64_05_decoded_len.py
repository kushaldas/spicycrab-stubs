"""Estimate base64 decoded length.

Demonstrates:
- Estimating the decoded size of base64 data
"""

from spicycrab_base64 import decode


def main() -> None:
    """Show decoded lengths for base64 strings."""
    # Decode various base64 strings and show their lengths
    b1: str = "YWJj"  # "abc"
    d1 = decode(b1)
    print(f"'{b1}' decodes to {len(d1)} bytes")

    b2: str = "SGVsbG8gV29ybGQh"  # "Hello World!"
    d2 = decode(b2)
    print(f"'{b2}' decodes to {len(d2)} bytes")

    b3: str = "VGhlIHF1aWNrIGJyb3duIGZveA=="  # "The quick brown fox"
    d3 = decode(b3)
    print(f"Encoded string decodes to {len(d3)} bytes")
