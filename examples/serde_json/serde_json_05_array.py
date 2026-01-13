"""Parse JSON array example.

Demonstrates:
- Parsing and checking JSON arrays
"""

from spicycrab_serde_json import from_str, Value


def main() -> None:
    """Parse a JSON array."""
    json_str: str = '[1, 2, 3, 4, 5]'
    value: Value = from_str(json_str)

    # Check if it's an array
    is_array: bool = value.is_array()
    print(f"Is array: {is_array}")

    # Check types
    is_string: bool = value.is_string()
    print(f"Is string: {is_string}")
