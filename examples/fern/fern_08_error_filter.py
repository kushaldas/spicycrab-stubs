"""Example 8: Error-level filtering with a nested dispatch.

Demonstrates filtering to only log error-level messages.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter, error, info
import sys


def setup_logger() -> None:
    """Set up logger that only shows errors."""
    # Error-only dispatch
    error_dispatch: Dispatch = Dispatch.new()
    error_dispatch = error_dispatch.level(LevelFilter.Error)
    error_dispatch = error_dispatch.chain(sys.stderr)

    # Main dispatch
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Info)
    dispatch = dispatch.chain(sys.stdout)
    dispatch = dispatch.chain(error_dispatch)
    dispatch.apply()


def main() -> None:
    setup_logger()
    info("Info record is written only to stdout")
    error("Error record is also written to the error dispatch")
