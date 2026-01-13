"""Parse JSON string example.

Demonstrates:
- Parsing a JSON string into a Value
"""

from spicycrab_serde_json import from_str, Value


def main() -> None:
    """Parse a JSON string."""
    json_str: str = '{"name": "Alice", "age": 30}'
    value: Value = from_str(json_str)
    print(f"Parsed JSON: {value}")
