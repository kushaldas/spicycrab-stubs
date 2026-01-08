"""Example 12: Custom version and about text.

Demonstrates:
- Setting version string
- Setting author information
- Long about text for detailed help

Usage:
    ./help_version --version
    ./help_version --help
    ./help_version run
"""
from spicycrab_clap import Arg, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("myapp")
    cmd = cmd.version("1.0.0")
    cmd = cmd.author("Example Author <author@example.com>")
    cmd = cmd.about("A sample application")
    cmd = cmd.long_about(
        "This is a sample application that demonstrates how to use clap "
        "for command-line argument parsing. It supports various features "
        "including subcommands, flags, and options."
    )
    cmd = cmd.arg(
        Arg.new("action")
        .help("Action to perform")
        .index(1)
        .default_value("info")
    )

    matches: ArgMatches = cmd.get_matches()
    action: str | None = matches.get_one("action")

    if action == "info":
        print("Application: myapp v1.0.0")
        print("Author: Example Author")
    elif action == "run":
        print("Running application...")
    else:
        if action is not None:
            print(f"Unknown action: {action}")
