"""Example 07: Subcommands like git add/commit.

Demonstrates:
- Adding subcommands to a command
- Getting subcommand name and matches
- Subcommand-specific arguments

Usage:
    ./subcommands add file.txt
    ./subcommands remove --force item
    ./subcommands list
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    add_cmd: Command = Command.new("add")
    add_cmd = add_cmd.about("Add an item")
    add_cmd = add_cmd.arg(
        Arg.new("item").help("Item to add").required(True).index(1)
    )

    remove_cmd: Command = Command.new("remove")
    remove_cmd = remove_cmd.about("Remove an item")
    remove_cmd = remove_cmd.arg(
        Arg.new("item").help("Item to remove").required(True).index(1)
    )
    remove_cmd = remove_cmd.arg(
        Arg.new("force")
        .short("f")
        .long("force")
        .help("Force removal")
        .action(ArgAction.SetTrue())
    )

    list_cmd: Command = Command.new("list")
    list_cmd = list_cmd.about("List all items")

    cmd: Command = Command.new("items")
    cmd = cmd.about("Manage items with subcommands")
    cmd = cmd.subcommand(add_cmd)
    cmd = cmd.subcommand(remove_cmd)
    cmd = cmd.subcommand(list_cmd)
    cmd = cmd.subcommand_required(True)

    matches: ArgMatches = cmd.get_matches()
    subcmd_name: str | None = matches.subcommand_name()

    if subcmd_name == "add":
        sub_matches: ArgMatches | None = matches.subcommand_matches("add")
        if sub_matches is not None:
            item: str | None = sub_matches.get_one("item")
            if item is not None:
                print(f"Adding item: {item}")
    elif subcmd_name == "remove":
        sub_matches2: ArgMatches | None = matches.subcommand_matches("remove")
        if sub_matches2 is not None:
            item2: str | None = sub_matches2.get_one("item")
            force: bool = sub_matches2.get_flag("force")
            if item2 is not None:
                if force:
                    print(f"Force removing item: {item2}")
                else:
                    print(f"Removing item: {item2}")
    elif subcmd_name == "list":
        print("Listing all items...")
