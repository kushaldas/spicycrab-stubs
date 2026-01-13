"""Basic SHA-256 digest example.

Demonstrates:
- One-shot SHA-256 hashing
"""

from spicycrab_sha2 import Sha256


def main() -> None:
    """Compute SHA-256 hash of a string."""
    data: str = "Hello, World!"
    hash_result = Sha256.digest(data.as_bytes())
    print(f"Input: {data}")
    print(f"SHA-256 hash length: {len(hash_result)} bytes")
