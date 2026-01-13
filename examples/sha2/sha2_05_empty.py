"""Hash empty string.

Demonstrates:
- SHA-256 of empty input
"""

from spicycrab_sha2 import Sha256


def main() -> None:
    """Compute SHA-256 of empty string."""
    empty: str = ""
    hash_result = Sha256.digest(empty.as_bytes())
    print(f"SHA-256 of empty string: {len(hash_result)} bytes")
