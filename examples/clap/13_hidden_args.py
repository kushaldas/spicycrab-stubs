"""Example 13: Hidden arguments (not shown in help).

Demonstrates:
- Hidden arguments for advanced/debug options
- Arguments that don't appear in --help

Usage:
    ./hidden_args --name Test
    ./hidden_args --name Test --internal-debug
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("hidden_demo")
    cmd = cmd.about("Application with hidden debug options")
    cmd = cmd.arg(
        Arg.new("name")
        .short("n")
        .long("name")
        .help("Your name")
        .required(True)
    )
    cmd = cmd.arg(
        Arg.new("internal_debug")
        .long("internal-debug")
        .help("Internal debug mode (hidden)")
        .action(ArgAction.SetTrue())
        .hide(True)
    )
    cmd = cmd.arg(
        Arg.new("trace_level")
        .long("trace-level")
        .help("Internal trace level (hidden)")
        .default_value("0")
        .hide(True)
    )

    matches: ArgMatches = cmd.get_matches()
    name: str | None = matches.get_one("name")
    internal_debug: bool = matches.get_flag("internal_debug")
    trace_level: str | None = matches.get_one("trace_level")

    if internal_debug:
        print("[DEBUG] Internal debug mode enabled")
        if trace_level is not None:
            print(f"[DEBUG] Trace level: {trace_level}")

    if name is not None:
        print(f"Hello, {name}!")
