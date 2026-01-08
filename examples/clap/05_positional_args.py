"""Example 05: Positional arguments.

Demonstrates:
- Positional arguments (without flags)
- Index-based argument ordering

Usage:
    ./positional_args source.txt dest.txt
"""
from spicycrab_clap import Arg, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("copy")
    cmd = cmd.about("Copy a file from source to destination")
    cmd = cmd.arg(
        Arg.new("source")
        .help("Source file to copy")
        .required(True)
        .index(1)
    )
    cmd = cmd.arg(
        Arg.new("destination")
        .help("Destination path")
        .required(True)
        .index(2)
    )

    matches: ArgMatches = cmd.get_matches()
    source: str | None = matches.get_one("source")
    destination: str | None = matches.get_one("destination")

    if source is not None and destination is not None:
        print(f"Copying {source} to {destination}")
