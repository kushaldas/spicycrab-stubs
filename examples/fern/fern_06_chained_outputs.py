"""Example 6: Chaining multiple outputs.

Demonstrates logging to both stdout and stderr based on level.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter
import sys


def setup_logger() -> None:
    """Set up logger with stdout for info and stderr for errors."""
    # Info+ messages go to stdout
    stdout_dispatch: Dispatch = Dispatch.new()
    stdout_dispatch = stdout_dispatch.level(LevelFilter.Info)
    stdout_dispatch = stdout_dispatch.chain(sys.stdout)

    # Error messages also go to stderr
    stderr_dispatch: Dispatch = Dispatch.new()
    stderr_dispatch = stderr_dispatch.level(LevelFilter.Error)
    stderr_dispatch = stderr_dispatch.chain(sys.stderr)

    # Main dispatch chains both
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.chain(stdout_dispatch)
    dispatch = dispatch.chain(stderr_dispatch)
    dispatch.apply()


def main() -> None:
    setup_logger()
    print("Multi-output logger initialized!")
