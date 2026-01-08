"""Example 1: Basic fern logging setup.

Demonstrates creating a simple logger that outputs to stdout.
"""

from spicycrab_fern import Dispatch


def setup_logger() -> None:
    """Set up a basic fern logger."""
    dispatch: Dispatch = Dispatch.new()
    dispatch.apply()


def main() -> None:
    setup_logger()
    print("Logger initialized!")
