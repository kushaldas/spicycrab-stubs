"""Estimate base64 decoded length.

Demonstrates:
- Estimating the decoded size of base64 data using the STANDARD engine
"""

from spicycrab_base64 import STANDARD


def main() -> None:
    """Show decoded lengths for base64 strings."""
    # Decode various base64 strings and show their lengths
    # Print input first to avoid ownership issues
    b1: str = "YWJj"  # "abc"
    print(f"'{b1}'", end="")
    d1 = STANDARD.decode(b1)
    print(f" decodes to {len(d1)} bytes")

    b2: str = "SGVsbG8gV29ybGQh"  # "Hello World!"
    print(f"'{b2}'", end="")
    d2 = STANDARD.decode(b2)
    print(f" decodes to {len(d2)} bytes")

    b3: str = "VGhlIHF1aWNrIGJyb3duIGZveA=="  # "The quick brown fox"
    d3 = STANDARD.decode(b3)
    print(f"Encoded string decodes to {len(d3)} bytes")
