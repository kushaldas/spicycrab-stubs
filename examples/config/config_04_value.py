"""Config Value example.

Demonstrates:
- Working with config values
"""

from spicycrab_config import Value


def main() -> None:
    """Create a config value."""
    # Create a simple value from a bool
    val = Value.from_(true)
    print(f"Created value: {val}")
