"""Example 5: Module-specific log levels.

Demonstrates setting different log levels for different modules.
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter, info, warn
import sys


def setup_logger() -> None:
    """Set up logger with module-specific levels."""
    dispatch: Dispatch = Dispatch.new()
    # Default level is Warn
    dispatch = dispatch.level(LevelFilter.Warn)
    # But allow Info for our app
    dispatch = dispatch.level_for("my_app", LevelFilter.Info)
    # And Debug for the database module
    dispatch = dispatch.level_for("my_app::database", LevelFilter.Debug)
    dispatch = dispatch.chain(sys.stdout)
    dispatch.apply()


def main() -> None:
    setup_logger()
    info("The crate-level info record is filtered by the Warn default")
    warn("The crate-level warning passes the default filter")
