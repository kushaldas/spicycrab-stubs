# spicycrab-stubs

Python type stubs for Rust crates, enabling transpilation with [spicycrab](https://github.com/kushaldas/spicycrab).

## Quick Start

```bash
# Install spicycrab (includes cookcrab)
pip install spicycrab

# Generate stubs for any crate
cookcrab generate chrono -o ./stubs

# Install the generated stubs
pip install -e ./stubs/chrono

# Write Python code using the stubs
# Then transpile to Rust
crabpy transpile myapp.py -o rust_myapp -n myapp
```

## Available Stubs

Pre-generated stubs in `stubs/` directory:

| Crate | Version | Description |
|-------|---------|-------------|
| [actix-web](stubs/actix-web) | 4.12.1 | Powerful web framework |
| [actix-web-lab](stubs/actix-web-lab) | 0.24.3 | Experimental actix-web features |
| [anyhow](stubs/anyhow) | 1.0.100 | Flexible error handling |
| [base64](stubs/base64) | 0.22.1 | Base64 encoding/decoding |
| [chrono](stubs/chrono) | 0.4.42 | Date and time library |
| [clap](stubs/clap) | 4.5.54 | Command-line argument parser |
| [clap_builder](stubs/clap_builder) | 4.5.54 | clap builder components |
| [config](stubs/config) | 0.15.19 | Configuration management |
| [env_logger](stubs/env_logger) | 0.11.8 | Environment-based logging |
| [fern](stubs/fern) | 0.7.1 | Simple logging |
| [josekit](stubs/josekit) | 0.10.3 | JWT/JWE/JWS operations |
| [lazy_static](stubs/lazy_static) | 1.5.0 | Lazy static initialization |
| [log](stubs/log) | 0.4.29 | Logging facade |
| [native-tls](stubs/native-tls) | 0.2.14 | Native TLS bindings |
| [redis](stubs/redis) | 1.0.2 | Redis client |
| [reqwest](stubs/reqwest) | 0.13.1 | HTTP client |
| [rustls](stubs/rustls) | 0.23.36 | Modern TLS library |
| [rustls-pemfile](stubs/rustls-pemfile) | 2.2.0 | PEM file parsing for rustls |
| [serde](stubs/serde) | 1.0.228 | Serialization framework |
| [serde_json](stubs/serde_json) | 1.0.149 | JSON serialization |
| [sha2](stubs/sha2) | 0.10.9 | SHA-2 hash functions |
| [tokio](stubs/tokio) | 1.49.0 | Async runtime |
| [toml](stubs/toml) | 0.9.11 | TOML parsing |
| [ureq](stubs/ureq) | 3.1.4 | Simple HTTP client |

## Examples

Working examples for each crate in `examples/` directory (143 total):

| Crate | Examples | Description |
|-------|----------|-------------|
| [actix-web](examples/actix-web) | 16 | Web server routes, handlers, middleware |
| [anyhow](examples/anyhow) | 8 | Result/Error handling patterns |
| [base64](examples/base64) | 5 | Encoding/decoding operations |
| [chrono](examples/chrono) | 10 | Date, time, timezone operations |
| [clap](examples/clap) | 15 | CLI argument parsing patterns |
| [config](examples/config) | 5 | Configuration loading |
| [env_logger](examples/env_logger) | 5 | Environment-based logging |
| [fern](examples/fern) | 10 | Logging configuration |
| [josekit](examples/josekit) | 21 | JWT signing, JWE encryption |
| [native_tls](examples/native_tls) | 1 | TLS connections |
| [reqwest](examples/reqwest) | 10 | HTTP requests |
| [rustls](examples/rustls) | 10 | TLS configuration |
| [serde_json](examples/serde_json) | 5 | JSON parsing/serialization |
| [sha2](examples/sha2) | 5 | SHA-256/SHA-512 hashing |
| [tokio](examples/tokio) | 6 | Async tasks, channels, Arc/Mutex |
| [toml](examples/toml) | 5 | TOML parsing |
| [ureq](examples/ureq) | 5 | HTTP requests |

### Running Examples

```bash
cd demospace  # or any working directory

# Install stubs
pip install -e ../spicycrab-stubs/stubs/chrono

# Transpile an example
crabpy transpile ../spicycrab-stubs/examples/chrono/chrono_01_naive_date.py \
    -o rust_naive_date -n chrono_naive_date

# Build and run
cd rust_naive_date
cargo build --release
./target/release/chrono_naive_date
```

### Batch Transpile and Test

```bash
# Use shared target directory for faster builds
export RUSTC_WRAPPER=/path/to/sccache
export CARGO_TARGET_DIR=/tmp/spicycrab-test-target

# Transpile all examples for a crate
for f in ../spicycrab-stubs/examples/chrono/*.py; do
    name=$(basename "$f" .py)
    crabpy transpile "$f" -o "rust_$name" -n "$name"
done

# Build all
for dir in rust_chrono_*; do
    (cd "$dir" && cargo build --release)
done
```

## Repository Structure

```
spicycrab-stubs/
├── stubs/                         # Pre-generated stub packages
│   ├── actix-web/
│   ├── anyhow/
│   ├── base64/
│   ├── chrono/
│   ├── clap/
│   ├── config/
│   ├── env_logger/
│   ├── fern/
│   ├── josekit/
│   ├── log/
│   ├── native-tls/
│   ├── redis/
│   ├── reqwest/
│   ├── rustls/
│   ├── serde/
│   ├── serde_json/
│   ├── sha2/
│   ├── tokio/
│   ├── toml/
│   └── ureq/
├── examples/                      # Working examples
│   ├── actix-web/
│   ├── anyhow/
│   ├── base64/
│   ├── chrono/
│   ├── clap/
│   ├── config/
│   ├── env_logger/
│   ├── fern/
│   ├── josekit/
│   ├── reqwest/
│   ├── rustls/
│   ├── serde_json/
│   ├── sha2/
│   ├── tokio/
│   ├── toml/
│   └── ureq/
├── justfile                       # Tag management commands
└── README.md
```

## Generating New Stubs

Use `cookcrab` to automatically generate stubs for any Rust crate:

```bash
# Generate stubs for a crate
cookcrab generate <crate_name> -o ./stubs

# Example: generate a new crate's stubs
cookcrab generate uuid -o ./stubs

# Install for use
pip install -e ./stubs/<crate_name>
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
just tag chrono 0.4.42

# Push tags
git push origin main && git push origin chrono-0.4.42
```

## Contributing

1. Generate stubs: `cookcrab generate <crate> -o ./stubs`
2. Write examples in `examples/<crate>/`
3. Test transpilation and compilation
4. Create version tag: `just tag <crate> <version>`
5. Submit PR

## License

MIT
