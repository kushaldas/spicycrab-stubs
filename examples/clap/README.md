# clap Examples

[clap](https://crates.io/crates/clap) is a full-featured, fast Command Line Argument Parser for Rust. These examples use the builder API pattern.

## Setup

Generate and install the stubs:

```bash
# Generate stubs (clap depends on clap_builder)
cookcrab generate clap -o /path/to/stubs
cookcrab generate clap_builder -o /path/to/stubs

# Install stubs
python3 -m pip install -e /path/to/stubs/clap
python3 -m pip install -e /path/to/stubs/clap_builder
```

## Usage

```python
from spicycrab_clap import Arg, ArgAction, Command

def main() -> None:
    cmd: Command = Command.new("myapp")
    cmd = cmd.version("1.0")
    cmd = cmd.about("My application")

    # Add a required argument
    arg: Arg = Arg.new("input")
    arg = arg.help("Input file")
    arg = arg.required(True)
    cmd = cmd.arg(arg)

    # Add a boolean flag
    flag: Arg = Arg.new("verbose")
    flag = flag.short('v')
    flag = flag.long("verbose")
    flag = flag.action(ArgAction.SetTrue)
    cmd = cmd.arg(flag)

    matches = cmd.get_matches()
```

This transpiles to idiomatic Rust:

```rust
pub fn main() {
    let mut cmd: clap::Command = clap::Command::new("myapp");
    cmd = cmd.version("1.0");
    cmd = cmd.about("My application");

    let mut arg: clap::Arg = clap::Arg::new("input");
    arg = arg.help("Input file");
    arg = arg.required(true);
    cmd = cmd.arg(arg);

    let mut flag: clap::Arg = clap::Arg::new("verbose");
    flag = flag.short('v');
    flag = flag.long("verbose");
    flag = flag.action(clap::ArgAction::SetTrue);
    cmd = cmd.arg(flag);

    let matches = cmd.get_matches();
}
```

## Key Types

| Python Type | Rust Type | Description |
|-------------|-----------|-------------|
| `Command` | `clap::Command` | CLI application builder |
| `Arg` | `clap::Arg` | Argument definition |
| `ArgAction` | `clap::ArgAction` | What happens when arg is parsed |
| `ArgGroup` | `clap::ArgGroup` | Group of related arguments |
| `ArgMatches` | `clap::ArgMatches` | Parsed argument results |

## ArgAction Values

| Python | Rust | Description |
|--------|------|-------------|
| `ArgAction.Set` | `clap::ArgAction::Set` | Store single value |
| `ArgAction.SetTrue` | `clap::ArgAction::SetTrue` | Set flag to true |
| `ArgAction.SetFalse` | `clap::ArgAction::SetFalse` | Set flag to false |
| `ArgAction.Count` | `clap::ArgAction::Count` | Count occurrences |
| `ArgAction.Append` | `clap::ArgAction::Append` | Collect multiple values |

## Examples

| Example | Description |
|---------|-------------|
| [clap_01_basic_args.py](clap_01_basic_args.py) | Basic argument parsing |
| [clap_02_flags.py](clap_02_flags.py) | Boolean flags with SetTrue |
| [clap_03_required_args.py](clap_03_required_args.py) | Required vs optional arguments |
| [clap_04_default_values.py](clap_04_default_values.py) | Default values for arguments |
| [clap_05_positional_args.py](clap_05_positional_args.py) | Positional arguments |
| [clap_06_multiple_values.py](clap_06_multiple_values.py) | Multiple values with Append |
| [clap_07_subcommands.py](clap_07_subcommands.py) | Subcommands like git add/commit |
| [clap_08_arg_groups.py](clap_08_arg_groups.py) | Mutually exclusive argument groups |
| [clap_09_conflicting_args.py](clap_09_conflicting_args.py) | Arguments that conflict |
| [clap_10_requires.py](clap_10_requires.py) | Arguments requiring other arguments |
| [clap_11_count_flag.py](clap_11_count_flag.py) | Counting flag occurrences (-vvv) |
| [clap_12_help_version.py](clap_12_help_version.py) | Custom version and about text |
| [clap_13_hidden_args.py](clap_13_hidden_args.py) | Hidden arguments (debug flags) |
| [clap_14_global_args.py](clap_14_global_args.py) | Global args for all subcommands |
| [clap_15_full_app.py](clap_15_full_app.py) | Complete application example |

## Transpiling Examples

```bash
# Transpile an example
crabpy transpile clap_01_basic_args.py -o rust_basic_args -n clap_basic_args

# Build and run
cd rust_basic_args
cargo build --release
./target/release/clap_basic_args --help
```

## Notes

- clap uses a builder pattern where each method returns Self
- Use `ArgAction.SetTrue` for boolean flags
- Use `ArgAction.Count` for verbosity flags (-v, -vv, -vvv)
- Character literals like `'v'` for short options are preserved
