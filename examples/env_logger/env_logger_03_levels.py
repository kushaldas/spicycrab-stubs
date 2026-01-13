"""All logging levels example.

Demonstrates:
- All five log levels: trace, debug, info, warn, error
"""

from spicycrab_env_logger import init
from spicycrab_log import trace, debug, info, warn, error


def main() -> None:
    """Show all log levels."""
    init()

    error("Error level - always shown")
    warn("Warn level")
    info("Info level")
    debug("Debug level")
    trace("Trace level - most verbose")
