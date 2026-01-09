"""Python stubs for the fern Rust crate.

Install with: cookcrab install fern
"""

from __future__ import annotations

from typing import Self

class Dispatch:
    """The base dispatch logger.

This allows for formatting log records, limiting what records can be passed
through, and then dispatching records to other dispatch loggers or output
loggers.

Note that all methods are position-insensitive.
`Dispatch::new().format(a).chain(b)` produces the exact same result
as `Dispatch::new().chain(b).format(a)`. Given this, it is preferred to put
'format' and other modifiers before 'chain' for the sake of clarity.

Example usage demonstrating all features:

```no_run
# // no_run because this creates log files.
use std::{fs, io};

# fn setup_logger() -> Result<(), fern::InitError> {
fern::Dispatch::new()
.format(|out, message, record| {
out.finish(format_args!(
"[{} {}] {}",
record.level(),
record.target(),
message,
))
})
.chain(
fern::Dispatch::new()
// by default only accept warn messages
.level(log::LevelFilter::Warn)
// accept info messages from the current crate too
.level_for("my_crate", log::LevelFilter::Info)
// `io::Stdout`, `io::Stderr` and `io::File` can be directly passed in.
.chain(io::stdout()),
)
.chain(
fern::Dispatch::new()
// output all messages
.level(log::LevelFilter::Trace)
// except for hyper, in that case only show info messages
.level_for("hyper", log::LevelFilter::Info)
// `log_file(x)` equates to
// `OpenOptions::new().write(true).append(true).create(true).open(x)`
.chain(fern::log_file("persistent-log.log")?)
.chain(
fs::OpenOptions::new()
.write(true)
.create(true)
.truncate(true)
.create(true)
.open("/tmp/temp.log")?,
),
)
.chain(
fern::Dispatch::new()
.level(log::LevelFilter::Error)
.filter(|_meta_data| {
// as an example, randomly reject half of the messages
# /*
rand::random()
# */
# true
})
.chain(io::stderr()),
)
// and finally, set as the global logger!
.apply()?;
# Ok(())
# }
#
# fn main() { setup_logger().expect("failed to set up logger") }
```"""

    @staticmethod
    def new() -> "Dispatch": ...

    def format(self, formatter: F) -> Self: ...

    def chain(self, logger: T) -> Self: ...

    def level(self, level: LevelFilter) -> Self: ...

    def level_for(self, module: T, level: LevelFilter) -> Self: ...

    def filter(self, filter: F) -> Self: ...

    def into_shared(self) -> SharedDispatch: ...

    def into_log(self) -> object: ...

    def apply(self) -> None: ...

    @staticmethod
    def default() -> "Dispatch": ...

    def fmt(self, f: Formatter) -> Result: ...

    def enabled(self, metadata: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class SharedDispatch:
    """Logger which is usable as an output for multiple other loggers.

This struct contains a built logger stored in an [`Arc`], and can be
safely cloned.

See [`Dispatch::into_shared`].

[`Arc`]: https://doc.rust-lang.org/std/sync/struct.Arc.html
[`Dispatch::into_shared`]: struct.Dispatch.html#method.into_shared"""
    pass

class Panic:
    """Logger which will panic whenever anything is logged. The panic
will be exactly the message of the log.

`Panic` is useful primarily as a secondary logger, filtered by warning or
error.

# Examples

This configuration will output all messages to stdout and panic if an Error
message is sent.

```
fern::Dispatch::new()
// format, etc.
.chain(std::io::stdout())
.chain(
fern::Dispatch::new()
.level(log::LevelFilter::Error)
.chain(fern::Panic),
)
# /*
.apply()?;
# */ .into_log();
```

This sets up a "panic on warn+" logger, and ignores errors so it can be
called multiple times.

This might be useful in test setup, for example, to disallow warn-level
messages.

```no_run
fn setup_panic_logging() {
fern::Dispatch::new()
.level(log::LevelFilter::Warn)
.chain(fern::Panic)
.apply()
// ignore errors from setting up logging twice
.ok();
}
```"""

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Output:
    """Configuration for a logger output."""

    @staticmethod
    def from_(log: Dispatch) -> "Output": ...

    @staticmethod
    def from_(log: SharedDispatch) -> "Output": ...

    @staticmethod
    def from_(log: dynLog) -> "Output": ...

    @staticmethod
    def from_(log: object) -> "Output": ...

    @staticmethod
    def from_(file: File) -> "Output": ...

    @staticmethod
    def from_(writer: object) -> "Output": ...

    @staticmethod
    def from_(reopen: object) -> "Output": ...

    @staticmethod
    def from_(reopen: object) -> "Output": ...

    @staticmethod
    def from_(stream: Stdout) -> "Output": ...

    @staticmethod
    def from_(stream: Stderr) -> "Output": ...

    @staticmethod
    def from_(stream: object) -> "Output": ...

    @staticmethod
    def from_(log: Logger) -> "Output": ...

    @staticmethod
    def from_(log: Logger) -> "Output": ...

    @staticmethod
    def from_(log: Syslog4Rfc3164Logger) -> "Output": ...

    @staticmethod
    def from_(log: Syslog6Rfc3164Logger) -> "Output": ...

    @staticmethod
    def from_(log: Syslog7Rfc3164Logger) -> "Output": ...

    @staticmethod
    def from_(_: Panic) -> "Output": ...

    @staticmethod
    def file(file: File, line_sep: T) -> "Output": ...

    @staticmethod
    def writer(writer: object, line_sep: T) -> "Output": ...

    @staticmethod
    def reopen(reopen: object, line_sep: T) -> "Output": ...

    @staticmethod
    def reopen1(reopen: object, line_sep: T) -> "Output": ...

    @staticmethod
    def stdout(line_sep: T) -> "Output": ...

    @staticmethod
    def stderr(line_sep: T) -> "Output": ...

    @staticmethod
    def sender(sender: object, line_sep: T) -> "Output": ...

    @staticmethod
    def syslog_5424(logger: Syslog4Rfc5424Logger, transform: F) -> "Output": ...

    @staticmethod
    def syslog6_5424(logger: Syslog6Rfc5424Logger, transform: F) -> "Output": ...

    @staticmethod
    def syslog7_5424(logger: Syslog7Rfc5424Logger, transform: F) -> "Output": ...

    @staticmethod
    def call(func: F) -> "Output": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(config: DateBased) -> "Output": ...

    def enabled(self, metadata: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class DateBased:
    """This is used to generate log file suffixed based on date, hour, and minute.

The log file will be rotated automatically when the date changes."""

    @staticmethod
    def new(file_prefix: T, file_suffix: U) -> "DateBased": ...

    def line_sep(self, line_sep: T) -> Self: ...

    def utc_time(self) -> Self: ...

    def local_time(self) -> Self: ...

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class WithFgColor:
    """Opaque structure which represents some text data and a color to display it
with.

This implements [`fmt::Display`] to displaying the inner text (usually a
log level) with ANSI color markers before to set the color and after to
reset the color.

`WithFgColor` instances can be created and displayed without any allocation."""

    def fmt(self, f: Formatter) -> Result: ...

class ColoredLevelConfig:
    """Configuration specifying colors a log level can be colored as.

Example usage setting custom 'info' and 'debug' colors:

```
use fern::colors::{Color, ColoredLevelConfig};

let colors = ColoredLevelConfig::new()
.info(Color::Green)
.debug(Color::Magenta);

fern::Dispatch::new()
.format(move |out, message, record| {
out.finish(format_args!(
"[{}] {}",
colors.color(record.level()),
message
))
})
.chain(std::io::stdout())
# /*
.apply()?;
# */
#   .into_log();
```"""

    @staticmethod
    def new() -> "ColoredLevelConfig": ...

    def error(self, error: Color) -> Self: ...

    def warn(self, warn: Color) -> Self: ...

    def info(self, info: Color) -> Self: ...

    def debug(self, debug: Color) -> Self: ...

    def trace(self, trace: Color) -> Self: ...

    def color(self, level: Level) -> object: ...

    def get_color(self, level: Level) -> Color: ...

    @staticmethod
    def default() -> "ColoredLevelConfig": ...

class Dispatch:

    @staticmethod
    def new() -> "Dispatch": ...

    def format(self, formatter: F) -> Self: ...

    def chain(self, logger: T) -> Self: ...

    def level(self, level: LevelFilter) -> Self: ...

    def level_for(self, module: T, level: LevelFilter) -> Self: ...

    def filter(self, filter: F) -> Self: ...

    def into_shared(self) -> SharedDispatch: ...

    def into_log(self) -> object: ...

    def apply(self) -> None: ...

    @staticmethod
    def default() -> "Dispatch": ...

    def fmt(self, f: Formatter) -> Result: ...

    def enabled(self, metadata: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class FormatCallback:
    """Callback struct for use within a formatter closure

Callbacks are used for formatting in order to allow usage of
[`std::fmt`]-based formatting without the allocation of the formatted
result which would be required to return it.

Example usage:

```
fern::Dispatch::new().format(|callback: fern::FormatCallback, message, record| {
callback.finish(format_args!("[{}] {}", record.level(), message))
})
# ;
```

[`std::fmt`]: https://doc.rust-lang.org/std/fmt/index.html"""

    def finish(self, formatted_message: Arguments) -> None: ...

class Stdout:
    pass

class Stderr:
    pass

class File:
    pass

class Sender:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Writer:
    pass

class Reopen:
    pass

class Reopen1:
    pass

class Syslog3:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Syslog4Rfc3164:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Syslog4Rfc5424:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Syslog6Rfc3164:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Syslog6Rfc5424:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Syslog7Rfc3164:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Syslog7Rfc5424:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Panic:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class Null:

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, _: Record) -> None: ...

    def flush(self) -> None: ...

class DateBased:
    """File logger with a dynamic time-based name."""

    @staticmethod
    def new(file_prefix: T, file_suffix: U) -> "DateBased": ...

    def line_sep(self, line_sep: T) -> Self: ...

    def utc_time(self) -> Self: ...

    def local_time(self) -> Self: ...

    def enabled(self, _: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class DateBasedConfig:

    @staticmethod
    def new(line_sep: object, file_prefix: PathBuf, file_suffix: object, timezone: ConfiguredTimezone) -> "DateBasedConfig": ...

    def compute_current_suffix(self) -> str: ...

    def compute_file_path(self, suffix: str) -> PathBuf: ...

    @staticmethod
    def open_log_file(path: Path) -> File: ...

    def open_current_log_file(self, suffix: str) -> File: ...

class DateBasedState:

    @staticmethod
    def new(current_suffix: str, file_stream: File | None) -> "DateBasedState": ...

    def replace_file(self, new_suffix: str, new_file: File | None) -> None: ...

class LevelConfiguration:
    JustDefault: "LevelConfiguration"
    Minimal: "LevelConfiguration"
    Many: "LevelConfiguration"

    @staticmethod
    def from_(levels: object) -> "LevelConfiguration": ...

class Output:
    Stdout: "Output"
    Stderr: "Output"
    File: "Output"
    Sender: "Output"
    Syslog3: "Output"
    Syslog4Rfc3164: "Output"
    Syslog4Rfc5424: "Output"
    Syslog6Rfc3164: "Output"
    Syslog6Rfc5424: "Output"
    Syslog7Rfc3164: "Output"
    Syslog7Rfc5424: "Output"
    Dispatch: "Output"
    SharedDispatch: "Output"
    OtherBoxed: "Output"
    OtherStatic: "Output"
    Panic: "Output"
    Writer: "Output"
    DateBased: "Output"
    Reopen: "Output"
    Reopen1: "Output"

    @staticmethod
    def from_(log: Dispatch) -> "Output": ...

    @staticmethod
    def from_(log: SharedDispatch) -> "Output": ...

    @staticmethod
    def from_(log: dynLog) -> "Output": ...

    @staticmethod
    def from_(log: object) -> "Output": ...

    @staticmethod
    def from_(file: File) -> "Output": ...

    @staticmethod
    def from_(writer: object) -> "Output": ...

    @staticmethod
    def from_(reopen: object) -> "Output": ...

    @staticmethod
    def from_(reopen: object) -> "Output": ...

    @staticmethod
    def from_(stream: Stdout) -> "Output": ...

    @staticmethod
    def from_(stream: Stderr) -> "Output": ...

    @staticmethod
    def from_(stream: object) -> "Output": ...

    @staticmethod
    def from_(log: Logger) -> "Output": ...

    @staticmethod
    def from_(log: Logger) -> "Output": ...

    @staticmethod
    def from_(log: Syslog4Rfc3164Logger) -> "Output": ...

    @staticmethod
    def from_(log: Syslog6Rfc3164Logger) -> "Output": ...

    @staticmethod
    def from_(log: Syslog7Rfc3164Logger) -> "Output": ...

    @staticmethod
    def from_(_: Panic) -> "Output": ...

    @staticmethod
    def file(file: File, line_sep: T) -> "Output": ...

    @staticmethod
    def writer(writer: object, line_sep: T) -> "Output": ...

    @staticmethod
    def reopen(reopen: object, line_sep: T) -> "Output": ...

    @staticmethod
    def reopen1(reopen: object, line_sep: T) -> "Output": ...

    @staticmethod
    def stdout(line_sep: T) -> "Output": ...

    @staticmethod
    def stderr(line_sep: T) -> "Output": ...

    @staticmethod
    def sender(sender: object, line_sep: T) -> "Output": ...

    @staticmethod
    def syslog_5424(logger: Syslog4Rfc5424Logger, transform: F) -> "Output": ...

    @staticmethod
    def syslog6_5424(logger: Syslog6Rfc5424Logger, transform: F) -> "Output": ...

    @staticmethod
    def syslog7_5424(logger: Syslog7Rfc5424Logger, transform: F) -> "Output": ...

    @staticmethod
    def call(func: F) -> "Output": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(config: DateBased) -> "Output": ...

    def enabled(self, metadata: Metadata) -> bool: ...

    def log(self, record: Record) -> None: ...

    def flush(self) -> None: ...

class ConfiguredTimezone:
    Local: "ConfiguredTimezone"
    Utc: "ConfiguredTimezone"

class InitError:
    """Convenience error combining possible errors which could occur while
initializing logging.

Fern does not use this error natively, but functions which set up fern and
open log files will often need to return both [`io::Error`] and
[`SetLoggerError`]. This error is for that purpose.

[`io::Error`]: https://doc.rust-lang.org/std/io/struct.Error.html
[`SetLoggerError`]: ../log/struct.SetLoggerError.html"""
    Io: "InitError"
    SetLoggerError: "InitError"

    @staticmethod
    def from_(error: Exception) -> "InitError": ...

    @staticmethod
    def from_(error: SetLoggerError) -> "InitError": ...

    def fmt(self, f: Formatter) -> None: ...

    def description(self) -> str: ...

    def cause(self) -> object: ...

"""Convenience method for opening a log file with common options.

Equivalent to:

```no_run
std::fs::OpenOptions::new()
.write(true)
.create(true)
.append(true)
.open("filename")
# ;
```

See [`OpenOptions`] for more information.

[`OpenOptions`]: https://doc.rust-lang.org/std/fs/struct.OpenOptions.html"""
def log_file(path: P) -> File: ...

"""Convenience method for opening a re-openable log file with common options.

The file opening is equivalent to:

```no_run
std::fs::OpenOptions::new()
.write(true)
.create(true)
.append(true)
.open("filename")
# ;
```

See [`OpenOptions`] for more information.

[`OpenOptions`]: https://doc.rust-lang.org/std/fs/struct.OpenOptions.html

This function is not available on Windows, and it requires the `reopen-03`
feature to be enabled."""
def log_reopen(path: Path, signal: c_int | None) -> object: ...

"""Convenience method for opening a re-openable log file with common options.

The file opening is equivalent to:

```no_run
std::fs::OpenOptions::new()
.write(true)
.create(true)
.append(true)
.open("filename")
# ;
```

See [`OpenOptions`] for more information.

[`OpenOptions`]: https://doc.rust-lang.org/std/fs/struct.OpenOptions.html

This function requires the `reopen-1` feature to be enabled."""
def log_reopen1(path: Path, signals: S) -> object: ...

__all__: list[str] = ["log_file", "log_reopen", "log_reopen1", "Dispatch", "SharedDispatch", "Panic", "Output", "DateBased", "WithFgColor", "ColoredLevelConfig", "Dispatch", "FormatCallback", "Stdout", "Stderr", "File", "Sender", "Writer", "Reopen", "Reopen1", "Syslog3", "Syslog4Rfc3164", "Syslog4Rfc5424", "Syslog6Rfc3164", "Syslog6Rfc5424", "Syslog7Rfc3164", "Syslog7Rfc5424", "Panic", "Null", "DateBased", "DateBasedConfig", "DateBasedState", "LevelConfiguration", "Output", "ConfiguredTimezone", "InitError"]
