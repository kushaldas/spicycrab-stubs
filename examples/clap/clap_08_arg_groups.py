"""Example 08: Argument groups (mutually exclusive options).

Demonstrates:
- Creating argument groups
- Making groups required
- Arguments belonging to a group

Usage:
    ./arg_groups --stdin
    ./arg_groups --file input.txt
    (Cannot use both --stdin and --file together)
"""
from spicycrab_clap import Arg, ArgAction, ArgGroup, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("input_selector")
    cmd = cmd.about("Select input source (stdin or file, but not both)")

    cmd = cmd.arg(
        Arg.new("stdin")
        .long("stdin")
        .help("Read from stdin")
        .action(ArgAction.SetTrue())
        .group("input_source")
    )
    cmd = cmd.arg(
        Arg.new("file")
        .short("f")
        .long("file")
        .help("Read from file")
        .group("input_source")
    )

    input_group: ArgGroup = ArgGroup.new("input_source")
    input_group = input_group.required(True)
    input_group = input_group.multiple(False)
    cmd = cmd.group(input_group)

    matches: ArgMatches = cmd.get_matches()
    use_stdin: bool = matches.get_flag("stdin")
    file_path: str | None = matches.get_one("file")

    if use_stdin:
        print("Reading from stdin...")
    elif file_path is not None:
        print(f"Reading from file: {file_path}")
