"""Safe logging initialization.

Demonstrates:
- Using try_init for safe initialization
"""

from spicycrab_env_logger import try_init
from spicycrab_log import info


def main() -> None:
    """Safe initialization example."""
    # try_init uses env_logger's fallible initialization path
    try_init()
    info("Logger initialized safely")
