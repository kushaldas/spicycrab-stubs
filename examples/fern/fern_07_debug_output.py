"""Example 7: Debug-level stdout logging.

Demonstrates a simple stdout logger with debug level.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter, debug
import sys


def setup_logger() -> None:
    """Set up logger with debug output to stdout."""
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Debug)
    dispatch = dispatch.chain(sys.stdout)
    dispatch.apply()


def main() -> None:
    setup_logger()
    debug("Debug-level stdout logging is active")
