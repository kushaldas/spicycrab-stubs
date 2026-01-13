"""Python stubs for the config Rust crate.

Install with: cookcrab install config
"""

from __future__ import annotations

from typing import Self

class Config:
    """A prioritized configuration repository.

It maintains a set of configuration sources, fetches values to populate those, and provides
them according to the source's priority."""

    @staticmethod
    def default() -> "Config": ...

    @staticmethod
    def builder() -> object: ...

    def get(self, key: str) -> T: ...

    def get_string(self, key: str) -> str: ...

    def get_int(self, key: str) -> int: ...

    def get_float(self, key: str) -> float: ...

    def get_bool(self, key: str) -> bool: ...

    def get_table(self, key: str) -> object: ...

    def get_array(self, key: str) -> list[Value]: ...

    def try_deserialize(self) -> T: ...

    @staticmethod
    def try_from(from_: T) -> object: ...

    def clone_into_box(self) -> object: ...

    def collect(self) -> object: ...

class FileSourceString:
    """Describes a file sourced from a string"""

    @staticmethod
    def from_(s: object) -> "FileSourceString": ...

    def resolve(self, format_hint: F | None) -> FileSourceResult: ...

class FileSourceResult:

    def uri(self) -> str | None: ...

    def content(self) -> str: ...

    def format(self) -> dynFormat: ...

class FileSourceFile:
    """Describes a file sourced from a file"""

    @staticmethod
    def new(name: PathBuf) -> "FileSourceFile": ...

    def resolve(self, format_hint: F | None) -> FileSourceResult: ...

class File:
    """A configuration source backed up by a file.

It supports optional automatic file format discovery."""

    @staticmethod
    def from_str(s: str, format: F) -> "File": ...

    @staticmethod
    def new(name: str, format: F) -> "File": ...

    @staticmethod
    def with_name(base_name: str) -> "File": ...

    def format(self, format: F) -> Self: ...

    def required(self, required: bool) -> Self: ...

    @staticmethod
    def from_(path: object) -> "File": ...

    @staticmethod
    def from_(path: PathBuf) -> "File": ...

    def clone_into_box(self) -> object: ...

    def collect(self) -> object: ...

class ReadmeDoctests:
    pass

class ConfigBuilder:
    """A configuration builder

It registers ordered sources of configuration to later build consistent [`Config`] from them.
Configuration sources it defines are defaults, [`Source`]s and overrides.

Defaults are always loaded first and can be overwritten by any of two other sources.
Overrides are always loaded last, thus cannot be overridden.
Both can be only set explicitly key by key in code
using [`set_default`](Self::set_default) or [`set_override`](Self::set_override).

An intermediate category, [`Source`], set groups of keys at once implicitly using data coming from external sources
like files, environment variables or others that one implements. Defining a [`Source`] is as simple as implementing
a trait for a struct.

Adding sources, setting defaults and overrides does not invoke any I/O nor builds a config.
It happens on demand when [`build`](Self::build) (or its alternative) is called.
Therefore all errors, related to any of the [`Source`] will only show up then.

# Sync and async builder

[`ConfigBuilder`] uses type parameter to keep track of builder state.

In [`DefaultState`] builder only supports [`Source`]s

In [`AsyncState`] it supports both [`Source`]s and [`AsyncSource`]s at the price of building using `async fn`.

# Examples

```rust
# use config::*;
# use std::error::Error;
# fn main() -> Result<(), Box<dyn Error>> {
# #[cfg(feature = "json")]
# {
let mut builder = Config::builder()
.set_default("default", "1")?
.add_source(File::new("config/settings", FileFormat::Json))
//  .add_async_source(...)
.set_override("override", "1")?;

match builder.build() {
Ok(config) => {
// use your config
},
Err(e) => {
// something went wrong
}
}
# }
# Ok(())
# }
```

If any [`AsyncSource`] is used, the builder will transition to [`AsyncState`].
In such case, it is required to _await_ calls to [`build`](Self::build) and its non-consuming sibling.

Calls can be not chained as well
```rust
# use std::error::Error;
# use config::*;
# fn main() -> Result<(), Box<dyn Error>> {
# #[cfg(feature = "json")]
# {
let mut builder = Config::builder();
builder = builder.set_default("default", "1")?;
builder = builder.add_source(File::new("config/settings", FileFormat::Json));
builder = builder.add_source(File::new("config/settings.prod", FileFormat::Json));
builder = builder.set_override("override", "1")?;
# }
# Ok(())
# }
```

Calling [`Config::builder`](Config::builder) yields builder in the default state.
If having an asynchronous state as the initial state is desired, _turbofish_ notation needs to be used.
```rust
# use config::{*, builder::AsyncState};
let mut builder = ConfigBuilder::<AsyncState>::default();
```

If for some reason acquiring builder in default state is required without calling [`Config::builder`](Config::builder)
it can also be achieved.
```rust
# use config::{*, builder::DefaultState};
let mut builder = ConfigBuilder::<DefaultState>::default();
```"""

    def set_default(self, key: S, value: T) -> object: ...

    def set_override(self, key: S, value: T) -> object: ...

    def set_override_option(self, key: S, value: T | None) -> object: ...

    def add_source(self, source: T) -> Self: ...

    def add_async_source(self, source: T) -> object: ...

    def build(self) -> Config: ...

    def build_cloned(self) -> Config: ...

    def add_source(self, source: T) -> Self: ...

    def add_async_source(self, source: T) -> Self: ...

    def build(self) -> Config: ...

    def build_cloned(self) -> Config: ...

class DefaultState:
    """Represents data specific to builder in default, synchronous state, without support for async."""
    pass

class AsyncState:
    """Represents data specific to builder in asynchronous state, with support for async."""
    pass

class Value:
    """A configuration value."""

    def deserialize_any(self, visitor: V) -> Value: ...

    def deserialize_bool(self, visitor: V) -> Value: ...

    def deserialize_i8(self, visitor: V) -> Value: ...

    def deserialize_i16(self, visitor: V) -> Value: ...

    def deserialize_i32(self, visitor: V) -> Value: ...

    def deserialize_i64(self, visitor: V) -> Value: ...

    def deserialize_u8(self, visitor: V) -> Value: ...

    def deserialize_u16(self, visitor: V) -> Value: ...

    def deserialize_u32(self, visitor: V) -> Value: ...

    def deserialize_u64(self, visitor: V) -> Value: ...

    def deserialize_f32(self, visitor: V) -> Value: ...

    def deserialize_f64(self, visitor: V) -> Value: ...

    def deserialize_str(self, visitor: V) -> Value: ...

    def deserialize_string(self, visitor: V) -> Value: ...

    def deserialize_option(self, visitor: V) -> Value: ...

    def deserialize_newtype_struct(self, _name: object, visitor: V) -> Value: ...

    def deserialize_enum(self, name: object, variants: object, visitor: V) -> Value: ...

    @staticmethod
    def new(origin: object, kind: V) -> "Value": ...

    def origin(self) -> object: ...

    def try_deserialize(self) -> T: ...

    def into_bool(self) -> bool: ...

    def into_int(self) -> int: ...

    def into_int128(self) -> int: ...

    def into_uint(self) -> int: ...

    def into_uint128(self) -> int: ...

    def into_float(self) -> float: ...

    def into_string(self) -> str: ...

    def into_array(self) -> object: ...

    def into_table(self) -> object: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def from_(value: T) -> "Value": ...

    def fmt(self, f: Formatter) -> Result: ...

class Environment:
    """An environment source collects a dictionary of environment variables values into a hierarchical
config Value type. We have to be aware how the config tree is created from the environment
dictionary, therefore we are mindful about prefixes for the environment keys, level separators,
encoding form (kebab, snake case) etc."""

    @staticmethod
    def with_prefix(s: str) -> "Environment": ...

    def prefix(self, s: str) -> Self: ...

    @staticmethod
    def with_convert_case(tt: Case) -> "Environment": ...

    def convert_case(self, tt: Case) -> Self: ...

    def prefix_separator(self, s: str) -> Self: ...

    def separator(self, s: str) -> Self: ...

    def list_separator(self, s: str) -> Self: ...

    def with_list_parse_key(self, key: str) -> Self: ...

    def ignore_empty(self, ignore: bool) -> Self: ...

    def try_parsing(self, try_parsing: bool) -> Self: ...

    def keep_prefix(self, keep: bool) -> Self: ...

    def source(self, source: object | None) -> Self: ...

    def clone_into_box(self) -> object: ...

    def collect(self) -> object: ...

class FileFormat:
    """File formats provided by the library.

Although it is possible to define custom formats using [`Format`] trait it is recommended to use `FileFormat` if possible."""
    Toml: "FileFormat"
    Json: "FileFormat"
    Yaml: "FileFormat"
    Ini: "FileFormat"
    Ron: "FileFormat"
    Json5: "FileFormat"
    Corn: "FileFormat"

    def parse(self, uri: object, text: str) -> object: ...

    def file_extensions(self) -> object: ...

class ValueKind:
    """Underlying kind of the configuration value.

Standard operations on a [`Value`] by users of this crate do not require
knowledge of [`ValueKind`]. Introspection of underlying kind is only required
when the configuration values are unstructured or do not have known types."""
    Nil: "ValueKind"
    Boolean: "ValueKind"
    I64: "ValueKind"
    I128: "ValueKind"
    U64: "ValueKind"
    U128: "ValueKind"
    Float: "ValueKind"
    String: "ValueKind"
    Table: "ValueKind"
    Array: "ValueKind"

    @staticmethod
    def from_(value: T | None) -> "ValueKind": ...

    @staticmethod
    def from_(value: str) -> "ValueKind": ...

    @staticmethod
    def from_(value: object) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: int) -> "ValueKind": ...

    @staticmethod
    def from_(value: float) -> "ValueKind": ...

    @staticmethod
    def from_(value: bool) -> "ValueKind": ...

    @staticmethod
    def from_(values: object) -> "ValueKind": ...

    @staticmethod
    def from_(values: list[T]) -> "ValueKind": ...

    def fmt(self, f: Formatter) -> Result: ...

class Unexpected:
    Bool: "Unexpected"
    I64: "Unexpected"
    I128: "Unexpected"
    U64: "Unexpected"
    U128: "Unexpected"
    Float: "Unexpected"
    Str: "Unexpected"
    Unit: "Unexpected"
    Seq: "Unexpected"
    Map: "Unexpected"

    def fmt(self, f: Formatter) -> None: ...

class ConfigError:
    """Represents all possible errors that can occur when working with
configuration."""
    Frozen: "ConfigError"
    NotFound: "ConfigError"
    PathParse: "ConfigError"
    FileParse: "ConfigError"
    Type: "ConfigError"
    At: "ConfigError"
    Message: "ConfigError"
    Foreign: "ConfigError"

    @staticmethod
    def invalid_type(origin: str | None, unexpected: Unexpected, expected: object) -> "ConfigError": ...

    @staticmethod
    def invalid_root(origin: object, unexpected: Unexpected) -> object: ...

    def extend_with_key(self, key: str) -> Self: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def custom(msg: T) -> "ConfigError": ...

    @staticmethod
    def missing_field(field: object) -> "ConfigError": ...

    @staticmethod
    def custom(msg: T) -> "ConfigError": ...

__all__: list[str] = ["Config", "FileSourceString", "FileSourceResult", "FileSourceFile", "File", "ReadmeDoctests", "ConfigBuilder", "DefaultState", "AsyncState", "Value", "Environment", "FileFormat", "ValueKind", "Unexpected", "ConfigError"]
