"""SHA-512 digest example.

Demonstrates:
- One-shot SHA-512 hashing
"""

from spicycrab_sha2 import Sha512


def main() -> None:
    """Compute SHA-512 hash of a string."""
    data: str = "Hello, World!"
    hash_result = Sha512.digest(data.as_bytes())
    print(f"Input: {data}")
    print(f"SHA-512 hash length: {len(hash_result)} bytes")
