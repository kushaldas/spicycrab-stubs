"""Pretty print JSON example.

Demonstrates:
- Serializing JSON with pretty formatting
"""

from spicycrab_serde_json import from_str, to_string_pretty, Value


def main() -> None:
    """Parse and pretty print JSON."""
    json_str: str = '{"name":"Bob","items":[1,2,3]}'
    value: Value = from_str(json_str)
    pretty: str = to_string_pretty(value)
    print(f"Pretty JSON:\n{pretty}")
