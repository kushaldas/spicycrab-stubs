"""Parse TOML table example.

Demonstrates:
- Parsing TOML with tables
"""

from spicycrab_toml import from_str, Value


def main() -> None:
    """Parse TOML with nested tables."""
    toml_str: str = '[package]\nname = "myapp"\n\n[dependencies]\nlog = "0.4"'
    value: Value = from_str(toml_str)
    is_table: bool = value.is_table()
    print(f"Is table: {is_table}")
