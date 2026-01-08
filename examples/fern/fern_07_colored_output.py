"""Example 7: Simple stdout with debug level.

Demonstrates a simple stdout logger with debug level.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter
import sys


def setup_logger() -> None:
    """Set up logger with debug output to stdout."""
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Debug)
    dispatch = dispatch.chain(sys.stdout)
    dispatch.apply()


def main() -> None:
    setup_logger()
    print("Debug logger initialized!")
