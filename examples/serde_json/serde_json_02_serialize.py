"""Serialize to JSON string example.

Demonstrates:
- Converting a Value to a JSON string
"""

from spicycrab_serde_json import to_string, Value


def main() -> None:
    """Serialize a value to JSON string."""
    # Create a simple Value
    value: Value = Value.Null
    json_str: str = to_string(value)
    print(f"JSON: {json_str}")
