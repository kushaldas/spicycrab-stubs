# chrono Examples

[chrono](https://crates.io/crates/chrono) is Rust's comprehensive date and time library. It provides timezone-aware and naive datetime types, duration calculations, and formatting.

## Setup

Generate and install the stubs:

```bash
# Generate stubs
cookcrab generate chrono -o /path/to/stubs

# Install stubs
python3 -m pip install -e /path/to/stubs/chrono
```

## Usage

```python
from spicycrab_chrono import NaiveDate, Utc, Local, TimeDelta

def main() -> None:
    # Create a date
    date: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 7, 4)
    if date is not None:
        print(f"Year: {date.year()}")

    # Get current UTC time
    now = Utc.now()
    print(f"UTC: {now.to_rfc3339()}")

    # Work with durations
    one_day: TimeDelta = TimeDelta.days(1)
    print(f"Hours in a day: {one_day.num_hours()}")
```

This transpiles to idiomatic Rust using `if let Some`:

```rust
pub fn main() {
    let date: Option<chrono::NaiveDate> = chrono::NaiveDate::from_ymd_opt(2024, 7, 4);
    if let Some(date) = date {
        println!("Year: {}", date.year());
    }

    let now = chrono::Utc::now();
    println!("UTC: {}", now.to_rfc3339());

    let one_day: chrono::TimeDelta = chrono::TimeDelta::days(1);
    println!("Hours in a day: {}", one_day.num_hours());
}
```

## Key Types

| Python Type | Rust Type | Description |
|-------------|-----------|-------------|
| `NaiveDate` | `chrono::NaiveDate` | Date without timezone |
| `NaiveTime` | `chrono::NaiveTime` | Time without timezone |
| `NaiveDateTime` | `chrono::NaiveDateTime` | DateTime without timezone |
| `DateTime` | `chrono::DateTime<Tz>` | Timezone-aware datetime |
| `Utc` | `chrono::Utc` | UTC timezone |
| `Local` | `chrono::Local` | Local timezone |
| `TimeDelta` | `chrono::TimeDelta` | Duration/time difference |
| `Weekday` | `chrono::Weekday` | Day of week enum |
| `Months` | `chrono::Months` | Calendar months duration |
| `Days` | `chrono::Days` | Calendar days duration |
| `FixedOffset` | `chrono::FixedOffset` | Fixed UTC offset timezone |

## Examples

| Example | Description |
|---------|-------------|
| [chrono_01_naive_date.py](chrono_01_naive_date.py) | Creating dates, accessing components, leap year check |
| [chrono_02_naive_time.py](chrono_02_naive_time.py) | Creating times, seconds from midnight |
| [chrono_03_naive_datetime.py](chrono_03_naive_datetime.py) | Combining date/time, timestamps |
| [chrono_04_utc_datetime.py](chrono_04_utc_datetime.py) | UTC time, RFC3339 format, timestamps |
| [chrono_05_local_datetime.py](chrono_05_local_datetime.py) | Local time, naive local conversion |
| [chrono_06_timedelta.py](chrono_06_timedelta.py) | Duration operations and conversions |
| [chrono_07_weekday.py](chrono_07_weekday.py) | Weekday enum, day numbering, succ/pred |
| [chrono_08_date_arithmetic.py](chrono_08_date_arithmetic.py) | Adding/subtracting days from dates |
| [chrono_09_months_days.py](chrono_09_months_days.py) | Adding months with overflow handling |
| [chrono_10_fixed_offset.py](chrono_10_fixed_offset.py) | Fixed timezone offsets (UTC+5:30, etc.) |

## Transpiling Examples

```bash
# Transpile an example
crabpy transpile chrono_01_naive_date.py -o rust_naive_date -n chrono_naive_date

# Build and run
cd rust_naive_date
cargo build --release
./target/release/chrono_naive_date
```

## Notes

- Methods like `year()`, `month()`, `day()` require the `Datelike` trait (auto-imported)
- Methods like `hour()`, `minute()`, `second()` require the `Timelike` trait (auto-imported)
- Use `T | None` pattern for fallible constructors like `from_ymd_opt`
