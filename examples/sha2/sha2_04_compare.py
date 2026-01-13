"""Compare SHA-256 and SHA-512.

Demonstrates:
- Computing both hash types
"""

from spicycrab_sha2 import Sha256, Sha512


def main() -> None:
    """Compare SHA-256 and SHA-512 output lengths."""
    data: str = "test"
    h256 = Sha256.digest(data.as_bytes())
    h512 = Sha512.digest(data.as_bytes())
    print(f"SHA-256 length: {len(h256)} bytes")
    print(f"SHA-512 length: {len(h512)} bytes")
