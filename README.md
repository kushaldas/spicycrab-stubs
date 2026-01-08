# spicycrab-stubs

Python type stubs for Rust crates, enabling transpilation with [spicycrab](https://github.com/kushaldas/spicycrab).

## Quick Start

```bash
# Install spicycrab (includes cookcrab)
python3 -m pip install spicycrab

# Generate stubs for any crate
cookcrab generate chrono -o ./stubs

# Install the generated stubs
python3 -m pip install -e ./stubs/chrono

# Write Python code using the stubs
# Then transpile to Rust
crabpy transpile myapp.py -o rust_myapp -n myapp
```

## Available Stubs

Pre-generated stubs in `stubs/` directory:

| Crate | Version | Description |
|-------|---------|-------------|
| [anyhow](stubs/anyhow) | 1.0.x | Flexible error handling |
| [chrono](stubs/chrono) | 0.4.x | Date and time library |
| [clap](stubs/clap) | 4.5.x | Command-line argument parser |
| [clap_builder](stubs/clap_builder) | 4.5.x | clap builder components |
| [fern](stubs/fern) | 0.7.x | Simple logging |
| [log](stubs/log) | 0.4.x | Logging facade |

## Examples

Working examples for each crate in `examples/` directory:

| Crate | Examples | Description |
|-------|----------|-------------|
| [anyhow](examples/anyhow) | 8 | Result/Error handling patterns |
| [chrono](examples/chrono) | 10 | Date, time, timezone operations |
| [clap](examples/clap) | 15 | CLI argument parsing patterns |
| [fern](examples/fern) | 10 | Logging configuration |

Each example directory contains a README with usage instructions.

### Running Examples

```bash
cd demospace  # or any working directory

# Install stubs
python3 -m pip install -e ../spicycrab-stubs/stubs/chrono

# Transpile an example
crabpy transpile ../spicycrab-stubs/examples/chrono/chrono_01_naive_date.py \
    -o rust_naive_date -n chrono_naive_date

# Build and run
cd rust_naive_date
cargo build --release
./target/release/chrono_naive_date
```

## Repository Structure

```
spicycrab-stubs/
├── stubs/                         # Pre-generated stub packages
│   ├── anyhow/
│   │   ├── pyproject.toml
│   │   └── spicycrab_anyhow/
│   │       ├── __init__.py        # Python stubs
│   │       └── _spicycrab.toml    # Transpilation mappings
│   ├── chrono/
│   ├── clap/
│   ├── clap_builder/
│   ├── fern/
│   └── log/
├── examples/                      # Working examples
│   ├── anyhow/
│   │   ├── README.md
│   │   └── anyhow_*.py
│   ├── chrono/
│   │   ├── README.md
│   │   └── chrono_*.py
│   ├── clap/
│   │   ├── README.md
│   │   └── clap_*.py
│   └── fern/
│       ├── README.md
│       └── fern_*.py
├── justfile                       # Tag management commands
└── README.md
```

## Generating New Stubs

Use `cookcrab` to automatically generate stubs for any Rust crate:

```bash
# Generate stubs for a crate
cookcrab generate <crate_name> -o ./stubs

# Example: generate tokio stubs
cookcrab generate tokio -o ./stubs

# Validate generated stubs
cookcrab validate ./stubs/<crate_name>

# Install for use
python3 -m pip install -e ./stubs/<crate_name>
```

## Stub Package Structure

Each stub package contains:

### `pyproject.toml`

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "spicycrab-<crate>"
version = "<crate_version>"
description = "spicycrab type stubs for the <crate> Rust crate"
requires-python = ">=3.11"

[project.entry-points."spicycrab.stubs"]
<crate> = "spicycrab_<crate>"

[tool.hatch.build.targets.wheel]
packages = ["spicycrab_<crate>"]
```

### `spicycrab_<crate>/__init__.py`

Python stubs mirroring the Rust API:

```python
"""Python stubs for the <crate> Rust crate."""
from typing import Self, Generic, TypeVar

T = TypeVar("T")

class SomeType:
    @staticmethod
    def new(arg: str) -> "SomeType": ...

    def method(self, x: int) -> Self: ...
```

### `spicycrab_<crate>/_spicycrab.toml`

Transpilation mappings:

```toml
[package]
name = "<crate>"
rust_crate = "<crate>"
rust_version = "<version>"
python_module = "spicycrab_<crate>"

[cargo.dependencies]
<crate> = { version = "<version>" }

[[mappings.functions]]
python = "<crate>.SomeType.new"
rust_code = "<crate>::SomeType::new({arg0})"

[[mappings.methods]]
python = "SomeType.method"
rust_code = "{self}.method({arg0})"
returns_self = true

[[mappings.types]]
python = "SomeType"
rust = "<crate>::SomeType"
```

## Mapping Reference

### Function Mappings

For static methods and constructors:

```toml
[[mappings.functions]]
python = "module.Type.function"
rust_code = "module::Type::function({arg0}, {arg1})"
rust_imports = ["module::Type"]
```

### Method Mappings

For instance methods (use `{self}` placeholder):

```toml
[[mappings.methods]]
python = "Type.method"
rust_code = "{self}.method({arg0})"
returns_self = true  # For builder pattern
```

### Type Mappings

Map Python types to Rust types:

```toml
[[mappings.types]]
python = "MyType"
rust = "crate::MyType"
```

### Placeholders

| Placeholder | Description |
|-------------|-------------|
| `{arg0}`, `{arg1}`, ... | Positional arguments |
| `{self}` | The instance (for methods) |

## Version Tags

Tags follow the format: `<crate>-<version>`

```bash
# Create a version tag
just tag chrono 0.4.38

# Push tags
git push origin main && git push origin chrono-0.4.38
```

## Contributing

1. Generate stubs: `cookcrab generate <crate> -o ./stubs`
2. Write examples in `examples/<crate>/`
3. Test transpilation and compilation
4. Create version tag: `just tag <crate> <version>`
5. Submit PR

## License

MIT
