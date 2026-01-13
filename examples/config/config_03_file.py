"""Config File example.

Demonstrates:
- Creating a File source with name
"""

from spicycrab_config import File


def main() -> None:
    """Create a file source."""
    file = File.with_name("config")
    print("Created file source for 'config'")
