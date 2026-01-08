"""Example 06: Multiple values for an argument.

Demonstrates:
- Accepting multiple values with ArgAction.Append
- Getting multiple values with get_many

Usage:
    ./multiple_values --file a.txt --file b.txt --file c.txt
    ./multiple_values -f one.txt -f two.txt
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("multi_file")
    cmd = cmd.about("Process multiple files")
    cmd = cmd.arg(
        Arg.new("file")
        .short("f")
        .long("file")
        .help("Files to process (can be specified multiple times)")
        .action(ArgAction.Append())
        .required(True)
    )

    matches: ArgMatches = cmd.get_matches()
    files: list[str] = matches.get_many("file")

    print(f"Processing {len(files)} files:")
    for f in files:
        print(f"  - {f}")
