"""Python stubs for the env_logger Rust crate.

Install with: cookcrab install env_logger
"""

from __future__ import annotations

from typing import Self

class Timestamp:
    """An [RFC3339] formatted timestamp.

The timestamp implements [`Display`] and can be written to a [`Formatter`].

[RFC3339]: https://www.ietf.org/rfc/rfc3339.txt
[`Display`]: std::fmt::Display"""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class Formatter:
    """A formatter to write logs into.

`Formatter` implements the standard [`Write`] trait for writing log records.
It also supports terminal styling using ANSI escape codes.

# Examples

Use the [`writeln`] macro to format a log record.
An instance of a `Formatter` is passed to an `env_logger` format as `buf`:

```
use std::io::Write;

let mut builder = env_logger::Builder::new();

builder.format(|buf, record| writeln!(buf, "{}: {}", record.level(), record.args()));
```

[`Write`]: std::io::Write
[`writeln`]: std::writeln"""

    def timestamp(self) -> Timestamp: ...

    def timestamp_seconds(self) -> Timestamp: ...

    def timestamp_millis(self) -> Timestamp: ...

    def timestamp_micros(self) -> Timestamp: ...

    def timestamp_nanos(self) -> Timestamp: ...

    def default_level_style(self, level: Level) -> Style: ...

    def write(self, buf: object) -> int: ...

    def flush(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class ConfigurableFormat:
    """A [custom format][crate::Builder::format] with settings for which fields to show"""

    def format(self, formatter: Formatter, record: Record) -> object: ...

    def level(self, write: bool) -> Self: ...

    def file(self, write: bool) -> Self: ...

    def line_number(self, write: bool) -> Self: ...

    def module_path(self, write: bool) -> Self: ...

    def target(self, write: bool) -> Self: ...

    def indent(self, indent: int | None) -> Self: ...

    def timestamp(self, timestamp: TimestampPrecision | None) -> Self: ...

    def suffix(self, suffix: object) -> Self: ...

    def key_values(self, format: F) -> Self: ...

    @staticmethod
    def default() -> "ConfigurableFormat": ...

    def format(self, formatter: Formatter, record: Record) -> object: ...

class Builder:
    """`Builder` acts as builder for initializing a `Logger`.

It can be used to customize the log format, change the environment variable used
to provide the logging directives and also set the default log level filter.

# Examples

```
# use std::io::Write;
use env_logger::Builder;
use log::{LevelFilter, error, info};

let mut builder = Builder::from_default_env();

builder
.format(|buf, record| writeln!(buf, "{} - {}", record.level(), record.args()))
.filter(None, LevelFilter::Info)
.init();

error!("error message");
info!("info message");
```"""

    @staticmethod
    def default() -> "Builder": ...

    @staticmethod
    def new() -> "Builder": ...

    @staticmethod
    def from_env(env: E) -> "Builder": ...

    def parse_env(self, env: E) -> Self: ...

    @staticmethod
    def from_default_env() -> "Builder": ...

    def parse_default_env(self) -> Self: ...

    def format(self, format: F) -> Self: ...

    def default_format(self) -> Self: ...

    def format_level(self, write: bool) -> Self: ...

    def format_file(self, write: bool) -> Self: ...

    def format_line_number(self, write: bool) -> Self: ...

    def format_source_path(self, write: bool) -> Self: ...

    def format_module_path(self, write: bool) -> Self: ...

    def format_target(self, write: bool) -> Self: ...

    def format_indent(self, indent: int | None) -> Self: ...

    def format_timestamp(self, timestamp: TimestampPrecision | None) -> Self: ...

    def format_timestamp_secs(self) -> Self: ...

    def format_timestamp_millis(self) -> Self: ...

    def format_timestamp_micros(self) -> Self: ...

    def format_timestamp_nanos(self) -> Self: ...

    def format_suffix(self, suffix: object) -> Self: ...

    def format_key_values(self, format: F) -> Self: ...

    def filter_module(self, module: str, level: LevelFilter) -> Self: ...

    def filter_level(self, level: LevelFilter) -> Self: ...

    def filter(self, module: object, level: LevelFilter) -> Self: ...

    def parse_filters(self, filters: str) -> Self: ...

    def target(self, target: Target) -> Self: ...

    def write_style(self, write_style: WriteStyle) -> Self: ...

    def parse_write_style(self, write_style: str) -> Self: ...

    def is_test(self, is_test: bool) -> Self: ...

    def try_init(self) -> None: ...

    def init(self) -> None: ...

    def build(self) -> Logger: ...

    def fmt(self, f: Formatter) -> Result: ...

class Logger:
    """The env logger.

This struct implements the `Log` trait from the [`log` crate][log-crate-url],
which allows it to act as a logger.

The [`init()`], [`try_init()`], [`Builder::init()`] and [`Builder::try_init()`]
methods will each construct a `Logger` and immediately initialize it as the
default global logger.

If you'd instead need access to the constructed `Logger`, you can use
the associated [`Builder`] and install it with the
[`log` crate][log-crate-url] directly.

[log-crate-url]: https://docs.rs/log
[`init()`]: fn.init.html
[`try_init()`]: fn.try_init.html
[`Builder::init()`]: struct.Builder.html#method.init
[`Builder::try_init()`]: struct.Builder.html#method.try_init
[`Builder`]: struct.Builder.html"""

    @staticmethod
    def from_env(env: E) -> "Logger": ...

    @staticmethod
    def from_default_env() -> "Logger": ...

    def filter(self) -> LevelFilter: ...

    def matches(self, record: Record) -> bool: ...

    def enabled(self, metadata: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

class Env:
    """Set of environment variables to configure from.

# Default environment variables

By default, the `Env` will read the following environment variables:

- `RUST_LOG`: the level filter
- `RUST_LOG_STYLE`: whether or not to print styles with records.

These sources can be configured using the builder methods on `Env`."""

    @staticmethod
    def new() -> "Env": ...

    def filter(self, filter_env: E) -> Self: ...

    def filter_or(self, filter_env: E, default: V) -> Self: ...

    def default_filter_or(self, default: V) -> Self: ...

    def write_style(self, write_style_env: E) -> Self: ...

    def write_style_or(self, write_style_env: E, default: V) -> Self: ...

    def default_write_style_or(self, default: V) -> Self: ...

    @staticmethod
    def from_(filter_env: T) -> "Env": ...

    @staticmethod
    def default() -> "Env": ...

class Target:
    """Log target, either `stdout`, `stderr` or a custom pipe."""
    Stdout: "Target"
    Stderr: "Target"
    Pipe: "Target"

    def fmt(self, f: Formatter) -> Result: ...

class WriteStyle:
    """Whether or not to print styles to the target."""
    Auto: "WriteStyle"
    Always: "WriteStyle"
    Never: "WriteStyle"

    @staticmethod
    def from_(choice: ColorChoice) -> "WriteStyle": ...

class TimestampPrecision:
    """Formatting precision of timestamps.

Seconds give precision of full seconds, milliseconds give thousands of a
second (3 decimal digits), microseconds are millionth of a second (6 decimal
digits) and nanoseconds are billionth of a second (9 decimal digits)."""
    Seconds: "TimestampPrecision"
    Millis: "TimestampPrecision"
    Micros: "TimestampPrecision"
    Nanos: "TimestampPrecision"

    @staticmethod
    def default() -> "TimestampPrecision": ...

"""Null Key Value Format

This function is intended to be passed to
[`Builder::format_key_values`](crate::Builder::format_key_values).

This key value format simply ignores any key/value fields and doesn't include them in the
output."""
def hidden_kv_format(_formatter: Formatter, _fields: dynSource) -> object: ...

"""Default Key Value Format

This function is intended to be passed to
[`Builder::format_key_values`](crate::Builder::format_key_values).

This is the default key/value format. Which uses an "=" as the separator between the key and
value and a " " between each pair.

For example: `ip=127.0.0.1 port=123456 path=/example`"""
def default_kv_format(formatter: Formatter, fields: dynSource) -> object: ...

"""Attempts to initialize the global logger with an env logger.

This should be called early in the execution of a Rust program. Any log
events that occur before initialization will be ignored.

# Errors

This function will fail if it is called more than once, or if another
library has already initialized a global logger."""
def try_init() -> None: ...

"""Initializes the global logger with an env logger.

This should be called early in the execution of a Rust program. Any log
events that occur before initialization will be ignored.

# Panics

This function will panic if it is called more than once, or if another
library has already initialized a global logger."""
def init() -> None: ...

"""Attempts to initialize the global logger with an env logger from the given
environment variables.

This should be called early in the execution of a Rust program. Any log
events that occur before initialization will be ignored.

# Examples

Initialise a logger using the `MY_LOG` environment variable for filters
and `MY_LOG_STYLE` for writing colors:

```
use env_logger::{Builder, Env};

# fn run() -> Result<(), Box<dyn ::std::error::Error>> {
let env = Env::new().filter("MY_LOG").write_style("MY_LOG_STYLE");

env_logger::try_init_from_env(env)?;

Ok(())
# }
# run().unwrap();
```

# Errors

This function will fail if it is called more than once, or if another
library has already initialized a global logger."""
def try_init_from_env(env: E) -> None: ...

"""Initializes the global logger with an env logger from the given environment
variables.

This should be called early in the execution of a Rust program. Any log
events that occur before initialization will be ignored.

# Examples

Initialise a logger using the `MY_LOG` environment variable for filters
and `MY_LOG_STYLE` for writing colors:

```
use env_logger::{Builder, Env};

let env = Env::new().filter("MY_LOG").write_style("MY_LOG_STYLE");

env_logger::init_from_env(env);
```

# Panics

This function will panic if it is called more than once, or if another
library has already initialized a global logger."""
def init_from_env(env: E) -> None: ...

"""Create a new builder with the default environment variables.

The builder can be configured before being initialized.
This is a convenient way of calling [`Builder::from_default_env`].

[`Builder::from_default_env`]: struct.Builder.html#method.from_default_env"""
def builder() -> Builder: ...

"""Create a builder from the given environment variables.

The builder can be configured before being initialized."""
def from_env(env: E) -> Builder: ...

__all__: list[str] = ["hidden_kv_format", "default_kv_format", "try_init", "init", "try_init_from_env", "init_from_env", "builder", "from_env", "Timestamp", "Formatter", "ConfigurableFormat", "Builder", "Logger", "Env", "Target", "WriteStyle", "TimestampPrecision"]
