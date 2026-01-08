"""Example 3: Logging to stdout.

Demonstrates chaining stdout output using std::io.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter
import sys


def setup_logger() -> None:
    """Set up logger that outputs to stdout."""
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Debug)
    dispatch = dispatch.chain(sys.stdout)
    dispatch.apply()


def main() -> None:
    setup_logger()
    print("Logger outputs to stdout!")
