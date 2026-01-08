# anyhow Examples

[anyhow](https://crates.io/crates/anyhow) provides flexible concrete Error type built on `std::error::Error`. It's ideal for applications where you want easy error handling without defining custom error types.

## Setup

Generate and install the stubs:

```bash
# Generate stubs
cookcrab generate anyhow -o /path/to/stubs

# Install stubs
python3 -m pip install -e /path/to/stubs/anyhow
```

## Usage

```python
from spicycrab_anyhow import Error, Result

def divide(a: int, b: int) -> Result[int, Error]:
    if b == 0:
        return Result.Err(Error.msg("Division by zero"))
    return Result.Ok(a // b)
```

This transpiles to idiomatic Rust:

```rust
pub fn divide(a: i64, b: i64) -> anyhow::Result<i64> {
    if b == 0 {
        return Err(anyhow::anyhow!("Division by zero"));
    }
    Ok(a / b)
}
```

## Key Features

- **Result[T, Error]**: Maps to `anyhow::Result<T>`
- **Result.Ok(value)**: Creates success variant
- **Result.Err(Error.msg("..."))**: Creates error with message
- **Automatic ? operator**: Error propagation in Result-returning functions

## Examples

| Example | Description |
|---------|-------------|
| [anyhow_01_basic_result.py](anyhow_01_basic_result.py) | Basic Result usage with Ok and Err |
| [anyhow_02_error_propagation.py](anyhow_02_error_propagation.py) | Error propagation with the ? operator |
| [anyhow_03_parse_and_validate.py](anyhow_03_parse_and_validate.py) | Input validation with descriptive errors |
| [anyhow_04_path_validation.py](anyhow_04_path_validation.py) | Path validation returning descriptive errors |
| [anyhow_05_chain_operations.py](anyhow_05_chain_operations.py) | Chaining multiple Result-returning operations |
| [anyhow_06_calculator.py](anyhow_06_calculator.py) | Calculator with Result error handling |
| [anyhow_07_conditional_errors.py](anyhow_07_conditional_errors.py) | Checking Result status conditionally |
| [anyhow_08_batch_processing.py](anyhow_08_batch_processing.py) | Batch processing with error collection |

## Transpiling Examples

```bash
# Transpile an example
crabpy transpile anyhow_01_basic_result.py -o rust_basic_result -n basic_result

# Build and run
cd rust_basic_result
cargo build --release
./target/release/basic_result 10 2
```
