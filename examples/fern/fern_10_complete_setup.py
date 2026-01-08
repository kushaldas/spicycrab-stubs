"""Example 10: Complete logging setup.

Demonstrates a production-ready logging configuration with:
- Console output for debugging
- Error-level filtering to stderr
- Module-specific log levels
"""

from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter
import sys


def setup_logger() -> None:
    """Set up a complete production-ready logger."""
    # Stdout dispatch for normal messages
    stdout_dispatch: Dispatch = Dispatch.new()
    stdout_dispatch = stdout_dispatch.level(LevelFilter.Debug)
    stdout_dispatch = stdout_dispatch.chain(sys.stdout)

    # Stderr dispatch for errors only
    stderr_dispatch: Dispatch = Dispatch.new()
    stderr_dispatch = stderr_dispatch.level(LevelFilter.Error)
    stderr_dispatch = stderr_dispatch.chain(sys.stderr)

    # Main dispatch configuration
    dispatch: Dispatch = Dispatch.new()
    # Default level is Warn
    dispatch = dispatch.level(LevelFilter.Warn)
    # Allow Info for our application
    dispatch = dispatch.level_for("my_app", LevelFilter.Info)
    # Allow Debug for specific modules
    dispatch = dispatch.level_for("my_app::api", LevelFilter.Debug)
    # Suppress noisy libraries
    dispatch = dispatch.level_for("hyper", LevelFilter.Warn)
    dispatch = dispatch.level_for("tokio", LevelFilter.Warn)
    # Chain outputs
    dispatch = dispatch.chain(stdout_dispatch)
    dispatch = dispatch.chain(stderr_dispatch)
    dispatch.apply()


def main() -> None:
    setup_logger()
    print("Production logger initialized!")
