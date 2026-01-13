"""Debug logging with env_logger.

Demonstrates:
- Using debug and trace levels
"""

from spicycrab_env_logger import init
from spicycrab_log import debug, trace, info


def main() -> None:
    """Debug logging example."""
    init()

    trace("Trace level message")
    debug("Debug level message")
    info("Info level message")
