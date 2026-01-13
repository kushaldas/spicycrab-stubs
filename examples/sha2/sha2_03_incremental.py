"""Incremental SHA-256 hashing.

Demonstrates:
- Creating a hasher
- Updating with multiple chunks
- Finalizing
"""

from spicycrab_sha2 import Sha256


def main() -> None:
    """Hash data incrementally."""
    hasher = Sha256.new()
    hasher.update("Hello, ".as_bytes())
    hasher.update("World!".as_bytes())
    result = hasher.finalize()
    print(f"Incremental SHA-256 hash length: {len(result)} bytes")
