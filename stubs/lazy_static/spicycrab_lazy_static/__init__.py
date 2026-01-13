"""Python stubs for the lazy_static Rust crate.

Install with: cookcrab install lazy_static
"""

from __future__ import annotations

from typing import Self

class Lazy:

    def get(self, builder: F) -> T: ...

    def get(self, f: F) -> T: ...

class Lazy:

    def get(self, builder: F) -> T: ...

    def get(self, f: F) -> T: ...

"""Takes a shared reference to a lazy static and initializes
it if it has not been already.

This can be used to control the initialization point of a lazy static.

Example:

```rust
use lazy_static::lazy_static;

lazy_static! {
static ref BUFFER: Vec<u8> = (0..255).collect();
}

fn main() {
lazy_static::initialize(&BUFFER);

// ...
work_with_initialized_data(&BUFFER);
}
# fn work_with_initialized_data(_: &[u8]) {}
```"""
def initialize(lazy: T) -> None: ...

__all__: list[str] = ["initialize", "Lazy", "Lazy"]
