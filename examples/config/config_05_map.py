"""Config Builder with defaults example.

Demonstrates:
- Building config from builder with defaults
"""

from spicycrab_config import Config


def main() -> None:
    """Build a config with defaults."""
    builder = Config.builder()
    cfg = builder.build_cloned()
    print("Built config with defaults")
