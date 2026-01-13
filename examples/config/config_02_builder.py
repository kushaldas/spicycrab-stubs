"""Config Builder example.

Demonstrates:
- Using Config::builder()
"""

from spicycrab_config import Config


def main() -> None:
    """Use config builder."""
    builder = Config.builder()
    print("Created config builder")
