"""Example 9: Trace-level logging.

Demonstrates enabling trace-level logging for verbose output.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter
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
    print("Trace-level logger initialized!")
