"""Parse TOML string example.

Demonstrates:
- Parsing a TOML string into a Value
"""

from spicycrab_toml import from_str, Value


def main() -> None:
    """Parse a TOML string."""
    toml_str: str = 'name = "example"\nversion = "1.0"'
    value: Value = from_str(toml_str)
    print(f"Parsed TOML: {value}")
