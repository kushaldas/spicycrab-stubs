"""Python stubs for the sha2 Rust crate.

Install with: cookcrab install sha2
"""

from __future__ import annotations

from typing import Self

class Sha256:
    """SHA-256 hasher.

    Maps to sha2::Sha256 in Rust (type alias for CoreWrapper<Sha256VarCore>).
    """

    @staticmethod
    def digest(data: bytes) -> bytes:
        """Compute SHA-256 hash of data in one shot.

        Args:
            data: Bytes to hash

        Returns:
            32-byte hash digest
        """
        ...

    @staticmethod
    def new() -> "Sha256":
        """Create a new SHA-256 hasher."""
        ...

    def update(self, data: bytes) -> None:
        """Update the hasher with data."""
        ...

    def finalize(self) -> bytes:
        """Finalize and return the hash."""
        ...


class Sha512:
    """SHA-512 hasher.

    Maps to sha2::Sha512 in Rust.
    """

    @staticmethod
    def digest(data: bytes) -> bytes:
        """Compute SHA-512 hash of data in one shot."""
        ...

    @staticmethod
    def new() -> "Sha512":
        """Create a new SHA-512 hasher."""
        ...


class Sha256VarCore:
    """Core block-level SHA-256 hasher with variable output size.

Supports initialization only for 28 and 32 byte output sizes,
i.e. 224 and 256 bits respectively."""

    def update_blocks(self, blocks: object) -> None: ...

    @staticmethod
    def new(output_size: int) -> object: ...

    def finalize_variable_core(self, buffer: object, out: object) -> None: ...

    @staticmethod
    def write_alg_name(f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

    def serialize(self) -> object: ...

    @staticmethod
    def deserialize(serialized_state: object) -> object: ...

class Sha512VarCore:
    """Core block-level SHA-512 hasher with variable output size.

Supports initialization only for 28, 32, 48, and 64 byte output sizes,
i.e. 224, 256, 384, and 512 bits respectively."""

    def update_blocks(self, blocks: object) -> None: ...

    @staticmethod
    def new(output_size: int) -> object: ...

    def finalize_variable_core(self, buffer: object, out: object) -> None: ...

    @staticmethod
    def write_alg_name(f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

    def serialize(self) -> object: ...

    @staticmethod
    def deserialize(serialized_state: object) -> object: ...

"""Raw SHA-256 compression function.

This is a low-level "hazmat" API which provides direct access to the core
functionality of SHA-256."""
def compress256(state: object, blocks: object) -> None: ...

"""Raw SHA-512 compression function.

This is a low-level "hazmat" API which provides direct access to the core
functionality of SHA-512."""
def compress512(state: object, blocks: object) -> None: ...

__all__: list[str] = ["compress256", "compress512", "Sha256VarCore", "Sha512VarCore"]
