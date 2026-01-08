"""Example 10: Arguments that require other arguments.

Demonstrates:
- Using requires to make one argument depend on another
- Conditional argument requirements

Usage:
    ./requires --config settings.toml
    ./requires --config settings.toml --validate
    (--validate requires --config to be present)
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("config_tool")
    cmd = cmd.about("Configuration tool with dependent arguments")
    cmd = cmd.arg(
        Arg.new("config")
        .short("c")
        .long("config")
        .help("Configuration file path")
        .value_name("FILE")
    )
    cmd = cmd.arg(
        Arg.new("validate")
        .long("validate")
        .help("Validate the configuration (requires --config)")
        .action(ArgAction.SetTrue())
        .requires("config")
    )
    cmd = cmd.arg(
        Arg.new("output")
        .short("o")
        .long("output")
        .help("Output file (requires --config)")
        .requires("config")
    )

    matches: ArgMatches = cmd.get_matches()
    config_path: str | None = matches.get_one("config")
    validate: bool = matches.get_flag("validate")
    output_path: str | None = matches.get_one("output")

    if config_path is not None:
        print(f"Loading config: {config_path}")
        if validate:
            print("Validating configuration...")
        if output_path is not None:
            print(f"Writing output to: {output_path}")
    else:
        print("No config specified. Use --help for usage.")
