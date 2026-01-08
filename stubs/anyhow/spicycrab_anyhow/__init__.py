"""Python stubs for the anyhow Rust crate.

Install with: cookcrab install anyhow
"""

from __future__ import annotations

from typing import Self, TypeVar, Generic

T = TypeVar('T')
E = TypeVar('E')


class Result(Generic[T, E]):
    """A Result type alias for anyhow.

    Maps to anyhow::Result which is an alias for core::result::Result<T,E>.
    """

    @staticmethod
    def Ok(value: T) -> "Result[T, E]":
        """Create a successful result."""
        ...

    @staticmethod
    def Err(error: E) -> "Result[T, E]":
        """Create an error result."""
        ...

class Error:
    """The `Error` type, a wrapper around a dynamic error type.

`Error` works a lot like `Box<dyn std::error::Error>`, but with these
differences:

- `Error` requires that the error is `Send`, `Sync`, and `'static`.
- `Error` guarantees that a backtrace is available, even if the underlying
error type does not provide one.
- `Error` is represented as a narrow pointer &mdash; exactly one word in
size instead of two.

<br>

# Display representations

When you print an error object using "{}" or to_string(), only the outermost
underlying error or context is printed, not any of the lower level causes.
This is exactly as if you had called the Display impl of the error from
which you constructed your anyhow::Error.

```console
Failed to read instrs from ./path/to/instrs.json
```

To print causes as well using anyhow's default formatting of causes, use the
alternate selector "{:#}".

```console
Failed to read instrs from ./path/to/instrs.json: No such file or directory (os error 2)
```

The Debug format "{:?}" includes your backtrace if one was captured. Note
that this is the representation you get by default if you return an error
from `fn main` instead of printing it explicitly yourself.

```console
Error: Failed to read instrs from ./path/to/instrs.json

Caused by:
No such file or directory (os error 2)
```

and if there is a backtrace available:

```console
Error: Failed to read instrs from ./path/to/instrs.json

Caused by:
No such file or directory (os error 2)

Stack backtrace:
0: <E as anyhow::context::ext::StdError>::ext_context
at /git/anyhow/src/backtrace.rs:26
1: core::result::Result<T,E>::map_err
at /git/rustc/src/libcore/result.rs:596
2: anyhow::context::<impl anyhow::Context<T,E> for core::result::Result<T,E>>::with_context
at /git/anyhow/src/context.rs:58
3: testing::main
at src/main.rs:5
4: std::rt::lang_start
at /git/rustc/src/libstd/rt.rs:61
5: main
6: __libc_start_main
7: _start
```

To see a conventional struct-style Debug representation, use "{:#?}".

```console
Error {
context: "Failed to read instrs from ./path/to/instrs.json",
source: Os {
code: 2,
kind: NotFound,
message: "No such file or directory",
},
}
```

If none of the built-in representations are appropriate and you would prefer
to render the error and its cause chain yourself, it can be done something
like this:

```
use anyhow::{Context, Result};

fn main() {
if let Err(err) = try_main() {
eprintln!("ERROR: {}", err);
err.chain().skip(1).for_each(|cause| eprintln!("because: {}", cause));
std::process::exit(1);
}
}

fn try_main() -> Result<()> {
# const IGNORE: &str = stringify! {
...
# };
# Ok(())
}
```"""

    def ext_context(self, context: C) -> Exception: ...

    @staticmethod
    def new(error: E) -> "Error": ...

    @staticmethod
    def msg(message: M) -> "Error": ...

    @staticmethod
    def from_boxed(boxed_error: object) -> "Error": ...

    def context(self, context: C) -> Self: ...

    def backtrace(self) -> object: ...

    def chain(self) -> Chain: ...

    def root_cause(self) -> object: ...

    def is_(self) -> bool: ...

    def downcast(self) -> E: ...

    def downcast_ref(self) -> object: ...

    def downcast_mut(self) -> object: ...

    def into_boxed_dyn_error(self) -> object: ...

    def reallocate_into_boxed_dyn_error_without_backtrace(self) -> object: ...

    def thiserror_provide(self, request: Request) -> None: ...

    @staticmethod
    def from_(error: E) -> "Error": ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, formatter: Formatter) -> Result: ...

    def fmt(self, formatter: Formatter) -> Result: ...

    def drop(self) -> None: ...

    def as_ref(self) -> object: ...

    def as_ref(self) -> object: ...

class Chain:
    """Iterator of a chain of source errors.

This type is the iterator returned by [`Error::chain`].

# Example

```
use anyhow::Error;
use std::io;

pub fn underlying_io_error_kind(error: &Error) -> Option<io::ErrorKind> {
for cause in error.chain() {
if let Some(io_error) = cause.downcast_ref::<io::Error>() {
return Some(io_error.kind());
}
}
None
}
```"""

    @staticmethod
    def new(head: object) -> "Chain": ...

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

    def len(self) -> int: ...

    @staticmethod
    def default() -> "Chain": ...

class MessageError:

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class DisplayError:

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class BoxedError:

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def source(self) -> object: ...

    def provide(self, request: Request) -> None: ...

class Own:

    def clone(self) -> Self: ...

    @staticmethod
    def new(ptr: T) -> "Own": ...

    def cast(self) -> object: ...

    def boxed(self) -> T: ...

    def by_ref(self) -> object: ...

    def by_mut(self) -> object: ...

class Ref:

    def clone(self) -> Self: ...

    @staticmethod
    def new(ptr: object) -> "Ref": ...

    @staticmethod
    def from_raw(ptr: object) -> "Ref": ...

    def cast(self) -> object: ...

    def by_mut(self) -> object: ...

    def as_ptr(self) -> object: ...

    def deref(self) -> object: ...

class Mut:

    def clone(self) -> Self: ...

    @staticmethod
    def new(ptr: object) -> "Mut": ...

    def cast(self) -> object: ...

    def by_ref(self) -> object: ...

    def extend(self) -> object: ...

    def deref_mut(self) -> object: ...

    def read(self) -> T: ...

class Adhoc:

    def new(self, message: M) -> Exception: ...

class Trait:

    def new(self, error: E) -> Exception: ...

class Boxed:

    def new(self, error: object) -> Exception: ...

__all__: list[str] = ["Result", "Error", "Chain", "MessageError", "DisplayError", "BoxedError", "Own", "Ref", "Mut", "Adhoc", "Trait", "Boxed"]
