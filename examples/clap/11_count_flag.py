"""Example 11: Counting flag occurrences.

Demonstrates:
- ArgAction.Count for counting flag occurrences
- Verbosity levels (-v, -vv, -vvv)

Usage:
    ./count_flag           # verbosity = 0
    ./count_flag -v        # verbosity = 1
    ./count_flag -vv       # verbosity = 2
    ./count_flag -vvv      # verbosity = 3
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("verbose_app")
    cmd = cmd.about("Application with verbosity levels")
    cmd = cmd.arg(
        Arg.new("verbose")
        .short("v")
        .long("verbose")
        .help("Increase verbosity (use multiple times for more)")
        .action(ArgAction.Count())
    )
    cmd = cmd.arg(
        Arg.new("message")
        .short("m")
        .long("message")
        .help("Message to process")
        .default_value("Hello, World!")
    )

    matches: ArgMatches = cmd.get_matches()
    verbosity: int = matches.get_count("verbose")
    message: str | None = matches.get_one("message")

    if message is not None:
        if verbosity == 0:
            print(message)
        elif verbosity == 1:
            print(f"INFO: {message}")
        elif verbosity == 2:
            print(f"DEBUG: Processing message...")
            print(f"DEBUG: {message}")
        else:
            print(f"TRACE: Verbosity level: {verbosity}")
            print(f"TRACE: Message length: {len(message)}")
            print(f"TRACE: Processing message...")
            print(f"TRACE: {message}")
