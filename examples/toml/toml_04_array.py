"""Parse TOML array example.

Demonstrates:
- Parsing TOML with arrays
"""

from spicycrab_toml import from_str, Value


def main() -> None:
    """Parse TOML with arrays."""
    toml_str: str = 'numbers = [1, 2, 3]\nnames = ["alice", "bob"]'
    value: Value = from_str(toml_str)
    print(f"Parsed array TOML: {value}")
