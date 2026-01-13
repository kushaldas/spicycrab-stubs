"""Default Config example.

Demonstrates:
- Creating a default Config
"""

from spicycrab_config import Config


def main() -> None:
    """Create a default config."""
    cfg = Config.default()
    print("Created default config")
