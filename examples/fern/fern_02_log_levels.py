"""Example 2: Logging with different levels.

Demonstrates using log levels with fern.
"""

import sys

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter, debug, info


def setup_logger() -> None:
    """Set up logger with info level filtering."""
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Info)
    dispatch = dispatch.chain(sys.stdout)
    dispatch.apply()


def main() -> None:
    setup_logger()
    debug("This debug record is filtered out")
    info("This info record passes the filter")
