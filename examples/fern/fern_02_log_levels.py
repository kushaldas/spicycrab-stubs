"""Example 2: Logging with different levels.

Demonstrates using log levels with fern.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter


def setup_logger() -> None:
    """Set up logger with info level filtering."""
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Info)
    dispatch.apply()


def main() -> None:
    setup_logger()
    print("Logger initialized with Info level!")
