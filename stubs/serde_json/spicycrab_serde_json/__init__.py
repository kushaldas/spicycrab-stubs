"""Python stubs for the serde_json Rust crate.

Install with: cookcrab install serde_json
"""

from __future__ import annotations

from typing import Self

class Map:
    """Represents a JSON key/value type."""

    @staticmethod
    def new() -> "Map": ...

    @staticmethod
    def with_capacity(capacity: int) -> "Map": ...

    def clear(self) -> None: ...

    def get(self, key: Q) -> object: ...

    def contains_key(self, key: Q) -> bool: ...

    def get_mut(self, key: Q) -> object: ...

    def get_key_value(self, key: Q) -> object | None: ...

    def insert(self, k: str, v: Value) -> Value | None: ...

    def shift_insert(self, index: int, k: str, v: Value) -> Value | None: ...

    def remove(self, key: Q) -> Value | None: ...

    def remove_entry(self, key: Q) -> object | None: ...

    def swap_remove(self, key: Q) -> Value | None: ...

    def swap_remove_entry(self, key: Q) -> object | None: ...

    def shift_remove(self, key: Q) -> Value | None: ...

    def shift_remove_entry(self, key: Q) -> object | None: ...

    def append(self, other: Self) -> None: ...

    def entry(self, key: S) -> Entry: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def iter(self) -> Iter: ...

    def iter_mut(self) -> IterMut: ...

    def keys(self) -> Keys: ...

    def values(self) -> Values: ...

    def values_mut(self) -> ValuesMut: ...

    def into_values(self) -> IntoValues: ...

    def retain(self, f: F) -> None: ...

    def sort_keys(self) -> None: ...

    @staticmethod
    def default() -> "Map": ...

    def clone(self) -> Self: ...

    def clone_from(self, source: Self) -> None: ...

    def eq(self, other: Self) -> bool: ...

    def hash(self, state: H) -> None: ...

    def index(self, index: Q) -> Value: ...

    def index_mut(self, index: Q) -> Value: ...

    def fmt(self, formatter: Formatter) -> None: ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def from_iter(iter: T) -> "Map": ...

    def extend(self, iter: T) -> None: ...

    def into_deserializer(self) -> Deserializer: ...

    def into_iter(self) -> IntoIter: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    def deserialize_any(self, visitor: V) -> Value: ...

    def deserialize_enum(self, _name: object, _variants: object, visitor: V) -> Value: ...

    def deserialize_ignored_any(self, visitor: V) -> Value: ...

class VacantEntry:
    """A vacant Entry. It is part of the [`Entry`] enum."""

    def key(self) -> str: ...

    def insert(self, value: Value) -> object: ...

class OccupiedEntry:
    """An occupied Entry. It is part of the [`Entry`] enum."""

    def key(self) -> str: ...

    def get(self) -> Value: ...

    def get_mut(self) -> Value: ...

    def into_mut(self) -> object: ...

    def insert(self, value: Value) -> Value: ...

    def remove(self) -> Value: ...

    def swap_remove(self) -> Value: ...

    def shift_remove(self) -> Value: ...

    def remove_entry(self) -> object: ...

    def swap_remove_entry(self) -> object: ...

    def shift_remove_entry(self) -> object: ...

class Iter:
    """An iterator over a serde_json::Map's entries."""
    pass

class IterMut:
    """A mutable iterator over a serde_json::Map's entries."""
    pass

class IntoIter:
    """An owning iterator over a serde_json::Map's entries."""
    pass

class Keys:
    """An iterator over a serde_json::Map's keys."""
    pass

class Values:
    """An iterator over a serde_json::Map's values."""
    pass

class ValuesMut:
    """A mutable iterator over a serde_json::Map's values."""
    pass

class IntoValues:
    """An owning iterator over a serde_json::Map's values."""
    pass

class LineColIterator:

    @staticmethod
    def new(iter: I) -> object: ...

    def line(self) -> int: ...

    def col(self) -> int: ...

    def byte_offset(self) -> int: ...

    def next(self) -> int | None: ...

class Error:

    def fmt(self, _formatter: Formatter) -> Result: ...

    def line(self) -> int: ...

    def column(self) -> int: ...

    def classify(self) -> Category: ...

    def is_io(self) -> bool: ...

    def is_syntax(self) -> bool: ...

    def is_data(self) -> bool: ...

    def is_eof(self) -> bool: ...

    def io_error_kind(self) -> ErrorKind | None: ...

    @staticmethod
    def from_(j: Exception) -> "Error": ...

    @staticmethod
    def io(error: Exception) -> "Error": ...

    def source(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def custom(msg: T) -> Exception: ...

    @staticmethod
    def invalid_type(unexp: Unexpected, exp: Expected) -> "Error": ...

    @staticmethod
    def invalid_value(unexp: Unexpected, exp: Expected) -> "Error": ...

    @staticmethod
    def custom(msg: T) -> Exception: ...

class Deserializer:
    """A structure that deserializes JSON into Rust values."""

    @staticmethod
    def new(read: R) -> "Deserializer": ...

    @staticmethod
    def from_reader(reader: R) -> "Deserializer": ...

    @staticmethod
    def from_slice(bytes: object) -> "Deserializer": ...

    @staticmethod
    def from_str(s: object) -> "Deserializer": ...

    def end(self) -> None: ...

    def into_iter(self) -> object: ...

    def disable_recursion_limit(self) -> None: ...

class StreamDeserializer:
    """Iterator that deserializes a stream into multiple JSON values.

A stream deserializer can be created from any JSON deserializer using the
`Deserializer::into_iter` method.

The data can consist of any JSON value. Values need to be a self-delineating value e.g.
arrays, objects, or strings, or be followed by whitespace or a self-delineating value.

```
use serde_json::{Deserializer, Value};

fn main() {
let data = "{\\"k\\": 3}1\\"cool\\"\\"stuff\\" 3{}  [0, 1, 2]";

let stream = Deserializer::from_str(data).into_iter::<Value>();

for value in stream {
println!("{}", value.unwrap());
}
}
```"""

    @staticmethod
    def new(read: R) -> "StreamDeserializer": ...

    def byte_offset(self) -> int: ...

    def next(self) -> T | None: ...

class Number:
    """Represents a JSON number, whether integer or floating point."""

    @staticmethod
    def from_str(s: str) -> object: ...

    def is_i64(self) -> bool: ...

    def is_u64(self) -> bool: ...

    def is_f64(self) -> bool: ...

    def as_i64(self) -> int | None: ...

    def as_u64(self) -> int | None: ...

    def as_f64(self) -> float | None: ...

    @staticmethod
    def from_f64(f: float) -> Number | None: ...

    def as_i128(self) -> int | None: ...

    def as_u128(self) -> int | None: ...

    @staticmethod
    def from_i128(i: int) -> Number | None: ...

    @staticmethod
    def from_u128(i: int) -> Number | None: ...

    def as_str(self) -> str: ...

    @staticmethod
    def from_string_unchecked(n: str) -> "Number": ...

    def fmt(self, formatter: Formatter) -> Result: ...

    def fmt(self, formatter: Formatter) -> Result: ...

    def fmt(self, formatter: Formatter) -> Result: ...

    def serialize(self, serializer: S) -> Ok: ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> "Number": ...

    @staticmethod
    def from_(value: ParserNumber) -> "Number": ...

class NumberFromString:

    @staticmethod
    def deserialize(deserializer: D) -> "NumberFromString": ...

class Position:
    pass

class IoRead:
    """JSON input source that reads from a std::io input stream."""

    @staticmethod
    def new(reader: R) -> "IoRead": ...

    def next(self) -> int | None: ...

    def peek(self) -> int | None: ...

    def discard(self) -> None: ...

    def discard(self) -> None: ...

    def position(self) -> Position: ...

    def peek_position(self) -> Position: ...

    def byte_offset(self) -> int: ...

    def parse_str(self, scratch: object) -> object: ...

    def parse_str_raw(self, scratch: object) -> object: ...

    def ignore_str(self) -> None: ...

    def decode_hex_escape(self) -> int: ...

    def begin_raw_buffering(self) -> None: ...

    def end_raw_buffering(self, visitor: V) -> Value: ...

    def set_failed(self, failed: mutbool) -> None: ...

class SliceRead:
    """JSON input source that reads from a slice of bytes."""

    @staticmethod
    def new(slice: object) -> "SliceRead": ...

    def next(self) -> int | None: ...

    def peek(self) -> int | None: ...

    def discard(self) -> None: ...

    def position(self) -> Position: ...

    def peek_position(self) -> Position: ...

    def byte_offset(self) -> int: ...

    def parse_str(self, scratch: object) -> object: ...

    def parse_str_raw(self, scratch: object) -> object: ...

    def ignore_str(self) -> None: ...

    def decode_hex_escape(self) -> int: ...

    def begin_raw_buffering(self) -> None: ...

    def end_raw_buffering(self, visitor: V) -> Value: ...

    def set_failed(self, _failed: mutbool) -> None: ...

class StrRead:
    """JSON input source that reads from a UTF-8 string."""

    @staticmethod
    def new(s: object) -> "StrRead": ...

    def next(self) -> int | None: ...

    def peek(self) -> int | None: ...

    def discard(self) -> None: ...

    def position(self) -> Position: ...

    def peek_position(self) -> Position: ...

    def byte_offset(self) -> int: ...

    def parse_str(self, scratch: object) -> object: ...

    def parse_str_raw(self, scratch: object) -> object: ...

    def ignore_str(self) -> None: ...

    def decode_hex_escape(self) -> int: ...

    def begin_raw_buffering(self) -> None: ...

    def end_raw_buffering(self, visitor: V) -> Value: ...

    def set_failed(self, failed: mutbool) -> None: ...

class Serializer:
    """A structure for serializing Rust values into JSON."""

    @staticmethod
    def new(writer: W) -> "Serializer": ...

    @staticmethod
    def pretty(writer: W) -> "Serializer": ...

    @staticmethod
    def with_formatter(writer: W, formatter: F) -> "Serializer": ...

    def into_inner(self) -> W: ...

    def serialize_bool(self, value: bool) -> Value: ...

    def serialize_i8(self, value: int) -> Value: ...

    def serialize_i16(self, value: int) -> Value: ...

    def serialize_i32(self, value: int) -> Value: ...

    def serialize_i64(self, value: int) -> Value: ...

    def serialize_i128(self, value: int) -> Value: ...

    def serialize_u8(self, value: int) -> Value: ...

    def serialize_u16(self, value: int) -> Value: ...

    def serialize_u32(self, value: int) -> Value: ...

    def serialize_u64(self, value: int) -> Value: ...

    def serialize_u128(self, value: int) -> Value: ...

    def serialize_f32(self, float: float) -> Value: ...

    def serialize_f64(self, float: float) -> Value: ...

    def serialize_char(self, value: str) -> Value: ...

    def serialize_str(self, value: str) -> Value: ...

    def serialize_bytes(self, value: object) -> Value: ...

    def serialize_unit(self) -> Value: ...

    def serialize_unit_struct(self, _name: object) -> Value: ...

    def serialize_unit_variant(self, _name: object, _variant_index: int, variant: object) -> Value: ...

    def serialize_newtype_struct(self, _name: object, value: T) -> Value: ...

    def serialize_newtype_variant(self, _name: object, _variant_index: int, variant: object, value: T) -> Value: ...

    def serialize_none(self) -> Value: ...

    def serialize_some(self, value: T) -> Value: ...

    def serialize_seq(self, len: int | None) -> SerializeSeq: ...

    def serialize_tuple(self, len: int) -> SerializeTuple: ...

    def serialize_tuple_struct(self, _name: object, len: int) -> SerializeTupleStruct: ...

    def serialize_tuple_variant(self, _name: object, _variant_index: int, variant: object, len: int) -> SerializeTupleVariant: ...

    def serialize_map(self, len: int | None) -> SerializeMap: ...

    def serialize_struct(self, name: object, len: int) -> SerializeStruct: ...

    def serialize_struct_variant(self, _name: object, _variant_index: int, variant: object, _len: int) -> SerializeStructVariant: ...

    def collect_str(self, value: T) -> Value: ...

class CompactFormatter:
    """This structure compacts a JSON value with no extra whitespace."""
    pass

class PrettyFormatter:
    """This structure pretty prints a JSON value to make it human readable."""

    @staticmethod
    def new() -> "PrettyFormatter": ...

    @staticmethod
    def with_indent(indent: object) -> "PrettyFormatter": ...

    @staticmethod
    def default() -> "PrettyFormatter": ...

    def begin_array(self, writer: W) -> object: ...

    def end_array(self, writer: W) -> object: ...

    def begin_array_value(self, writer: W, first: bool) -> object: ...

    def end_array_value(self, _writer: W) -> object: ...

    def begin_object(self, writer: W) -> object: ...

    def end_object(self, writer: W) -> object: ...

    def begin_object_key(self, writer: W, first: bool) -> object: ...

    def begin_object_value(self, writer: W) -> object: ...

    def end_object_value(self, _writer: W) -> object: ...

class Serializer:
    """Serializer whose output is a `Value`.

This is the serializer that backs [`serde_json::to_value`][crate::to_value].
Unlike the main serde_json serializer which goes from some serializable
value of type `T` to JSON text, this one goes from `T` to
`serde_json::Value`.

The `to_value` function is implementable as:

```
use serde::Serialize;
use serde_json::{Error, Value};

pub fn to_value<T>(input: T) -> Result<Value, Error>
where
T: Serialize,
{
input.serialize(serde_json::value::Serializer)
}
```"""

    @staticmethod
    def new(writer: W) -> "Serializer": ...

    @staticmethod
    def pretty(writer: W) -> "Serializer": ...

    @staticmethod
    def with_formatter(writer: W, formatter: F) -> "Serializer": ...

    def into_inner(self) -> W: ...

    def serialize_bool(self, value: bool) -> Value: ...

    def serialize_i8(self, value: int) -> Value: ...

    def serialize_i16(self, value: int) -> Value: ...

    def serialize_i32(self, value: int) -> Value: ...

    def serialize_i64(self, value: int) -> Value: ...

    def serialize_i128(self, value: int) -> Value: ...

    def serialize_u8(self, value: int) -> Value: ...

    def serialize_u16(self, value: int) -> Value: ...

    def serialize_u32(self, value: int) -> Value: ...

    def serialize_u64(self, value: int) -> Value: ...

    def serialize_u128(self, value: int) -> Value: ...

    def serialize_f32(self, float: float) -> Value: ...

    def serialize_f64(self, float: float) -> Value: ...

    def serialize_char(self, value: str) -> Value: ...

    def serialize_str(self, value: str) -> Value: ...

    def serialize_bytes(self, value: object) -> Value: ...

    def serialize_unit(self) -> Value: ...

    def serialize_unit_struct(self, _name: object) -> Value: ...

    def serialize_unit_variant(self, _name: object, _variant_index: int, variant: object) -> Value: ...

    def serialize_newtype_struct(self, _name: object, value: T) -> Value: ...

    def serialize_newtype_variant(self, _name: object, _variant_index: int, variant: object, value: T) -> Value: ...

    def serialize_none(self) -> Value: ...

    def serialize_some(self, value: T) -> Value: ...

    def serialize_seq(self, len: int | None) -> SerializeSeq: ...

    def serialize_tuple(self, len: int) -> SerializeTuple: ...

    def serialize_tuple_struct(self, _name: object, len: int) -> SerializeTupleStruct: ...

    def serialize_tuple_variant(self, _name: object, _variant_index: int, variant: object, len: int) -> SerializeTupleVariant: ...

    def serialize_map(self, len: int | None) -> SerializeMap: ...

    def serialize_struct(self, name: object, len: int) -> SerializeStruct: ...

    def serialize_struct_variant(self, _name: object, _variant_index: int, variant: object, _len: int) -> SerializeStructVariant: ...

    def collect_str(self, value: T) -> Value: ...

class SerializeVec:

    def serialize_element(self, value: T) -> None: ...

    def end(self) -> Value: ...

    def serialize_element(self, value: T) -> None: ...

    def end(self) -> Value: ...

    def serialize_field(self, value: T) -> None: ...

    def end(self) -> Value: ...

class SerializeTupleVariant:

    def serialize_field(self, value: T) -> None: ...

    def end(self) -> Value: ...

class SerializeStructVariant:

    def serialize_field(self, key: object, value: T) -> None: ...

    def end(self) -> Value: ...

class Error:
    """This type represents all possible errors that can occur when serializing or
deserializing JSON data."""

    def fmt(self, _formatter: Formatter) -> Result: ...

    def line(self) -> int: ...

    def column(self) -> int: ...

    def classify(self) -> Category: ...

    def is_io(self) -> bool: ...

    def is_syntax(self) -> bool: ...

    def is_data(self) -> bool: ...

    def is_eof(self) -> bool: ...

    def io_error_kind(self) -> ErrorKind | None: ...

    @staticmethod
    def from_(j: Exception) -> "Error": ...

    @staticmethod
    def io(error: Exception) -> "Error": ...

    def source(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def custom(msg: T) -> Exception: ...

    @staticmethod
    def invalid_type(unexp: Unexpected, exp: Expected) -> "Error": ...

    @staticmethod
    def invalid_value(unexp: Unexpected, exp: Expected) -> "Error": ...

    @staticmethod
    def custom(msg: T) -> Exception: ...

class RawValue:
    """Reference to a range of bytes encompassing a single valid JSON value in the
input data.

A `RawValue` can be used to defer parsing parts of a payload until later,
or to avoid parsing it at all in the case that part of the payload just
needs to be transferred verbatim into a different output object.

When serializing, a value of this type will retain its original formatting
and will not be minified or pretty-printed.

# Note

`RawValue` is only available if serde\\_json is built with the `"raw_value"`
feature.

```toml
[dependencies]
serde_json = { version = "1.0", features = ["raw_value"] }
```

# Example

```
use serde::{Deserialize, Serialize};
use serde_json::{Result, value::RawValue};

#[derive(Deserialize)]
struct Input<'a> {
code: u32,
#[serde(borrow)]
payload: &'a RawValue,
}

#[derive(Serialize)]
struct Output<'a> {
info: (u32, &'a RawValue),
}

// Efficiently rearrange JSON input containing separate "code" and "payload"
// keys into a single "info" key holding an array of code and payload.
//
// This could be done equivalently using serde_json::Value as the type for
// payload, but &RawValue will perform better because it does not require
// memory allocation. The correct range of bytes is borrowed from the input
// data and pasted verbatim into the output.
fn rearrange(input: &str) -> Result<String> {
let input: Input = serde_json::from_str(input)?;

let output = Output {
info: (input.code, input.payload),
};

serde_json::to_string(&output)
}

fn main() -> Result<()> {
let out = rearrange(r#" {"code": 200, "payload": {}} "#)?;

assert_eq!(out, r#"{"info":[200,{}]}"#);

Ok(())
}
```

# Ownership

The typical usage of `RawValue` will be in the borrowed form:

```
# use serde::Deserialize;
# use serde_json::value::RawValue;
#
#[derive(Deserialize)]
struct SomeStruct<'a> {
#[serde(borrow)]
raw_value: &'a RawValue,
}
```

The borrowed form is suitable when deserializing through
[`serde_json::from_str`] and [`serde_json::from_slice`] which support
borrowing from the input data without memory allocation.

When deserializing through [`serde_json::from_reader`] you will need to use
the boxed form of `RawValue` instead. This is almost as efficient but
involves buffering the raw value from the I/O stream into memory.

[`serde_json::from_str`]: crate::from_str
[`serde_json::from_slice`]: crate::from_slice
[`serde_json::from_reader`]: crate::from_reader

```
# use serde::Deserialize;
# use serde_json::value::RawValue;
#
#[derive(Deserialize)]
struct SomeStruct {
raw_value: Box<RawValue>,
}
```"""

    def to_owned(self) -> Owned: ...

    def fmt(self, formatter: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_string(json: str) -> object: ...

    def get(self) -> str: ...

    def serialize(self, serializer: S) -> Ok: ...

class ReferenceFromString:

    def deserialize(self, deserializer: D) -> Value: ...

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_borrowed_str(self, s: object) -> Value: ...

class BoxedFromString:

    def deserialize(self, deserializer: D) -> Value: ...

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_str(self, s: str) -> Value: ...

    def visit_string(self, s: str) -> Value: ...

class OwnedRawDeserializer:

    def next_key_seed(self, seed: K) -> Value | None: ...

    def next_value_seed(self, seed: V) -> Value: ...

class BorrowedRawDeserializer:

    def next_key_seed(self, seed: K) -> Value | None: ...

    def next_value_seed(self, seed: V) -> Value: ...

class Entry:
    """A view into a single entry in a map, which may either be vacant or occupied.
This enum is constructed from the [`entry`] method on [`Map`].

[`entry`]: Map::entry"""
    Vacant: "Entry"
    Occupied: "Entry"

    def key(self) -> str: ...

    def or_insert(self, default: Value) -> object: ...

    def or_insert_with(self, default: F) -> object: ...

    def and_modify(self, f: F) -> Self: ...

class ErrorKind:
    Other: "ErrorKind"

class Reference:
    Borrowed: "Reference"
    Copied: "Reference"

    def deref(self) -> Target: ...

class State:
    Empty: "State"
    First: "State"
    Rest: "State"

class Compound:
    Map: "Compound"
    Number: "Compound"
    RawValue: "Compound"

    def serialize_element(self, value: T) -> None: ...

    def end(self) -> None: ...

    def serialize_element(self, value: T) -> None: ...

    def end(self) -> None: ...

    def serialize_field(self, value: T) -> None: ...

    def end(self) -> None: ...

    def serialize_field(self, value: T) -> None: ...

    def end(self) -> None: ...

    def serialize_key(self, key: T) -> None: ...

    def serialize_value(self, value: T) -> None: ...

    def end(self) -> None: ...

    def serialize_field(self, key: object, value: T) -> None: ...

    def end(self) -> None: ...

    def serialize_field(self, key: object, value: T) -> None: ...

    def end(self) -> None: ...

class CharEscape:
    """Represents a character escape code in a type-safe manner."""
    Quote: "CharEscape"
    ReverseSolidus: "CharEscape"
    Solidus: "CharEscape"
    Backspace: "CharEscape"
    FormFeed: "CharEscape"
    LineFeed: "CharEscape"
    CarriageReturn: "CharEscape"
    Tab: "CharEscape"
    AsciiControl: "CharEscape"

class SerializeMap:
    Map: "SerializeMap"
    Number: "SerializeMap"
    RawValue: "SerializeMap"

    def serialize_key(self, key: T) -> None: ...

    def serialize_value(self, value: T) -> None: ...

    def end(self) -> Value: ...

    def serialize_field(self, key: object, value: T) -> None: ...

    def end(self) -> Value: ...

class Value:
    """Represents any valid JSON value.

See the [`serde_json::value` module documentation](self) for usage examples."""
    Null: "Value"
    Bool: "Value"
    Number: "Value"
    String: "Value"
    Array: "Value"
    Object: "Value"

    @staticmethod
    def deserialize(deserializer: D) -> "Value": ...

    @staticmethod
    def from_str(s: str) -> "Value": ...

    def deserialize_any(self, visitor: V) -> Value: ...

    def deserialize_option(self, visitor: V) -> Value: ...

    def deserialize_enum(self, name: object, variants: object, visitor: V) -> Value: ...

    def deserialize_newtype_struct(self, name: object, visitor: V) -> Value: ...

    def deserialize_bool(self, visitor: V) -> Value: ...

    def deserialize_char(self, visitor: V) -> Value: ...

    def deserialize_str(self, visitor: V) -> Value: ...

    def deserialize_string(self, visitor: V) -> Value: ...

    def deserialize_bytes(self, visitor: V) -> Value: ...

    def deserialize_byte_buf(self, visitor: V) -> Value: ...

    def deserialize_unit(self, visitor: V) -> Value: ...

    def deserialize_unit_struct(self, _name: object, visitor: V) -> Value: ...

    def deserialize_seq(self, visitor: V) -> Value: ...

    def deserialize_tuple(self, _len: int, visitor: V) -> Value: ...

    def deserialize_tuple_struct(self, _name: object, _len: int, visitor: V) -> Value: ...

    def deserialize_map(self, visitor: V) -> Value: ...

    def deserialize_struct(self, _name: object, _fields: object, visitor: V) -> Value: ...

    def deserialize_identifier(self, visitor: V) -> Value: ...

    def deserialize_ignored_any(self, visitor: V) -> Value: ...

    def into_deserializer(self) -> Deserializer: ...

    @staticmethod
    def from_(f: float) -> "Value": ...

    @staticmethod
    def from_(f: float) -> "Value": ...

    @staticmethod
    def from_(f: bool) -> "Value": ...

    @staticmethod
    def from_(f: str) -> "Value": ...

    @staticmethod
    def from_(f: str) -> "Value": ...

    @staticmethod
    def from_(f: object) -> "Value": ...

    @staticmethod
    def from_(f: Number) -> "Value": ...

    @staticmethod
    def from_(f: object) -> "Value": ...

    @staticmethod
    def from_(f: list[T]) -> "Value": ...

    @staticmethod
    def from_(array: object) -> "Value": ...

    @staticmethod
    def from_(f: object) -> "Value": ...

    @staticmethod
    def from_iter(iter: I) -> "Value": ...

    @staticmethod
    def from_iter(iter: I) -> "Value": ...

    @staticmethod
    def from_(_: None) -> "Value": ...

    @staticmethod
    def from_(opt: T | None) -> "Value": ...

    def serialize(self, serializer: S) -> Ok: ...

    def fmt(self, formatter: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def get(self, index: I) -> object: ...

    def get_mut(self, index: I) -> object: ...

    def is_object(self) -> bool: ...

    def as_object(self) -> object: ...

    def as_object_mut(self) -> object: ...

    def is_array(self) -> bool: ...

    def as_array(self) -> object: ...

    def as_array_mut(self) -> object: ...

    def is_string(self) -> bool: ...

    def as_str(self) -> object: ...

    def is_number(self) -> bool: ...

    def as_number(self) -> object: ...

    def is_i64(self) -> bool: ...

    def is_u64(self) -> bool: ...

    def is_f64(self) -> bool: ...

    def as_i64(self) -> int | None: ...

    def as_u64(self) -> int | None: ...

    def as_f64(self) -> float | None: ...

    def is_boolean(self) -> bool: ...

    def as_bool(self) -> bool | None: ...

    def is_null(self) -> bool: ...

    def as_null(self) -> object: ...

    def pointer(self, pointer: str) -> object: ...

    def pointer_mut(self, pointer: str) -> object: ...

    def take(self) -> Value: ...

    def sort_all_objects(self) -> None: ...

    @staticmethod
    def default() -> "Value": ...

    def index(self, index: I) -> Value: ...

    def index_mut(self, index: I) -> Value: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: str) -> bool: ...

class Category:
    """Categorizes the cause of a `serde_json::Error`."""
    Io: "Category"
    Syntax: "Category"
    Data: "Category"
    Eof: "Category"

"""Deserialize an instance of type `T` from an I/O stream of JSON.

The content of the I/O stream is deserialized directly from the stream
without being buffered in memory by serde_json.

When reading from a source against which short reads are not efficient, such
as a [`File`], you will want to apply your own buffering because serde_json
will not buffer the input. See [`std::io::BufReader`].

It is expected that the input stream ends after the deserialized object.
If the stream does not end, such as in the case of a persistent socket connection,
this function will not return. It is possible instead to deserialize from a prefix of an input
stream without looking for EOF by managing your own [`Deserializer`].

Note that counter to intuition, this function is usually slower than
reading a file completely into memory and then applying [`from_str`]
or [`from_slice`] on it. See [issue #160].

[`File`]: std::fs::File
[issue #160]: https://github.com/serde-rs/json/issues/160

# Example

Reading the contents of a file.

```
use serde::Deserialize;

use std::error::Error;
use std::fs::File;
use std::io::BufReader;
use std::path::Path;

#[derive(Deserialize, Debug)]
struct User {
fingerprint: String,
location: String,
}

fn read_user_from_file<P: AsRef<Path>>(path: P) -> Result<User, Box<dyn Error>> {
// Open the file in read-only mode with buffer.
let file = File::open(path)?;
let reader = BufReader::new(file);

// Read the JSON contents of the file as an instance of `User`.
let u = serde_json::from_reader(reader)?;

// Return the `User`.
Ok(u)
}

fn main() {
# }
# fn fake_main() {
let u = read_user_from_file("test.json").unwrap();
println!("{:#?}", u);
}
```

Reading from a persistent socket connection.

```
use serde::Deserialize;

use std::error::Error;
use std::io::BufReader;
use std::net::{TcpListener, TcpStream};

#[derive(Deserialize, Debug)]
struct User {
fingerprint: String,
location: String,
}

fn read_user_from_stream(stream: &mut BufReader<TcpStream>) -> Result<User, Box<dyn Error>> {
let mut de = serde_json::Deserializer::from_reader(stream);
let u = User::deserialize(&mut de)?;

Ok(u)
}

fn main() {
# }
# fn fake_main() {
let listener = TcpListener::bind("127.0.0.1:4000").unwrap();

for tcp_stream in listener.incoming() {
let mut buffered = BufReader::new(tcp_stream.unwrap());
println!("{:#?}", read_user_from_stream(&mut buffered));
}
}
```

# Errors

This conversion can fail if the structure of the input does not match the
structure expected by `T`, for example if `T` is a struct type but the input
contains something other than a JSON map. It can also fail if the structure
is correct but `T`'s implementation of `Deserialize` decides that something
is wrong with the data, for example required struct fields are missing from
the JSON map or some number is too big to fit in the expected primitive
type."""
def from_reader(rdr: R) -> T: ...

"""Deserialize an instance of type `T` from bytes of JSON text.

# Example

```
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User {
fingerprint: String,
location: String,
}

fn main() {
// The type of `j` is `&[u8]`
let j = b"
{
\\"fingerprint\\": \\"0xF9BA143B95FF6D82\\",
\\"location\\": \\"Menlo Park, CA\\"
}";

let u: User = serde_json::from_slice(j).unwrap();
println!("{:#?}", u);
}
```

# Errors

This conversion can fail if the structure of the input does not match the
structure expected by `T`, for example if `T` is a struct type but the input
contains something other than a JSON map. It can also fail if the structure
is correct but `T`'s implementation of `Deserialize` decides that something
is wrong with the data, for example required struct fields are missing from
the JSON map or some number is too big to fit in the expected primitive
type."""
def from_slice(v: object) -> T: ...

"""Deserialize an instance of type `T` from a string of JSON text.

# Example

```
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct User {
fingerprint: String,
location: String,
}

fn main() {
// The type of `j` is `&str`
let j = "
{
\\"fingerprint\\": \\"0xF9BA143B95FF6D82\\",
\\"location\\": \\"Menlo Park, CA\\"
}";

let u: User = serde_json::from_str(j).unwrap();
println!("{:#?}", u);
}
```

# Errors

This conversion can fail if the structure of the input does not match the
structure expected by `T`, for example if `T` is a struct type but the input
contains something other than a JSON map. It can also fail if the structure
is correct but `T`'s implementation of `Deserialize` decides that something
is wrong with the data, for example required struct fields are missing from
the JSON map or some number is too big to fit in the expected primitive
type."""
def from_str(s: object) -> T: ...

"""Serialize the given data structure as JSON into the I/O stream.

Serialization guarantees it only feeds valid UTF-8 sequences to the writer.

# Errors

Serialization can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys."""
def to_writer(writer: W, value: T) -> None: ...

"""Serialize the given data structure as pretty-printed JSON into the I/O
stream.

Serialization guarantees it only feeds valid UTF-8 sequences to the writer.

# Errors

Serialization can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys."""
def to_writer_pretty(writer: W, value: T) -> None: ...

"""Serialize the given data structure as a JSON byte vector.

# Errors

Serialization can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys."""
def to_vec(value: T) -> list[int]: ...

"""Serialize the given data structure as a pretty-printed JSON byte vector.

# Errors

Serialization can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys."""
def to_vec_pretty(value: T) -> list[int]: ...

"""Serialize the given data structure as a String of JSON.

# Errors

Serialization can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys."""
def to_string(value: T) -> str: ...

"""Serialize the given data structure as a pretty-printed String of JSON.

# Errors

Serialization can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys."""
def to_string_pretty(value: T) -> str: ...

"""Convert a `T` into `serde_json::Value` which is an enum that can represent
any valid JSON data.

# Example

```
use serde::Serialize;
use serde_json::json;
use std::error::Error;

#[derive(Serialize)]
struct User {
fingerprint: String,
location: String,
}

fn compare_json_values() -> Result<(), Box<dyn Error>> {
let u = User {
fingerprint: "0xF9BA143B95FF6D82".to_owned(),
location: "Menlo Park, CA".to_owned(),
};

// The type of `expected` is `serde_json::Value`
let expected = json!({
"fingerprint": "0xF9BA143B95FF6D82",
"location": "Menlo Park, CA",
});

let v = serde_json::to_value(u).unwrap();
assert_eq!(v, expected);

Ok(())
}
#
# compare_json_values().unwrap();
```

# Errors

This conversion can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys.

```
use std::collections::BTreeMap;

fn main() {
// The keys in this map are vectors, not strings.
let mut map = BTreeMap::new();
map.insert(vec![32, 64], "x86");

println!("{}", serde_json::to_value(map).unwrap_err());
}
```"""
def to_value(value: T) -> Value: ...

"""Interpret a `serde_json::Value` as an instance of type `T`.

# Example

```
use serde::Deserialize;
use serde_json::json;

#[derive(Deserialize, Debug)]
struct User {
fingerprint: String,
location: String,
}

fn main() {
// The type of `j` is `serde_json::Value`
let j = json!({
"fingerprint": "0xF9BA143B95FF6D82",
"location": "Menlo Park, CA"
});

let u: User = serde_json::from_value(j).unwrap();
println!("{:#?}", u);
}
```

# Errors

This conversion can fail if the structure of the Value does not match the
structure expected by `T`, for example if `T` is a struct type but the Value
contains something other than a JSON map. It can also fail if the structure
is correct but `T`'s implementation of `Deserialize` decides that something
is wrong with the data, for example required struct fields are missing from
the JSON map or some number is too big to fit in the expected primitive
type."""
def from_value(value: Value) -> T: ...

"""Check if any of the remaining bits are non-zero."""
def nonzero(x: object, rindex: int) -> bool: ...

"""Add two small integers and return the resulting value and if overflow happens."""
def add(x: Limb, y: Limb) -> object: ...

"""AddAssign two small integers and return if overflow happens."""
def iadd(x: Limb, y: Limb) -> bool: ...

"""Subtract two small integers and return the resulting value and if overflow happens."""
def sub(x: Limb, y: Limb) -> object: ...

"""SubAssign two small integers and return if overflow happens."""
def isub(x: Limb, y: Limb) -> bool: ...

"""Multiply two small integers (with carry) (and return the overflow contribution).

Returns the (low, high) components."""
def mul(x: Limb, y: Limb, carry: Limb) -> object: ...

"""Multiply two small integers (with carry) (and return if overflow happens)."""
def imul(x: Limb, y: Limb, carry: Limb) -> Limb: ...

"""Implied AddAssign implementation for adding a small integer to bigint.

Allows us to choose a start-index in x to store, to allow incrementing
from a non-zero start."""
def iadd_impl(x: list[Limb], y: Limb, xstart: int) -> None: ...

"""AddAssign small integer to bigint."""
def iadd(x: list[Limb], y: Limb) -> None: ...

"""SubAssign small integer to bigint.
Does not do overflowing subtraction."""
def isub_impl(x: list[Limb], y: Limb, xstart: int) -> None: ...

"""MulAssign small integer to bigint."""
def imul(x: list[Limb], y: Limb) -> None: ...

"""Mul small integer to bigint."""
def mul(x: object, y: Limb) -> list[Limb]: ...

"""MulAssign by a power.

Theoretically...

Use an exponentiation by squaring method, since it reduces the time
complexity of the multiplication to ~`O(log(n))` for the squaring,
and `O(n*m)` for the result. Since `m` is typically a lower-order
factor, this significantly reduces the number of multiplications
we need to do. Iteratively multiplying by small powers follows
the nth triangular number series, which scales as `O(p^2)`, but
where `p` is `n+m`. In short, it scales very poorly.

Practically....

Exponentiation by Squaring:
running 2 tests
test bigcomp_f32_lexical ... bench:       1,018 ns/iter (+/- 78)
test bigcomp_f64_lexical ... bench:       3,639 ns/iter (+/- 1,007)

Exponentiation by Iterative Small Powers:
running 2 tests
test bigcomp_f32_lexical ... bench:         518 ns/iter (+/- 31)
test bigcomp_f64_lexical ... bench:         583 ns/iter (+/- 47)

Exponentiation by Iterative Large Powers (of 2):
running 2 tests
test bigcomp_f32_lexical ... bench:         671 ns/iter (+/- 31)
test bigcomp_f64_lexical ... bench:       1,394 ns/iter (+/- 47)

Even using worst-case scenarios, exponentiation by squaring is
significantly slower for our workloads. Just multiply by small powers,
in simple cases, and use precalculated large powers in other cases."""
def imul_pow5(x: list[Limb], n: int) -> None: ...

"""Get number of leading zero bits in the storage."""
def leading_zeros(x: object) -> int: ...

"""Calculate the bit-length of the big-integer."""
def bit_length(x: object) -> int: ...

"""Shift-left bits inside a buffer.

Assumes `n < Limb::BITS`, IE, internally shifting bits."""
def ishl_bits(x: list[Limb], n: int) -> None: ...

"""Shift-left `n` digits inside a buffer.

Assumes `n` is not 0."""
def ishl_limbs(x: list[Limb], n: int) -> None: ...

"""Shift-left buffer by n bits."""
def ishl(x: list[Limb], n: int) -> None: ...

"""Normalize the container by popping any leading zeros."""
def normalize(x: list[Limb]) -> None: ...

"""Compare `x` to `y`, in little-endian order."""
def compare(x: object, y: object) -> Ordering: ...

"""Check if x is less than y."""
def less(x: object, y: object) -> bool: ...

"""Check if x is greater than or equal to y."""
def greater_equal(x: object, y: object) -> bool: ...

"""Implied AddAssign implementation for bigints.

Allows us to choose a start-index in x to store, so we can avoid
padding the buffer with zeros when not needed, optimized for vectors."""
def iadd_impl(x: list[Limb], y: object, xstart: int) -> None: ...

"""AddAssign bigint to bigint."""
def iadd(x: list[Limb], y: object) -> None: ...

"""Add bigint to bigint."""
def add(x: object, y: object) -> list[Limb]: ...

"""SubAssign bigint to bigint."""
def isub(x: list[Limb], y: object) -> None: ...

"""Split two buffers into halfway, into (lo, hi)."""
def karatsuba_split(z: object, m: int) -> object: ...

"""MulAssign bigint to bigint."""
def imul(x: list[Limb], y: object) -> None: ...

"""Parse float for which the entire integer and fraction parts fit into a 64
bit mantissa."""
def parse_concise_float(mantissa: int, mant_exp: int) -> F: ...

"""Parse float from extracted float components.

* `integer`     - Slice containing the integer digits.
* `fraction`    - Slice containing the fraction digits.
* `exponent`    - Parsed, 32-bit exponent.

Precondition: The integer must not have leading zeros."""
def parse_truncated_float(integer: object, fraction: object, exponent: int) -> F: ...

"""Convert a `T` into a boxed `RawValue`.

# Example

```
// Upstream crate
# #[derive(Serialize)]
pub struct Thing {
foo: String,
bar: Option<String>,
extra_data: Box<RawValue>,
}

// Local crate
use serde::Serialize;
use serde_json::value::{to_raw_value, RawValue};

#[derive(Serialize)]
struct MyExtraData {
a: u32,
b: u32,
}

let my_thing = Thing {
foo: "FooVal".into(),
bar: None,
extra_data: to_raw_value(&MyExtraData { a: 1, b: 2 }).unwrap(),
};
# assert_eq!(
#     serde_json::to_value(my_thing).unwrap(),
#     serde_json::json!({
#         "foo": "FooVal",
#         "bar": null,
#         "extra_data": { "a": 1, "b": 2 }
#     })
# );
```

# Errors

This conversion can fail if `T`'s implementation of `Serialize` decides to
fail, or if `T` contains a map with non-string keys.

```
use std::collections::BTreeMap;

// The keys in this map are vectors, not strings.
let mut map = BTreeMap::new();
map.insert(vec![32, 64], "x86");

println!("{}", serde_json::value::to_raw_value(&map).unwrap_err());
```"""
def to_raw_value(value: T) -> RawValue: ...

__all__: list[str] = ["from_reader", "from_slice", "from_str", "to_writer", "to_writer_pretty", "to_vec", "to_vec_pretty", "to_string", "to_string_pretty", "to_value", "from_value", "nonzero", "add", "iadd", "sub", "isub", "mul", "imul", "iadd_impl", "iadd", "isub_impl", "imul", "mul", "imul_pow5", "leading_zeros", "bit_length", "ishl_bits", "ishl_limbs", "ishl", "normalize", "compare", "less", "greater_equal", "iadd_impl", "iadd", "add", "isub", "karatsuba_split", "imul", "parse_concise_float", "parse_truncated_float", "to_raw_value", "Map", "VacantEntry", "OccupiedEntry", "Iter", "IterMut", "IntoIter", "Keys", "Values", "ValuesMut", "IntoValues", "LineColIterator", "Error", "Deserializer", "StreamDeserializer", "Number", "NumberFromString", "Position", "IoRead", "SliceRead", "StrRead", "Serializer", "CompactFormatter", "PrettyFormatter", "Serializer", "SerializeVec", "SerializeTupleVariant", "SerializeStructVariant", "Error", "RawValue", "ReferenceFromString", "BoxedFromString", "OwnedRawDeserializer", "BorrowedRawDeserializer", "Entry", "ErrorKind", "Reference", "State", "Compound", "CharEscape", "SerializeMap", "Value", "Category"]
