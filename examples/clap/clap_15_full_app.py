"""Example 15: Full application with multiple features.

Demonstrates:
- Combining multiple clap features
- Complete CLI application pattern
- Subcommands with options and flags

Usage:
    ./full_app --config app.toml init
    ./full_app -v task add "Buy groceries" --priority high
    ./full_app task list --filter pending
    ./full_app task done 1
"""
from spicycrab_clap import Arg, ArgAction, ArgMatches, Command


def main() -> None:
    # Task add subcommand
    add_cmd: Command = Command.new("add")
    add_cmd = add_cmd.about("Add a new task")
    add_cmd = add_cmd.arg(
        Arg.new("description")
        .help("Task description")
        .required(True)
        .index(1)
    )
    add_cmd = add_cmd.arg(
        Arg.new("priority")
        .short("p")
        .long("priority")
        .help("Task priority")
        .default_value("medium")
    )
    add_cmd = add_cmd.arg(
        Arg.new("tags")
        .short("t")
        .long("tag")
        .help("Add tags to the task")
        .action(ArgAction.Append())
    )

    # Task list subcommand
    list_cmd: Command = Command.new("list")
    list_cmd = list_cmd.about("List all tasks")
    list_cmd = list_cmd.arg(
        Arg.new("filter")
        .short("f")
        .long("filter")
        .help("Filter tasks by status")
        .default_value("all")
    )
    list_cmd = list_cmd.arg(
        Arg.new("sort")
        .short("s")
        .long("sort")
        .help("Sort by field")
        .default_value("created")
    )

    # Task done subcommand
    done_cmd: Command = Command.new("done")
    done_cmd = done_cmd.about("Mark a task as done")
    done_cmd = done_cmd.arg(
        Arg.new("task_id")
        .help("Task ID to mark as done")
        .required(True)
        .index(1)
    )

    # Task subcommand group
    task_cmd: Command = Command.new("task")
    task_cmd = task_cmd.about("Manage tasks")
    task_cmd = task_cmd.subcommand(add_cmd)
    task_cmd = task_cmd.subcommand(list_cmd)
    task_cmd = task_cmd.subcommand(done_cmd)
    task_cmd = task_cmd.subcommand_required(True)

    # Init subcommand
    init_cmd: Command = Command.new("init")
    init_cmd = init_cmd.about("Initialize the application")

    # Main command
    cmd: Command = Command.new("taskmaster")
    cmd = cmd.version("1.0.0")
    cmd = cmd.about("A task management CLI application")
    cmd = cmd.arg(
        Arg.new("config")
        .short("c")
        .long("config")
        .help("Configuration file path")
        .default_value("config.toml")
        .global_(True)
    )
    cmd = cmd.arg(
        Arg.new("verbose")
        .short("v")
        .long("verbose")
        .help("Enable verbose output")
        .action(ArgAction.SetTrue())
        .global_(True)
    )
    cmd = cmd.subcommand(task_cmd)
    cmd = cmd.subcommand(init_cmd)
    cmd = cmd.subcommand_required(True)

    matches: ArgMatches = cmd.get_matches()
    config_path: str | None = matches.get_one("config")
    verbose: bool = matches.get_flag("verbose")
    subcmd_name: str | None = matches.subcommand_name()

    if verbose and config_path is not None:
        print(f"[INFO] Using config: {config_path}")

    if subcmd_name == "init":
        print("Initializing taskmaster...")
        print("Created config file and database.")

    elif subcmd_name == "task":
        task_matches: ArgMatches | None = matches.subcommand_matches("task")
        if task_matches is not None:
            task_subcmd: str | None = task_matches.subcommand_name()

            if task_subcmd == "add":
                add_matches: ArgMatches | None = task_matches.subcommand_matches("add")
                if add_matches is not None:
                    desc: str | None = add_matches.get_one("description")
                    priority: str | None = add_matches.get_one("priority")
                    tags: list[str] = add_matches.get_many("tags")

                    if desc is not None:
                        print(f"Adding task: {desc}")
                        if priority is not None:
                            print(f"  Priority: {priority}")
                        if len(tags) > 0:
                            print(f"  Tags: {tags}")

            elif task_subcmd == "list":
                list_matches: ArgMatches | None = task_matches.subcommand_matches(
                    "list"
                )
                if list_matches is not None:
                    filter_val: str | None = list_matches.get_one("filter")
                    sort_val: str | None = list_matches.get_one("sort")
                    print("Listing tasks...")
                    if filter_val is not None:
                        print(f"  Filter: {filter_val}")
                    if sort_val is not None:
                        print(f"  Sort: {sort_val}")

            elif task_subcmd == "done":
                done_matches: ArgMatches | None = task_matches.subcommand_matches(
                    "done"
                )
                if done_matches is not None:
                    task_id: str | None = done_matches.get_one("task_id")
                    if task_id is not None:
                        print(f"Marking task {task_id} as done")
