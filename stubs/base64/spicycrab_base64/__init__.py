"""Python stubs for the base64 Rust crate.

Install with: cookcrab install base64
"""

from __future__ import annotations

from typing import Self

class Naive:
    """Comparatively simple implementation that can be used as something to compare against in tests"""

    @staticmethod
    def new(alphabet: Alphabet, config: NaiveConfig) -> "Naive": ...

    def internal_encode(self, input: object, output: object) -> int: ...

    def internal_decoded_len_estimate(self, input_len: int) -> DecodeEstimate: ...

    def internal_decode(self, input: object, output: object, estimate: DecodeEstimate) -> DecodeMetadata: ...

    def config(self) -> Config: ...

class NaiveEstimate:

    def decoded_len_estimate(self) -> int: ...

class NaiveConfig:

    def encode_padding(self) -> bool: ...

class GeneralPurpose:
    """A general-purpose base64 engine.

- It uses no vector CPU instructions, so it will work on any system.
- It is reasonably fast (~2-3GiB/s).
- It is not constant-time, though, so it is vulnerable to timing side-channel attacks. For loading cryptographic keys, etc, it is suggested to use the forthcoming constant-time implementation."""

    @staticmethod
    def new(alphabet: Alphabet, config: GeneralPurposeConfig) -> "GeneralPurpose": ...

    def internal_encode(self, input: object, output: object) -> int: ...

    def internal_decoded_len_estimate(self, input_len: int) -> DecodeEstimate: ...

    def internal_decode(self, input: object, output: object, estimate: DecodeEstimate) -> DecodeMetadata: ...

    def config(self) -> Config: ...

class GeneralPurposeConfig:
    """Contains configuration parameters for base64 encoding and decoding.

```
# use base64::engine::GeneralPurposeConfig;
let config = GeneralPurposeConfig::new()
.with_encode_padding(false);
// further customize using `.with_*` methods as needed
```

The constants [PAD] and [NO_PAD] cover most use cases.

To specify the characters used, see [Alphabet]."""

    @staticmethod
    def new() -> "GeneralPurposeConfig": ...

    def with_encode_padding(self, padding: bool) -> Self: ...

    def with_decode_allow_trailing_bits(self, allow: bool) -> Self: ...

    def with_decode_padding_mode(self, mode: DecodePaddingMode) -> Self: ...

    @staticmethod
    def default() -> "GeneralPurposeConfig": ...

    def encode_padding(self) -> bool: ...

class GeneralPurposeEstimate:

    def decoded_len_estimate(self) -> int: ...

class DecodeMetadata:
    """Metadata about the result of a decode operation"""
    pass

class Alphabet:
    """An alphabet defines the 64 ASCII characters (symbols) used for base64.

Common alphabets are provided as constants, and custom alphabets
can be made via `from_str` or the `TryFrom<str>` implementation.

# Examples

Building and using a custom Alphabet:

```
let custom = base64::alphabet::Alphabet::new("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/").unwrap();

let engine = base64::engine::GeneralPurpose::new(
&custom,
base64::engine::general_purpose::PAD);
```

Building a const:

```
use base64::alphabet::Alphabet;

static CUSTOM: Alphabet = {
// Result::unwrap() isn't const yet, but panic!() is OK
match Alphabet::new("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/") {
Ok(x) => x,
Err(_) => panic!("creation of alphabet failed"),
}
};
```

Building lazily:

```
use base64::{
alphabet::Alphabet,
engine::{general_purpose::GeneralPurpose, GeneralPurposeConfig},
};
use once_cell::sync::Lazy;

static CUSTOM: Lazy<Alphabet> = Lazy::new(||
Alphabet::new("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/").unwrap()
);
```"""

    @staticmethod
    def new(alphabet: str) -> object: ...

    def as_str(self) -> str: ...

    @staticmethod
    def try_from(value: str) -> object: ...

class EncoderStringWriter:
    """A `Write` implementation that base64-encodes data using the provided config and accumulates the
resulting base64 utf8 `&str` in a [StrConsumer] implementation (typically `String`), which is
then exposed via `into_inner()`.

# Examples

Buffer base64 in a new String:

```
use std::io::Write;
use base64::engine::general_purpose;

let mut enc = base64::write::EncoderStringWriter::new(&general_purpose::STANDARD);

enc.write_all(b"asdf").unwrap();

// get the resulting String
let b64_string = enc.into_inner();

assert_eq!("YXNkZg==", &b64_string);
```

Or, append to an existing `String`, which implements `StrConsumer`:

```
use std::io::Write;
use base64::engine::general_purpose;

let mut buf = String::from("base64: ");

let mut enc = base64::write::EncoderStringWriter::from_consumer(
&mut buf,
&general_purpose::STANDARD);

enc.write_all(b"asdf").unwrap();

// release the &mut reference on buf
let _ = enc.into_inner();

assert_eq!("base64: YXNkZg==", &buf);
```

# Performance

Because it has to validate that the base64 is UTF-8, it is about 80% as fast as writing plain
bytes to a `io::Write`."""

    @staticmethod
    def from_consumer(str_consumer: S, engine: object) -> "EncoderStringWriter": ...

    def into_inner(self) -> S: ...

    @staticmethod
    def new(engine: object) -> "EncoderStringWriter": ...

    def write(self, buf: object) -> int: ...

    def flush(self) -> object: ...

class EncoderWriter:
    """A `Write` implementation that base64 encodes data before delegating to the wrapped writer.

Because base64 has special handling for the end of the input data (padding, etc), there's a
`finish()` method on this type that encodes any leftover input bytes and adds padding if
appropriate. It's called automatically when deallocated (see the `Drop` implementation), but
any error that occurs when invoking the underlying writer will be suppressed. If you want to
handle such errors, call `finish()` yourself.

# Examples

```
use std::io::Write;
use base64::engine::general_purpose;

// use a vec as the simplest possible `Write` -- in real code this is probably a file, etc.
let mut enc = base64::write::EncoderWriter::new(Vec::new(), &general_purpose::STANDARD);

// handle errors as you normally would
enc.write_all(b"asdf").unwrap();

// could leave this out to be called by Drop, if you don't care
// about handling errors or getting the delegate writer back
let delegate = enc.finish().unwrap();

// base64 was written to the writer
assert_eq!(b"YXNkZg==", &delegate[..]);

```

# Panics

Calling `write()` (or related methods) or `finish()` after `finish()` has completed without
error is invalid and will panic.

# Errors

Base64 encoding itself does not generate errors, but errors from the wrapped writer will be
returned as per the contract of `Write`.

# Performance

It has some minor performance loss compared to encoding slices (a couple percent).
It does not do any heap allocation.

# Limitations

Owing to the specification of the `write` and `flush` methods on the `Write` trait and their
implications for a buffering implementation, these methods may not behave as expected. In
particular, calling `write_all` on this interface may fail with `io::ErrorKind::WriteZero`.
See the documentation of the `Write` trait implementation for further details."""

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(delegate: W, engine: object) -> object: ...

    def finish(self) -> W: ...

    def into_inner(self) -> W: ...

    def write(self, input: object) -> int: ...

    def flush(self) -> None: ...

    def drop(self) -> None: ...

class DecoderReader:
    """A `Read` implementation that decodes base64 data read from an underlying reader.

# Examples

```
use std::io::Read;
use std::io::Cursor;
use base64::engine::general_purpose;

// use a cursor as the simplest possible `Read` -- in real code this is probably a file, etc.
let mut wrapped_reader = Cursor::new(b"YXNkZg==");
let mut decoder = base64::read::DecoderReader::new(
&mut wrapped_reader,
&general_purpose::STANDARD);

// handle errors as you normally would
let mut result = Vec::new();
decoder.read_to_end(&mut result).unwrap();

assert_eq!(b"asdf", &result[..]);

```"""

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(reader: R, engine: object) -> "DecoderReader": ...

    def into_inner(self) -> R: ...

    def read(self, buf: object) -> int: ...

class ChunkedEncoder:
    """A base64 encoder that emits encoded bytes in chunks without heap allocation."""

    @staticmethod
    def new(engine: object) -> object: ...

    def encode(self, bytes: object, sink: S) -> None: ...

class Base64Display:
    """A convenience wrapper for base64'ing bytes into a format string without heap allocation."""

    @staticmethod
    def new(bytes: object, engine: object) -> object: ...

    def fmt(self, formatter: Formatter) -> None: ...

class DecodePaddingMode:
    """Controls how pad bytes are handled when decoding.

Each [Engine] must support at least the behavior indicated by
[DecodePaddingMode::RequireCanonical], and may support other modes."""
    Indifferent: "DecodePaddingMode"
    RequireCanonical: "DecodePaddingMode"
    RequireNone: "DecodePaddingMode"

class EncodeSliceError:
    """Errors that can occur while encoding into a slice."""
    OutputSliceTooSmall: "EncodeSliceError"

    def fmt(self, f: Formatter) -> Result: ...

class ParseAlphabetError:
    """Possible errors when constructing an [Alphabet] from a `str`."""
    InvalidLength: "ParseAlphabetError"
    DuplicatedByte: "ParseAlphabetError"
    UnprintableByte: "ParseAlphabetError"
    ReservedByte: "ParseAlphabetError"

    def fmt(self, f: Formatter) -> Result: ...

class DecodeError:
    """Errors that can occur while decoding."""
    InvalidByte: "DecodeError"
    InvalidLength: "DecodeError"
    InvalidLastSymbol: "DecodeError"
    InvalidPadding: "DecodeError"

    def fmt(self, f: Formatter) -> Result: ...

class DecodeSliceError:
    """Errors that can occur while decoding into a slice."""
    DecodeError: "DecodeSliceError"
    OutputSliceTooSmall: "DecodeSliceError"

    def fmt(self, f: Formatter) -> Result: ...

    def source(self) -> object: ...

    @staticmethod
    def from_(e: DecodeError) -> "DecodeSliceError": ...

"""Encode arbitrary octets as base64 using the [`STANDARD` engine](STANDARD).

See [Engine::encode]."""
def encode(input: T) -> str: ...

"""Encode arbitrary octets as base64 using the provided `Engine` into a new `String`.

See [Engine::encode]."""
def encode_engine(input: T, engine: E) -> str: ...

"""Encode arbitrary octets as base64 into a supplied `String`.

See [Engine::encode_string]."""
def encode_engine_string(input: T, output_buf: str, engine: E) -> None: ...

"""Encode arbitrary octets as base64 into a supplied slice.

See [Engine::encode_slice]."""
def encode_engine_slice(input: T, output_buf: object, engine: E) -> int: ...

"""Calculate the base64 encoded length for a given input length, optionally including any
appropriate padding bytes.

Returns `None` if the encoded length can't be represented in `usize`. This will happen for
input lengths in approximately the top quarter of the range of `usize`."""
def encoded_len(bytes_len: int, padding: bool) -> int | None: ...

def chunked_encode_matches_normal_encode_random(sink_test_helper: S) -> None: ...

def assert_encode_sanity(encoded: str, padded: bool, input_len: int) -> None: ...

def random_config(rng: R) -> GeneralPurposeConfig: ...

def random_alphabet(rng: R) -> Alphabet: ...

def random_engine(rng: R) -> GeneralPurpose: ...

"""Decode base64 using the [`STANDARD` engine](STANDARD).

See [Engine::decode]."""
def decode(input: T) -> list[int]: ...

"""Decode from string reference as octets using the specified [Engine].

See [Engine::decode].
Returns a `Result` containing a `Vec<u8>`."""
def decode_engine(input: T, engine: E) -> list[int]: ...

"""Decode from string reference as octets.

See [Engine::decode_vec]."""
def decode_engine_vec(input: T, buffer: list[int], engine: E) -> None: ...

"""Decode the input into the provided output slice.

See [Engine::decode_slice]."""
def decode_engine_slice(input: T, output: object, engine: E) -> int: ...

"""Returns a conservative estimate of the decoded size of `encoded_len` base64 symbols (rounded up
to the next group of 3 decoded bytes).

The resulting length will be a safe choice for the size of a decode buffer, but may have up to
2 trailing bytes that won't end up being needed.

# Examples

```
use base64::decoded_len_estimate;

assert_eq!(3, decoded_len_estimate(1));
assert_eq!(3, decoded_len_estimate(2));
assert_eq!(3, decoded_len_estimate(3));
assert_eq!(3, decoded_len_estimate(4));
// start of the next quad of encoded symbols
assert_eq!(6, decoded_len_estimate(5));
```"""
def decoded_len_estimate(encoded_len: int) -> int: ...

# ====================================================
# Module-level Constants
# ====================================================

URL_SAFE_NO_PAD: GeneralPurpose = ...
STANDARD: GeneralPurpose = ...
STANDARD_NO_PAD: GeneralPurpose = ...
URL_SAFE: GeneralPurpose = ...

__all__: list[str] = ["encode", "encode_engine", "encode_engine_string", "encode_engine_slice", "encoded_len", "chunked_encode_matches_normal_encode_random", "assert_encode_sanity", "random_config", "random_alphabet", "random_engine", "decode", "decode_engine", "decode_engine_vec", "decode_engine_slice", "decoded_len_estimate", "Naive", "NaiveEstimate", "NaiveConfig", "GeneralPurpose", "GeneralPurposeConfig", "GeneralPurposeEstimate", "DecodeMetadata", "Alphabet", "EncoderStringWriter", "EncoderWriter", "DecoderReader", "ChunkedEncoder", "Base64Display", "DecodePaddingMode", "EncodeSliceError", "ParseAlphabetError", "DecodeError", "DecodeSliceError", "URL_SAFE_NO_PAD", "STANDARD", "STANDARD_NO_PAD", "URL_SAFE"]
