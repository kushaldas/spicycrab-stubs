# fern Examples

[fern](https://crates.io/crates/fern) is a simple, efficient logging library for Rust. It integrates with the standard `log` crate facade.

## Setup

Generate and install the stubs:

```bash
# Generate stubs (fern uses log crate for LevelFilter)
cookcrab generate fern -o /path/to/stubs
cookcrab generate log -o /path/to/stubs

# Install stubs
python3 -m pip install -e /path/to/stubs/fern
python3 -m pip install -e /path/to/stubs/log
```

## Usage

```python
from spicycrab_fern import Dispatch
from spicycrab_log import LevelFilter

def setup_logger() -> None:
    dispatch: Dispatch = Dispatch.new()
    dispatch = dispatch.level(LevelFilter.Info)
    dispatch = dispatch.chain(std_io_stdout())
    dispatch.apply()

def main() -> None:
    setup_logger()
    print("Logger initialized!")
```

This transpiles to idiomatic Rust:

```rust
pub fn setup_logger() {
    let mut dispatch: fern::Dispatch = fern::Dispatch::new();
    dispatch = dispatch.level(log::LevelFilter::Info);
    dispatch = dispatch.chain(std::io::stdout());
    dispatch.apply();
}

pub fn main() {
    setup_logger();
    println!("Logger initialized!");
}
```

## Key Types

| Python Type | Rust Type | Description |
|-------------|-----------|-------------|
| `Dispatch` | `fern::Dispatch` | Logger configuration builder |
| `LevelFilter` | `log::LevelFilter` | Log level filtering |

## LevelFilter Values

| Python | Rust | Description |
|--------|------|-------------|
| `LevelFilter.Off` | `log::LevelFilter::Off` | Disable all logging |
| `LevelFilter.Error` | `log::LevelFilter::Error` | Errors only |
| `LevelFilter.Warn` | `log::LevelFilter::Warn` | Warnings and above |
| `LevelFilter.Info` | `log::LevelFilter::Info` | Info and above |
| `LevelFilter.Debug` | `log::LevelFilter::Debug` | Debug and above |
| `LevelFilter.Trace` | `log::LevelFilter::Trace` | All messages |

## Dispatch Methods

| Method | Description |
|--------|-------------|
| `Dispatch.new()` | Create new dispatcher |
| `.level(LevelFilter)` | Set minimum log level |
| `.level_for(module, LevelFilter)` | Set level for specific module |
| `.chain(output)` | Add output destination |
| `.apply()` | Apply configuration globally |

## Examples

| Example | Description |
|---------|-------------|
| [fern_01_basic_setup.py](fern_01_basic_setup.py) | Basic logger outputting to stdout |
| [fern_02_log_levels.py](fern_02_log_levels.py) | Using different log levels |
| [fern_03_stdout_logging.py](fern_03_stdout_logging.py) | Logging to stdout with std::io |
| [fern_04_stderr_logging.py](fern_04_stderr_logging.py) | Logging errors to stderr |
| [fern_05_module_levels.py](fern_05_module_levels.py) | Module-specific log levels |
| [fern_06_chained_outputs.py](fern_06_chained_outputs.py) | Multiple output destinations |
| [fern_07_colored_output.py](fern_07_colored_output.py) | Debug-level stdout logger |
| [fern_08_panic_on_error.py](fern_08_panic_on_error.py) | Error-level filtering |
| [fern_09_date_based_files.py](fern_09_date_based_files.py) | Trace-level verbose logging |
| [fern_10_complete_setup.py](fern_10_complete_setup.py) | Production-ready configuration |

## Transpiling Examples

```bash
# Transpile an example
crabpy transpile fern_01_basic_setup.py -o rust_basic_setup -n fern_basic_setup

# Build and run
cd rust_basic_setup
cargo build --release
./target/release/fern_basic_setup
```

## Notes

- fern integrates with the standard `log` crate facade
- `LevelFilter` comes from `spicycrab_log`, not `spicycrab_fern`
- Use `.chain()` to add outputs (stdout, stderr, files)
- Call `.apply()` to activate the logger configuration
- The builder pattern allows method chaining
