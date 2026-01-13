"""Using env_logger Builder directly.

Demonstrates:
- Using Builder::new() for configuration
"""

from spicycrab_env_logger import Builder
from spicycrab_log import info


def main() -> None:
    """Builder pattern example."""
    # Use Builder static method
    Builder.new().init()

    info("Logger configured with builder")
