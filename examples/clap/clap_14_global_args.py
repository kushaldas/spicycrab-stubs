"""Example 14: Global arguments available to all subcommands.

Demonstrates:
- Global arguments that propagate to subcommands
- Accessing global args from subcommand matches

Usage:
    ./global_args --verbose start
    ./global_args -v stop --force
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    start_cmd: Command = Command.new("start")
    start_cmd = start_cmd.about("Start the service")

    stop_cmd: Command = Command.new("stop")
    stop_cmd = stop_cmd.about("Stop the service")
    stop_cmd = stop_cmd.arg(
        Arg.new("force")
        .short("f")
        .long("force")
        .help("Force stop")
        .action(ArgAction.SetTrue())
    )

    status_cmd: Command = Command.new("status")
    status_cmd = status_cmd.about("Show service status")

    cmd: Command = Command.new("service")
    cmd = cmd.about("Service management with global verbose flag")
    cmd = cmd.arg(
        Arg.new("verbose")
        .short("v")
        .long("verbose")
        .help("Enable verbose output")
        .action(ArgAction.SetTrue())
        .global_(True)
    )
    cmd = cmd.subcommand(start_cmd)
    cmd = cmd.subcommand(stop_cmd)
    cmd = cmd.subcommand(status_cmd)
    cmd = cmd.subcommand_required(True)

    matches: ArgMatches = cmd.get_matches()
    verbose: bool = matches.get_flag("verbose")
    subcmd_name: str | None = matches.subcommand_name()

    if verbose:
        print("[VERBOSE] Verbose mode enabled globally")

    if subcmd_name == "start":
        if verbose:
            print("[VERBOSE] Starting service...")
        print("Service started")
    elif subcmd_name == "stop":
        sub_matches: ArgMatches | None = matches.subcommand_matches("stop")
        if sub_matches is not None:
            force: bool = sub_matches.get_flag("force")
            if verbose:
                print("[VERBOSE] Stopping service...")
            if force:
                print("Force stopping service...")
            print("Service stopped")
    elif subcmd_name == "status":
        if verbose:
            print("[VERBOSE] Checking status...")
        print("Service is running")
