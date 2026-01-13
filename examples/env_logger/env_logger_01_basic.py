"""Basic logging with env_logger.

Demonstrates:
- Initializing env_logger
- Using log macros
"""

from spicycrab_env_logger import init
from spicycrab_log import info, warn, error


def main() -> None:
    """Basic logging example."""
    init()

    info("Application started")
    warn("This is a warning")
    error("This is an error")
