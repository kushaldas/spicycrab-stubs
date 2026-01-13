"""Access JSON values example.

Demonstrates:
- Accessing fields in parsed JSON
"""

from spicycrab_serde_json import from_str, Value


def main() -> None:
    """Access values in parsed JSON."""
    json_str: str = '{"name": "Carol", "active": true}'
    value: Value = from_str(json_str)

    # Check if it's an object
    is_obj: bool = value.is_object()
    print(f"Is object: {is_obj}")

    # Check for null
    is_null: bool = value.is_null()
    print(f"Is null: {is_null}")
