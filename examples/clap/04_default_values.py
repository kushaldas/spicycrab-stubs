"""Example 04: Default values for arguments.

Demonstrates:
- Setting default values with default_value
- Value names in help text

Usage:
    ./default_values
    ./default_values --port 3000
    ./default_values --host 0.0.0.0 --port 8080
"""
from spicycrab_clap import Arg, ArgMatches, Command


def main() -> None:
    cmd: Command = Command.new("server")
    cmd = cmd.about("A server with configurable host and port")
    cmd = cmd.arg(
        Arg.new("host")
        .short("H")
        .long("host")
        .help("Host address to bind")
        .default_value("127.0.0.1")
        .value_name("ADDRESS")
    )
    cmd = cmd.arg(
        Arg.new("port")
        .short("p")
        .long("port")
        .help("Port number to listen on")
        .default_value("8000")
        .value_name("PORT")
    )

    matches: ArgMatches = cmd.get_matches()
    host: str | None = matches.get_one("host")
    port: str | None = matches.get_one("port")

    if host is not None and port is not None:
        print(f"Starting server at {host}:{port}")
