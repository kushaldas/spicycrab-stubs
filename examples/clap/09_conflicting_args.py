"""Example 09: Conflicting arguments.

Demonstrates:
- Arguments that conflict with each other
- Using conflicts_with

Usage:
    ./conflicting_args --json
    ./conflicting_args --yaml
    (Cannot use both --json and --yaml together)
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("formatter")
    cmd = cmd.about("Output in different formats")
    cmd = cmd.arg(
        Arg.new("json")
        .long("json")
        .help("Output as JSON")
        .action(ArgAction.SetTrue())
        .conflicts_with("yaml")
    )
    cmd = cmd.arg(
        Arg.new("yaml")
        .long("yaml")
        .help("Output as YAML")
        .action(ArgAction.SetTrue())
        .conflicts_with("json")
    )
    cmd = cmd.arg(
        Arg.new("pretty")
        .short("p")
        .long("pretty")
        .help("Pretty print output")
        .action(ArgAction.SetTrue())
    )

    matches: ArgMatches = cmd.get_matches()
    use_json: bool = matches.get_flag("json")
    use_yaml: bool = matches.get_flag("yaml")
    pretty: bool = matches.get_flag("pretty")

    data: str = "example data"

    if use_json:
        if pretty:
            print(f"Pretty JSON: {data}")
        else:
            print(f"JSON: {data}")
    elif use_yaml:
        if pretty:
            print(f"Pretty YAML: {data}")
        else:
            print(f"YAML: {data}")
    else:
        print(f"Plain text: {data}")
