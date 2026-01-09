"""Python stubs for the log Rust crate.

Install with: cookcrab install log
"""

from __future__ import annotations

from typing import Self

class Record:
    """The "payload" of a log message.

# Use

`Record` structures are passed as parameters to the [`log`][method.log]
method of the [`Log`] trait. Logger implementors manipulate these
structures in order to display log messages. `Record`s are automatically
created by the [`log!`] macro and so are not seen by log users.

Note that the [`level()`] and [`target()`] accessors are equivalent to
`self.metadata().level()` and `self.metadata().target()` respectively.
These methods are provided as a convenience for users of this structure.

# Example

The following example shows a simple logger that displays the level,
module path, and message of any `Record` that is passed to it.

```
struct SimpleLogger;

impl log::Log for SimpleLogger {
fn enabled(&self, _metadata: &log::Metadata) -> bool {
true
}

fn log(&self, record: &log::Record) {
if !self.enabled(record.metadata()) {
return;
}

println!("{}:{} -- {}",
record.level(),
record.target(),
record.args());
}
fn flush(&self) {}
}
```

[method.log]: trait.Log.html#tymethod.log
[`Log`]: trait.Log.html
[`log!`]: macro.log.html
[`level()`]: struct.Record.html#method.level
[`target()`]: struct.Record.html#method.target"""

    @staticmethod
    def builder() -> RecordBuilder: ...

    def args(self) -> Arguments: ...

    def metadata(self) -> Metadata: ...

    def level(self) -> Level: ...

    def target(self) -> object: ...

    def module_path(self) -> object: ...

    def module_path_static(self) -> object: ...

    def file(self) -> object: ...

    def file_static(self) -> object: ...

    def line(self) -> int | None: ...

    def key_values(self) -> Source: ...

    def to_builder(self) -> RecordBuilder: ...

class RecordBuilder:
    """Builder for [`Record`](struct.Record.html).

Typically should only be used by log library creators or for testing and "shim loggers".
The `RecordBuilder` can set the different parameters of `Record` object, and returns
the created object when `build` is called.

# Examples

```
use log::{Level, Record};

let record = Record::builder()
.args(format_args!("Error!"))
.level(Level::Error)
.target("myApp")
.file(Some("server.rs"))
.line(Some(144))
.module_path(Some("server"))
.build();
```

Alternatively, use [`MetadataBuilder`](struct.MetadataBuilder.html):

```
use log::{Record, Level, MetadataBuilder};

let error_metadata = MetadataBuilder::new()
.target("myApp")
.level(Level::Error)
.build();

let record = Record::builder()
.metadata(error_metadata)
.args(format_args!("Error!"))
.line(Some(433))
.file(Some("app.rs"))
.module_path(Some("server"))
.build();
```"""

    @staticmethod
    def new() -> "RecordBuilder": ...

    def args(self, args: Arguments) -> RecordBuilder: ...

    def metadata(self, metadata: Metadata) -> RecordBuilder: ...

    def level(self, level: Level) -> RecordBuilder: ...

    def target(self, target: object) -> RecordBuilder: ...

    def module_path(self, path: object) -> RecordBuilder: ...

    def module_path_static(self, path: object) -> RecordBuilder: ...

    def file(self, file: object) -> RecordBuilder: ...

    def file_static(self, file: object) -> RecordBuilder: ...

    def line(self, line: int | None) -> RecordBuilder: ...

    def key_values(self, kvs: Source) -> RecordBuilder: ...

    def build(self) -> Record: ...

    @staticmethod
    def default() -> "RecordBuilder": ...

class Metadata:
    """Metadata about a log message.

# Use

`Metadata` structs are created when users of the library use
logging macros.

They are consumed by implementations of the `Log` trait in the
`enabled` method.

`Record`s use `Metadata` to determine the log message's severity
and target.

Users should use the `log_enabled!` macro in their code to avoid
constructing expensive log messages.

# Examples

```
use log::{Record, Level, Metadata};

struct MyLogger;

impl log::Log for MyLogger {
fn enabled(&self, metadata: &Metadata) -> bool {
metadata.level() <= Level::Info
}

fn log(&self, record: &Record) {
if self.enabled(record.metadata()) {
println!("{} - {}", record.level(), record.args());
}
}
fn flush(&self) {}
}

# fn main(){}
```"""

    @staticmethod
    def builder() -> MetadataBuilder: ...

    def level(self) -> Level: ...

    def target(self) -> object: ...

class MetadataBuilder:
    """Builder for [`Metadata`](struct.Metadata.html).

Typically should only be used by log library creators or for testing and "shim loggers".
The `MetadataBuilder` can set the different parameters of a `Metadata` object, and returns
the created object when `build` is called.

# Example

```
let target = "myApp";
use log::{Level, MetadataBuilder};
let metadata = MetadataBuilder::new()
.level(Level::Debug)
.target(target)
.build();
```"""

    @staticmethod
    def new() -> "MetadataBuilder": ...

    def level(self, arg: Level) -> MetadataBuilder: ...

    def target(self, target: object) -> MetadataBuilder: ...

    def build(self) -> Metadata: ...

    @staticmethod
    def default() -> "MetadataBuilder": ...

class SetLoggerError:
    """The type returned by [`set_logger`] if [`set_logger`] has already been called.

[`set_logger`]: fn.set_logger.html"""

    def fmt(self, fmt: Formatter) -> Result: ...

class ParseLevelError:
    """The type returned by [`from_str`] when the string doesn't match any of the log levels.

[`from_str`]: https://doc.rust-lang.org/std/str/trait.FromStr.html#tymethod.from_str"""

    def fmt(self, fmt: Formatter) -> Result: ...

class Key:
    """A key in a key-value."""

    def to_key(self) -> Key: ...

    @staticmethod
    def from_str(key: object) -> "Key": ...

    def as_str(self) -> str: ...

    def to_borrowed_str(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def as_ref(self) -> str: ...

    def borrow(self) -> str: ...

    @staticmethod
    def from_(s: object) -> "Key": ...

    def stream(self, stream: S) -> Result: ...

    def stream_ref(self, stream: S) -> Result: ...

    def serialize(self, serializer: S) -> Ok: ...

class Value:
    """A value in a key-value.

Values are an anonymous bag containing some structured datum.

# Capturing values

There are a few ways to capture a value:

- Using the `Value::from_*` methods.
- Using the `ToValue` trait.
- Using the standard `From` trait.

## Using the `Value::from_*` methods

`Value` offers a few constructor methods that capture values of different kinds.

```
use log::kv::Value;

let value = Value::from_debug(&42i32);

assert_eq!(None, value.to_i64());
```

## Using the `ToValue` trait

The `ToValue` trait can be used to capture values generically.
It's the bound used by `Source`.

```
# use log::kv::ToValue;
let value = 42i32.to_value();

assert_eq!(Some(42), value.to_i64());
```

## Using the standard `From` trait

Standard types that implement `ToValue` also implement `From`.

```
use log::kv::Value;

let value = Value::from(42i32);

assert_eq!(Some(42), value.to_i64());
```

# Data model

Values can hold one of a number of types:

- **Null:** The absence of any other meaningful value. Note that
`Some(Value::null())` is not the same as `None`. The former is
`null` while the latter is `undefined`. This is important to be
able to tell the difference between a key-value that was logged,
but its value was empty (`Some(Value::null())`) and a key-value
that was never logged at all (`None`).
- **Strings:** `str`, `char`.
- **Booleans:** `bool`.
- **Integers:** `u8`-`u128`, `i8`-`i128`, `NonZero*`.
- **Floating point numbers:** `f32`-`f64`.
- **Errors:** `dyn (Error + 'static)`.
- **`serde`:** Any type in `serde`'s data model.
- **`sval`:** Any type in `sval`'s data model.

# Serialization

Values provide a number of ways to be serialized.

For basic types the [`Value::visit`] method can be used to extract the
underlying typed value. However, this is limited in the amount of types
supported (see the [`VisitValue`] trait methods).

For more complex types one of the following traits can be used:
* `sval::Value`, requires the `kv_sval` feature.
* `serde::Serialize`, requires the `kv_serde` feature.

You don't need a visitor to serialize values through `serde` or `sval`.

A value can always be serialized using any supported framework, regardless
of how it was captured. If, for example, a value was captured using its
`Display` implementation, it will serialize through `serde` as a string. If it was
captured as a struct using `serde`, it will also serialize as a struct
through `sval`, or can be formatted using a `Debug`-compatible representation."""

    def to_value(self) -> Value: ...

    @staticmethod
    def from_any(value: object) -> "Value": ...

    @staticmethod
    def from_debug(value: object) -> "Value": ...

    @staticmethod
    def from_display(value: object) -> "Value": ...

    @staticmethod
    def from_serde(value: object) -> "Value": ...

    @staticmethod
    def from_sval(value: object) -> "Value": ...

    @staticmethod
    def from_dyn_debug(value: Debug) -> "Value": ...

    @staticmethod
    def from_dyn_display(value: Display) -> "Value": ...

    @staticmethod
    def from_dyn_error(err: object) -> "Value": ...

    @staticmethod
    def null() -> "Value": ...

    def visit(self, visitor: object) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def serialize(self, s: S) -> Ok: ...

    def stream(self, stream: S) -> Result: ...

    def stream_ref(self, stream: S) -> Result: ...

    @staticmethod
    def from_(value: object) -> "Value": ...

    def to_borrowed_error(self) -> object: ...

    def to_borrowed_str(self) -> object: ...

    def to_cow_str(self) -> object: ...

    @staticmethod
    def from_(v: object) -> "Value": ...

    @staticmethod
    def capture_debug(value: object) -> "Value": ...

    @staticmethod
    def capture_display(value: object) -> "Value": ...

    @staticmethod
    def capture_error(err: object) -> "Value": ...

    @staticmethod
    def capture_serde(value: object) -> "Value": ...

    @staticmethod
    def capture_sval(value: object) -> "Value": ...

    def is_(self) -> bool: ...

    def downcast_ref(self) -> object: ...

class Error:
    """An error encountered while working with structured data."""

    @staticmethod
    def msg(msg: object) -> "Error": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(_: Exception) -> "Error": ...

    @staticmethod
    def boxed(err: E) -> "Error": ...

    @staticmethod
    def from_(err: Exception) -> "Error": ...

class GlobalLogger:
    """The global logger proxy."""

    def enabled(self, metadata: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Level:
    """An enum representing the available verbosity levels of the logger.

Typical usage includes: checking if a certain `Level` is enabled with
[`log_enabled!`](macro.log_enabled.html), specifying the `Level` of
[`log!`](macro.log.html), and comparing a `Level` directly to a
[`LevelFilter`](enum.LevelFilter.html)."""
    Error: "Level"
    Warn: "Level"
    Info: "Level"
    Debug: "Level"
    Trace: "Level"

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    def eq(self, other: LevelFilter) -> bool: ...

    def partial_cmp(self, other: LevelFilter) -> Ordering | None: ...

    @staticmethod
    def from_str(level: str) -> "Level": ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def max() -> "Level": ...

    def to_level_filter(self) -> LevelFilter: ...

    def as_str(self) -> object: ...

    @staticmethod
    def iter() -> object: ...

    def increment_severity(self) -> Self: ...

    def decrement_severity(self) -> Self: ...

class LevelFilter:
    """An enum representing the available verbosity level filters of the logger.

A `LevelFilter` may be compared directly to a [`Level`]. Use this type
to get and set the maximum log level with [`max_level()`] and [`set_max_level`].

[`Level`]: enum.Level.html
[`max_level()`]: fn.max_level.html
[`set_max_level`]: fn.set_max_level.html"""
    Off: "LevelFilter"
    Error: "LevelFilter"
    Warn: "LevelFilter"
    Info: "LevelFilter"
    Debug: "LevelFilter"
    Trace: "LevelFilter"

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    def eq(self, other: Level) -> bool: ...

    def partial_cmp(self, other: Level) -> Ordering | None: ...

    @staticmethod
    def from_str(level: str) -> "LevelFilter": ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def max() -> "LevelFilter": ...

    def to_level(self) -> Level | None: ...

    def as_str(self) -> object: ...

    @staticmethod
    def iter() -> object: ...

    def increment_severity(self) -> Self: ...

    def decrement_severity(self) -> Self: ...

class Inner:
    None_: "Inner"
    Bool: "Inner"
    Str: "Inner"
    Char: "Inner"
    I64: "Inner"
    U64: "Inner"
    F64: "Inner"
    I128: "Inner"
    U128: "Inner"
    Debug: "Inner"
    Display: "Inner"

    @staticmethod
    def from_(_: None) -> "Inner": ...

    @staticmethod
    def from_(v: bool) -> "Inner": ...

    @staticmethod
    def from_(v: str) -> "Inner": ...

    @staticmethod
    def from_(v: float) -> "Inner": ...

    @staticmethod
    def from_(v: float) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: int) -> "Inner": ...

    @staticmethod
    def from_(v: object) -> "Inner": ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_debug(value: object) -> "Inner": ...

    @staticmethod
    def from_display(value: object) -> "Inner": ...

    @staticmethod
    def from_dyn_debug(value: Debug) -> "Inner": ...

    @staticmethod
    def from_dyn_display(value: Display) -> "Inner": ...

    @staticmethod
    def empty() -> "Inner": ...

    def to_bool(self) -> bool | None: ...

    def to_char(self) -> str | None: ...

    def to_f64(self) -> float | None: ...

    def to_i64(self) -> int | None: ...

    def to_u64(self) -> int | None: ...

    def to_u128(self) -> int | None: ...

    def to_i128(self) -> int | None: ...

    def to_borrowed_str(self) -> object: ...

    def to_test_token(self) -> Token: ...

class Token:
    None_: "Token"
    Bool: "Token"
    Char: "Token"
    Str: "Token"
    F64: "Token"
    I64: "Token"
    U64: "Token"

"""Sets the global maximum log level.

Generally, this should only be called by the active logging implementation.

Note that `Trace` is the maximum level, because it provides the maximum amount of detail in the emitted logs."""
def set_max_level(level: LevelFilter) -> None: ...

"""A thread-unsafe version of [`set_max_level`].

This function is available on all platforms, even those that do not have
support for atomics that is needed by [`set_max_level`].

In almost all cases, [`set_max_level`] should be preferred.

# Safety

This function is only safe to call when it cannot race with any other
calls to `set_max_level` or `set_max_level_racy`.

This can be upheld by (for example) making sure that **there are no other
threads**, and (on embedded) that **interrupts are disabled**.

It is safe to use all other logging functions while this function runs
(including all logging macros).

[`set_max_level`]: fn.set_max_level.html"""
def set_max_level_racy(level: LevelFilter) -> None: ...

"""Returns the current maximum log level.

The [`log!`], [`error!`], [`warn!`], [`info!`], [`debug!`], and [`trace!`] macros check
this value and discard any message logged at a higher level. The maximum
log level is set by the [`set_max_level`] function.

[`log!`]: macro.log.html
[`error!`]: macro.error.html
[`warn!`]: macro.warn.html
[`info!`]: macro.info.html
[`debug!`]: macro.debug.html
[`trace!`]: macro.trace.html
[`set_max_level`]: fn.set_max_level.html"""
def max_level() -> LevelFilter: ...

"""Sets the global logger to a `Box<Log>`.

This is a simple convenience wrapper over `set_logger`, which takes a
`Box<Log>` rather than a `&'static Log`. See the documentation for
[`set_logger`] for more details.

Requires the `std` feature.

# Errors

An error is returned if a logger has already been set.

[`set_logger`]: fn.set_logger.html"""
def set_boxed_logger(logger: dynLog) -> None: ...

"""Sets the global logger to a `&'static Log`.

This function may only be called once in the lifetime of a program. Any log
events that occur before the call to `set_logger` completes will be ignored.

This function does not typically need to be called manually. Logger
implementations should provide an initialization method that installs the
logger internally.

# Availability

This method is available even when the `std` feature is disabled. However,
it is currently unavailable on `thumbv6` targets, which lack support for
some atomic operations which are used by this function. Even on those
targets, [`set_logger_racy`] will be available.

# Errors

An error is returned if a logger has already been set.

# Examples

```
use log::{error, info, warn, Record, Level, Metadata, LevelFilter};

static MY_LOGGER: MyLogger = MyLogger;

struct MyLogger;

impl log::Log for MyLogger {
fn enabled(&self, metadata: &Metadata) -> bool {
metadata.level() <= Level::Info
}

fn log(&self, record: &Record) {
if self.enabled(record.metadata()) {
println!("{} - {}", record.level(), record.args());
}
}
fn flush(&self) {}
}

# fn main(){
log::set_logger(&MY_LOGGER).unwrap();
log::set_max_level(LevelFilter::Info);

info!("hello log");
warn!("warning");
error!("oops");
# }
```

[`set_logger_racy`]: fn.set_logger_racy.html"""
def set_logger(logger: object) -> None: ...

"""A thread-unsafe version of [`set_logger`].

This function is available on all platforms, even those that do not have
support for atomics that is needed by [`set_logger`].

In almost all cases, [`set_logger`] should be preferred.

# Safety

This function is only safe to call when it cannot race with any other
calls to `set_logger` or `set_logger_racy`.

This can be upheld by (for example) making sure that **there are no other
threads**, and (on embedded) that **interrupts are disabled**.

It is safe to use other logging functions while this function runs
(including all logging macros).

[`set_logger`]: fn.set_logger.html"""
def set_logger_racy(logger: object) -> None: ...

"""Returns a reference to the logger.

If a logger has not been set, a no-op implementation is returned."""
def logger() -> object: ...

def visit(inner: Inner, visitor: object) -> None: ...

def visit(inner: Inner, visitor: object) -> None: ...

def log(logger: L, args: Arguments, level: Level, target_module_path_and_loc: object, kvs: K) -> None: ...

def enabled(logger: L, level: Level, target: str) -> bool: ...

def loc() -> object: ...

def capture_to_value(v: object) -> Value: ...

def capture_debug(v: object) -> Value: ...

def capture_display(v: object) -> Value: ...

def capture_error(v: object) -> Value: ...

def capture_sval(v: object) -> Value: ...

def capture_serde(v: object) -> Value: ...

__all__: list[str] = ["set_max_level", "set_max_level_racy", "max_level", "set_boxed_logger", "set_logger", "set_logger_racy", "logger", "visit", "visit", "log", "enabled", "loc", "capture_to_value", "capture_debug", "capture_display", "capture_error", "capture_sval", "capture_serde", "Record", "RecordBuilder", "Metadata", "MetadataBuilder", "SetLoggerError", "ParseLevelError", "Key", "Value", "Error", "GlobalLogger", "Level", "LevelFilter", "Inner", "Token"]
