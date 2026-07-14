"""Example 9: Trace-level stdout logging.

Demonstrates enabling trace-level logging for verbose output.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter, trace
import sys


def setup_logger() -> None:
    """Set up logger with trace-level output."""
    dispatch: Dispatch = Dispatch.new()
    # Enable all log levels including trace
    dispatch = dispatch.level(LevelFilter.Trace)
    dispatch = dispatch.chain(sys.stdout)
    dispatch.apply()


def main() -> None:
    setup_logger()
    trace("Trace record written by the most verbose level")
