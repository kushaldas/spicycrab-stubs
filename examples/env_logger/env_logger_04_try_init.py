"""Safe logging initialization.

Demonstrates:
- Using try_init for safe initialization
"""

from spicycrab_env_logger import try_init
from spicycrab_log import info


def main() -> None:
    """Safe initialization example."""
    # try_init doesn't panic if already initialized
    try_init()
    info("Logger initialized safely")
