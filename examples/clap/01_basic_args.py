"""Example 01: Basic argument parsing with clap.

Demonstrates:
- Creating a Command with name and about
- Adding arguments with short and long flags
- Getting argument values from matches

Usage:
    ./basic_args --name Alice
    ./basic_args -n Bob
"""
from spicycrab_clap import Arg, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("greeter")
    cmd = cmd.about("A simple greeting program")
    cmd = cmd.arg(
        Arg.new("name").short("n").long("name").help("Name to greet").required(True)
    )

    matches: ArgMatches = cmd.get_matches()
    name: str | None = matches.get_one("name")

    if name is not None:
        print(f"Hello, {name}!")
