"""Example 4: Logging to stderr.

Demonstrates chaining stderr output for errors.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter
import sys


def setup_logger() -> None:
    """Set up logger that outputs errors to stderr."""
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Error)
    dispatch = dispatch.chain(sys.stderr)
    dispatch.apply()


def main() -> None:
    setup_logger()
    print("Error logger outputs to stderr!")
