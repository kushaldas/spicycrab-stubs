"""Serialize to TOML string example.

Demonstrates:
- Converting a Value to a TOML string
"""

from spicycrab_toml import from_str, to_string_pretty, Value


def main() -> None:
    """Serialize a value to TOML string."""
    toml_str: str = 'name = "test"\n[package]\nversion = "0.1"'
    value: Value = from_str(toml_str)
    pretty: str = to_string_pretty(value)
    print(f"Pretty TOML:\n{pretty}")
