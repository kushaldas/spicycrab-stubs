"""Example 1: Basic fern logging setup.

Demonstrates creating a simple logger that outputs to stdout.
"""

import sys

from spicycrab_fern import Dispatch
from spicycrab_log import info


def setup_logger() -> None:
    """Set up a basic fern logger."""
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.chain(sys.stdout)
    dispatch.apply()


def main() -> None:
    setup_logger()
    info("Hello from the fern logger")
