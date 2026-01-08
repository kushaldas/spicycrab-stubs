"""Example 03: Required vs optional arguments.

Demonstrates:
- Required arguments
- Optional arguments with default values
- Checking if arguments were provided

Usage:
    ./required_args --input data.txt
    ./required_args --input data.txt --output results.txt
"""
from spicycrab_clap import Arg, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("file_processor")
    cmd = cmd.about("Process files with required and optional arguments")
    cmd = cmd.arg(
        Arg.new("input")
        .short("i")
        .long("input")
        .help("Input file (required)")
        .required(True)
    )
    cmd = cmd.arg(
        Arg.new("output")
        .short("o")
        .long("output")
        .help("Output file (optional)")
        .required(False)
    )

    matches: ArgMatches = cmd.get_matches()
    input_file: str | None = matches.get_one("input")
    output_file: str | None = matches.get_one("output")

    if input_file is not None:
        print(f"Input file: {input_file}")

    if output_file is not None:
        print(f"Output file: {output_file}")
    else:
        print("Output: stdout")
