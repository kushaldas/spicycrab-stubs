"""Example 02: Boolean flags with clap.

Demonstrates:
- Creating boolean flags with ArgAction.SetTrue
- Checking flag values with get_flag

Usage:
    ./flags --verbose
    ./flags -v -d
    ./flags --verbose --debug
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("flags_demo")
    cmd = cmd.about("Demonstrates boolean flags")
    cmd = cmd.arg(
        Arg.new("verbose")
        .short("v")
        .long("verbose")
        .help("Enable verbose output")
        .action(ArgAction.SetTrue())
    )
    cmd = cmd.arg(
        Arg.new("debug")
        .short("d")
        .long("debug")
        .help("Enable debug mode")
        .action(ArgAction.SetTrue())
    )

    matches: ArgMatches = cmd.get_matches()
    verbose: bool = matches.get_flag("verbose")
    debug: bool = matches.get_flag("debug")

    if verbose:
        print("Verbose mode enabled")
    if debug:
        print("Debug mode enabled")
    if not verbose and not debug:
        print("Running in quiet mode")
