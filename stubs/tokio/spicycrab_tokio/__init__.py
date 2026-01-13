"""Python stubs for the tokio Rust crate.

Install with: cookcrab install tokio
"""

from __future__ import annotations

from typing import Self

class Duration:
    """A Duration type representing a span of time.

    Maps to std::time::Duration in Rust.
    """

    @staticmethod
    def from_secs(secs: int) -> "Duration":
        """Creates a new Duration from seconds."""
        ...

    @staticmethod
    def from_millis(millis: int) -> "Duration":
        """Creates a new Duration from milliseconds."""
        ...

    @staticmethod
    def from_micros(micros: int) -> "Duration":
        """Creates a new Duration from microseconds."""
        ...

    @staticmethod
    def from_nanos(nanos: int) -> "Duration":
        """Creates a new Duration from nanoseconds."""
        ...

    def as_secs(self) -> int:
        """Returns the number of whole seconds."""
        ...

    def as_millis(self) -> int:
        """Returns the total number of milliseconds."""
        ...


class Instant:
    """A measurement of a monotonically nondecreasing clock.

    Maps to tokio::time::Instant in Rust.
    """

    @staticmethod
    def now() -> "Instant":
        """Returns the current instant."""
        ...

    def elapsed(self) -> Duration:
        """Returns the time elapsed since this instant."""
        ...


class MpscSender:
    """Sender half of a bounded mpsc channel.

    Maps to tokio::sync::mpsc::Sender<String> in Rust.
    Use with mpsc_channel() for type-safe channel creation.
    """

    async def send(self, value: str) -> None:
        """Sends a value, waiting until there is capacity."""
        ...

    def clone(self) -> "MpscSender":
        """Clones this sender."""
        ...

    def is_closed(self) -> bool:
        """Returns True if the receiver has been dropped."""
        ...


class MpscReceiver:
    """Receiver half of a bounded mpsc channel.

    Maps to tokio::sync::mpsc::Receiver<String> in Rust.
    Use with mpsc_channel() for type-safe channel creation.
    """

    async def recv(self) -> str | None:
        """Receives the next value, or None if the channel is closed."""
        ...

    def close(self) -> None:
        """Closes the receiving half without dropping it."""
        ...


from typing import TypeVar, Generic

T = TypeVar("T")


class Arc(Generic[T]):
    """Thread-safe reference-counting pointer.

    Arc stands for Atomically Reference Counted. It provides shared ownership
    of a value of type T, allocated on the heap. Cloning an Arc produces a new
    Arc that points to the same allocation, increasing the reference count.

    Maps to std::sync::Arc<T> in Rust.

    Common use cases:
    - Sharing immutable data between spawned tasks
    - Combined with Mutex for shared mutable state: Arc[Mutex[T]]

    Example:
        data: Arc[str] = Arc.new("shared config")
        cloned: Arc[str] = Arc.clone(data)

        # Share between tasks
        handle1 = spawn(worker(Arc.clone(data)))
        handle2 = spawn(worker(Arc.clone(data)))
    """

    @staticmethod
    def new(value: T) -> "Arc[T]":
        """Constructs a new Arc<T>.

        Args:
            value: The value to wrap in an Arc.

        Returns:
            A new Arc containing the value.
        """
        ...

    @staticmethod
    def clone(arc: "Arc[T]") -> "Arc[T]":
        """Creates a new Arc that points to the same allocation.

        This increments the strong reference count.

        Args:
            arc: The Arc to clone.

        Returns:
            A new Arc pointing to the same data.
        """
        ...

    @staticmethod
    def strong_count(arc: "Arc[T]") -> int:
        """Gets the number of strong (Arc) pointers to this allocation.

        Args:
            arc: The Arc to check.

        Returns:
            The number of strong references.
        """
        ...

    @staticmethod
    def weak_count(arc: "Arc[T]") -> int:
        """Gets the number of weak (Weak) pointers to this allocation.

        Args:
            arc: The Arc to check.

        Returns:
            The number of weak references.
        """
        ...

    @staticmethod
    def try_unwrap(arc: "Arc[T]") -> T | None:
        """Returns the inner value if the Arc has exactly one strong reference.

        If there are multiple strong references, returns None.

        Args:
            arc: The Arc to unwrap.

        Returns:
            The inner value if ref count is 1, otherwise None.
        """
        ...

    @staticmethod
    def into_inner(arc: "Arc[T]") -> T | None:
        """Returns the inner value if the Arc has exactly one strong reference.

        This is similar to try_unwrap but available on Rust 1.70+.

        Args:
            arc: The Arc to unwrap.

        Returns:
            The inner value if ref count is 1, otherwise None.
        """
        ...


class Mutex(Generic[T]):
    """An asynchronous mutual exclusion primitive.

    This is tokio's async-aware Mutex, suitable for use across .await points.
    Unlike std::sync::Mutex, holding a tokio::sync::Mutex guard across an
    await point is safe.

    Maps to tokio::sync::Mutex<T> in Rust.

    Common use case - shared mutable state between tasks:
        counter: Arc[Mutex[int]] = Arc.new(Mutex.new(0))

        async def increment(c: Arc[Mutex[int]]) -> None:
            guard = await c.lock()
            # modify the value through the guard

    Example:
        mutex: Mutex[int] = Mutex.new(0)
        guard = await mutex.lock()
    """

    @staticmethod
    def new(value: T) -> "Mutex[T]":
        """Creates a new Mutex wrapping the given value.

        Args:
            value: The value to protect with the mutex.

        Returns:
            A new Mutex containing the value.
        """
        ...

    async def lock(self) -> "MutexGuard[T]":
        """Locks this mutex, waiting asynchronously if it's already locked.

        Returns:
            A guard that releases the lock when dropped.
        """
        ...

    def try_lock(self) -> "MutexGuard[T] | None":
        """Attempts to acquire the lock without waiting.

        Returns:
            A guard if successful, None if the mutex is already locked.
        """
        ...

    def is_locked(self) -> bool:
        """Returns True if the mutex is currently locked.

        Returns:
            True if locked, False otherwise.
        """
        ...


class MutexGuard(Generic[T]):
    """A guard that releases the mutex when dropped.

    This is returned by Mutex.lock() and provides access to the protected data.
    The lock is automatically released when the guard goes out of scope.
    """
    pass


class RwLock(Generic[T]):
    """An asynchronous reader-writer lock.

    This type of lock allows multiple readers or a single writer at any point
    in time. Useful when you have data that is read frequently but written
    infrequently.

    Maps to tokio::sync::RwLock<T> in Rust.

    Example:
        data: RwLock[list[str]] = RwLock.new(["initial"])

        # Multiple readers allowed
        read_guard = await data.read()

        # Single writer, blocks readers
        write_guard = await data.write()
    """

    @staticmethod
    def new(value: T) -> "RwLock[T]":
        """Creates a new RwLock wrapping the given value.

        Args:
            value: The value to protect with the lock.

        Returns:
            A new RwLock containing the value.
        """
        ...

    async def read(self) -> "RwLockReadGuard[T]":
        """Locks this RwLock for reading, waiting if a writer holds the lock.

        Multiple readers can hold the lock simultaneously.

        Returns:
            A read guard that releases the lock when dropped.
        """
        ...

    async def write(self) -> "RwLockWriteGuard[T]":
        """Locks this RwLock for writing, waiting if any readers or writers hold the lock.

        Returns:
            A write guard that releases the lock when dropped.
        """
        ...

    def try_read(self) -> "RwLockReadGuard[T] | None":
        """Attempts to acquire the read lock without waiting.

        Returns:
            A read guard if successful, None if the lock is held by a writer.
        """
        ...

    def try_write(self) -> "RwLockWriteGuard[T] | None":
        """Attempts to acquire the write lock without waiting.

        Returns:
            A write guard if successful, None if the lock is held.
        """
        ...


class RwLockReadGuard(Generic[T]):
    """A guard that releases the read lock when dropped."""
    pass


class RwLockWriteGuard(Generic[T]):
    """A guard that releases the write lock when dropped."""
    pass


async def spawn(future: F) -> JoinHandle:
    """Spawns a new asynchronous task.

    The spawned task may execute on the current thread or another thread.
    Maps to tokio::spawn in Rust.
    """
    ...


async def spawn_blocking(f: F) -> JoinHandle:
    """Runs a blocking function on a dedicated thread pool.

    Maps to tokio::task::spawn_blocking in Rust.
    """
    ...


def mpsc_channel(buffer: int) -> tuple:
    """Creates a bounded mpsc channel for communication between tasks.

    Returns a tuple of (Sender, Receiver).
    Maps to tokio::sync::mpsc::channel in Rust.
    """
    ...


def mpsc_unbounded_channel() -> tuple:
    """Creates an unbounded mpsc channel for communication between tasks.

    Returns a tuple of (UnboundedSender, UnboundedReceiver).
    Maps to tokio::sync::mpsc::unbounded_channel in Rust.
    """
    ...


class AsyncFd:
    """Associates an IO object backed by a Unix file descriptor with the tokio
reactor, allowing for readiness to be polled. The file descriptor must be of
a type that can be used with the OS polling facilities (ie, `poll`, `epoll`,
`kqueue`, etc), such as a network socket or pipe, and the file descriptor
must have the nonblocking mode set to true.

Creating an [`AsyncFd`] registers the file descriptor with the current tokio
Reactor, allowing you to directly await the file descriptor being readable
or writable. Once registered, the file descriptor remains registered until
the [`AsyncFd`] is dropped.

The [`AsyncFd`] takes ownership of an arbitrary object to represent the IO
object. It is intended that the inner object will handle closing the file
descriptor when it is dropped, avoiding resource leaks and ensuring that the
[`AsyncFd`] can clean up the registration before closing the file descriptor.
The [`AsyncFd::into_inner`] function can be used to extract the inner object
to retake control from the tokio IO reactor. The [`OwnedFd`] type is often
used as the inner object, as it is the simplest type that closes the fd on
drop.

The inner object is required to implement [`AsRawFd`]. This file descriptor
must not change while [`AsyncFd`] owns the inner object, i.e. the
[`AsRawFd::as_raw_fd`] method on the inner type must always return the same
file descriptor when called multiple times. Failure to uphold this results
in unspecified behavior in the IO driver, which may include breaking
notifications for other sockets/etc.

Polling for readiness is done by calling the async functions [`readable`]
and [`writable`]. These functions complete when the associated readiness
condition is observed. Any number of tasks can query the same `AsyncFd` in
parallel, on the same or different conditions.

On some platforms, the readiness detecting mechanism relies on
edge-triggered notifications. This means that the OS will only notify Tokio
when the file descriptor transitions from not-ready to ready. For this to
work you should first try to read or write and only poll for readiness
if that fails with an error of [`std::io::ErrorKind::WouldBlock`].

Tokio internally tracks when it has received a ready notification, and when
readiness checking functions like [`readable`] and [`writable`] are called,
if the readiness flag is set, these async functions will complete
immediately. This however does mean that it is critical to ensure that this
ready flag is cleared when (and only when) the file descriptor ceases to be
ready. The [`AsyncFdReadyGuard`] returned from readiness checking functions
serves this function; after calling a readiness-checking async function,
you must use this [`AsyncFdReadyGuard`] to signal to tokio whether the file
descriptor is no longer in a ready state.

## Use with to a poll-based API

In some cases it may be desirable to use `AsyncFd` from APIs similar to
[`TcpStream::poll_read_ready`]. The [`AsyncFd::poll_read_ready`] and
[`AsyncFd::poll_write_ready`] functions are provided for this purpose.
Because these functions don't create a future to hold their state, they have
the limitation that only one task can wait on each direction (read or write)
at a time.

# Examples

This example shows how to turn [`std::net::TcpStream`] asynchronous using
`AsyncFd`.  It implements the read/write operations both as an `async fn`
and using the IO traits [`AsyncRead`] and [`AsyncWrite`].

```no_run
use std::io::{self, Read, Write};
use std::net::TcpStream;
use std::pin::Pin;
use std::task::{ready, Context, Poll};
use tokio::io::{AsyncRead, AsyncWrite, ReadBuf};
use tokio::io::unix::AsyncFd;

pub struct AsyncTcpStream {
inner: AsyncFd<TcpStream>,
}

impl AsyncTcpStream {
pub fn new(tcp: TcpStream) -> io::Result<Self> {
tcp.set_nonblocking(true)?;
Ok(Self {
inner: AsyncFd::new(tcp)?,
})
}

pub async fn read(&self, out: &mut [u8]) -> io::Result<usize> {
loop {
let mut guard = self.inner.readable().await?;

match guard.try_io(|inner| inner.get_ref().read(out)) {
Ok(result) => return result,
Err(_would_block) => continue,
}
}
}

pub async fn write(&self, buf: &[u8]) -> io::Result<usize> {
loop {
let mut guard = self.inner.writable().await?;

match guard.try_io(|inner| inner.get_ref().write(buf)) {
Ok(result) => return result,
Err(_would_block) => continue,
}
}
}
}

impl AsyncRead for AsyncTcpStream {
fn poll_read(
self: Pin<&mut Self>,
cx: &mut Context<'_>,
buf: &mut ReadBuf<'_>
) -> Poll<io::Result<()>> {
loop {
let mut guard = ready!(self.inner.poll_read_ready(cx))?;

let unfilled = buf.initialize_unfilled();
match guard.try_io(|inner| inner.get_ref().read(unfilled)) {
Ok(Ok(len)) => {
buf.advance(len);
return Poll::Ready(Ok(()));
},
Ok(Err(err)) => return Poll::Ready(Err(err)),
Err(_would_block) => continue,
}
}
}
}

impl AsyncWrite for AsyncTcpStream {
fn poll_write(
self: Pin<&mut Self>,
cx: &mut Context<'_>,
buf: &[u8]
) -> Poll<io::Result<usize>> {
loop {
let mut guard = ready!(self.inner.poll_write_ready(cx))?;

match guard.try_io(|inner| inner.get_ref().write(buf)) {
Ok(result) => return Poll::Ready(result),
Err(_would_block) => continue,
}
}
}

fn poll_flush(
self: Pin<&mut Self>,
cx: &mut Context<'_>,
) -> Poll<io::Result<()>> {
// tcp flush is a no-op
Poll::Ready(Ok(()))
}

fn poll_shutdown(
self: Pin<&mut Self>,
cx: &mut Context<'_>,
) -> Poll<io::Result<()>> {
self.inner.get_ref().shutdown(std::net::Shutdown::Write)?;
Poll::Ready(Ok(()))
}
}
```

[`readable`]: method@Self::readable
[`writable`]: method@Self::writable
[`AsyncFdReadyGuard`]: struct@self::AsyncFdReadyGuard
[`TcpStream::poll_read_ready`]: struct@crate::net::TcpStream
[`AsyncRead`]: trait@crate::io::AsyncRead
[`AsyncWrite`]: trait@crate::io::AsyncWrite
[`OwnedFd`]: struct@std::os::fd::OwnedFd"""

    @staticmethod
    def new(inner: T) -> object: ...

    @staticmethod
    def with_interest(inner: T, interest: Interest) -> object: ...

    @staticmethod
    def try_new(inner: T) -> object: ...

    @staticmethod
    def try_with_interest(inner: T, interest: Interest) -> object: ...

    def get_ref(self) -> T: ...

    def get_mut(self) -> T: ...

    def into_inner(self) -> T: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def poll_read_ready_mut(self, cx: Context) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def poll_write_ready_mut(self, cx: Context) -> object: ...

    def ready(self, interest: Interest) -> object: ...

    def ready_mut(self, interest: Interest) -> object: ...

    def readable(self) -> object: ...

    def readable_mut(self) -> object: ...

    def writable(self) -> object: ...

    def writable_mut(self) -> object: ...

    def async_io(self, interest: Interest, f: object) -> R: ...

    def async_io_mut(self, interest: Interest, f: object) -> R: ...

    def try_io(self, interest: Interest, f: object) -> R: ...

    def try_io_mut(self, interest: Interest, f: object) -> R: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

class AsyncFdReadyGuard:
    """Represents an IO-ready event detected on a particular file descriptor that
has not yet been acknowledged. This is a `must_use` structure to help ensure
that you do not forget to explicitly clear (or not clear) the event.

This type exposes an immutable reference to the underlying IO object."""

    def clear_ready(self) -> None: ...

    def clear_ready_matching(self, ready: Ready) -> None: ...

    def retain_ready(self) -> None: ...

    def ready(self) -> Ready: ...

    def try_io(self, f: object) -> R: ...

    def get_ref(self) -> object: ...

    def get_inner(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class AsyncFdReadyMutGuard:
    """Represents an IO-ready event detected on a particular file descriptor that
has not yet been acknowledged. This is a `must_use` structure to help ensure
that you do not forget to explicitly clear (or not clear) the event.

This type exposes a mutable reference to the underlying IO object."""

    def clear_ready(self) -> None: ...

    def clear_ready_matching(self, ready: Ready) -> None: ...

    def retain_ready(self) -> None: ...

    def ready(self) -> Ready: ...

    def try_io(self, f: object) -> R: ...

    def get_ref(self) -> object: ...

    def get_mut(self) -> object: ...

    def get_inner(self) -> Inner: ...

    def get_inner_mut(self) -> Inner: ...

    def fmt(self, f: Formatter) -> Result: ...

class TryIoError:
    """The error type returned by [`try_io`].

This error indicates that the IO resource returned a [`WouldBlock`] error.

[`WouldBlock`]: std::io::ErrorKind::WouldBlock
[`try_io`]: method@AsyncFdReadyGuard::try_io"""
    pass

class AsyncFdTryNewError:
    """Error returned by [`try_new`] or [`try_with_interest`].

[`try_new`]: AsyncFd::try_new
[`try_with_interest`]: AsyncFd::try_with_interest"""

    def into_parts(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def source(self) -> object: ...

class DuplexStream:
    """A bidirectional pipe to read and write bytes in memory.

A pair of `DuplexStream`s are created together, and they act as a "channel"
that can be used as in-memory IO types. Writing to one of the pairs will
allow that data to be read from the other, and vice versa.

# Closing a `DuplexStream`

If one end of the `DuplexStream` channel is dropped, any pending reads on
the other side will continue to read data until the buffer is drained, then
they will signal EOF by returning 0 bytes. Any writes to the other side,
including pending ones (that are waiting for free space in the buffer) will
return `Err(BrokenPipe)` immediately.

# Example

```
# async fn ex() -> std::io::Result<()> {
# use tokio::io::{AsyncReadExt, AsyncWriteExt};
let (mut client, mut server) = tokio::io::duplex(64);

client.write_all(b"ping").await?;

let mut buf = [0u8; 4];
server.read_exact(&mut buf).await?;
assert_eq!(&buf, b"ping");

server.write_all(b"pong").await?;

client.read_exact(&mut buf).await?;
assert_eq!(&buf, b"pong");
# Ok(())
# }
```"""

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, cx: Context) -> object: ...

    def poll_shutdown(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

class SimplexStream:
    """A unidirectional pipe to read and write bytes in memory.

It can be constructed by [`simplex`] function which will create a pair of
reader and writer or by calling [`SimplexStream::new_unsplit`] that will
create a handle for both reading and writing.

# Example

```
# async fn ex() -> std::io::Result<()> {
# use tokio::io::{AsyncReadExt, AsyncWriteExt};
let (mut receiver, mut sender) = tokio::io::simplex(64);

sender.write_all(b"ping").await?;

let mut buf = [0u8; 4];
receiver.read_exact(&mut buf).await?;
assert_eq!(&buf, b"ping");
# Ok(())
# }
```"""

    @staticmethod
    def new_unsplit(max_buf_size: int) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

class ReadBuf:
    """A wrapper around a byte buffer that is incrementally filled and initialized.

This type is a sort of "double cursor". It tracks three regions in the
buffer: a region at the beginning of the buffer that has been logically
filled with data, a region that has been initialized at some point but not
yet logically filled, and a region at the end that may be uninitialized.
The filled region is guaranteed to be a subset of the initialized region.

In summary, the contents of the buffer can be visualized as:

```not_rust
[             capacity              ]
[ filled |         unfilled         ]
[    initialized    | uninitialized ]
```

It is undefined behavior to de-initialize any bytes from the uninitialized
region, since it is merely unknown whether this region is uninitialized or
not, and if part of it turns out to be initialized, it must stay initialized."""

    def poll(self, cx: Context) -> object: ...

    @staticmethod
    def new(buf: object) -> "ReadBuf": ...

    @staticmethod
    def uninit(buf: object) -> "ReadBuf": ...

    def capacity(self) -> int: ...

    def filled(self) -> object: ...

    def filled_mut(self) -> object: ...

    def take(self, n: int) -> ReadBuf: ...

    def initialized(self) -> object: ...

    def initialized_mut(self) -> object: ...

    def inner_mut(self) -> object: ...

    def unfilled_mut(self) -> object: ...

    def initialize_unfilled(self) -> object: ...

    def initialize_unfilled_to(self, n: int) -> object: ...

    def remaining(self) -> int: ...

    def clear(self) -> None: ...

    def advance(self, n: int) -> None: ...

    def set_filled(self, n: int) -> None: ...

    def assume_init(self, n: int) -> None: ...

    def put_slice(self, buf: object) -> None: ...

    def remaining_mut(self) -> int: ...

    def advance_mut(self, cnt: int) -> None: ...

    def chunk_mut(self) -> UninitSlice: ...

    def fmt(self, f: Formatter) -> Result: ...

class Aio:
    """Associates a POSIX AIO control block with the reactor that drives it.

`Aio`'s wrapped type must implement [`AioSource`] to be driven
by the reactor.

The wrapped source may be accessed through the `Aio` via the `Deref` and
`DerefMut` traits.

## Clearing readiness

If [`Aio::poll_ready`] returns ready, but the consumer determines that the
Source is not completely ready and must return to the Pending state,
[`Aio::clear_ready`] may be used.  This can be useful with
[`lio_listio`], which may generate a kevent when only a portion of the
operations have completed.

## Platforms

Only FreeBSD implements POSIX AIO with kqueue notification, so
`Aio` is only available for that operating system.

[`lio_listio`]: https://pubs.opengroup.org/onlinepubs/9699919799/functions/lio_listio.html"""

    @staticmethod
    def new_for_aio(io: E) -> object: ...

    @staticmethod
    def new_for_lio(io: E) -> object: ...

    def clear_ready(self, ev: AioEvent) -> None: ...

    def into_inner(self) -> E: ...

    def poll_ready(self, cx: Context) -> object: ...

    def deref(self) -> E: ...

    def deref_mut(self) -> E: ...

    def fmt(self, f: Formatter) -> Result: ...

class AioEvent:
    """Opaque data returned by [`Aio::poll_ready`].

It can be fed back to [`Aio::clear_ready`]."""
    pass

class Interest:
    """Readiness event interest.

Specifies the readiness events the caller is interested in when awaiting on
I/O resource readiness states."""

    def is_readable(self) -> bool: ...

    def is_writable(self) -> bool: ...

    def is_error(self) -> bool: ...

    def is_priority(self) -> bool: ...

    def add(self, other: Interest) -> Interest: ...

    def remove(self, other: Interest) -> Interest | None: ...

    def bitor(self, other: Self) -> Self: ...

    def bitor_assign(self, other: Self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class Ready:
    """Describes the readiness state of an I/O resources.

`Ready` tracks which operation an I/O resource is ready to perform."""

    def is_empty(self) -> bool: ...

    def is_readable(self) -> bool: ...

    def is_writable(self) -> bool: ...

    def is_read_closed(self) -> bool: ...

    def is_write_closed(self) -> bool: ...

    def is_priority(self) -> bool: ...

    def is_error(self) -> bool: ...

    def bitor(self, other: Ready) -> Ready: ...

    def bitor_assign(self, other: Ready) -> None: ...

    def bitand(self, other: Ready) -> Ready: ...

    def sub(self, other: Ready) -> Ready: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class RngSeed:
    """A seed for random number generation.

In order to make certain functions within a runtime deterministic, a seed
can be specified at the time of creation."""

    @staticmethod
    def from_bytes(bytes: object) -> "RngSeed": ...

class SetOnce:
    """A thread-safe cell that can be written to only once.

A `SetOnce` is inspired from python's [`asyncio.Event`] type. It can be
used to wait until the value of the `SetOnce` is set like a "Event" mechanism.

# Example

```
use tokio::sync::{SetOnce, SetOnceError};

static ONCE: SetOnce<u32> = SetOnce::const_new();

# #[tokio::main(flavor = "current_thread")]
# async fn main() -> Result<(), SetOnceError<u32>> {

// set the value inside a task somewhere...
tokio::spawn(async move { ONCE.set(20) });

// checking with .get doesn't block main thread
println!("{:?}", ONCE.get());

// wait until the value is set, blocks the thread
println!("{:?}", ONCE.wait().await);

Ok(())
# }
```

A `SetOnce` is typically used for global variables that need to be
initialized once on first use, but need no further changes. The `SetOnce`
in Tokio allows the initialization procedure to be asynchronous.

# Example

```
use tokio::sync::{SetOnce, SetOnceError};
use std::sync::Arc;

# #[tokio::main(flavor = "current_thread")]
# async fn main() -> Result<(), SetOnceError<u32>> {
let once = SetOnce::new();

let arc = Arc::new(once);
let first_cl = Arc::clone(&arc);
let second_cl = Arc::clone(&arc);

// set the value inside a task
tokio::spawn(async move { first_cl.set(20) }).await.unwrap()?;

// wait inside task to not block the main thread
tokio::spawn(async move {
// wait inside async context for the value to be set
assert_eq!(*second_cl.wait().await, 20);
}).await.unwrap();

// subsequent set calls will fail
assert!(arc.set(30).is_err());

println!("{:?}", arc.get());

Ok(())
# }
```

[`asyncio.Event`]: https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event"""

    @staticmethod
    def default() -> object: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def clone(self) -> object: ...

    def eq(self, other: object) -> bool: ...

    def drop(self) -> None: ...

    @staticmethod
    def from_(value: T) -> "SetOnce": ...

    @staticmethod
    def new() -> "SetOnce": ...

    @staticmethod
    def const_new() -> "SetOnce": ...

    @staticmethod
    def new_with(value: T | None) -> "SetOnce": ...

    @staticmethod
    def const_new_with(value: T) -> "SetOnce": ...

    def initialized(self) -> bool: ...

    def get(self) -> object: ...

    def set(self, value: T) -> None: ...

    def into_inner(self) -> T | None: ...

    def wait(self) -> T: ...

class SetOnceError:
    """Error that can be returned from [`SetOnce::set`].

This error means that the `SetOnce` was already initialized when
set was called

[`SetOnce::set`]: crate::sync::SetOnce::set"""

    def fmt(self, f: Formatter) -> Result: ...

class OwnedRwLockReadGuard:
    """Owned RAII structure used to release the shared read access of a lock when
dropped.

This structure is created by the [`read_owned`] method on
[`RwLock`].

[`read_owned`]: method@crate::sync::RwLock::read_owned
[`RwLock`]: struct@crate::sync::RwLock"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    @staticmethod
    def rwlock(this: Self) -> object: ...

    def deref(self) -> U: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

class RwLockWriteGuard:
    """RAII structure used to release the exclusive write access of a lock when
dropped.

This structure is created by the [`write`] method
on [`RwLock`].

[`write`]: method@crate::sync::RwLock::write
[`RwLock`]: struct@crate::sync::RwLock"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def downgrade_map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_downgrade_map(this: Self, f: F) -> object: ...

    @staticmethod
    def into_mapped(this: Self) -> object: ...

    def downgrade(self) -> object: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

class RwLockMappedWriteGuard:
    """RAII structure used to release the exclusive write access of a lock when
dropped.

This structure is created by [mapping] an [`RwLockWriteGuard`]. It is a
separate type from `RwLockWriteGuard` to disallow downgrading a mapped
guard, since doing so can cause undefined behavior.

[mapping]: method@crate::sync::RwLockWriteGuard::map
[`RwLockWriteGuard`]: struct@crate::sync::RwLockWriteGuard"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

class RwLockReadGuard:
    """RAII structure used to release the shared read access of a lock when
dropped.

This structure is created by the [`read`] method on
[`RwLock`].

[`read`]: method@crate::sync::RwLock::read
[`RwLock`]: struct@crate::sync::RwLock"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    def deref(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

    def deref(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

class OwnedRwLockWriteGuard:
    """Owned RAII structure used to release the exclusive write access of a lock when
dropped.

This structure is created by the [`write_owned`] method
on [`RwLock`].

[`write_owned`]: method@crate::sync::RwLock::write_owned
[`RwLock`]: struct@crate::sync::RwLock"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def downgrade_map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_downgrade_map(this: Self, f: F) -> object: ...

    @staticmethod
    def into_mapped(this: Self) -> object: ...

    def downgrade(self) -> object: ...

    @staticmethod
    def rwlock(this: Self) -> object: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

class OwnedRwLockMappedWriteGuard:
    """Owned RAII structure used to release the exclusive write access of a lock when
dropped.

This structure is created by [mapping] an [`OwnedRwLockWriteGuard`]. It is a
separate type from `OwnedRwLockWriteGuard` to disallow downgrading a mapped
guard, since doing so can cause undefined behavior.

[mapping]: method@crate::sync::OwnedRwLockWriteGuard::map
[`OwnedRwLockWriteGuard`]: struct@crate::sync::OwnedRwLockWriteGuard"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    @staticmethod
    def rwlock(this: Self) -> object: ...

    def deref(self) -> U: ...

    def deref_mut(self) -> U: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def drop(self) -> None: ...

class Sender:
    """Sends a value to the associated [`Receiver`].

A pair of both a [`Sender`] and a [`Receiver`]  are created by the
[`channel`](fn@channel) function.

# Examples

```
use tokio::sync::oneshot;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, rx) = oneshot::channel();

tokio::spawn(async move {
if let Err(_) = tx.send(3) {
println!("the receiver dropped");
}
});

match rx.await {
Ok(v) => println!("got = {:?}", v),
Err(_) => println!("the sender dropped"),
}
# }
```

If the sender is dropped without sending, the receiver will fail with
[`error::RecvError`]:

```
use tokio::sync::oneshot;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, rx) = oneshot::channel::<u32>();

tokio::spawn(async move {
drop(tx);
});

match rx.await {
Ok(_) => panic!("This doesn't happen"),
Err(_) => println!("the sender dropped"),
}
# }
```

To use a `Sender` from a destructor, put it in an [`Option`] and call
[`Option::take`].

```
use tokio::sync::oneshot;

struct SendOnDrop {
sender: Option<oneshot::Sender<&'static str>>,
}
impl Drop for SendOnDrop {
fn drop(&mut self) {
if let Some(sender) = self.sender.take() {
// Using `let _ =` to ignore send errors.
let _ = sender.send("I got dropped!");
}
}
}

# #[tokio::main(flavor = "current_thread")]
# async fn _doc() {}
# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (send, recv) = oneshot::channel();

let send_on_drop = SendOnDrop { sender: Some(send) };
drop(send_on_drop);

assert_eq!(recv.await, Ok("I got dropped!"));
# }
```

[`Option`]: std::option::Option
[`Option::take`]: std::option::Option::take"""

    def send(self, t: T) -> None: ...

    def closed(self) -> None: ...

    def is_closed(self) -> bool: ...

    def poll_closed(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

    def clone(self) -> Self: ...

    @staticmethod
    def default() -> "Sender": ...

    @staticmethod
    def new(init: T) -> "Sender": ...

    def send(self, value: T) -> None: ...

    def send_modify(self, modify: F) -> None: ...

    def send_if_modified(self, modify: F) -> bool: ...

    def send_replace(self, value: T) -> T: ...

    def borrow(self) -> object: ...

    def is_closed(self) -> bool: ...

    def closed(self) -> None: ...

    def subscribe(self) -> object: ...

    def receiver_count(self) -> int: ...

    def sender_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def drop(self) -> None: ...

    def send(self, value: T) -> None: ...

    def closed(self) -> None: ...

    def try_send(self, message: T) -> None: ...

    def send_timeout(self, value: T, timeout: Duration) -> None: ...

    def blocking_send(self, value: T) -> None: ...

    def is_closed(self) -> bool: ...

    def reserve(self) -> object: ...

    def reserve_many(self, n: int) -> object: ...

    def reserve_owned(self) -> object: ...

    def try_reserve(self) -> object: ...

    def try_reserve_many(self, n: int) -> object: ...

    def try_reserve_owned(self) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def capacity(self) -> int: ...

    def downgrade(self) -> object: ...

    def max_capacity(self) -> int: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new(capacity: int) -> "Sender": ...

    def send(self, value: T) -> int: ...

    def subscribe(self) -> object: ...

    def downgrade(self) -> object: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def receiver_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def closed(self) -> None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Sender": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Sender": ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class Receiver:
    """Receives a value from the associated [`Sender`].

A pair of both a [`Sender`] and a [`Receiver`]  are created by the
[`channel`](fn@channel) function.

This channel has no `recv` method because the receiver itself implements the
[`Future`] trait. To receive a `Result<T, `[`error::RecvError`]`>`, `.await` the `Receiver` object directly.

The `poll` method on the `Future` trait is allowed to spuriously return
`Poll::Pending` even if the message has been sent. If such a spurious
failure happens, then the caller will be woken when the spurious failure has
been resolved so that the caller can attempt to receive the message again.
Note that receiving such a wakeup does not guarantee that the next call will
succeed — it could fail with another spurious failure. (A spurious failure
does not mean that the message is lost. It is just delayed.)

[`Future`]: trait@std::future::Future

# Cancellation safety

The `Receiver` is cancel safe. If it is used as the event in a
[`tokio::select!`](crate::select) statement and some other branch
completes first, it is guaranteed that no message was received on this
channel.

# Examples

```
use tokio::sync::oneshot;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, rx) = oneshot::channel();

tokio::spawn(async move {
if let Err(_) = tx.send(3) {
println!("the receiver dropped");
}
});

match rx.await {
Ok(v) => println!("got = {:?}", v),
Err(_) => println!("the sender dropped"),
}
# }
```

If the sender is dropped without sending, the receiver will fail with
[`error::RecvError`]:

```
use tokio::sync::oneshot;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, rx) = oneshot::channel::<u32>();

tokio::spawn(async move {
drop(tx);
});

match rx.await {
Ok(_) => panic!("This doesn't happen"),
Err(_) => println!("the sender dropped"),
}
# }
```

To use a `Receiver` in a `tokio::select!` loop, add `&mut` in front of the
channel.

```
use tokio::sync::oneshot;
use tokio::time::{interval, sleep, Duration};

# #[tokio::main(flavor = "current_thread")]
# async fn _doc() {}
# #[tokio::main(flavor = "current_thread", start_paused = true)]
# async fn main() {
let (send, mut recv) = oneshot::channel();
let mut interval = interval(Duration::from_millis(100));

# let handle =
tokio::spawn(async move {
sleep(Duration::from_secs(1)).await;
send.send("shut down").unwrap();
});

loop {
tokio::select! {
_ = interval.tick() => println!("Another 100ms"),
msg = &mut recv => {
println!("Got message: {}", msg.unwrap());
break;
}
}
}
# handle.await.unwrap();
# }
```"""

    def close(self) -> None: ...

    def is_terminated(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def poll(self, cx: Context) -> object: ...

    def borrow(self) -> object: ...

    def borrow_and_update(self) -> object: ...

    def has_changed(self) -> bool: ...

    def mark_changed(self) -> None: ...

    def mark_unchanged(self) -> None: ...

    def changed(self) -> None: ...

    def wait_for(self, f: object) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def recv(self) -> T | None: ...

    def recv_many(self, buffer: list[T], limit: int) -> int: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T | None: ...

    def blocking_recv_many(self, buffer: list[T], limit: int) -> int: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    def capacity(self) -> int: ...

    def max_capacity(self) -> int: ...

    def poll_recv(self, cx: Context) -> object: ...

    def poll_recv_many(self, cx: Context, buffer: list[T], limit: int) -> object: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def same_channel(self, other: Self) -> bool: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def is_closed(self) -> bool: ...

    def resubscribe(self) -> Self: ...

    def recv(self) -> T: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Receiver": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Receiver": ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class RecvError:
    """Error returned by the `Future` implementation for `Receiver`.

This error is returned by the receiver when the sender is dropped without sending."""

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class RwLock:
    """An asynchronous reader-writer lock.

This type of lock allows a number of readers or at most one writer at any
point in time. The write portion of this lock typically allows modification
of the underlying data (exclusive access) and the read portion of this lock
typically allows for read-only access (shared access).

In comparison, a [`Mutex`] does not distinguish between readers or writers
that acquire the lock, therefore causing any tasks waiting for the lock to
become available to yield. An `RwLock` will allow any number of readers to
acquire the lock as long as a writer is not holding the lock.

The priority policy of Tokio's read-write lock is _fair_ (or
[_write-preferring_]), in order to ensure that readers cannot starve
writers. Fairness is ensured using a first-in, first-out queue for the tasks
awaiting the lock; if a task that wishes to acquire the write lock is at the
head of the queue, read locks will not be given out until the write lock has
been released. This is in contrast to the Rust standard library's
`std::sync::RwLock`, where the priority policy is dependent on the
operating system's implementation.

The type parameter `T` represents the data that this lock protects. It is
required that `T` satisfies [`Send`] to be shared across threads. The RAII guards
returned from the locking methods implement [`Deref`](trait@std::ops::Deref)
(and [`DerefMut`](trait@std::ops::DerefMut)
for the `write` methods) to allow access to the content of the lock.

# Examples

```
use tokio::sync::RwLock;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let lock = RwLock::new(5);

// many reader locks can be held at once
{
let r1 = lock.read().await;
let r2 = lock.read().await;
assert_eq!(*r1, 5);
assert_eq!(*r2, 5);
} // read locks are dropped at this point

// only one write lock may be held, however
{
let mut w = lock.write().await;
*w += 1;
assert_eq!(*w, 6);
} // write lock is dropped here
# }
```

[`Mutex`]: struct@super::Mutex
[`RwLock`]: struct@RwLock
[`RwLockReadGuard`]: struct@RwLockReadGuard
[`RwLockWriteGuard`]: struct@RwLockWriteGuard
[`Send`]: trait@std::marker::Send
[_write-preferring_]: https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock#Priority_policies"""

    @staticmethod
    def new(value: T) -> object: ...

    @staticmethod
    def with_max_readers(value: T, max_reads: int) -> object: ...

    @staticmethod
    def const_new(value: T) -> object: ...

    @staticmethod
    def const_with_max_readers(value: T, max_reads: int) -> object: ...

    def read(self) -> object: ...

    def blocking_read(self) -> object: ...

    def read_owned(self) -> object: ...

    def try_read(self) -> object: ...

    def try_read_owned(self) -> object: ...

    def write(self) -> object: ...

    def blocking_write(self) -> object: ...

    def write_owned(self) -> object: ...

    def try_write(self) -> object: ...

    def try_write_owned(self) -> object: ...

    def get_mut(self) -> T: ...

    def into_inner(self) -> T: ...

    @staticmethod
    def from_(s: T) -> "RwLock": ...

    @staticmethod
    def default() -> "RwLock": ...

    def fmt(self, f: Formatter) -> Result: ...

class Notify:
    """Notifies a single task to wake up.

`Notify` provides a basic mechanism to notify a single task of an event.
`Notify` itself does not carry any data. Instead, it is to be used to signal
another task to perform an operation.

A `Notify` can be thought of as a [`Semaphore`] starting with 0 permits. The
[`notified().await`] method waits for a permit to become available, and
[`notify_one()`] sets a permit **if there currently are no available
permits**.

The synchronization details of `Notify` are similar to
[`thread::park`][park] and [`Thread::unpark`][unpark] from std. A [`Notify`]
value contains a single permit. [`notified().await`] waits for the permit to
be made available, consumes the permit, and resumes.  [`notify_one()`] sets
the permit, waking a pending task if there is one.

If `notify_one()` is called **before** `notified().await`, then the next
call to `notified().await` will complete immediately, consuming the permit.
Any subsequent calls to `notified().await` will wait for a new permit.

If `notify_one()` is called **multiple** times before `notified().await`,
only a **single** permit is stored. The next call to `notified().await` will
complete immediately, but the one after will wait for a new permit.

# Examples

Basic usage.

```
use tokio::sync::Notify;
use std::sync::Arc;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let notify = Arc::new(Notify::new());
let notify2 = notify.clone();

let handle = tokio::spawn(async move {
notify2.notified().await;
println!("received notification");
});

println!("sending notification");
notify.notify_one();

// Wait for task to receive notification.
handle.await.unwrap();
# }
```

Unbound multi-producer single-consumer (mpsc) channel.

No wakeups can be lost when using this channel because the call to
`notify_one()` will store a permit in the `Notify`, which the following call
to `notified()` will consume.

```
use tokio::sync::Notify;

use std::collections::VecDeque;
use std::sync::Mutex;

struct Channel<T> {
values: Mutex<VecDeque<T>>,
notify: Notify,
}

impl<T> Channel<T> {
pub fn send(&self, value: T) {
self.values.lock().unwrap()
.push_back(value);

// Notify the consumer a value is available
self.notify.notify_one();
}

// This is a single-consumer channel, so several concurrent calls to
// `recv` are not allowed.
pub async fn recv(&self) -> T {
loop {
// Drain values
if let Some(value) = self.values.lock().unwrap().pop_front() {
return value;
}

// Wait for values to be available
self.notify.notified().await;
}
}
}
```

Unbound multi-producer multi-consumer (mpmc) channel.

The call to [`enable`] is important because otherwise if you have two
calls to `recv` and two calls to `send` in parallel, the following could
happen:

1. Both calls to `try_recv` return `None`.
2. Both new elements are added to the vector.
3. The `notify_one` method is called twice, adding only a single
permit to the `Notify`.
4. Both calls to `recv` reach the `Notified` future. One of them
consumes the permit, and the other sleeps forever.

By adding the `Notified` futures to the list by calling `enable` before
`try_recv`, the `notify_one` calls in step three would remove the
futures from the list and mark them notified instead of adding a permit
to the `Notify`. This ensures that both futures are woken.

Notice that this failure can only happen if there are two concurrent calls
to `recv`. This is why the mpsc example above does not require a call to
`enable`.

```
use tokio::sync::Notify;

use std::collections::VecDeque;
use std::sync::Mutex;

struct Channel<T> {
messages: Mutex<VecDeque<T>>,
notify_on_sent: Notify,
}

impl<T> Channel<T> {
pub fn send(&self, msg: T) {
let mut locked_queue = self.messages.lock().unwrap();
locked_queue.push_back(msg);
drop(locked_queue);

// Send a notification to one of the calls currently
// waiting in a call to `recv`.
self.notify_on_sent.notify_one();
}

pub fn try_recv(&self) -> Option<T> {
let mut locked_queue = self.messages.lock().unwrap();
locked_queue.pop_front()
}

pub async fn recv(&self) -> T {
let future = self.notify_on_sent.notified();
tokio::pin!(future);

loop {
// Make sure that no wakeup is lost if we get
// `None` from `try_recv`.
future.as_mut().enable();

if let Some(msg) = self.try_recv() {
return msg;
}

// Wait for a call to `notify_one`.
//
// This uses `.as_mut()` to avoid consuming the future,
// which lets us call `Pin::set` below.
future.as_mut().await;

// Reset the future in case another call to
// `try_recv` got the message before us.
future.set(self.notify_on_sent.notified());
}
}
}
```

[park]: std::thread::park
[unpark]: std::thread::Thread::unpark
[`notified().await`]: Notify::notified()
[`notify_one()`]: Notify::notify_one()
[`enable`]: Notified::enable()
[`Semaphore`]: crate::sync::Semaphore"""

    @staticmethod
    def new() -> "Notify": ...

    @staticmethod
    def const_new() -> "Notify": ...

    def notified(self) -> Notified: ...

    def notified_owned(self) -> OwnedNotified: ...

    def notify_one(self) -> None: ...

    def notify_last(self) -> None: ...

    def notify_waiters(self) -> None: ...

    @staticmethod
    def default() -> "Notify": ...

class Notified:
    """Future returned from [`Notify::notified()`].

This future is fused, so once it has completed, any future calls to poll
will immediately return `Poll::Ready`."""

    def enable(self) -> bool: ...

    def poll(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class OwnedNotified:
    """Future returned from [`Notify::notified_owned()`].

This future is fused, so once it has completed, any future calls to poll
will immediately return `Poll::Ready`."""

    def enable(self) -> bool: ...

    def poll(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

class Receiver:
    """Receives values from the associated [`Sender`](struct@Sender).

Instances are created by the [`channel`](fn@channel) function.

To turn this receiver into a `Stream`, you can use the [`WatchStream`]
wrapper.

[`WatchStream`]: https://docs.rs/tokio-stream/0.1/tokio_stream/wrappers/struct.WatchStream.html"""

    def close(self) -> None: ...

    def is_terminated(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def poll(self, cx: Context) -> object: ...

    def borrow(self) -> object: ...

    def borrow_and_update(self) -> object: ...

    def has_changed(self) -> bool: ...

    def mark_changed(self) -> None: ...

    def mark_unchanged(self) -> None: ...

    def changed(self) -> None: ...

    def wait_for(self, f: object) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def recv(self) -> T | None: ...

    def recv_many(self, buffer: list[T], limit: int) -> int: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T | None: ...

    def blocking_recv_many(self, buffer: list[T], limit: int) -> int: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    def capacity(self) -> int: ...

    def max_capacity(self) -> int: ...

    def poll_recv(self, cx: Context) -> object: ...

    def poll_recv_many(self, cx: Context, buffer: list[T], limit: int) -> object: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def same_channel(self, other: Self) -> bool: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def is_closed(self) -> bool: ...

    def resubscribe(self) -> Self: ...

    def recv(self) -> T: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Receiver": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Receiver": ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class Sender:
    """Sends values to the associated [`Receiver`](struct@Receiver).

Instances are created by the [`channel`](fn@channel) function."""

    def send(self, t: T) -> None: ...

    def closed(self) -> None: ...

    def is_closed(self) -> bool: ...

    def poll_closed(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

    def clone(self) -> Self: ...

    @staticmethod
    def default() -> "Sender": ...

    @staticmethod
    def new(init: T) -> "Sender": ...

    def send(self, value: T) -> None: ...

    def send_modify(self, modify: F) -> None: ...

    def send_if_modified(self, modify: F) -> bool: ...

    def send_replace(self, value: T) -> T: ...

    def borrow(self) -> object: ...

    def is_closed(self) -> bool: ...

    def closed(self) -> None: ...

    def subscribe(self) -> object: ...

    def receiver_count(self) -> int: ...

    def sender_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def drop(self) -> None: ...

    def send(self, value: T) -> None: ...

    def closed(self) -> None: ...

    def try_send(self, message: T) -> None: ...

    def send_timeout(self, value: T, timeout: Duration) -> None: ...

    def blocking_send(self, value: T) -> None: ...

    def is_closed(self) -> bool: ...

    def reserve(self) -> object: ...

    def reserve_many(self, n: int) -> object: ...

    def reserve_owned(self) -> object: ...

    def try_reserve(self) -> object: ...

    def try_reserve_many(self, n: int) -> object: ...

    def try_reserve_owned(self) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def capacity(self) -> int: ...

    def downgrade(self) -> object: ...

    def max_capacity(self) -> int: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new(capacity: int) -> "Sender": ...

    def send(self, value: T) -> int: ...

    def subscribe(self) -> object: ...

    def downgrade(self) -> object: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def receiver_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def closed(self) -> None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Sender": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Sender": ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class Ref:
    """Returns a reference to the inner value.

Outstanding borrows hold a read lock on the inner value. This means that
long-lived borrows could cause the producer half to block. It is recommended
to keep the borrow as short-lived as possible. Additionally, if you are
running in an environment that allows `!Send` futures, you must ensure that
the returned `Ref` type is never held alive across an `.await` point,
otherwise, it can lead to a deadlock.

The priority policy of the lock is dependent on the underlying lock
implementation, and this type does not guarantee that any particular policy
will be used. In particular, a producer which is waiting to acquire the lock
in `send` might or might not block concurrent calls to `borrow`, e.g.:

<details><summary>Potential deadlock example</summary>

```text
// Task 1 (on thread A)    |  // Task 2 (on thread B)
let _ref1 = rx.borrow();   |
|  // will block
|  let _ = tx.send(());
// may deadlock            |
let _ref2 = rx.borrow();   |
```
</details>"""

    def has_changed(self) -> bool: ...

    def deref(self) -> T: ...

class SendError:
    """Error produced when sending a value fails."""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class RecvError:
    """Error produced when receiving a change notification."""

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class Barrier:
    """A barrier enables multiple tasks to synchronize the beginning of some computation.

```
# #[tokio::main(flavor = "current_thread")]
# async fn main() {
use tokio::sync::Barrier;
use std::sync::Arc;

let mut handles = Vec::with_capacity(10);
let barrier = Arc::new(Barrier::new(10));
for _ in 0..10 {
let c = barrier.clone();
// The same messages will be printed together.
// You will NOT see any interleaving.
handles.push(tokio::spawn(async move {
println!("before wait");
let wait_result = c.wait().await;
println!("after wait");
wait_result
}));
}

// Will not resolve until all "after wait" messages have been printed
let mut num_leaders = 0;
for handle in handles {
let wait_result = handle.await.unwrap();
if wait_result.is_leader() {
num_leaders += 1;
}
}

// Exactly one barrier will resolve as the "leader"
assert_eq!(num_leaders, 1);
# }
```"""

    @staticmethod
    def new(n: int) -> "Barrier": ...

    def wait(self) -> BarrierWaitResult: ...

    def fmt(self, f: Formatter) -> Result: ...

class BarrierWaitResult:
    """A `BarrierWaitResult` is returned by `wait` when all tasks in the `Barrier` have rendezvoused."""

    def is_leader(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class Sender:
    """Sends values to the associated `Receiver`.

Instances are created by the [`channel`] function.

To convert the `Sender` into a `Sink` or use it in a poll function, you can
use the [`PollSender`] utility.

[`PollSender`]: https://docs.rs/tokio-util/latest/tokio_util/sync/struct.PollSender.html"""

    def send(self, t: T) -> None: ...

    def closed(self) -> None: ...

    def is_closed(self) -> bool: ...

    def poll_closed(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

    def clone(self) -> Self: ...

    @staticmethod
    def default() -> "Sender": ...

    @staticmethod
    def new(init: T) -> "Sender": ...

    def send(self, value: T) -> None: ...

    def send_modify(self, modify: F) -> None: ...

    def send_if_modified(self, modify: F) -> bool: ...

    def send_replace(self, value: T) -> T: ...

    def borrow(self) -> object: ...

    def is_closed(self) -> bool: ...

    def closed(self) -> None: ...

    def subscribe(self) -> object: ...

    def receiver_count(self) -> int: ...

    def sender_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def drop(self) -> None: ...

    def send(self, value: T) -> None: ...

    def closed(self) -> None: ...

    def try_send(self, message: T) -> None: ...

    def send_timeout(self, value: T, timeout: Duration) -> None: ...

    def blocking_send(self, value: T) -> None: ...

    def is_closed(self) -> bool: ...

    def reserve(self) -> object: ...

    def reserve_many(self, n: int) -> object: ...

    def reserve_owned(self) -> object: ...

    def try_reserve(self) -> object: ...

    def try_reserve_many(self, n: int) -> object: ...

    def try_reserve_owned(self) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def capacity(self) -> int: ...

    def downgrade(self) -> object: ...

    def max_capacity(self) -> int: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new(capacity: int) -> "Sender": ...

    def send(self, value: T) -> int: ...

    def subscribe(self) -> object: ...

    def downgrade(self) -> object: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def receiver_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def closed(self) -> None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Sender": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Sender": ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class WeakSender:
    """A sender that does not prevent the channel from being closed.

If all [`Sender`] instances of a channel were dropped and only `WeakSender`
instances remain, the channel is closed.

In order to send messages, the `WeakSender` needs to be upgraded using
[`WeakSender::upgrade`], which returns `Option<Sender>`. It returns `None`
if all `Sender`s have been dropped, and otherwise it returns a `Sender`.

[`Sender`]: Sender
[`WeakSender::upgrade`]: WeakSender::upgrade

# Examples

```
use tokio::sync::mpsc::channel;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, _rx) = channel::<i32>(15);
let tx_weak = tx.downgrade();

// Upgrading will succeed because `tx` still exists.
assert!(tx_weak.upgrade().is_some());

// If we drop `tx`, then it will fail.
drop(tx);
assert!(tx_weak.clone().upgrade().is_none());
# }
```"""

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def upgrade(self) -> object | None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def upgrade(self) -> object | None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class Permit:
    """Permits to send one value into the channel.

`Permit` values are returned by [`Sender::reserve()`] and [`Sender::try_reserve()`]
and are used to guarantee channel capacity before generating a message to send.

[`Sender::reserve()`]: Sender::reserve
[`Sender::try_reserve()`]: Sender::try_reserve"""

    def send(self, value: T) -> None: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class PermitIterator:
    """An [`Iterator`] of [`Permit`] that can be used to hold `n` slots in the channel.

`PermitIterator` values are returned by [`Sender::reserve_many()`] and [`Sender::try_reserve_many()`]
and are used to guarantee channel capacity before generating `n` messages to send.

[`Sender::reserve_many()`]: Sender::reserve_many
[`Sender::try_reserve_many()`]: Sender::try_reserve_many"""

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class OwnedPermit:
    """Owned permit to send one value into the channel.

This is identical to the [`Permit`] type, except that it moves the sender
rather than borrowing it.

`OwnedPermit` values are returned by [`Sender::reserve_owned()`] and
[`Sender::try_reserve_owned()`] and are used to guarantee channel capacity
before generating a message to send.

[`Permit`]: Permit
[`Sender::reserve_owned()`]: Sender::reserve_owned
[`Sender::try_reserve_owned()`]: Sender::try_reserve_owned"""

    def send(self, value: T) -> object: ...

    def release(self) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def same_channel_as_sender(self, sender: object) -> bool: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class Receiver:
    """Receives values from the associated `Sender`.

Instances are created by the [`channel`] function.

This receiver can be turned into a `Stream` using [`ReceiverStream`].

[`ReceiverStream`]: https://docs.rs/tokio-stream/0.1/tokio_stream/wrappers/struct.ReceiverStream.html"""

    def close(self) -> None: ...

    def is_terminated(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def poll(self, cx: Context) -> object: ...

    def borrow(self) -> object: ...

    def borrow_and_update(self) -> object: ...

    def has_changed(self) -> bool: ...

    def mark_changed(self) -> None: ...

    def mark_unchanged(self) -> None: ...

    def changed(self) -> None: ...

    def wait_for(self, f: object) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def recv(self) -> T | None: ...

    def recv_many(self, buffer: list[T], limit: int) -> int: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T | None: ...

    def blocking_recv_many(self, buffer: list[T], limit: int) -> int: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    def capacity(self) -> int: ...

    def max_capacity(self) -> int: ...

    def poll_recv(self, cx: Context) -> object: ...

    def poll_recv_many(self, cx: Context, buffer: list[T], limit: int) -> object: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def same_channel(self, other: Self) -> bool: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def is_closed(self) -> bool: ...

    def resubscribe(self) -> Self: ...

    def recv(self) -> T: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Receiver": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Receiver": ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class UnboundedSender:
    """Send values to the associated `UnboundedReceiver`.

Instances are created by the [`unbounded_channel`] function."""

    def clone(self) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def send(self, message: T) -> None: ...

    def closed(self) -> None: ...

    def is_closed(self) -> bool: ...

    def same_channel(self, other: Self) -> bool: ...

    def downgrade(self) -> object: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

class WeakUnboundedSender:
    """An unbounded sender that does not prevent the channel from being closed.

If all [`UnboundedSender`] instances of a channel were dropped and only
`WeakUnboundedSender` instances remain, the channel is closed.

In order to send messages, the `WeakUnboundedSender` needs to be upgraded using
[`WeakUnboundedSender::upgrade`], which returns `Option<UnboundedSender>`. It returns `None`
if all `UnboundedSender`s have been dropped, and otherwise it returns an `UnboundedSender`.

[`UnboundedSender`]: UnboundedSender
[`WeakUnboundedSender::upgrade`]: WeakUnboundedSender::upgrade

# Examples

```
use tokio::sync::mpsc::unbounded_channel;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, _rx) = unbounded_channel::<i32>();
let tx_weak = tx.downgrade();

// Upgrading will succeed because `tx` still exists.
assert!(tx_weak.upgrade().is_some());

// If we drop `tx`, then it will fail.
drop(tx);
assert!(tx_weak.clone().upgrade().is_none());
# }
```"""

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def upgrade(self) -> object | None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class UnboundedReceiver:
    """Receive values from the associated `UnboundedSender`.

Instances are created by the [`unbounded_channel`] function.

This receiver can be turned into a `Stream` using [`UnboundedReceiverStream`].

[`UnboundedReceiverStream`]: https://docs.rs/tokio-stream/0.1/tokio_stream/wrappers/struct.UnboundedReceiverStream.html"""

    def fmt(self, fmt: Formatter) -> Result: ...

    def recv(self) -> T | None: ...

    def recv_many(self, buffer: list[T], limit: int) -> int: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T | None: ...

    def blocking_recv_many(self, buffer: list[T], limit: int) -> int: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    def poll_recv(self, cx: Context) -> object: ...

    def poll_recv_many(self, cx: Context, buffer: list[T], limit: int) -> object: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

class SendError:
    """Error returned by [`Sender::send`](super::Sender::send)."""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class RecvError:
    """Error returned by `Receiver`."""

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class Mutex:
    """An asynchronous `Mutex`-like type.

This type acts similarly to [`std::sync::Mutex`], with two major
differences: [`lock`] is an async method so does not block, and the lock
guard is designed to be held across `.await` points.

Tokio's Mutex operates on a guaranteed FIFO basis.
This means that the order in which tasks call the [`lock`] method is
the exact order in which they will acquire the lock.

# Which kind of mutex should you use?

Contrary to popular belief, it is ok and often preferred to use the ordinary
[`Mutex`][std] from the standard library in asynchronous code.

The feature that the async mutex offers over the blocking mutex is the
ability to keep it locked across an `.await` point. This makes the async
mutex more expensive than the blocking mutex, so the blocking mutex should
be preferred in the cases where it can be used. The primary use case for the
async mutex is to provide shared mutable access to IO resources such as a
database connection. If the value behind the mutex is just data, it's
usually appropriate to use a blocking mutex such as the one in the standard
library or [`parking_lot`].

Note that, although the compiler will not prevent the std `Mutex` from holding
its guard across `.await` points in situations where the task is not movable
between threads, this virtually never leads to correct concurrent code in
practice as it can easily lead to deadlocks.

A common pattern is to wrap the `Arc<Mutex<...>>` in a struct that provides
non-async methods for performing operations on the data within, and only
lock the mutex inside these methods. The [mini-redis] example provides an
illustration of this pattern.

Additionally, when you _do_ want shared access to an IO resource, it is
often better to spawn a task to manage the IO resource, and to use message
passing to communicate with that task.

[std]: std::sync::Mutex
[`parking_lot`]: https://docs.rs/parking_lot
[mini-redis]: https://github.com/tokio-rs/mini-redis/blob/master/src/db.rs

# Examples:

```rust,no_run
use tokio::sync::Mutex;
use std::sync::Arc;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let data1 = Arc::new(Mutex::new(0));
let data2 = Arc::clone(&data1);

tokio::spawn(async move {
let mut lock = data2.lock().await;
*lock += 1;
});

let mut lock = data1.lock().await;
*lock += 1;
# }
```


```rust,no_run
use tokio::sync::Mutex;
use std::sync::Arc;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let count = Arc::new(Mutex::new(0));

for i in 0..5 {
let my_count = Arc::clone(&count);
tokio::spawn(async move {
for j in 0..10 {
let mut lock = my_count.lock().await;
*lock += 1;
println!("{} {} {}", i, j, lock);
}
});
}

loop {
if *count.lock().await >= 50 {
break;
}
}
println!("Count hit 50.");
# }
```
There are a few things of note here to pay attention to in this example.
1. The mutex is wrapped in an [`Arc`] to allow it to be shared across
threads.
2. Each spawned task obtains a lock and releases it on every iteration.
3. Mutation of the data protected by the Mutex is done by de-referencing
the obtained lock as seen on lines 13 and 20.

Tokio's Mutex works in a simple FIFO (first in, first out) style where all
calls to [`lock`] complete in the order they were performed. In that way the
Mutex is "fair" and predictable in how it distributes the locks to inner
data. Locks are released and reacquired after every iteration, so basically,
each thread goes to the back of the line after it increments the value once.
Note that there's some unpredictability to the timing between when the
threads are started, but once they are going they alternate predictably.
Finally, since there is only a single valid lock at any given time, there is
no possibility of a race condition when mutating the inner value.

Note that in contrast to [`std::sync::Mutex`], this implementation does not
poison the mutex when a thread holding the [`MutexGuard`] panics. In such a
case, the mutex will be unlocked. If the panic is caught, this might leave
the data protected by the mutex in an inconsistent state.

[`Mutex`]: struct@Mutex
[`MutexGuard`]: struct@MutexGuard
[`Arc`]: struct@std::sync::Arc
[`std::sync::Mutex`]: struct@std::sync::Mutex
[`Send`]: trait@std::marker::Send
[`lock`]: method@Mutex::lock"""

    @staticmethod
    def new(t: T) -> "Mutex": ...

    @staticmethod
    def const_new(t: T) -> "Mutex": ...

    def lock(self) -> object: ...

    def blocking_lock(self) -> object: ...

    def blocking_lock_owned(self) -> object: ...

    def lock_owned(self) -> object: ...

    def try_lock(self) -> object: ...

    def get_mut(self) -> T: ...

    def try_lock_owned(self) -> object: ...

    def into_inner(self) -> T: ...

    @staticmethod
    def from_(s: T) -> "Mutex": ...

    @staticmethod
    def default() -> "Mutex": ...

    def fmt(self, f: Formatter) -> Result: ...

class MutexGuard:
    """A handle to a held `Mutex`. The guard can be held across any `.await` point
as it is [`Send`].

As long as you have this guard, you have exclusive access to the underlying
`T`. The guard internally borrows the `Mutex`, so the mutex will not be
dropped while a guard exists.

The lock is automatically released whenever the guard is dropped, at which
point `lock` will succeed yet again."""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    @staticmethod
    def mutex(this: Self) -> object: ...

    def drop(self) -> None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

class OwnedMutexGuard:
    """An owned handle to a held `Mutex`.

This guard is only available from a `Mutex` that is wrapped in an [`Arc`]. It
is identical to `MutexGuard`, except that rather than borrowing the `Mutex`,
it clones the `Arc`, incrementing the reference count. This means that
unlike `MutexGuard`, it will have the `'static` lifetime.

As long as you have this guard, you have exclusive access to the underlying
`T`. The guard internally keeps a reference-counted pointer to the original
`Mutex`, so even if the lock goes away, the guard remains valid.

The lock is automatically released whenever the guard is dropped, at which
point `lock` will succeed yet again.

[`Arc`]: std::sync::Arc"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    @staticmethod
    def mutex(this: Self) -> object: ...

    def drop(self) -> None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class MappedMutexGuard:
    """A handle to a held `Mutex` that has had a function applied to it via [`MutexGuard::map`].

This can be used to hold a subfield of the protected data.

[`MutexGuard::map`]: method@MutexGuard::map"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    def drop(self) -> None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class OwnedMappedMutexGuard:
    """A owned handle to a held `Mutex` that has had a function applied to it via
[`OwnedMutexGuard::map`].

This can be used to hold a subfield of the protected data.

[`OwnedMutexGuard::map`]: method@OwnedMutexGuard::map"""

    @staticmethod
    def map(this: Self, f: F) -> object: ...

    @staticmethod
    def try_map(this: Self, f: F) -> object: ...

    def drop(self) -> None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class TryLockError:
    """Error returned from the [`Mutex::try_lock`], [`RwLock::try_read`] and
[`RwLock::try_write`] functions.

`Mutex::try_lock` operation will only fail if the mutex is already locked.

`RwLock::try_read` operation will only fail if the lock is currently held
by an exclusive writer.

`RwLock::try_write` operation will only fail if the lock is currently held
by any reader or by an exclusive writer.

[`Mutex::try_lock`]: Mutex::try_lock
[`RwLock::try_read`]: fn@super::RwLock::try_read
[`RwLock::try_write`]: fn@super::RwLock::try_write"""

    def fmt(self, fmt: Formatter) -> Result: ...

class Semaphore:
    """Counting semaphore performing asynchronous permit acquisition.

A semaphore maintains a set of permits. Permits are used to synchronize
access to a shared resource. A semaphore differs from a mutex in that it
can allow more than one concurrent caller to access the shared resource at a
time.

When `acquire` is called and the semaphore has remaining permits, the
function immediately returns a permit. However, if no remaining permits are
available, `acquire` (asynchronously) waits until an outstanding permit is
dropped. At this point, the freed permit is assigned to the caller.

This `Semaphore` is fair, which means that permits are given out in the order
they were requested. This fairness is also applied when `acquire_many` gets
involved, so if a call to `acquire_many` at the front of the queue requests
more permits than currently available, this can prevent a call to `acquire`
from completing, even if the semaphore has enough permits complete the call
to `acquire`.

To use the `Semaphore` in a poll function, you can use the [`PollSemaphore`]
utility.

# Examples

Basic usage:

```
use tokio::sync::{Semaphore, TryAcquireError};

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let semaphore = Semaphore::new(3);

let a_permit = semaphore.acquire().await.unwrap();
let two_permits = semaphore.acquire_many(2).await.unwrap();

assert_eq!(semaphore.available_permits(), 0);

let permit_attempt = semaphore.try_acquire();
assert_eq!(permit_attempt.err(), Some(TryAcquireError::NoPermits));
# }
```

## Limit the number of simultaneously opened files in your program

Most operating systems have limits on the number of open file
handles. Even in systems without explicit limits, resource constraints
implicitly set an upper bound on the number of open files. If your
program attempts to open a large number of files and exceeds this
limit, it will result in an error.

This example uses a Semaphore with 100 permits. By acquiring a permit from
the Semaphore before accessing a file, you ensure that your program opens
no more than 100 files at a time. When trying to open the 101st
file, the program will wait until a permit becomes available before
proceeding to open another file.
```
# #[cfg(not(target_family = "wasm"))]
# {
use std::io::Result;
use tokio::fs::File;
use tokio::sync::Semaphore;
use tokio::io::AsyncWriteExt;

static PERMITS: Semaphore = Semaphore::const_new(100);

async fn write_to_file(message: &[u8]) -> Result<()> {
let _permit = PERMITS.acquire().await.unwrap();
let mut buffer = File::create("example.txt").await?;
buffer.write_all(message).await?;
Ok(()) // Permit goes out of scope here, and is available again for acquisition
}
# }
```

## Limit the number of outgoing requests being sent at the same time

In some scenarios, it might be required to limit the number of outgoing
requests being sent in parallel. This could be due to limits of a consumed
API or the network resources of the system the application is running on.

This example uses an `Arc<Semaphore>` with 10 permits. Each task spawned is
given a reference to the semaphore by cloning the `Arc<Semaphore>`. Before
a task sends a request, it must acquire a permit from the semaphore by
calling [`Semaphore::acquire`]. This ensures that at most 10 requests are
sent in parallel at any given time. After a task has sent a request, it
drops the permit to allow other tasks to send requests.

```
use std::sync::Arc;
use tokio::sync::Semaphore;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
// Define maximum number of parallel requests.
let semaphore = Arc::new(Semaphore::new(5));
// Spawn many tasks that will send requests.
let mut jhs = Vec::new();
for task_id in 0..50 {
let semaphore = semaphore.clone();
let jh = tokio::spawn(async move {
// Acquire permit before sending request.
let _permit = semaphore.acquire().await.unwrap();
// Send the request.
let response = send_request(task_id).await;
// Drop the permit after the request has been sent.
drop(_permit);
// Handle response.
// ...

response
});
jhs.push(jh);
}
// Collect responses from tasks.
let mut responses = Vec::new();
for jh in jhs {
let response = jh.await.unwrap();
responses.push(response);
}
// Process responses.
// ...
# }
# async fn send_request(task_id: usize) {
#     // Send request.
# }
```

## Limit the number of incoming requests being handled at the same time

Similar to limiting the number of simultaneously opened files, network handles
are a limited resource. Allowing an unbounded amount of requests to be processed
could result in a denial-of-service, among many other issues.

This example uses an `Arc<Semaphore>` instead of a global variable.
To limit the number of requests that can be processed at the time,
we acquire a permit for each task before spawning it. Once acquired,
a new task is spawned; and once finished, the permit is dropped inside
of the task to allow others to spawn. Permits must be acquired via
[`Semaphore::acquire_owned`] to be movable across the task boundary.
(Since our semaphore is not a global variable — if it was, then `acquire` would be enough.)

```no_run
# #[cfg(not(target_family = "wasm"))]
# {
use std::sync::Arc;
use tokio::sync::Semaphore;
use tokio::net::TcpListener;

#[tokio::main]
async fn main() -> std::io::Result<()> {
let semaphore = Arc::new(Semaphore::new(3));
let listener = TcpListener::bind("127.0.0.1:8080").await?;

loop {
// Acquire permit before accepting the next socket.
//
// We use `acquire_owned` so that we can move `permit` into
// other tasks.
let permit = semaphore.clone().acquire_owned().await.unwrap();
let (mut socket, _) = listener.accept().await?;

tokio::spawn(async move {
// Do work using the socket.
handle_connection(&mut socket).await;
// Drop socket while the permit is still live.
drop(socket);
// Drop the permit, so more tasks can be created.
drop(permit);
});
}
}
# async fn handle_connection(_socket: &mut tokio::net::TcpStream) {
#   // Do work
# }
# }
```

## Prevent tests from running in parallel

By default, Rust runs tests in the same file in parallel. However, in some
cases, running two tests in parallel may lead to problems. For example, this
can happen when tests use the same database.

Consider the following scenario:
1. `test_insert`: Inserts a key-value pair into the database, then retrieves
the value using the same key to verify the insertion.
2. `test_update`: Inserts a key, then updates the key to a new value and
verifies that the value has been accurately updated.
3. `test_others`: A third test that doesn't modify the database state. It
can run in parallel with the other tests.

In this example, `test_insert` and `test_update` need to run in sequence to
work, but it doesn't matter which test runs first. We can leverage a
semaphore with a single permit to address this challenge.

```
# use tokio::sync::Mutex;
# use std::collections::BTreeMap;
# struct Database {
#   map: Mutex<BTreeMap<String, i32>>,
# }
# impl Database {
#    pub const fn setup() -> Database {
#        Database {
#            map: Mutex::const_new(BTreeMap::new()),
#        }
#    }
#    pub async fn insert(&self, key: &str, value: i32) {
#        self.map.lock().await.insert(key.to_string(), value);
#    }
#    pub async fn update(&self, key: &str, value: i32) {
#        self.map.lock().await
#            .entry(key.to_string())
#            .and_modify(|origin| *origin = value);
#    }
#    pub async fn delete(&self, key: &str) {
#        self.map.lock().await.remove(key);
#    }
#    pub async fn get(&self, key: &str) -> i32 {
#        *self.map.lock().await.get(key).unwrap()
#    }
# }
use tokio::sync::Semaphore;

// Initialize a static semaphore with only one permit, which is used to
// prevent test_insert and test_update from running in parallel.
static PERMIT: Semaphore = Semaphore::const_new(1);

// Initialize the database that will be used by the subsequent tests.
static DB: Database = Database::setup();

#[tokio::test]
# async fn fake_test_insert() {}
async fn test_insert() {
// Acquire permit before proceeding. Since the semaphore has only one permit,
// the test will wait if the permit is already acquired by other tests.
let permit = PERMIT.acquire().await.unwrap();

// Do the actual test stuff with database

// Insert a key-value pair to database
let (key, value) = ("name", 0);
DB.insert(key, value).await;

// Verify that the value has been inserted correctly.
assert_eq!(DB.get(key).await, value);

// Undo the insertion, so the database is empty at the end of the test.
DB.delete(key).await;

// Drop permit. This allows the other test to start running.
drop(permit);
}

#[tokio::test]
# async fn fake_test_update() {}
async fn test_update() {
// Acquire permit before proceeding. Since the semaphore has only one permit,
// the test will wait if the permit is already acquired by other tests.
let permit = PERMIT.acquire().await.unwrap();

// Do the same insert.
let (key, value) = ("name", 0);
DB.insert(key, value).await;

// Update the existing value with a new one.
let new_value = 1;
DB.update(key, new_value).await;

// Verify that the value has been updated correctly.
assert_eq!(DB.get(key).await, new_value);

// Undo any modificattion.
DB.delete(key).await;

// Drop permit. This allows the other test to start running.
drop(permit);
}

#[tokio::test]
# async fn fake_test_others() {}
async fn test_others() {
// This test can run in parallel with test_insert and test_update,
// so it does not use PERMIT.
}
# #[tokio::main(flavor = "current_thread")]
# async fn main() {
#   test_insert().await;
#   test_update().await;
#   test_others().await;
# }
```

## Rate limiting using a token bucket

This example showcases the [`add_permits`] and [`SemaphorePermit::forget`] methods.

Many applications and systems have constraints on the rate at which certain
operations should occur. Exceeding this rate can result in suboptimal
performance or even errors.

This example implements rate limiting using a [token bucket]. A token bucket is a form of rate
limiting that doesn't kick in immediately, to allow for short bursts of incoming requests that
arrive at the same time.

With a token bucket, each incoming request consumes a token, and the tokens are refilled at a
certain rate that defines the rate limit. When a burst of requests arrives, tokens are
immediately given out until the bucket is empty. Once the bucket is empty, requests will have to
wait for new tokens to be added.

Unlike the example that limits how many requests can be handled at the same time, we do not add
tokens back when we finish handling a request. Instead, tokens are added only by a timer task.

Note that this implementation is suboptimal when the duration is small, because it consumes a
lot of cpu constantly looping and sleeping.

[token bucket]: https://en.wikipedia.org/wiki/Token_bucket
[`add_permits`]: crate::sync::Semaphore::add_permits
[`SemaphorePermit::forget`]: crate::sync::SemaphorePermit::forget
```
use std::sync::Arc;
use tokio::sync::Semaphore;
use tokio::time::{interval, Duration};

struct TokenBucket {
sem: Arc<Semaphore>,
jh: tokio::task::JoinHandle<()>,
}

impl TokenBucket {
fn new(duration: Duration, capacity: usize) -> Self {
let sem = Arc::new(Semaphore::new(capacity));

// refills the tokens at the end of each interval
let jh = tokio::spawn({
let sem = sem.clone();
let mut interval = interval(duration);
interval.set_missed_tick_behavior(tokio::time::MissedTickBehavior::Skip);

async move {
loop {
interval.tick().await;

if sem.available_permits() < capacity {
sem.add_permits(1);
}
}
}
});

Self { jh, sem }
}

async fn acquire(&self) {
// This can return an error if the semaphore is closed, but we
// never close it, so this error can never happen.
let permit = self.sem.acquire().await.unwrap();
// To avoid releasing the permit back to the semaphore, we use
// the `SemaphorePermit::forget` method.
permit.forget();
}
}

impl Drop for TokenBucket {
fn drop(&mut self) {
// Kill the background task so it stops taking up resources when we
// don't need it anymore.
self.jh.abort();
}
}

# #[tokio::main(flavor = "current_thread")]
# async fn _hidden() {}
# #[tokio::main(flavor = "current_thread", start_paused = true)]
# async fn main() {
let capacity = 5;
let update_interval = Duration::from_secs_f32(1.0 / capacity as f32);
let bucket = TokenBucket::new(update_interval, capacity);

for _ in 0..5 {
bucket.acquire().await;

// do the operation
}
# }
```

[`PollSemaphore`]: https://docs.rs/tokio-util/latest/tokio_util/sync/struct.PollSemaphore.html
[`Semaphore::acquire_owned`]: crate::sync::Semaphore::acquire_owned"""

    def add_permit(self) -> None: ...

    def add_permits(self, n: int) -> None: ...

    def is_idle(self) -> bool: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def add_permit(self) -> None: ...

    def add_permits(self, n: int) -> None: ...

    def is_idle(self) -> bool: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    @staticmethod
    def new(permits: int) -> "Semaphore": ...

    @staticmethod
    def const_new(permits: int) -> "Semaphore": ...

    def available_permits(self) -> int: ...

    def add_permits(self, n: int) -> None: ...

    def forget_permits(self, n: int) -> int: ...

    def acquire(self) -> SemaphorePermit: ...

    def acquire_many(self, n: int) -> SemaphorePermit: ...

    def try_acquire(self) -> SemaphorePermit: ...

    def try_acquire_many(self, n: int) -> SemaphorePermit: ...

    def acquire_owned(self) -> OwnedSemaphorePermit: ...

    def acquire_many_owned(self, n: int) -> OwnedSemaphorePermit: ...

    def try_acquire_owned(self) -> OwnedSemaphorePermit: ...

    def try_acquire_many_owned(self, n: int) -> OwnedSemaphorePermit: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class SemaphorePermit:
    """A permit from the semaphore.

This type is created by the [`acquire`] method.

[`acquire`]: crate::sync::Semaphore::acquire()"""

    def forget(self) -> None: ...

    def merge(self, other: Self) -> None: ...

    def split(self, n: int) -> object: ...

    def num_permits(self) -> int: ...

    def drop(self) -> None: ...

class OwnedSemaphorePermit:
    """An owned permit from the semaphore.

This type is created by the [`acquire_owned`] method.

[`acquire_owned`]: crate::sync::Semaphore::acquire_owned()"""

    def forget(self) -> None: ...

    def merge(self, other: Self) -> None: ...

    def split(self, n: int) -> object: ...

    def semaphore(self) -> object: ...

    def num_permits(self) -> int: ...

    def drop(self) -> None: ...

class Sender:
    """Sending-half of the [`broadcast`] channel.

May be used from many threads. Messages can be sent with
[`send`][Sender::send].

# Examples

```
use tokio::sync::broadcast;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, mut rx1) = broadcast::channel(16);
let mut rx2 = tx.subscribe();

tokio::spawn(async move {
assert_eq!(rx1.recv().await.unwrap(), 10);
assert_eq!(rx1.recv().await.unwrap(), 20);
});

tokio::spawn(async move {
assert_eq!(rx2.recv().await.unwrap(), 10);
assert_eq!(rx2.recv().await.unwrap(), 20);
});

tx.send(10).unwrap();
tx.send(20).unwrap();
# }
```

[`broadcast`]: crate::sync::broadcast"""

    def send(self, t: T) -> None: ...

    def closed(self) -> None: ...

    def is_closed(self) -> bool: ...

    def poll_closed(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

    def clone(self) -> Self: ...

    @staticmethod
    def default() -> "Sender": ...

    @staticmethod
    def new(init: T) -> "Sender": ...

    def send(self, value: T) -> None: ...

    def send_modify(self, modify: F) -> None: ...

    def send_if_modified(self, modify: F) -> bool: ...

    def send_replace(self, value: T) -> T: ...

    def borrow(self) -> object: ...

    def is_closed(self) -> bool: ...

    def closed(self) -> None: ...

    def subscribe(self) -> object: ...

    def receiver_count(self) -> int: ...

    def sender_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def drop(self) -> None: ...

    def send(self, value: T) -> None: ...

    def closed(self) -> None: ...

    def try_send(self, message: T) -> None: ...

    def send_timeout(self, value: T, timeout: Duration) -> None: ...

    def blocking_send(self, value: T) -> None: ...

    def is_closed(self) -> bool: ...

    def reserve(self) -> object: ...

    def reserve_many(self, n: int) -> object: ...

    def reserve_owned(self) -> object: ...

    def try_reserve(self) -> object: ...

    def try_reserve_many(self, n: int) -> object: ...

    def try_reserve_owned(self) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def capacity(self) -> int: ...

    def downgrade(self) -> object: ...

    def max_capacity(self) -> int: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new(capacity: int) -> "Sender": ...

    def send(self, value: T) -> int: ...

    def subscribe(self) -> object: ...

    def downgrade(self) -> object: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def receiver_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def closed(self) -> None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Sender": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Sender": ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class WeakSender:
    """A sender that does not prevent the channel from being closed.

If all [`Sender`] instances of a channel were dropped and only `WeakSender`
instances remain, the channel is closed.

In order to send messages, the `WeakSender` needs to be upgraded using
[`WeakSender::upgrade`], which returns `Option<Sender>`. It returns `None`
if all `Sender`s have been dropped, and otherwise it returns a `Sender`.

[`Sender`]: Sender
[`WeakSender::upgrade`]: WeakSender::upgrade

# Examples

```
use tokio::sync::broadcast::channel;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, _rx) = channel::<i32>(15);
let tx_weak = tx.downgrade();

// Upgrading will succeed because `tx` still exists.
assert!(tx_weak.upgrade().is_some());

// If we drop `tx`, then it will fail.
drop(tx);
assert!(tx_weak.clone().upgrade().is_none());
# }
```"""

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def upgrade(self) -> object | None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def upgrade(self) -> object | None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class Receiver:
    """Receiving-half of the [`broadcast`] channel.

Must not be used concurrently. Messages may be retrieved using
[`recv`][Receiver::recv].

To turn this receiver into a `Stream`, you can use the [`BroadcastStream`]
wrapper.

[`BroadcastStream`]: https://docs.rs/tokio-stream/0.1/tokio_stream/wrappers/struct.BroadcastStream.html

# Examples

```
use tokio::sync::broadcast;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, mut rx1) = broadcast::channel(16);
let mut rx2 = tx.subscribe();

tokio::spawn(async move {
assert_eq!(rx1.recv().await.unwrap(), 10);
assert_eq!(rx1.recv().await.unwrap(), 20);
});

tokio::spawn(async move {
assert_eq!(rx2.recv().await.unwrap(), 10);
assert_eq!(rx2.recv().await.unwrap(), 20);
});

tx.send(10).unwrap();
tx.send(20).unwrap();
# }
```

[`broadcast`]: crate::sync::broadcast"""

    def close(self) -> None: ...

    def is_terminated(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def poll(self, cx: Context) -> object: ...

    def borrow(self) -> object: ...

    def borrow_and_update(self) -> object: ...

    def has_changed(self) -> bool: ...

    def mark_changed(self) -> None: ...

    def mark_unchanged(self) -> None: ...

    def changed(self) -> None: ...

    def wait_for(self, f: object) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def recv(self) -> T | None: ...

    def recv_many(self, buffer: list[T], limit: int) -> int: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T | None: ...

    def blocking_recv_many(self, buffer: list[T], limit: int) -> int: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    def capacity(self) -> int: ...

    def max_capacity(self) -> int: ...

    def poll_recv(self, cx: Context) -> object: ...

    def poll_recv_many(self, cx: Context, buffer: list[T], limit: int) -> object: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def same_channel(self, other: Self) -> bool: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def is_closed(self) -> bool: ...

    def resubscribe(self) -> Self: ...

    def recv(self) -> T: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Receiver": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Receiver": ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class SendError:
    """Error returned by the [`send`] function on a [`Sender`].

A **send** operation can only fail if there are no active receivers,
implying that the message could never be received. The error contains the
message being sent as a payload so it can be recovered.

[`send`]: crate::sync::broadcast::Sender::send
[`Sender`]: crate::sync::broadcast::Sender"""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class AcquireError:
    """Error returned from the [`Semaphore::acquire`] function.

An `acquire` operation can only fail if the semaphore has been
[closed].

[closed]: crate::sync::Semaphore::close
[`Semaphore::acquire`]: crate::sync::Semaphore::acquire"""

    def fmt(self, fmt: Formatter) -> Result: ...

class OnceCell:
    """A thread-safe cell that can be written to only once.

A `OnceCell` is typically used for global variables that need to be
initialized once on first use, but need no further changes. The `OnceCell`
in Tokio allows the initialization procedure to be asynchronous.

# Examples

```
use tokio::sync::OnceCell;

async fn some_computation() -> u32 {
1 + 1
}

static ONCE: OnceCell<u32> = OnceCell::const_new();

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let result = ONCE.get_or_init(some_computation).await;
assert_eq!(*result, 2);
# }
```

It is often useful to write a wrapper method for accessing the value.

```
use tokio::sync::OnceCell;

static ONCE: OnceCell<u32> = OnceCell::const_new();

async fn get_global_integer() -> &'static u32 {
ONCE.get_or_init(|| async {
1 + 1
}).await
}

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let result = get_global_integer().await;
assert_eq!(*result, 2);
# }
```"""

    @staticmethod
    def default() -> object: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def clone(self) -> object: ...

    def eq(self, other: object) -> bool: ...

    def drop(self) -> None: ...

    @staticmethod
    def from_(value: T) -> "OnceCell": ...

    @staticmethod
    def new() -> "OnceCell": ...

    @staticmethod
    def const_new() -> "OnceCell": ...

    @staticmethod
    def new_with(value: T | None) -> "OnceCell": ...

    @staticmethod
    def const_new_with(value: T) -> "OnceCell": ...

    def initialized(self) -> bool: ...

    def get(self) -> object: ...

    def get_mut(self) -> object: ...

    def set(self, value: T) -> None: ...

    def get_or_init(self, f: F) -> T: ...

    def get_or_try_init(self, f: F) -> object: ...

    def into_inner(self) -> T | None: ...

    def take(self) -> T | None: ...

class NamedPipeServer:
    """A [Windows named pipe] server.

Accepting client connections involves creating a server with
[`ServerOptions::create`] and waiting for clients to connect using
[`NamedPipeServer::connect`].

To avoid having clients sporadically fail with
[`std::io::ErrorKind::NotFound`] when they connect to a server, we must
ensure that at least one server instance is available at all times. This
means that the typical listen loop for a server is a bit involved, because
we have to ensure that we never drop a server accidentally while a client
might connect.

So a correctly implemented server looks like this:

```no_run
use std::io;
use tokio::net::windows::named_pipe::ServerOptions;

const PIPE_NAME: &str = r"\\\\.\\pipe\\named-pipe-idiomatic-server";

# #[tokio::main] async fn main() -> std::io::Result<()> {
// The first server needs to be constructed early so that clients can
// be correctly connected. Otherwise calling .wait will cause the client to
// error.
//
// Here we also make use of `first_pipe_instance`, which will ensure that
// there are no other servers up and running already.
let mut server = ServerOptions::new()
.first_pipe_instance(true)
.create(PIPE_NAME)?;

// Spawn the server loop.
let server = tokio::spawn(async move {
loop {
// Wait for a client to connect.
server.connect().await?;
let connected_client = server;

// Construct the next server to be connected before sending the one
// we already have of onto a task. This ensures that the server
// isn't closed (after it's done in the task) before a new one is
// available. Otherwise the client might error with
// `io::ErrorKind::NotFound`.
server = ServerOptions::new().create(PIPE_NAME)?;

let client = tokio::spawn(async move {
/* use the connected client */
#           Ok::<_, std::io::Error>(())
});
#       if true { break } // needed for type inference to work
}

Ok::<_, io::Error>(())
});

/* do something else not server related here */
# Ok(()) }
```

[Windows named pipe]: https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes"""

    @staticmethod
    def from_raw_handle(handle: RawHandle) -> object: ...

    def info(self) -> PipeInfo: ...

    def connect(self) -> object: ...

    def disconnect(self) -> object: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def writable(self) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def try_io(self, interest: Interest, f: object) -> R: ...

    def async_io(self, interest: Interest, f: object) -> R: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def poll_flush(self, _cx: Context) -> object: ...

    def poll_shutdown(self, cx: Context) -> object: ...

    def as_raw_handle(self) -> RawHandle: ...

    def as_handle(self) -> BorrowedHandle: ...

class NamedPipeClient:
    """A [Windows named pipe] client.

Constructed using [`ClientOptions::open`].

Connecting a client correctly involves a few steps. When connecting through
[`ClientOptions::open`], it might error indicating one of two things:

* [`std::io::ErrorKind::NotFound`] - There is no server available.
* [`ERROR_PIPE_BUSY`] - There is a server available, but it is busy. Sleep
for a while and try again.

So a correctly implemented client looks like this:

```no_run
use std::time::Duration;
use tokio::net::windows::named_pipe::ClientOptions;
use tokio::time;
use windows_sys::Win32::Foundation::ERROR_PIPE_BUSY;

const PIPE_NAME: &str = r"\\\\.\\pipe\\named-pipe-idiomatic-client";

# #[tokio::main] async fn main() -> std::io::Result<()> {
let client = loop {
match ClientOptions::new().open(PIPE_NAME) {
Ok(client) => break client,
Err(e) if e.raw_os_error() == Some(ERROR_PIPE_BUSY as i32) => (),
Err(e) => return Err(e),
}

time::sleep(Duration::from_millis(50)).await;
};

/* use the connected client */
# Ok(()) }
```

[`ERROR_PIPE_BUSY`]: https://docs.rs/windows-sys/latest/windows_sys/Win32/Foundation/constant.ERROR_PIPE_BUSY.html
[Windows named pipe]: https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes"""

    @staticmethod
    def from_raw_handle(handle: RawHandle) -> object: ...

    def info(self) -> PipeInfo: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def writable(self) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def try_io(self, interest: Interest, f: object) -> R: ...

    def async_io(self, interest: Interest, f: object) -> R: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def poll_flush(self, _cx: Context) -> object: ...

    def poll_shutdown(self, cx: Context) -> object: ...

    def as_raw_handle(self) -> RawHandle: ...

    def as_handle(self) -> BorrowedHandle: ...

class ServerOptions:
    """A builder structure for construct a named pipe with named pipe-specific
options. This is required to use for named pipe servers who wants to modify
pipe-related options.

See [`ServerOptions::create`]."""

    @staticmethod
    def new() -> "ServerOptions": ...

    def pipe_mode(self, pipe_mode: PipeMode) -> Self: ...

    def access_inbound(self, allowed: bool) -> Self: ...

    def access_outbound(self, allowed: bool) -> Self: ...

    def first_pipe_instance(self, first: bool) -> Self: ...

    def write_dac(self, requested: bool) -> Self: ...

    def write_owner(self, requested: bool) -> Self: ...

    def access_system_security(self, requested: bool) -> Self: ...

    def reject_remote_clients(self, reject: bool) -> Self: ...

    def max_instances(self, instances: int) -> Self: ...

    def out_buffer_size(self, buffer: int) -> Self: ...

    def in_buffer_size(self, buffer: int) -> Self: ...

    def create(self, addr: object) -> NamedPipeServer: ...

    def create_with_security_attributes_raw(self, addr: object, attrs: object) -> NamedPipeServer: ...

class ClientOptions:
    """A builder suitable for building and interacting with named pipes from the
client side.

See [`ClientOptions::open`]."""

    @staticmethod
    def new() -> "ClientOptions": ...

    def read(self, allowed: bool) -> Self: ...

    def write(self, allowed: bool) -> Self: ...

    def security_qos_flags(self, flags: int) -> Self: ...

    def pipe_mode(self, pipe_mode: PipeMode) -> Self: ...

    def open(self, addr: object) -> NamedPipeClient: ...

    def open_with_security_attributes_raw(self, addr: object, attrs: object) -> NamedPipeClient: ...

class PipeInfo:
    """Information about a named pipe.

Constructed through [`NamedPipeServer::info`] or [`NamedPipeClient::info`]."""
    pass

class SocketAddr:
    """An address associated with a Tokio Unix socket.

This type is a thin wrapper around [`std::os::unix::net::SocketAddr`]. You
can convert to and from the standard library `SocketAddr` type using the
[`From`] trait."""

    def is_unnamed(self) -> bool: ...

    def as_pathname(self) -> object: ...

    def as_abstract_name(self) -> object: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_(value: SocketAddr) -> "SocketAddr": ...

    @staticmethod
    def from_(value: SocketAddr) -> "SocketAddr": ...

    def to_socket_addrs(self, _: Internal) -> Future: ...

class ReadHalf:
    """Borrowed read half of a [`UnixStream`], created by [`split`].

Reading from a `ReadHalf` is usually done using the convenience methods found on the
[`AsyncReadExt`] trait.

[`UnixStream`]: UnixStream
[`split`]: UnixStream::split()
[`AsyncReadExt`]: trait@crate::io::AsyncReadExt"""

    def is_pair_of(self, other: object) -> bool: ...

    def unsplit(self, wr: object) -> T: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def poll_peek(self, cx: Context, buf: ReadBuf) -> object: ...

    def peek(self, buf: object) -> int: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> TcpStream: ...

class WriteHalf:
    """Borrowed write half of a [`UnixStream`], created by [`split`].

Note that in the [`AsyncWrite`] implementation of this type, [`poll_shutdown`] will
shut down the [`UnixStream`] stream in the write direction.

Writing to an `WriteHalf` is usually done using the convenience methods found
on the [`AsyncWriteExt`] trait.

[`UnixStream`]: UnixStream
[`split`]: UnixStream::split()
[`AsyncWrite`]: trait@crate::io::AsyncWrite
[`poll_shutdown`]: fn@crate::io::AsyncWrite::poll_shutdown
[`AsyncWriteExt`]: trait@crate::io::AsyncWriteExt"""

    def is_pair_of(self, other: object) -> bool: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_flush(self, cx: Context) -> object: ...

    def poll_shutdown(self, cx: Context) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> TcpStream: ...

class UCred:
    """Credentials of a process."""

    def uid(self) -> uid_t: ...

    def gid(self) -> gid_t: ...

    def pid(self) -> pid_t | None: ...

class OwnedReadHalf:
    """Owned read half of a [`UnixStream`], created by [`into_split`].

Reading from an `OwnedReadHalf` is usually done using the convenience methods found
on the [`AsyncReadExt`] trait.

[`UnixStream`]: crate::net::UnixStream
[`into_split`]: crate::net::UnixStream::into_split()
[`AsyncReadExt`]: trait@crate::io::AsyncReadExt"""

    def reunite(self, other: OwnedWriteHalf) -> UnixStream: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def reunite(self, other: OwnedWriteHalf) -> TcpStream: ...

    def poll_peek(self, cx: Context, buf: ReadBuf) -> object: ...

    def peek(self, buf: object) -> int: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> TcpStream: ...

class OwnedWriteHalf:
    """Owned write half of a [`UnixStream`], created by [`into_split`].

Note that in the [`AsyncWrite`] implementation of this type,
[`poll_shutdown`] will shut down the stream in the write direction.
Dropping the write half will also shut down the write half of the stream.

Writing to an `OwnedWriteHalf` is usually done using the convenience methods
found on the [`AsyncWriteExt`] trait.

[`UnixStream`]: crate::net::UnixStream
[`into_split`]: crate::net::UnixStream::into_split()
[`AsyncWrite`]: trait@crate::io::AsyncWrite
[`poll_shutdown`]: fn@crate::io::AsyncWrite::poll_shutdown
[`AsyncWriteExt`]: trait@crate::io::AsyncWriteExt"""

    def reunite(self, other: OwnedReadHalf) -> UnixStream: ...

    def forget(self) -> None: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def drop(self) -> None: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def reunite(self, other: OwnedReadHalf) -> TcpStream: ...

    def forget(self) -> None: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def drop(self) -> None: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> TcpStream: ...

class ReuniteError:
    """Error indicating that two halves were not from the same socket, and thus could
not be reunited."""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class OpenOptions:
    """Options and flags which can be used to configure how a FIFO file is opened.

This builder allows configuring how to create a pipe end from a FIFO file.
Generally speaking, when using `OpenOptions`, you'll first call [`new`],
then chain calls to methods to set each option, then call either
[`open_receiver`] or [`open_sender`], passing the path of the FIFO file you
are trying to open. This will give you a [`io::Result`] with a pipe end
inside that you can further operate on.

[`new`]: OpenOptions::new
[`open_receiver`]: OpenOptions::open_receiver
[`open_sender`]: OpenOptions::open_sender

# Examples

Opening a pair of pipe ends from a FIFO file:

```no_run
use tokio::net::unix::pipe;
# use std::error::Error;

const FIFO_NAME: &str = "path/to/a/fifo";

# async fn dox() -> Result<(), Box<dyn Error>> {
let rx = pipe::OpenOptions::new().open_receiver(FIFO_NAME)?;
let tx = pipe::OpenOptions::new().open_sender(FIFO_NAME)?;
# Ok(())
# }
```

Opening a [`Sender`] on Linux when you are sure the file is a FIFO:

```ignore
use tokio::net::unix::pipe;
use nix::{unistd::mkfifo, sys::stat::Mode};
# use std::error::Error;

// Our program has exclusive access to this path.
const FIFO_NAME: &str = "path/to/a/new/fifo";

# async fn dox() -> Result<(), Box<dyn Error>> {
mkfifo(FIFO_NAME, Mode::S_IRWXU)?;
let tx = pipe::OpenOptions::new()
.read_write(true)
.unchecked(true)
.open_sender(FIFO_NAME)?;
# Ok(())
# }
```"""

    @staticmethod
    def new() -> "OpenOptions": ...

    def read_write(self, value: bool) -> Self: ...

    def unchecked(self, value: bool) -> Self: ...

    def open_receiver(self, path: P) -> Receiver: ...

    def open_sender(self, path: P) -> Sender: ...

    @staticmethod
    def default() -> "OpenOptions": ...

    @staticmethod
    def new() -> "OpenOptions": ...

    def read(self, read: bool) -> OpenOptions: ...

    def write(self, write: bool) -> OpenOptions: ...

    def append(self, append: bool) -> OpenOptions: ...

    def truncate(self, truncate: bool) -> OpenOptions: ...

    def create(self, create: bool) -> OpenOptions: ...

    def create_new(self, create_new: bool) -> OpenOptions: ...

    def open(self, path: object) -> File: ...

    @staticmethod
    def from_(options: StdOpenOptions) -> "OpenOptions": ...

    @staticmethod
    def default() -> "OpenOptions": ...

class Sender:
    """Writing end of a Unix pipe.

It can be constructed from a FIFO file with [`OpenOptions::open_sender`].

Opening a named pipe for writing involves a few steps.
Call to [`OpenOptions::open_sender`] might fail with an error indicating
different things:

* [`io::ErrorKind::NotFound`] - There is no file at the specified path.
* [`io::ErrorKind::InvalidInput`] - The file exists, but it is not a FIFO.
* [`ENXIO`] - The file is a FIFO, but no process has it open for reading.
Sleep for a while and try again.
* Other OS errors not specific to opening FIFO files.

Opening a `Sender` from a FIFO file should look like this:

```no_run
use tokio::net::unix::pipe;
use tokio::time::{self, Duration};

const FIFO_NAME: &str = "path/to/a/fifo";

# async fn dox() -> Result<(), Box<dyn std::error::Error>> {
// Wait for a reader to open the file.
let tx = loop {
match pipe::OpenOptions::new().open_sender(FIFO_NAME) {
Ok(tx) => break tx,
Err(e) if e.raw_os_error() == Some(libc::ENXIO) => {},
Err(e) => return Err(e.into()),
}

time::sleep(Duration::from_millis(50)).await;
};
# Ok(())
# }
```

On Linux, it is possible to create a `Sender` without waiting in a sleeping
loop. This is done by opening a named pipe in read-write access mode with
`OpenOptions::read_write`. This way, a `Sender` can at the same time hold
both a writing end and a reading end, and the latter allows to open a FIFO
without [`ENXIO`] error since the pipe is open for reading as well.

`Sender` cannot be used to read from a pipe, so in practice the read access
is only used when a FIFO is opened. However, using a `Sender` in read-write
mode **may lead to lost data**, because written data will be dropped by the
system as soon as all pipe ends are closed. To avoid lost data you have to
make sure that a reading end has been opened before dropping a `Sender`.

Note that using read-write access mode with FIFO files is not defined by
the POSIX standard and it is only guaranteed to work on Linux.

```ignore
use tokio::io::AsyncWriteExt;
use tokio::net::unix::pipe;

const FIFO_NAME: &str = "path/to/a/fifo";

# async fn dox() -> Result<(), Box<dyn std::error::Error>> {
let mut tx = pipe::OpenOptions::new()
.read_write(true)
.open_sender(FIFO_NAME)?;

// Asynchronously write to the pipe before a reader.
tx.write_all(b"hello world").await?;
# Ok(())
# }
```

[`ENXIO`]: https://docs.rs/libc/latest/libc/constant.ENXIO.html"""

    def send(self, t: T) -> None: ...

    def closed(self) -> None: ...

    def is_closed(self) -> bool: ...

    def poll_closed(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

    def clone(self) -> Self: ...

    @staticmethod
    def default() -> "Sender": ...

    @staticmethod
    def new(init: T) -> "Sender": ...

    def send(self, value: T) -> None: ...

    def send_modify(self, modify: F) -> None: ...

    def send_if_modified(self, modify: F) -> bool: ...

    def send_replace(self, value: T) -> T: ...

    def borrow(self) -> object: ...

    def is_closed(self) -> bool: ...

    def closed(self) -> None: ...

    def subscribe(self) -> object: ...

    def receiver_count(self) -> int: ...

    def sender_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def drop(self) -> None: ...

    def send(self, value: T) -> None: ...

    def closed(self) -> None: ...

    def try_send(self, message: T) -> None: ...

    def send_timeout(self, value: T, timeout: Duration) -> None: ...

    def blocking_send(self, value: T) -> None: ...

    def is_closed(self) -> bool: ...

    def reserve(self) -> object: ...

    def reserve_many(self, n: int) -> object: ...

    def reserve_owned(self) -> object: ...

    def try_reserve(self) -> object: ...

    def try_reserve_many(self, n: int) -> object: ...

    def try_reserve_owned(self) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def capacity(self) -> int: ...

    def downgrade(self) -> object: ...

    def max_capacity(self) -> int: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new(capacity: int) -> "Sender": ...

    def send(self, value: T) -> int: ...

    def subscribe(self) -> object: ...

    def downgrade(self) -> object: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def receiver_count(self) -> int: ...

    def same_channel(self, other: Self) -> bool: ...

    def closed(self) -> None: ...

    def strong_count(self) -> int: ...

    def weak_count(self) -> int: ...

    def clone(self) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Sender": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Sender": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Sender": ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def poll_write_ready(self, cx: Context) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class Receiver:
    """Reading end of a Unix pipe.

It can be constructed from a FIFO file with [`OpenOptions::open_receiver`].

# Examples

Receiving messages from a named pipe in a loop:

```no_run
use tokio::net::unix::pipe;
use tokio::io::{self, AsyncReadExt};

const FIFO_NAME: &str = "path/to/a/fifo";

# async fn dox() -> Result<(), Box<dyn std::error::Error>> {
let mut rx = pipe::OpenOptions::new().open_receiver(FIFO_NAME)?;
loop {
let mut msg = vec![0; 256];
match rx.read_exact(&mut msg).await {
Ok(_) => {
/* handle the message */
}
Err(e) if e.kind() == io::ErrorKind::UnexpectedEof => {
// Writing end has been closed, we should reopen the pipe.
rx = pipe::OpenOptions::new().open_receiver(FIFO_NAME)?;
}
Err(e) => return Err(e.into()),
}
}
# }
```

On Linux, you can use a `Receiver` in read-write access mode to implement
resilient reading from a named pipe. Unlike `Receiver` opened in read-only
mode, read from a pipe in read-write mode will not fail with `UnexpectedEof`
when the writing end is closed. This way, a `Receiver` can asynchronously
wait for the next writer to open the pipe.

You should not use functions waiting for EOF such as [`read_to_end`] with
a `Receiver` in read-write access mode, since it **may wait forever**.
`Receiver` in this mode also holds an open writing end, which prevents
receiving EOF.

To set the read-write access mode you can use `OpenOptions::read_write`.
Note that using read-write access mode with FIFO files is not defined by
the POSIX standard and it is only guaranteed to work on Linux.

```ignore
use tokio::net::unix::pipe;
use tokio::io::AsyncReadExt;
# use std::error::Error;

const FIFO_NAME: &str = "path/to/a/fifo";

# async fn dox() -> Result<(), Box<dyn Error>> {
let mut rx = pipe::OpenOptions::new()
.read_write(true)
.open_receiver(FIFO_NAME)?;
loop {
let mut msg = vec![0; 256];
rx.read_exact(&mut msg).await?;
/* handle the message */
}
# }
```

[`read_to_end`]: crate::io::AsyncReadExt::read_to_end"""

    def close(self) -> None: ...

    def is_terminated(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def poll(self, cx: Context) -> object: ...

    def borrow(self) -> object: ...

    def borrow_and_update(self) -> object: ...

    def has_changed(self) -> bool: ...

    def mark_changed(self) -> None: ...

    def mark_unchanged(self) -> None: ...

    def changed(self) -> None: ...

    def wait_for(self, f: object) -> object: ...

    def same_channel(self, other: Self) -> bool: ...

    def clone(self) -> Self: ...

    def drop(self) -> None: ...

    def recv(self) -> T | None: ...

    def recv_many(self, buffer: list[T], limit: int) -> int: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T | None: ...

    def blocking_recv_many(self, buffer: list[T], limit: int) -> int: ...

    def close(self) -> None: ...

    def is_closed(self) -> bool: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    def capacity(self) -> int: ...

    def max_capacity(self) -> int: ...

    def poll_recv(self, cx: Context) -> object: ...

    def poll_recv_many(self, cx: Context, buffer: list[T], limit: int) -> object: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def same_channel(self, other: Self) -> bool: ...

    def sender_strong_count(self) -> int: ...

    def sender_weak_count(self) -> int: ...

    def is_closed(self) -> bool: ...

    def resubscribe(self) -> Self: ...

    def recv(self) -> T: ...

    def try_recv(self) -> T: ...

    def blocking_recv(self) -> T: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_file(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd(owned_fd: OwnedFd) -> "Receiver": ...

    @staticmethod
    def from_file_unchecked(file: File) -> "Receiver": ...

    @staticmethod
    def from_owned_fd_unchecked(owned_fd: OwnedFd) -> "Receiver": ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def poll_read_ready(self, cx: Context) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def into_blocking_fd(self) -> OwnedFd: ...

    def into_nonblocking_fd(self) -> OwnedFd: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

class ReadHalf:
    """Borrowed read half of a [`TcpStream`], created by [`split`].

Reading from a `ReadHalf` is usually done using the convenience methods found on the
[`AsyncReadExt`] trait.

[`TcpStream`]: TcpStream
[`split`]: TcpStream::split()
[`AsyncReadExt`]: trait@crate::io::AsyncReadExt"""

    def is_pair_of(self, other: object) -> bool: ...

    def unsplit(self, wr: object) -> T: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def poll_peek(self, cx: Context, buf: ReadBuf) -> object: ...

    def peek(self, buf: object) -> int: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> TcpStream: ...

class WriteHalf:
    """Borrowed write half of a [`TcpStream`], created by [`split`].

Note that in the [`AsyncWrite`] implementation of this type, [`poll_shutdown`] will
shut down the TCP stream in the write direction.

Writing to an `WriteHalf` is usually done using the convenience methods found
on the [`AsyncWriteExt`] trait.

[`TcpStream`]: TcpStream
[`split`]: TcpStream::split()
[`AsyncWrite`]: trait@crate::io::AsyncWrite
[`poll_shutdown`]: fn@crate::io::AsyncWrite::poll_shutdown
[`AsyncWriteExt`]: trait@crate::io::AsyncWriteExt"""

    def is_pair_of(self, other: object) -> bool: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_flush(self, cx: Context) -> object: ...

    def poll_shutdown(self, cx: Context) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> TcpStream: ...

class OwnedReadHalf:
    """Owned read half of a [`TcpStream`], created by [`into_split`].

Reading from an `OwnedReadHalf` is usually done using the convenience methods found
on the [`AsyncReadExt`] trait.

[`TcpStream`]: TcpStream
[`into_split`]: TcpStream::into_split()
[`AsyncReadExt`]: trait@crate::io::AsyncReadExt"""

    def reunite(self, other: OwnedWriteHalf) -> UnixStream: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def reunite(self, other: OwnedWriteHalf) -> TcpStream: ...

    def poll_peek(self, cx: Context, buf: ReadBuf) -> object: ...

    def peek(self, buf: object) -> int: ...

    def ready(self, interest: Interest) -> Ready: ...

    def readable(self) -> object: ...

    def try_read(self, buf: object) -> int: ...

    def try_read_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def as_ref(self) -> TcpStream: ...

class OwnedWriteHalf:
    """Owned write half of a [`TcpStream`], created by [`into_split`].

Note that in the [`AsyncWrite`] implementation of this type, [`poll_shutdown`] will
shut down the TCP stream in the write direction.  Dropping the write half
will also shut down the write half of the TCP stream.

Writing to an `OwnedWriteHalf` is usually done using the convenience methods found
on the [`AsyncWriteExt`] trait.

[`TcpStream`]: TcpStream
[`into_split`]: TcpStream::into_split()
[`AsyncWrite`]: trait@crate::io::AsyncWrite
[`poll_shutdown`]: fn@crate::io::AsyncWrite::poll_shutdown
[`AsyncWriteExt`]: trait@crate::io::AsyncWriteExt"""

    def reunite(self, other: OwnedReadHalf) -> UnixStream: ...

    def forget(self) -> None: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, buf: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def drop(self) -> None: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> UnixStream: ...

    def reunite(self, other: OwnedReadHalf) -> TcpStream: ...

    def forget(self) -> None: ...

    def ready(self, interest: Interest) -> Ready: ...

    def writable(self) -> object: ...

    def try_write(self, buf: object) -> int: ...

    def try_write_vectored(self, bufs: object) -> int: ...

    def peer_addr(self) -> SocketAddr: ...

    def local_addr(self) -> SocketAddr: ...

    def drop(self) -> None: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, _: Context) -> object: ...

    def poll_shutdown(self, _: Context) -> object: ...

    def as_ref(self) -> TcpStream: ...

class ReuniteError:
    """Error indicating that two halves were not from the same socket, and thus could
not be reunited."""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class Internal:
    pass

class Command:
    """This structure mimics the API of [`std::process::Command`] found in the standard library, but
replaces functions that create a process with an asynchronous variant. The main provided
asynchronous functions are [spawn](Command::spawn), [status](Command::status), and
[output](Command::output).

`Command` uses asynchronous versions of some `std` types (for example [`Child`]).

[`std::process::Command`]: std::process::Command
[`Child`]: struct@Child"""

    @staticmethod
    def new(program: S) -> "Command": ...

    def as_std(self) -> StdCommand: ...

    def as_std_mut(self) -> StdCommand: ...

    def into_std(self) -> StdCommand: ...

    def arg(self, arg: S) -> Command: ...

    def args(self, args: I) -> Command: ...

    def env(self, key: K, val: V) -> Command: ...

    def envs(self, vars: I) -> Command: ...

    def env_remove(self, key: K) -> Command: ...

    def env_clear(self) -> Command: ...

    def current_dir(self, dir: P) -> Command: ...

    def stdin(self, cfg: T) -> Command: ...

    def stdout(self, cfg: T) -> Command: ...

    def stderr(self, cfg: T) -> Command: ...

    def kill_on_drop(self, kill_on_drop: bool) -> Command: ...

    def uid(self, id: int) -> Command: ...

    def gid(self, id: int) -> Command: ...

    def arg0(self, arg: S) -> Command: ...

    def pre_exec(self, f: F) -> Command: ...

    def process_group(self, pgroup: int) -> Command: ...

    def spawn(self) -> Child: ...

    def spawn_with(self, with_: object) -> Child: ...

    def status(self) -> object: ...

    def output(self) -> object: ...

    def get_kill_on_drop(self) -> bool: ...

    @staticmethod
    def from_(std: StdCommand) -> "Command": ...

class Child:
    """Representation of a child process spawned onto an event loop.

# Caveats
Similar to the behavior to the standard library, and unlike the futures
paradigm of dropping-implies-cancellation, a spawned process will, by
default, continue to execute even after the `Child` handle has been dropped.

The `Command::kill_on_drop` method can be used to modify this behavior
and kill the child process if the `Child` wrapper is dropped before it
has exited."""

    def fmt(self, fmt: Formatter) -> Result: ...

    def kill(self) -> object: ...

    def poll(self, cx: Context) -> object: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def kill(self) -> object: ...

    def poll(self, cx: Context) -> object: ...

    def as_raw_handle(self) -> RawHandle: ...

    def id(self) -> int | None: ...

    def start_kill(self) -> object: ...

    def kill(self) -> object: ...

    def wait(self) -> ExitStatus: ...

    def try_wait(self) -> ExitStatus | None: ...

    def wait_with_output(self) -> Output: ...

class ChildStdin:
    """The standard input stream for spawned children.

This type implements the `AsyncWrite` trait to pass data to the stdin
handle of a child process asynchronously."""

    @staticmethod
    def from_std(inner: ChildStdin) -> object: ...

    def poll_write(self, cx: Context, buf: object) -> object: ...

    def poll_flush(self, cx: Context) -> object: ...

    def poll_shutdown(self, cx: Context) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def try_into(self) -> Stdio: ...

class ChildStdout:
    """The standard output stream for spawned children.

This type implements the `AsyncRead` trait to read data from the stdout
handle of a child process asynchronously."""

    @staticmethod
    def from_std(inner: ChildStdout) -> object: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def try_into(self) -> Stdio: ...

class ChildStderr:
    """The standard error stream for spawned children.

This type implements the `AsyncRead` trait to read data from the stderr
handle of a child process asynchronously."""

    @staticmethod
    def from_std(inner: ChildStderr) -> object: ...

    def poll_read(self, cx: Context, buf: ReadBuf) -> object: ...

    def try_into(self) -> Stdio: ...

class SelectNormal:
    """Marker type indicating that the starting branch should
rotate each poll."""
    pass

class SelectBiased:
    """Marker type indicating that the starting branch should
be the first declared branch each poll."""
    pass

class Rotator:
    """Rotates by one each [`Self::num_skip`] call up to COUNT - 1."""

    def num_skip(self) -> int: ...

class BiasedRotator:
    """[`Self::num_skip`] always returns 0."""

    def num_skip(self) -> int: ...

class SignalKind:
    """Represents the specific kind of signal to listen for."""

    @staticmethod
    def from_raw(signum: c_int) -> "SignalKind": ...

    def as_raw_value(self) -> c_int: ...

    @staticmethod
    def alarm() -> "SignalKind": ...

    @staticmethod
    def child() -> "SignalKind": ...

    @staticmethod
    def hangup() -> "SignalKind": ...

    @staticmethod
    def info() -> "SignalKind": ...

    @staticmethod
    def interrupt() -> "SignalKind": ...

    @staticmethod
    def io() -> "SignalKind": ...

    @staticmethod
    def io() -> "SignalKind": ...

    @staticmethod
    def pipe() -> "SignalKind": ...

    @staticmethod
    def quit() -> "SignalKind": ...

    @staticmethod
    def terminate() -> "SignalKind": ...

    @staticmethod
    def user_defined1() -> "SignalKind": ...

    @staticmethod
    def user_defined2() -> "SignalKind": ...

    @staticmethod
    def window_change() -> "SignalKind": ...

    @staticmethod
    def from_(signum: c_int) -> "SignalKind": ...

class Signal:
    """An listener for receiving a particular type of OS signal.

The listener can be turned into a `Stream` using [`SignalStream`].

[`SignalStream`]: https://docs.rs/tokio-stream/latest/tokio_stream/wrappers/struct.SignalStream.html

In general signal handling on Unix is a pretty tricky topic, and this
structure is no exception! There are some important limitations to keep in
mind when using `Signal` streams:

* Signals handling in Unix already necessitates coalescing signals
together sometimes. This `Signal` stream is also no exception here in
that it will also coalesce signals. That is, even if the signal handler
for this process runs multiple times, the `Signal` stream may only return
one signal notification. Specifically, before `poll` is called, all
signal notifications are coalesced into one item returned from `poll`.
Once `poll` has been called, however, a further signal is guaranteed to
be yielded as an item.

Put another way, any element pulled off the returned listener corresponds to
*at least one* signal, but possibly more.

* Signal handling in general is relatively inefficient. Although some
improvements are possible in this crate, it's recommended to not plan on
having millions of signal channels open.

If you've got any questions about this feel free to open an issue on the
repo! New approaches to alleviate some of these limitations are always
appreciated!

# Caveats

The first time that a `Signal` instance is registered for a particular
signal kind, an OS signal-handler is installed which replaces the default
platform behavior when that signal is received, **for the duration of the
entire process**.

For example, Unix systems will terminate a process by default when it
receives `SIGINT`. But, when a `Signal` instance is created to listen for
this signal, the next `SIGINT` that arrives will be translated to a stream
event, and the process will continue to execute. **Even if this `Signal`
instance is dropped, subsequent `SIGINT` deliveries will end up captured by
Tokio, and the default platform behavior will NOT be reset**.

Thus, applications should take care to ensure the expected signal behavior
occurs as expected after listening for specific signals.

# Examples

Wait for `SIGHUP`

```rust,no_run
use tokio::signal::unix::{signal, SignalKind};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
// An infinite stream of hangup signals.
let mut sig = signal(SignalKind::hangup())?;

// Print whenever a HUP signal is received
loop {
sig.recv().await;
println!("got signal HUP");
}
}
```"""

    def recv(self) -> object: ...

    def poll_recv(self, cx: Context) -> object: ...

    def poll_recv(self, cx: Context) -> object: ...

class CtrlC:
    """Represents a listener which receives "ctrl-c" notifications sent to the process
via `SetConsoleCtrlHandler`.

This event can be turned into a `Stream` using [`CtrlCStream`].

[`CtrlCStream`]: https://docs.rs/tokio-stream/latest/tokio_stream/wrappers/struct.CtrlCStream.html

A notification to this process notifies *all* receivers for
this event. Moreover, the notifications **are coalesced** if they aren't processed
quickly enough. This means that if two notifications are received back-to-back,
then the listener may only receive one item about the two notifications."""

    def recv(self) -> object: ...

    def poll_recv(self, cx: Context) -> object: ...

class CtrlBreak:
    """Represents a listener which receives "ctrl-break" notifications sent to the process
via `SetConsoleCtrlHandler`.

This listener can be turned into a `Stream` using [`CtrlBreakStream`].

[`CtrlBreakStream`]: https://docs.rs/tokio-stream/latest/tokio_stream/wrappers/struct.CtrlBreakStream.html

A notification to this process notifies *all* receivers for
this event. Moreover, the notifications **are coalesced** if they aren't processed
quickly enough. This means that if two notifications are received back-to-back,
then the listener may only receive one item about the two notifications."""

    def recv(self) -> object: ...

    def poll_recv(self, cx: Context) -> object: ...

class CtrlClose:
    """Represents a listener which receives "ctrl-close" notifications sent to the process
via `SetConsoleCtrlHandler`.

A notification to this process notifies *all* listeners listening for
this event. Moreover, the notifications **are coalesced** if they aren't processed
quickly enough. This means that if two notifications are received back-to-back,
then the listener may only receive one item about the two notifications."""

    def recv(self) -> object: ...

    def poll_recv(self, cx: Context) -> object: ...

class CtrlShutdown:
    """Represents a listener which receives "ctrl-shutdown" notifications sent to the process
via `SetConsoleCtrlHandler`.

A notification to this process notifies *all* listeners listening for
this event. Moreover, the notifications **are coalesced** if they aren't processed
quickly enough. This means that if two notifications are received back-to-back,
then the listener may only receive one item about the two notifications."""

    def recv(self) -> object: ...

    def poll_recv(self, cx: Context) -> object: ...

class CtrlLogoff:
    """Represents a listener which receives "ctrl-logoff" notifications sent to the process
via `SetConsoleCtrlHandler`.

A notification to this process notifies *all* listeners listening for
this event. Moreover, the notifications **are coalesced** if they aren't processed
quickly enough. This means that if two notifications are received back-to-back,
then the listener may only receive one item about the two notifications."""

    def recv(self) -> object: ...

    def poll_recv(self, cx: Context) -> object: ...

class Handle:
    """Handle to the runtime.

The handle is internally reference-counted and can be freely cloned. A handle can be
obtained using the [`Runtime::handle`] method.

[`Runtime::handle`]: crate::runtime::Runtime::handle()"""

    def enter(self) -> EnterGuard: ...

    @staticmethod
    def current() -> "Handle": ...

    @staticmethod
    def try_current() -> object: ...

    def spawn(self, future: F) -> object: ...

    def spawn_blocking(self, func: F) -> object: ...

    def block_on(self, future: F) -> Output: ...

    def runtime_flavor(self) -> RuntimeFlavor: ...

    def id(self) -> Id: ...

    def metrics(self) -> RuntimeMetrics: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def wake(arc_self: object) -> None: ...

    @staticmethod
    def wake_by_ref(arc_self: object) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def push(self, task: object) -> None: ...

    def push_batch(self, iter: I) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

class EnterGuard:
    """Runtime context guard.

Returned by [`Runtime::enter`] and [`Handle::enter`], the context guard exits
the runtime context on drop.

[`Runtime::enter`]: fn@crate::runtime::Runtime::enter"""
    pass

class TryCurrentError:
    """Error returned by `try_current` when no Runtime has been started"""

    def is_missing_context(self) -> bool: ...

    def is_thread_local_destroyed(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class Runtime:
    """The Tokio runtime.

The runtime provides an I/O driver, task scheduler, [timer], and
blocking pool, necessary for running asynchronous tasks.

Instances of `Runtime` can be created using [`new`], or [`Builder`].
However, most users will use the [`#[tokio::main]`][main] annotation on
their entry point instead.

See [module level][mod] documentation for more details.

# Shutdown

Shutting down the runtime is done by dropping the value, or calling
[`shutdown_background`] or [`shutdown_timeout`].

Tasks spawned through [`Runtime::spawn`] keep running until they yield.
Then they are dropped. They are not *guaranteed* to run to completion, but
*might* do so if they do not yield until completion.

Blocking functions spawned through [`Runtime::spawn_blocking`] keep running
until they return.

The thread initiating the shutdown blocks until all spawned work has been
stopped. This can take an indefinite amount of time. The `Drop`
implementation waits forever for this.

The [`shutdown_background`] and [`shutdown_timeout`] methods can be used if
waiting forever is undesired. When the timeout is reached, spawned work that
did not stop in time and threads running it are leaked. The work continues
to run until one of the stopping conditions is fulfilled, but the thread
initiating the shutdown is unblocked.

Once the runtime has been dropped, any outstanding I/O resources bound to
it will no longer function. Calling any method on them will result in an
error.

# Sharing

There are several ways to establish shared access to a Tokio runtime:

* Using an <code>[Arc]\\<Runtime></code>.
* Using a [`Handle`].
* Entering the runtime context.

Using an <code>[Arc]\\<Runtime></code> or [`Handle`] allows you to do various
things with the runtime such as spawning new tasks or entering the runtime
context. Both types can be cloned to create a new handle that allows access
to the same runtime. By passing clones into different tasks or threads, you
will be able to access the runtime from those tasks or threads.

The difference between <code>[Arc]\\<Runtime></code> and [`Handle`] is that
an <code>[Arc]\\<Runtime></code> will prevent the runtime from shutting down,
whereas a [`Handle`] does not prevent that. This is because shutdown of the
runtime happens when the destructor of the `Runtime` object runs.

Calls to [`shutdown_background`] and [`shutdown_timeout`] require exclusive
ownership of the `Runtime` type. When using an <code>[Arc]\\<Runtime></code>,
this can be achieved via [`Arc::try_unwrap`] when only one strong count
reference is left over.

The runtime context is entered using the [`Runtime::enter`] or
[`Handle::enter`] methods, which use a thread-local variable to store the
current runtime. Whenever you are inside the runtime context, methods such
as [`tokio::spawn`] will use the runtime whose context you are inside.

[timer]: crate::time
[mod]: index.html
[`new`]: method@Self::new
[`Builder`]: struct@Builder
[`Handle`]: struct@Handle
[main]: macro@crate::main
[`tokio::spawn`]: crate::spawn
[`Arc::try_unwrap`]: std::sync::Arc::try_unwrap
[Arc]: std::sync::Arc
[`shutdown_background`]: method@Runtime::shutdown_background
[`shutdown_timeout`]: method@Runtime::shutdown_timeout"""

    def release(self, task: object) -> object: ...

    def schedule(self, task: object) -> None: ...

    def hooks(self) -> TaskHarnessScheduleHooks: ...

    @staticmethod
    def new() -> "Runtime": ...

    def handle(self) -> Handle: ...

    def spawn(self, future: F) -> object: ...

    def spawn_blocking(self, func: F) -> object: ...

    def block_on(self, future: F) -> Output: ...

    def enter(self) -> EnterGuard: ...

    def shutdown_timeout(self, duration: Duration) -> None: ...

    def shutdown_background(self) -> None: ...

    def metrics(self) -> RuntimeMetrics: ...

    def drop(self) -> None: ...

class LocalOptions:
    """[`LocalRuntime`]-only config options

Currently, there are no such options, but in the future, things like `!Send + !Sync` hooks may
be added.

Use `LocalOptions::default()` to create the default set of options. This type is used with
[`Builder::build_local`].

[`Builder::build_local`]: crate::runtime::Builder::build_local
[`LocalRuntime`]: crate::runtime::LocalRuntime"""
    pass

class LocalRuntime:
    """A local Tokio runtime.

This runtime is capable of driving tasks which are not `Send + Sync` without the use of a
`LocalSet`, and thus supports `spawn_local` without the need for a `LocalSet` context.

This runtime cannot be moved between threads or driven from different threads.

This runtime is incompatible with `LocalSet`. You should not attempt to drive a `LocalSet` within a
`LocalRuntime`.

Currently, this runtime supports one flavor, which is internally identical to `current_thread`,
save for the aforementioned differences related to `spawn_local`.

For more general information on how to use runtimes, see the [module] docs.

[runtime]: crate::runtime::Runtime
[module]: crate::runtime"""

    @staticmethod
    def new() -> "LocalRuntime": ...

    def handle(self) -> Handle: ...

    def spawn_local(self, future: F) -> object: ...

    def spawn_blocking(self, func: F) -> object: ...

    def block_on(self, future: F) -> Output: ...

    def enter(self) -> EnterGuard: ...

    def shutdown_timeout(self, duration: Duration) -> None: ...

    def shutdown_background(self) -> None: ...

    def metrics(self) -> RuntimeMetrics: ...

    def drop(self) -> None: ...

class Dump:
    """A snapshot of a runtime's state.

See [`Handle::dump`][crate::runtime::Handle::dump]."""

    def tasks(self) -> Tasks: ...

class Tasks:
    """Snapshots of tasks.

See [`Handle::dump`][crate::runtime::Handle::dump]."""

    def iter(self) -> object: ...

class Task:
    """A snapshot of a task.

See [`Handle::dump`][crate::runtime::Handle::dump]."""

    def id(self) -> Id: ...

    def trace(self) -> Trace: ...

    def drop(self) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def as_raw(handle: object) -> object: ...

    @staticmethod
    def from_raw(ptr: object) -> object: ...

    @staticmethod
    def pointers(target: object) -> object: ...

    @staticmethod
    def get_shard_id(target: object) -> int: ...

class BacktraceSymbol:
    """A backtrace symbol.

This struct provides accessors for backtrace symbols, similar to [`backtrace::BacktraceSymbol`]."""

    def name_raw(self) -> object: ...

    def name_demangled(self) -> object: ...

    def addr(self) -> object | None: ...

    def filename(self) -> object: ...

    def lineno(self) -> int | None: ...

    def colno(self) -> int | None: ...

class BacktraceFrame:
    """A backtrace frame.

This struct represents one stack frame in a captured backtrace, similar to [`backtrace::BacktraceFrame`]."""

    def ip(self) -> object: ...

    def symbol_address(self) -> object: ...

    def symbols(self) -> object: ...

class Backtrace:
    """A captured backtrace.

This struct provides access to each backtrace frame, similar to [`backtrace::Backtrace`]."""

    def frames(self) -> object: ...

class Trace:
    """An execution trace of a task's last poll.

<div class="warning">

Resolving a backtrace, either via the [`Display`][std::fmt::Display] impl or via
[`resolve_backtraces`][Trace::resolve_backtraces], parses debuginfo, which is
possibly a CPU-expensive operation that can take a platform-specific but
long time to run - often over 100 milliseconds, especially if the current
process's binary is big. In some cases, the platform might internally cache some of the
debuginfo, so successive calls to `resolve_backtraces` might be faster than
the first call, but all guarantees are platform-dependent.

To avoid blocking the runtime, it is recommended
that you resolve backtraces inside of a [`spawn_blocking()`][crate::task::spawn_blocking]
and to have some concurrency-limiting mechanism to avoid unexpected performance impact.
</div>

See [`Handle::dump`][crate::runtime::Handle::dump]."""

    def poll(self, cx: Context) -> object: ...

    def resolve_backtraces(self) -> list[Backtrace]: ...

    @staticmethod
    def capture(f: F) -> object: ...

    @staticmethod
    def root(f: F) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class RuntimeMetrics:
    """Handle to the runtime's metrics.

This handle is internally reference-counted and can be freely cloned. A
`RuntimeMetrics` handle is obtained using the [`Runtime::metrics`] method.

[`Runtime::metrics`]: crate::runtime::Runtime::metrics()"""

    def num_workers(self) -> int: ...

    def num_alive_tasks(self) -> int: ...

    def global_queue_depth(self) -> int: ...

class LogHistogram:
    """Log Histogram

This implements an [H2 Histogram](https://iop.systems/blog/h2-histogram/), a histogram similar
to HdrHistogram, but with better performance. It guarantees an error bound of `2^-p`.

Unlike a traditional H2 histogram this has two small changes:
1. The 0th bucket runs for `0..min_value`. This allows truncating a large number of buckets that
would cover extremely short timescales that customers usually don't care about.
2. The final bucket runs all the way to `u64::MAX` — traditional H2 histograms would truncate
or reject these values.

For information about the default configuration, see [`LogHistogramBuilder`]."""

    @staticmethod
    def default() -> "LogHistogram": ...

    @staticmethod
    def builder() -> LogHistogramBuilder: ...

    def max_value(self) -> int: ...

    @staticmethod
    def from_(value: LogHistogramBuilder) -> "LogHistogram": ...

class LogHistogramBuilder:
    """Configuration for a [`LogHistogram`]

The log-scaled histogram implements an H2 histogram where the first bucket covers
the range from 0 to [`LogHistogramBuilder::min_value`] and the final bucket covers
[`LogHistogramBuilder::max_value`] to infinity. The precision is bounded to the specified
[`LogHistogramBuilder::max_error`]. Specifically, the precision is the next smallest value
of `2^-p` such that it is smaller than the requested max error. You can also select `p` directly
with [`LogHistogramBuilder::precision_exact`].

Depending on the selected parameters, the number of buckets required is variable. To ensure
that the histogram size is acceptable, callers may call [`LogHistogramBuilder::max_buckets`].
If the resulting histogram would require more buckets, then the method will return an error.

## Default values
The default configuration provides the following settings:
1. `min_value`: 100ns
2. `max_value`: 68 seconds. The final bucket covers all values >68 seconds
3. `precision`: max error of 25%

This uses 237 64-bit buckets."""

    def max_error(self, max_error: float) -> Self: ...

    def precision_exact(self, p: int) -> Self: ...

    def min_value(self, duration: Duration) -> Self: ...

    def max_value(self, duration: Duration) -> Self: ...

    def max_buckets(self, max_buckets: int) -> LogHistogram: ...

    def build(self) -> LogHistogram: ...

class Builder:
    """Builds Tokio Runtime with custom configuration values.

Methods can be chained in order to set the configuration values. The
Runtime is constructed by calling [`build`].

New instances of `Builder` are obtained via [`Builder::new_multi_thread`]
or [`Builder::new_current_thread`].

See function level documentation for details on the various configuration
settings.

[`build`]: method@Self::build
[`Builder::new_multi_thread`]: method@Self::new_multi_thread
[`Builder::new_current_thread`]: method@Self::new_current_thread

# Examples

```
# #[cfg(not(target_family = "wasm"))]
# {
use tokio::runtime::Builder;

fn main() {
// build runtime
let runtime = Builder::new_multi_thread()
.worker_threads(4)
.thread_name("my-custom-name")
.thread_stack_size(3 * 1024 * 1024)
.build()
.unwrap();

// use runtime ...
}
# }
```"""

    @staticmethod
    def new_current_thread() -> "Builder": ...

    @staticmethod
    def new_multi_thread() -> "Builder": ...

    def enable_all(self) -> Self: ...

    def enable_alt_timer(self) -> Self: ...

    def worker_threads(self, val: int) -> Self: ...

    def max_blocking_threads(self, val: int) -> Self: ...

    def thread_name(self, val: object) -> Self: ...

    def thread_name_fn(self, f: F) -> Self: ...

    def thread_stack_size(self, val: int) -> Self: ...

    def on_thread_start(self, f: F) -> Self: ...

    def on_thread_stop(self, f: F) -> Self: ...

    def on_thread_park(self, f: F) -> Self: ...

    def on_thread_unpark(self, f: F) -> Self: ...

    def on_task_spawn(self, f: F) -> Self: ...

    def on_before_task_poll(self, f: F) -> Self: ...

    def on_after_task_poll(self, f: F) -> Self: ...

    def on_task_terminate(self, f: F) -> Self: ...

    def build(self) -> Runtime: ...

    def build_local(self, options: LocalOptions) -> LocalRuntime: ...

    def thread_keep_alive(self, duration: Duration) -> Self: ...

    def global_queue_interval(self, val: int) -> Self: ...

    def event_interval(self, val: int) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new() -> "Builder": ...

    def name(self, name: object) -> Self: ...

    def spawn(self, future: Fut) -> object: ...

    def spawn_on(self, future: Fut, handle: Handle) -> object: ...

    def spawn_local(self, future: Fut) -> object: ...

    def spawn_local_on(self, future: Fut, local_set: LocalSet) -> object: ...

    def spawn_blocking(self, function: Function) -> object: ...

    def spawn_blocking_on(self, function: Function, handle: Handle) -> object: ...

    def name(self, name: object) -> Self: ...

    def spawn(self, future: F) -> AbortHandle: ...

    def spawn_on(self, future: F, handle: Handle) -> AbortHandle: ...

    def spawn_blocking(self, f: F) -> AbortHandle: ...

    def spawn_blocking_on(self, f: F, handle: Handle) -> AbortHandle: ...

    def spawn_local(self, future: F) -> AbortHandle: ...

    def spawn_local_on(self, future: F, local_set: LocalSet) -> AbortHandle: ...

    def fmt(self, f: Formatter) -> Result: ...

class Id:
    """An opaque ID that uniquely identifies a runtime relative to all other currently
running runtimes.

# Notes

- Runtime IDs are unique relative to other *currently running* runtimes.
When a runtime completes, the same ID may be used for another runtime.
- Runtime IDs are *not* sequential, and do not indicate the order in which
runtimes are started or any other data.
- The runtime ID of the currently running task can be obtained from the
Handle.

# Examples

```
# #[cfg(not(target_family = "wasm"))]
# {
use tokio::runtime::Handle;

#[tokio::main(flavor = "multi_thread", worker_threads = 4)]
async fn main() {
println!("Current runtime id: {}", Handle::current().id());
}
# }
```"""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class AbortHandle:
    """An owned permission to abort a spawned task, without awaiting its completion.

Unlike a [`JoinHandle`], an `AbortHandle` does *not* represent the
permission to await the task's completion, only to terminate it.

The task may be aborted by calling the [`AbortHandle::abort`] method.
Dropping an `AbortHandle` releases the permission to terminate the task
--- it does *not* abort the task.

Be aware that tasks spawned using [`spawn_blocking`] cannot be aborted
because they are not async. If you call `abort` on a `spawn_blocking` task,
then this *will not have any effect*, and the task will continue running
normally. The exception is if the task has not started running yet; in that
case, calling `abort` may prevent the task from starting.

[`JoinHandle`]: crate::task::JoinHandle
[`spawn_blocking`]: crate::task::spawn_blocking"""

    def abort(self) -> None: ...

    def is_finished(self) -> bool: ...

    def id(self) -> Id: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def drop(self) -> None: ...

    def clone(self) -> Self: ...

class Id:
    """An opaque ID that uniquely identifies a task relative to all other currently
running tasks.

A task's ID may be re-used for another task only once *both* of the
following happen:
1. The task itself exits.
2. There is no active [`JoinHandle`] associated with this task.

A [`JoinHandle`] is considered active in the following situations:
- You are explicitly holding a [`JoinHandle`], [`AbortHandle`], or
`tokio_util::task::AbortOnDropHandle`.
- The task is being tracked by a [`JoinSet`] or `tokio_util::task::JoinMap`.

# Notes

- Task IDs are *not* sequential, and do not indicate the order in which
tasks are spawned, what runtime a task is spawned on, or any other data.
- The task ID of the currently running task can be obtained from inside the
task via the [`task::try_id()`](crate::task::try_id()) and
[`task::id()`](crate::task::id()) functions and from outside the task via
the [`JoinHandle::id()`](crate::task::JoinHandle::id()) function.

[`JoinHandle`]: crate::task::JoinHandle
[`AbortHandle`]: crate::task::AbortHandle
[`JoinSet`]: crate::task::JoinSet"""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class TaskMeta:
    """Task metadata supplied to user-provided hooks for task events.

**Note**: This is an [unstable API][unstable]. The public API of this type
may break in 1.x releases. See [the documentation on unstable
features][unstable] for details.

[unstable]: crate#unstable-features"""

    def id(self) -> Id: ...

    def spawned_at(self) -> Location: ...

class ReadDir:
    """Reads the entries in a directory.

This struct is returned from the [`read_dir`] function of this module and
will yield instances of [`DirEntry`]. Through a [`DirEntry`] information
like the entry's path and possibly other metadata can be learned.

A `ReadDir` can be turned into a `Stream` with [`ReadDirStream`].

[`ReadDirStream`]: https://docs.rs/tokio-stream/0.1/tokio_stream/wrappers/struct.ReadDirStream.html

# Errors

This stream will return an [`Err`] if there's some sort of intermittent
IO error during iteration.

[`read_dir`]: read_dir
[`DirEntry`]: DirEntry
[`Err`]: std::result::Result::Err"""

    def next_entry(self) -> DirEntry | None: ...

    def poll_next_entry(self, cx: Context) -> object: ...

class DirEntry:
    """Entries returned by the [`ReadDir`] stream.

[`ReadDir`]: struct@ReadDir

This is a specialized version of [`std::fs::DirEntry`] for usage from the
Tokio runtime.

An instance of `DirEntry` represents an entry inside of a directory on the
filesystem. Each entry can be inspected via methods to learn about the full
path or possibly other metadata through per-platform extension traits."""

    def path(self) -> PathBuf: ...

    def file_name(self) -> OsString: ...

    def metadata(self) -> Metadata: ...

    def file_type(self) -> FileType: ...

class OpenOptions:
    """Options and flags which can be used to configure how a file is opened.

This builder exposes the ability to configure how a [`File`] is opened and
what operations are permitted on the open file. The [`File::open`] and
[`File::create`] methods are aliases for commonly used options using this
builder.

Generally speaking, when using `OpenOptions`, you'll first call [`new`],
then chain calls to methods to set each option, then call [`open`], passing
the path of the file you're trying to open. This will give you a
[`io::Result`] with a [`File`] inside that you can further operate
on.

This is a specialized version of [`std::fs::OpenOptions`] for usage from
the Tokio runtime.

`From<std::fs::OpenOptions>` is implemented for more advanced configuration
than the methods provided here.

[`new`]: OpenOptions::new
[`open`]: OpenOptions::open
[`File`]: File
[`File::open`]: File::open
[`File::create`]: File::create

# Examples

Opening a file to read:

```no_run
use tokio::fs::OpenOptions;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
let file = OpenOptions::new()
.read(true)
.open("foo.txt")
.await?;

Ok(())
}
```

Opening a file for both reading and writing, as well as creating it if it
doesn't exist:

```no_run
use tokio::fs::OpenOptions;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
let file = OpenOptions::new()
.read(true)
.write(true)
.create(true)
.open("foo.txt")
.await?;

Ok(())
}
```"""

    @staticmethod
    def new() -> "OpenOptions": ...

    def read_write(self, value: bool) -> Self: ...

    def unchecked(self, value: bool) -> Self: ...

    def open_receiver(self, path: P) -> Receiver: ...

    def open_sender(self, path: P) -> Sender: ...

    @staticmethod
    def default() -> "OpenOptions": ...

    @staticmethod
    def new() -> "OpenOptions": ...

    def read(self, read: bool) -> OpenOptions: ...

    def write(self, write: bool) -> OpenOptions: ...

    def append(self, append: bool) -> OpenOptions: ...

    def truncate(self, truncate: bool) -> OpenOptions: ...

    def create(self, create: bool) -> OpenOptions: ...

    def create_new(self, create_new: bool) -> OpenOptions: ...

    def open(self, path: object) -> File: ...

    @staticmethod
    def from_(options: StdOpenOptions) -> "OpenOptions": ...

    @staticmethod
    def default() -> "OpenOptions": ...

class File:
    """A reference to an open file on the filesystem.

This is a specialized version of [`std::fs::File`] for usage from the
Tokio runtime.

An instance of a `File` can be read and/or written depending on what options
it was opened with. Files also implement [`AsyncSeek`] to alter the logical
cursor that the file contains internally.

A file will not be closed immediately when it goes out of scope if there
are any IO operations that have not yet completed. To ensure that a file is
closed immediately when it is dropped, you should call [`flush`] before
dropping it. Note that this does not ensure that the file has been fully
written to disk; the operating system might keep the changes around in an
in-memory buffer. See the [`sync_all`] method for telling the OS to write
the data to disk.

Reading and writing to a `File` is usually done using the convenience
methods found on the [`AsyncReadExt`] and [`AsyncWriteExt`] traits.

[`AsyncSeek`]: trait@crate::io::AsyncSeek
[`flush`]: fn@crate::io::AsyncWriteExt::flush
[`sync_all`]: fn@crate::fs::File::sync_all
[`AsyncReadExt`]: trait@crate::io::AsyncReadExt
[`AsyncWriteExt`]: trait@crate::io::AsyncWriteExt

# Examples

Create a new file and asynchronously write bytes to it:

```no_run
use tokio::fs::File;
use tokio::io::AsyncWriteExt; // for write_all()

# async fn dox() -> std::io::Result<()> {
let mut file = File::create("foo.txt").await?;
file.write_all(b"hello, world!").await?;
# Ok(())
# }
```

Read the contents of a file into a buffer:

```no_run
use tokio::fs::File;
use tokio::io::AsyncReadExt; // for read_to_end()

# async fn dox() -> std::io::Result<()> {
let mut file = File::open("foo.txt").await?;

let mut contents = vec![];
file.read_to_end(&mut contents).await?;

println!("len = {}", contents.len());
# Ok(())
# }
```"""

    @staticmethod
    def open(path: object) -> "File": ...

    @staticmethod
    def create(path: object) -> "File": ...

    @staticmethod
    def create_new(path: P) -> "File": ...

    @staticmethod
    def options() -> OpenOptions: ...

    @staticmethod
    def from_std(std: StdFile) -> "File": ...

    def sync_all(self) -> object: ...

    def sync_data(self) -> object: ...

    def set_len(self, size: int) -> object: ...

    def metadata(self) -> Metadata: ...

    def try_clone(self) -> File: ...

    def into_std(self) -> StdFile: ...

    def try_into_std(self) -> StdFile: ...

    def set_permissions(self, perm: Permissions) -> object: ...

    def set_max_buf_size(self, max_buf_size: int) -> None: ...

    def max_buf_size(self) -> int: ...

    def poll_read(self, cx: Context, dst: ReadBuf) -> object: ...

    def start_seek(self, pos: SeekFrom) -> object: ...

    def poll_complete(self, cx: Context) -> object: ...

    def poll_write(self, cx: Context, src: object) -> object: ...

    def poll_write_vectored(self, cx: Context, bufs: object) -> object: ...

    def is_write_vectored(self) -> bool: ...

    def poll_flush(self, cx: Context) -> object: ...

    def poll_shutdown(self, cx: Context) -> object: ...

    @staticmethod
    def from_(std: StdFile) -> "File": ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def as_raw_fd(self) -> RawFd: ...

    def as_fd(self) -> BorrowedFd: ...

    @staticmethod
    def from_raw_fd(fd: RawFd) -> "File": ...

class DirBuilder:
    """A builder for creating directories in various manners.

This is a specialized version of [`std::fs::DirBuilder`] for usage on
the Tokio runtime."""

    @staticmethod
    def new() -> "DirBuilder": ...

    def recursive(self, recursive: bool) -> Self: ...

    def create(self, path: object) -> object: ...

class Instant:
    """A measurement of a monotonically nondecreasing clock.
Opaque and useful only with `Duration`.

Instants are always guaranteed to be no less than any previously measured
instant when created, and are often useful for tasks such as measuring
benchmarks or timing how long an operation takes.

Note, however, that instants are not guaranteed to be **steady**. In other
words, each tick of the underlying clock may not be the same length (e.g.
some seconds may be longer than others). An instant may jump forwards or
experience time dilation (slow down or speed up), but it will never go
backwards.

Instants are opaque types that can only be compared to one another. There is
no method to get "the number of seconds" from an instant. Instead, it only
allows measuring the duration between two instants (or comparing two
instants).

The size of an `Instant` struct may vary depending on the target operating
system.

# Note

This type wraps the inner `std` variant and is used to align the Tokio
clock for uses of `now()`. This can be useful for testing where you can
take advantage of `time::pause()` and `time::advance()`."""

    @staticmethod
    def now() -> "Instant": ...

    @staticmethod
    def from_std(std: Instant) -> "Instant": ...

    def into_std(self) -> Instant: ...

    def duration_since(self, earlier: Instant) -> Duration: ...

    def checked_duration_since(self, earlier: Instant) -> Duration | None: ...

    def saturating_duration_since(self, earlier: Instant) -> Duration: ...

    def elapsed(self) -> Duration: ...

    def checked_add(self, duration: Duration) -> Instant | None: ...

    def checked_sub(self, duration: Duration) -> Instant | None: ...

    @staticmethod
    def from_(time: Instant) -> "Instant": ...

    @staticmethod
    def from_(time: Instant) -> "Instant": ...

    def add(self, other: Duration) -> Instant: ...

    def add_assign(self, rhs: Duration) -> None: ...

    def sub(self, rhs: Instant) -> Duration: ...

    def sub(self, rhs: Duration) -> Instant: ...

    def sub_assign(self, rhs: Duration) -> None: ...

    def fmt(self, fmt: Formatter) -> Result: ...

class Interval:
    """Interval returned by [`interval`] and [`interval_at`].

This type allows you to wait on a sequence of instants with a certain
duration between each instant. Unlike calling [`sleep`] in a loop, this lets
you count the time spent between the calls to [`sleep`] as well.

An `Interval` can be turned into a `Stream` with [`IntervalStream`].

[`IntervalStream`]: https://docs.rs/tokio-stream/latest/tokio_stream/wrappers/struct.IntervalStream.html
[`sleep`]: crate::time::sleep()"""

    def tick(self) -> Instant: ...

    def poll_tick(self, cx: Context) -> object: ...

    def reset(self) -> None: ...

    def reset_immediately(self) -> None: ...

    def reset_after(self, after: Duration) -> None: ...

    def reset_at(self, deadline: Instant) -> None: ...

    def missed_tick_behavior(self) -> MissedTickBehavior: ...

    def set_missed_tick_behavior(self, behavior: MissedTickBehavior) -> None: ...

    def period(self) -> Duration: ...

class Error:
    """Errors encountered by the timer implementation.

Currently, there are two different errors that can occur:

* `shutdown` occurs when a timer operation is attempted, but the timer
instance has been dropped. In this case, the operation will never be able
to complete and the `shutdown` error is returned. This is a permanent
error, i.e., once this error is observed, timer operations will never
succeed in the future.

* `at_capacity` occurs when a timer operation is attempted, but the timer
instance is currently handling its maximum number of outstanding sleep instances.
In this case, the operation is not able to be performed at the current
moment, and `at_capacity` is returned. This is a transient error, i.e., at
some point in the future, if the operation is attempted again, it might
succeed. Callers that observe this error should attempt to [shed load]. One
way to do this would be dropping the future that issued the timer operation.

[shed load]: https://en.wikipedia.org/wiki/Load_Shedding"""

    @staticmethod
    def from_(value: object) -> "Error": ...

    @staticmethod
    def from_(src: JoinError) -> Exception: ...

    @staticmethod
    def from_(e: SpawnError) -> "Error": ...

    @staticmethod
    def from_(k: Kind) -> "Error": ...

    @staticmethod
    def shutdown() -> Exception: ...

    def is_shutdown(self) -> bool: ...

    @staticmethod
    def at_capacity() -> Exception: ...

    def is_at_capacity(self) -> bool: ...

    @staticmethod
    def invalid() -> Exception: ...

    def is_invalid(self) -> bool: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_(_err: Elapsed) -> Exception: ...

class Elapsed:
    """Errors returned by `Timeout`.

This error is returned when a timeout expires before the function was able
to finish."""

    def fmt(self, fmt: Formatter) -> Result: ...

class LocalEnterGuard:
    """Context guard for `LocalSet`"""

    def drop(self) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

class Builder:
    """Factory which is used to configure the properties of a new task.

**Note**: This is an [unstable API][unstable]. The public API of this type
may break in 1.x releases. See [the documentation on unstable
features][unstable] for details.

Methods can be chained in order to configure it.

Currently, there is only one configuration option:

- [`name`], which specifies an associated name for
the task

There are three types of task that can be spawned from a Builder:
- [`spawn_local`] for executing futures on the current thread
- [`spawn`] for executing [`Send`] futures on the runtime
- [`spawn_blocking`] for executing blocking code in the
blocking thread pool.

## Example

```no_run
use tokio::net::{TcpListener, TcpStream};

use std::io;

async fn process(socket: TcpStream) {
// ...
# drop(socket);
}

#[tokio::main]
async fn main() -> io::Result<()> {
let listener = TcpListener::bind("127.0.0.1:8080").await?;

loop {
let (socket, _) = listener.accept().await?;

tokio::task::Builder::new()
.name("tcp connection handler")
.spawn(async move {
// Process each socket concurrently.
process(socket).await
})?;
}
}
```
[unstable]: crate#unstable-features
[`name`]: Builder::name
[`spawn_local`]: Builder::spawn_local
[`spawn`]: Builder::spawn
[`spawn_blocking`]: Builder::spawn_blocking"""

    @staticmethod
    def new_current_thread() -> "Builder": ...

    @staticmethod
    def new_multi_thread() -> "Builder": ...

    def enable_all(self) -> Self: ...

    def enable_alt_timer(self) -> Self: ...

    def worker_threads(self, val: int) -> Self: ...

    def max_blocking_threads(self, val: int) -> Self: ...

    def thread_name(self, val: object) -> Self: ...

    def thread_name_fn(self, f: F) -> Self: ...

    def thread_stack_size(self, val: int) -> Self: ...

    def on_thread_start(self, f: F) -> Self: ...

    def on_thread_stop(self, f: F) -> Self: ...

    def on_thread_park(self, f: F) -> Self: ...

    def on_thread_unpark(self, f: F) -> Self: ...

    def on_task_spawn(self, f: F) -> Self: ...

    def on_before_task_poll(self, f: F) -> Self: ...

    def on_after_task_poll(self, f: F) -> Self: ...

    def on_task_terminate(self, f: F) -> Self: ...

    def build(self) -> Runtime: ...

    def build_local(self, options: LocalOptions) -> LocalRuntime: ...

    def thread_keep_alive(self, duration: Duration) -> Self: ...

    def global_queue_interval(self, val: int) -> Self: ...

    def event_interval(self, val: int) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new() -> "Builder": ...

    def name(self, name: object) -> Self: ...

    def spawn(self, future: Fut) -> object: ...

    def spawn_on(self, future: Fut, handle: Handle) -> object: ...

    def spawn_local(self, future: Fut) -> object: ...

    def spawn_local_on(self, future: Fut, local_set: LocalSet) -> object: ...

    def spawn_blocking(self, function: Function) -> object: ...

    def spawn_blocking_on(self, function: Function, handle: Handle) -> object: ...

    def name(self, name: object) -> Self: ...

    def spawn(self, future: F) -> AbortHandle: ...

    def spawn_on(self, future: F, handle: Handle) -> AbortHandle: ...

    def spawn_blocking(self, f: F) -> AbortHandle: ...

    def spawn_blocking_on(self, f: F, handle: Handle) -> AbortHandle: ...

    def spawn_local(self, future: F) -> AbortHandle: ...

    def spawn_local_on(self, future: F, local_set: LocalSet) -> AbortHandle: ...

    def fmt(self, f: Formatter) -> Result: ...

class JoinSet:
    """A collection of tasks spawned on a Tokio runtime.

A `JoinSet` can be used to await the completion of some or all of the tasks
in the set. The set is not ordered, and the tasks will be returned in the
order they complete.

All of the tasks must have the same return type `T`.

When the `JoinSet` is dropped, all tasks in the `JoinSet` are immediately aborted.

# Examples

Spawn multiple tasks and wait for them.

```
use tokio::task::JoinSet;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let mut set = JoinSet::new();

for i in 0..10 {
set.spawn(async move { i });
}

let mut seen = [false; 10];
while let Some(res) = set.join_next().await {
let idx = res.unwrap();
seen[idx] = true;
}

for i in 0..10 {
assert!(seen[i]);
}
# }
```

# Task ID guarantees

While a task is tracked in a `JoinSet`, that task's ID is unique relative
to all other running tasks in Tokio. For this purpose, tracking a task in a
`JoinSet` is equivalent to holding a [`JoinHandle`] to it. See the [task ID]
documentation for more info.

[`JoinHandle`]: crate::task::JoinHandle
[task ID]: crate::task::Id"""

    @staticmethod
    def new() -> "JoinSet": ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def build_task(self) -> object: ...

    def spawn(self, task: F) -> AbortHandle: ...

    def spawn_on(self, task: F, handle: Handle) -> AbortHandle: ...

    def spawn_local(self, task: F) -> AbortHandle: ...

    def spawn_local_on(self, task: F, local_set: LocalSet) -> AbortHandle: ...

    def spawn_blocking(self, f: F) -> AbortHandle: ...

    def spawn_blocking_on(self, f: F, handle: Handle) -> AbortHandle: ...

    def join_next(self) -> T | None: ...

    def join_next_with_id(self) -> object | None: ...

    def try_join_next(self) -> T | None: ...

    def try_join_next_with_id(self) -> object | None: ...

    def shutdown(self) -> None: ...

    def join_all(self) -> list[T]: ...

    def abort_all(self) -> None: ...

    def detach_all(self) -> None: ...

    def poll_join_next(self, cx: Context) -> object: ...

    def poll_join_next_with_id(self, cx: Context) -> object: ...

    def drop(self) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def default() -> "JoinSet": ...

    @staticmethod
    def from_iter(iter: I) -> "JoinSet": ...

    def extend(self, iter: I) -> None: ...

class Builder:
    """A variant of [`task::Builder`] that spawns tasks on a [`JoinSet`] rather
than on the current default runtime.

[`task::Builder`]: crate::task::Builder"""

    @staticmethod
    def new_current_thread() -> "Builder": ...

    @staticmethod
    def new_multi_thread() -> "Builder": ...

    def enable_all(self) -> Self: ...

    def enable_alt_timer(self) -> Self: ...

    def worker_threads(self, val: int) -> Self: ...

    def max_blocking_threads(self, val: int) -> Self: ...

    def thread_name(self, val: object) -> Self: ...

    def thread_name_fn(self, f: F) -> Self: ...

    def thread_stack_size(self, val: int) -> Self: ...

    def on_thread_start(self, f: F) -> Self: ...

    def on_thread_stop(self, f: F) -> Self: ...

    def on_thread_park(self, f: F) -> Self: ...

    def on_thread_unpark(self, f: F) -> Self: ...

    def on_task_spawn(self, f: F) -> Self: ...

    def on_before_task_poll(self, f: F) -> Self: ...

    def on_after_task_poll(self, f: F) -> Self: ...

    def on_task_terminate(self, f: F) -> Self: ...

    def build(self) -> Runtime: ...

    def build_local(self, options: LocalOptions) -> LocalRuntime: ...

    def thread_keep_alive(self, duration: Duration) -> Self: ...

    def global_queue_interval(self, val: int) -> Self: ...

    def event_interval(self, val: int) -> Self: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def new() -> "Builder": ...

    def name(self, name: object) -> Self: ...

    def spawn(self, future: Fut) -> object: ...

    def spawn_on(self, future: Fut, handle: Handle) -> object: ...

    def spawn_local(self, future: Fut) -> object: ...

    def spawn_local_on(self, future: Fut, local_set: LocalSet) -> object: ...

    def spawn_blocking(self, function: Function) -> object: ...

    def spawn_blocking_on(self, function: Function, handle: Handle) -> object: ...

    def name(self, name: object) -> Self: ...

    def spawn(self, future: F) -> AbortHandle: ...

    def spawn_on(self, future: F, handle: Handle) -> AbortHandle: ...

    def spawn_blocking(self, f: F) -> AbortHandle: ...

    def spawn_blocking_on(self, f: F, handle: Handle) -> AbortHandle: ...

    def spawn_local(self, future: F) -> AbortHandle: ...

    def spawn_local_on(self, future: F, local_set: LocalSet) -> AbortHandle: ...

    def fmt(self, f: Formatter) -> Result: ...

class LocalKey:
    """A key for task-local data.

This type is generated by the [`task_local!`] macro.

Unlike [`std::thread::LocalKey`], `tokio::task::LocalKey` will
_not_ lazily initialize the value on first access. Instead, the
value is first initialized when the future containing
the task-local is first polled by a futures executor, like Tokio.

# Examples

```
# async fn dox() {
tokio::task_local! {
static NUMBER: u32;
}

NUMBER.scope(1, async move {
assert_eq!(NUMBER.get(), 1);
}).await;

NUMBER.scope(2, async move {
assert_eq!(NUMBER.get(), 2);

NUMBER.scope(3, async move {
assert_eq!(NUMBER.get(), 3);
}).await;
}).await;
# }
```

[`std::thread::LocalKey`]: struct@std::thread::LocalKey
[`task_local!`]: ../macro.task_local.html"""

    def scope(self, value: T, f: F) -> object: ...

    def sync_scope(self, value: T, f: F) -> R: ...

    def with_(self, f: F) -> R: ...

    def try_with(self, f: F) -> R: ...

    def get(self) -> T: ...

    def try_get(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

class AccessError:
    """An error returned by [`LocalKey::try_with`](method@LocalKey::try_with)."""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class TryRecvError:
    """Error returned by the `try_recv` function on `Receiver`."""
    Empty: "TryRecvError"
    Closed: "TryRecvError"

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class TrySendError:
    """Error returned by [`Sender::try_send`](super::Sender::try_send)."""
    Full: "TrySendError"
    Closed: "TrySendError"

    def into_inner(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_(src: object) -> object: ...

class TryRecvError:
    """Error returned by [`Receiver::try_recv`](super::Receiver::try_recv)."""
    Empty: "TryRecvError"
    Disconnected: "TryRecvError"

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class RecvError:
    """An error returned from the [`recv`] function on a [`Receiver`].

[`recv`]: crate::sync::broadcast::Receiver::recv
[`Receiver`]: crate::sync::broadcast::Receiver"""
    Closed: "RecvError"
    Lagged: "RecvError"

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class TryRecvError:
    """An error returned from the [`try_recv`] function on a [`Receiver`].

[`try_recv`]: crate::sync::broadcast::Receiver::try_recv
[`Receiver`]: crate::sync::broadcast::Receiver"""
    Empty: "TryRecvError"
    Closed: "TryRecvError"
    Lagged: "TryRecvError"

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class TryAcquireError:
    """Error returned from the [`Semaphore::try_acquire`] function.

[`Semaphore::try_acquire`]: crate::sync::Semaphore::try_acquire"""
    Closed: "TryAcquireError"
    NoPermits: "TryAcquireError"

    def fmt(self, fmt: Formatter) -> Result: ...

class SetError:
    """Errors that can be returned from [`OnceCell::set`].

[`OnceCell::set`]: crate::sync::OnceCell::set"""
    AlreadyInitializedError: "SetError"
    InitializingError: "SetError"

    def fmt(self, f: Formatter) -> Result: ...

    def is_already_init_err(self) -> bool: ...

    def is_initializing_err(self) -> bool: ...

class NotDefinedHere:
    """The name of a type which is not defined here.

This is typically used as an alias for another type, like so:

```rust,ignore
/// See [some::other::location](https://example.com).
type DEFINED_ELSEWHERE = crate::doc::NotDefinedHere;
```

This type is uninhabitable like the [`never` type] to ensure that no one
will ever accidentally use it.

[`never` type]: https://doc.rust-lang.org/std/primitive.never.html"""

    def register(self, _registry: Registry, _token: Token, _interests: Interest) -> object: ...

    def reregister(self, _registry: Registry, _token: Token, _interests: Interest) -> object: ...

    def deregister(self, _registry: Registry) -> object: ...

class PipeMode:
    """The pipe mode of a named pipe.

Set through [`ServerOptions::pipe_mode`]."""
    Byte: "PipeMode"
    Message: "PipeMode"

class PipeEnd:
    """Indicates the end of a named pipe."""
    Client: "PipeEnd"
    Server: "PipeEnd"

class RuntimeFlavor:
    """The flavor of a `Runtime`.

This is the return type for [`Handle::runtime_flavor`](crate::runtime::Handle::runtime_flavor())."""
    CurrentThread: "RuntimeFlavor"
    MultiThread: "RuntimeFlavor"

class InvalidHistogramConfiguration:
    """Error constructing a histogram"""
    TooManyBuckets: "InvalidHistogramConfiguration"

    def fmt(self, f: Formatter) -> Result: ...

class MissedTickBehavior:
    """Defines the behavior of an [`Interval`] when it misses a tick.

Sometimes, an [`Interval`]'s tick is missed. For example, consider the
following:

```
use tokio::time::{self, Duration};
# async fn task_that_takes_one_to_three_millis() {}

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
// ticks every 2 milliseconds
let mut interval = time::interval(Duration::from_millis(2));
for _ in 0..5 {
interval.tick().await;
// if this takes more than 2 milliseconds, a tick will be delayed
task_that_takes_one_to_three_millis().await;
}
# }
```

Generally, a tick is missed if too much time is spent without calling
[`Interval::tick()`].

By default, when a tick is missed, [`Interval`] fires ticks as quickly as it
can until it is "caught up" in time to where it should be.
`MissedTickBehavior` can be used to specify a different behavior for
[`Interval`] to exhibit. Each variant represents a different strategy.

Note that because the executor cannot guarantee exact precision with timers,
these strategies will only apply when the delay is greater than 5
milliseconds."""
    Burst: "MissedTickBehavior"
    Delay: "MissedTickBehavior"
    Skip: "MissedTickBehavior"

    @staticmethod
    def default() -> "MissedTickBehavior": ...

"""Create a new pair of `DuplexStream`s that act like a pair of connected sockets.

The `max_buf_size` argument is the maximum amount of bytes that can be
written to a side before the write returns `Poll::Pending`."""
def duplex(max_buf_size: int) -> object: ...

"""Creates unidirectional buffer that acts like in memory pipe.

The `max_buf_size` argument is the maximum amount of bytes that can be
written to a buffer before the it returns `Poll::Pending`.

# Unify reader and writer

The reader and writer half can be unified into a single structure
of `SimplexStream` that supports both reading and writing or
the `SimplexStream` can be already created as unified structure
using [`SimplexStream::new_unsplit()`].

```
# async fn ex() -> std::io::Result<()> {
# use tokio::io::{AsyncReadExt, AsyncWriteExt};
let (reader, writer) = tokio::io::simplex(64);
let mut simplex_stream = reader.unsplit(writer);
simplex_stream.write_all(b"hello").await?;

let mut buf = [0u8; 5];
simplex_stream.read_exact(&mut buf).await?;
assert_eq!(&buf, b"hello");
# Ok(())
# }
```"""
def simplex(max_buf_size: int) -> object: ...

"""Copies data in both directions between `a` and `b`.

This function returns a future that will read from both streams,
writing any data read to the opposing stream.
This happens in both directions concurrently.

If an EOF is observed on one stream, [`shutdown()`] will be invoked on
the other, and reading from that stream will stop. Copying of data in
the other direction will continue.

The future will complete successfully once both directions of communication has been shut down.
A direction is shut down when the reader reports EOF,
at which point [`shutdown()`] is called on the corresponding writer. When finished,
it will return a tuple of the number of bytes copied from a to b
and the number of bytes copied from b to a, in that order.

It uses two 8 KB buffers for transferring bytes between `a` and `b` by default.
To set your own buffers sizes use [`copy_bidirectional_with_sizes()`].

[`shutdown()`]: crate::io::AsyncWriteExt::shutdown

# Errors

The future will immediately return an error if any IO operation on `a`
or `b` returns an error. Some data read from either stream may be lost (not
written to the other stream) in this case.

# Return value

Returns a tuple of bytes copied `a` to `b` and bytes copied `b` to `a`."""
async def copy_bidirectional(a: A, b: B) -> object: ...

"""Copies data in both directions between `a` and `b` using buffers of the specified size.

This method is the same as the [`copy_bidirectional()`], except that it allows you to set the
size of the internal buffers used when copying data."""
async def copy_bidirectional_with_sizes(a: A, b: B, a_to_b_buf_size: int, b_to_a_buf_size: int) -> object: ...

"""Join two values implementing `AsyncRead` and `AsyncWrite` into a
single handle."""
def join(reader: R, writer: W) -> object: ...

"""This is a fuzz test. You run it by entering `cargo fuzz run fuzz_linked_list` in CLI in `/tokio/` module."""
def fuzz_linked_list(ops: object) -> None: ...

"""Creates a new one-shot channel for sending single values across asynchronous
tasks.

The function returns separate "send" and "receive" handles. The `Sender`
handle is used by the producer to send the value. The `Receiver` handle is
used by the consumer to receive the value.

Each handle can be used on separate tasks.

# Examples

```
use tokio::sync::oneshot;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, rx) = oneshot::channel();

tokio::spawn(async move {
if let Err(_) = tx.send(3) {
println!("the receiver dropped");
}
});

match rx.await {
Ok(v) => println!("got = {:?}", v),
Err(_) => println!("the sender dropped"),
}
# }
```"""
def channel() -> object: ...

"""Creates a new watch channel, returning the "send" and "receive" handles.

All values sent by [`Sender`] will become visible to the [`Receiver`] handles.
Only the last value sent is made available to the [`Receiver`] half. All
intermediate values are dropped.

# Examples

The following example prints `hello! world! `.

```
use tokio::sync::watch;
use tokio::time::{Duration, sleep};

# async fn dox() -> Result<(), Box<dyn std::error::Error>> {
let (tx, mut rx) = watch::channel("hello");

tokio::spawn(async move {
// Use the equivalent of a "do-while" loop so the initial value is
// processed before awaiting the `changed()` future.
loop {
println!("{}! ", *rx.borrow_and_update());
if rx.changed().await.is_err() {
break;
}
}
});

sleep(Duration::from_millis(100)).await;
tx.send("world")?;
# Ok(())
# }
```

[`Sender`]: struct@Sender
[`Receiver`]: struct@Receiver"""
def channel(init: T) -> object: ...

"""Creates a bounded mpsc channel for communicating between asynchronous tasks
with backpressure.

The channel will buffer up to the provided number of messages.  Once the
buffer is full, attempts to send new messages will wait until a message is
received from the channel. The provided buffer capacity must be at least 1.

All data sent on `Sender` will become available on `Receiver` in the same
order as it was sent.

The `Sender` can be cloned to `send` to the same channel from multiple code
locations. Only one `Receiver` is supported.

If the `Receiver` is disconnected while trying to `send`, the `send` method
will return a `SendError`. Similarly, if `Sender` is disconnected while
trying to `recv`, the `recv` method will return `None`.

# Panics

Panics if the buffer capacity is 0, or too large. Currently the maximum
capacity is [`Semaphore::MAX_PERMITS`].

[`Semaphore::MAX_PERMITS`]: crate::sync::Semaphore::MAX_PERMITS

# Examples

```rust
use tokio::sync::mpsc;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, mut rx) = mpsc::channel(100);

tokio::spawn(async move {
for i in 0..10 {
if let Err(_) = tx.send(i).await {
println!("receiver dropped");
return;
}
}
});

while let Some(i) = rx.recv().await {
println!("got = {}", i);
}
# }
```"""
def channel(buffer: int) -> object: ...

"""Creates an unbounded mpsc channel for communicating between asynchronous
tasks without backpressure.

A `send` on this channel will always succeed as long as the receive half has
not been closed. If the receiver falls behind, messages will be arbitrarily
buffered.

**Note** that the amount of available system memory is an implicit bound to
the channel. Using an `unbounded` channel has the ability of causing the
process to run out of memory. In this case, the process will be aborted."""
def unbounded_channel() -> object: ...

"""Create a bounded, multi-producer, multi-consumer channel where each sent
value is broadcasted to all active receivers.

**Note:** The actual capacity may be greater than the provided `capacity`.

All data sent on [`Sender`] will become available on every active
[`Receiver`] in the same order as it was sent.

The `Sender` can be cloned to `send` to the same channel from multiple
points in the process or it can be used concurrently from an `Arc`. New
`Receiver` handles are created by calling [`Sender::subscribe`].

If all [`Receiver`] handles are dropped, the `send` method will return a
[`SendError`]. Similarly, if all [`Sender`] handles are dropped, the [`recv`]
method will return a [`RecvError`].

[`Sender`]: crate::sync::broadcast::Sender
[`Sender::subscribe`]: crate::sync::broadcast::Sender::subscribe
[`Receiver`]: crate::sync::broadcast::Receiver
[`recv`]: crate::sync::broadcast::Receiver::recv
[`SendError`]: crate::sync::broadcast::error::SendError
[`RecvError`]: crate::sync::broadcast::error::RecvError

# Examples

```
use tokio::sync::broadcast;

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let (tx, mut rx1) = broadcast::channel(16);
let mut rx2 = tx.subscribe();

tokio::spawn(async move {
assert_eq!(rx1.recv().await.unwrap(), 10);
assert_eq!(rx1.recv().await.unwrap(), 20);
});

tokio::spawn(async move {
assert_eq!(rx2.recv().await.unwrap(), 10);
assert_eq!(rx2.recv().await.unwrap(), 20);
});

tx.send(10).unwrap();
tx.send(20).unwrap();
# }
```

# Panics

This will panic if `capacity` is equal to `0`.

This pre-allocates space for `capacity` messages. Allocation failure may result in a panic or
[an allocation error](std::alloc::handle_alloc_error)."""
def channel(capacity: int) -> object: ...

"""Creates a new anonymous Unix pipe.

This function will open a new pipe and associate both pipe ends with the default
event loop.

If you need to create a pipe for communication with a spawned process, you can
use [`Stdio::piped()`] instead.

[`Stdio::piped()`]: std::process::Stdio::piped

# Errors

If creating a pipe fails, this function will return with the related OS error.

# Examples

Create a pipe and pass the writing end to a spawned process.

```no_run
use tokio::net::unix::pipe;
use tokio::process::Command;
# use tokio::io::AsyncReadExt;
# use std::error::Error;

# async fn dox() -> Result<(), Box<dyn Error>> {
let (tx, mut rx) = pipe::pipe()?;
let mut buffer = String::new();

let status = Command::new("echo")
.arg("Hello, world!")
.stdout(tx.into_blocking_fd()?)
.status();
rx.read_to_string(&mut buffer).await?;

assert!(status.await?.success());
assert_eq!(buffer, "Hello, world!\\n");
# Ok(())
# }
```

# Panics

This function panics if it is not called from within a runtime with
IO enabled.

The runtime is usually set implicitly when this function is called
from a future driven by a tokio runtime, otherwise runtime can be set
explicitly with [`Runtime::enter`](crate::runtime::Runtime::enter) function."""
def pipe() -> object: ...

"""Wraps a future into a `MaybeDone`."""
def maybe_done(future: F) -> object: ...

"""Creates a new listener which will receive notifications when the current
process receives the specified signal `kind`.

This function will create a new stream which binds to the default reactor.
The `Signal` stream is an infinite stream which will receive
notifications whenever a signal is received. More documentation can be
found on `Signal` itself, but to reiterate:

* Signals may be coalesced beyond what the kernel already does.
* Once a signal handler is registered with the process the underlying
libc signal handler is never unregistered.

A `Signal` stream can be created for a particular signal number
multiple times. When a signal is received then all the associated
channels will receive the signal notification.

# Errors

* If the lower-level C functions fail for some reason.
* If the previous initialization of this specific signal failed.
* If the signal is one of
[`signal_hook::FORBIDDEN`](fn@signal_hook_registry::register#panics)

# Panics

This function panics if there is no current reactor set, or if the `rt`
feature flag is not enabled."""
def signal(kind: SignalKind) -> Signal: ...

"""Completes when a "ctrl-c" notification is sent to the process.

While signals are handled very differently between Unix and Windows, both
platforms support receiving a signal on "ctrl-c". This function provides a
portable API for receiving this notification.

Once the returned future is polled, a listener is registered. The future
will complete on the first received `ctrl-c` **after** the initial call to
either `Future::poll` or `.await`.

# Caveats

On Unix platforms, the first time that a `Signal` instance is registered for a
particular signal kind, an OS signal-handler is installed which replaces the
default platform behavior when that signal is received, **for the duration of
the entire process**.

For example, Unix systems will terminate a process by default when it
receives a signal generated by `"CTRL+C"` on the terminal. But, when a
`ctrl_c` stream is created to listen for this signal, the time it arrives,
it will be translated to a stream event, and the process will continue to
execute.  **Even if this `Signal` instance is dropped, subsequent `SIGINT`
deliveries will end up captured by Tokio, and the default platform behavior
will NOT be reset**.

Thus, applications should take care to ensure the expected signal behavior
occurs as expected after listening for specific signals.

# Examples

```rust,no_run
use tokio::signal;

#[tokio::main]
async fn main() {
println!("waiting for ctrl-c");

signal::ctrl_c().await.expect("failed to listen for event");

println!("received ctrl-c event");
}
```

Listen in the background:

```rust,no_run
tokio::spawn(async move {
tokio::signal::ctrl_c().await.unwrap();
// Your handler here
});
```"""
async def ctrl_c() -> object: ...

"""Creates a new listener which receives "ctrl-c" notifications sent to the
process.

# Examples

```rust,no_run
use tokio::signal::windows::ctrl_c;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
// A listener of CTRL-C events.
let mut signal = ctrl_c()?;

// Print whenever a CTRL-C event is received.
for countdown in (0..3).rev() {
signal.recv().await;
println!("got CTRL-C. {} more to exit", countdown);
}

Ok(())
}
```"""
def ctrl_c() -> CtrlC: ...

"""Creates a new listener which receives "ctrl-break" notifications sent to the
process.

# Examples

```rust,no_run
use tokio::signal::windows::ctrl_break;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
// A listener of CTRL-BREAK events.
let mut signal = ctrl_break()?;

// Print whenever a CTRL-BREAK event is received.
loop {
signal.recv().await;
println!("got signal CTRL-BREAK");
}
}
```"""
def ctrl_break() -> CtrlBreak: ...

"""Creates a new listener which receives "ctrl-close" notifications sent to the
process.

# Examples

```rust,no_run
use tokio::signal::windows::ctrl_close;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
// A listener of CTRL-CLOSE events.
let mut signal = ctrl_close()?;

// Print whenever a CTRL-CLOSE event is received.
for countdown in (0..3).rev() {
signal.recv().await;
println!("got CTRL-CLOSE. {} more to exit", countdown);
}

Ok(())
}
```"""
def ctrl_close() -> CtrlClose: ...

"""Creates a new listener which receives "ctrl-shutdown" notifications sent to the
process.

# Examples

```rust,no_run
use tokio::signal::windows::ctrl_shutdown;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
// A listener of CTRL-SHUTDOWN events.
let mut signal = ctrl_shutdown()?;

signal.recv().await;
println!("got CTRL-SHUTDOWN. Cleaning up before exiting");

Ok(())
}
```"""
def ctrl_shutdown() -> CtrlShutdown: ...

"""Creates a new listener which receives "ctrl-logoff" notifications sent to the
process.

# Examples

```rust,no_run
use tokio::signal::windows::ctrl_logoff;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
// A listener of CTRL-LOGOFF events.
let mut signal = ctrl_logoff()?;

signal.recv().await;
println!("got CTRL-LOGOFF. Cleaning up before exiting");

Ok(())
}
```"""
def ctrl_logoff() -> CtrlLogoff: ...

"""Returns the [`Id`] of the currently running task.

# Panics

This function panics if called from outside a task. Please note that calls
to `block_on` do not have task IDs, so the method will panic if called from
within a call to `block_on`. For a version of this function that doesn't
panic, see [`task::try_id()`](crate::runtime::task::try_id()).

[task ID]: crate::task::Id"""
def id() -> Id: ...

"""Returns the [`Id`] of the currently running task, or `None` if called outside
of a task.

This function is similar to  [`task::id()`](crate::runtime::task::id()), except
that it returns `None` rather than panicking if called outside of a task
context.

[task ID]: crate::task::Id"""
def try_id() -> Id | None: ...

"""Creates a new directory symlink on the filesystem.

The `link` path will be a directory symbolic link pointing to the `original`
path.

This is an async version of [`std::os::windows::fs::symlink_dir`][std]

[std]: https://doc.rust-lang.org/std/os/windows/fs/fn.symlink_dir.html"""
async def symlink_dir(original: object, link: object) -> object: ...

"""Queries the file system metadata for a path.

This is an async version of [`std::fs::symlink_metadata`][std]

[std]: fn@std::fs::symlink_metadata"""
async def symlink_metadata(path: object) -> Metadata: ...

"""Given a path, queries the file system to get information about a file,
directory, etc.

This is an async version of [`std::fs::metadata`].

This function will traverse symbolic links to query information about the
destination file.

# Platform-specific behavior

This function currently corresponds to the `stat` function on Unix and the
`GetFileAttributesEx` function on Windows.  Note that, this [may change in
the future][changes].

[changes]: https://doc.rust-lang.org/std/io/index.html#platform-specific-behavior

# Errors

This function will return an error in the following situations, but is not
limited to just these cases:

* The user lacks permissions to perform `metadata` call on `path`.
* `path` does not exist.

# Examples

```rust,no_run
use tokio::fs;

#[tokio::main]
async fn main() -> std::io::Result<()> {
let attr = fs::metadata("/some/file/path.txt").await?;
// inspect attr ...
Ok(())
}
```"""
async def metadata(path: object) -> Metadata: ...

"""Returns a stream over the entries within a directory.

This is an async version of [`std::fs::read_dir`].

This operation is implemented by running the equivalent blocking
operation on a separate thread pool using [`spawn_blocking`].

[`spawn_blocking`]: crate::task::spawn_blocking"""
async def read_dir(path: object) -> ReadDir: ...

"""Returns the canonical, absolute form of a path with all intermediate
components normalized and symbolic links resolved.

This is an async version of [`std::fs::canonicalize`].

# Platform-specific behavior

This function currently corresponds to the `realpath` function on Unix
and the `CreateFile` and `GetFinalPathNameByHandle` functions on Windows.
Note that, this [may change in the future][changes].

On Windows, this converts the path to use [extended length path][path]
syntax, which allows your program to use longer path names, but means you
can only join backslash-delimited paths to it, and it may be incompatible
with other applications (if passed to the application on the command-line,
or written to a file another application may read).

[changes]: https://doc.rust-lang.org/std/io/index.html#platform-specific-behavior
[path]: https://msdn.microsoft.com/en-us/library/windows/desktop/aa365247(v=vs.85).aspx#maxpath

# Errors

This function will return an error in the following situations, but is not
limited to just these cases:

* `path` does not exist.
* A non-final component in path is not a directory.

# Examples

```no_run
use tokio::fs;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
let path = fs::canonicalize("../a/../foo.txt").await?;
Ok(())
}
```"""
async def canonicalize(path: object) -> PathBuf: ...

"""Removes an existing, empty directory.

This is an async version of [`std::fs::remove_dir`]."""
async def remove_dir(path: object) -> object: ...

"""Creates a future which will open a file for reading and read the entire
contents into a string and return said string.

This is the async equivalent of [`std::fs::read_to_string`][std].

This operation is implemented by running the equivalent blocking operation
on a separate thread pool using [`spawn_blocking`].

[`spawn_blocking`]: crate::task::spawn_blocking
[std]: fn@std::fs::read_to_string

# Examples

```no_run
use tokio::fs;

# async fn dox() -> std::io::Result<()> {
let contents = fs::read_to_string("foo.txt").await?;
println!("foo.txt contains {} bytes", contents.len());
# Ok(())
# }
```"""
async def read_to_string(path: object) -> str: ...

"""Creates a new symbolic link on the filesystem.

The `link` path will be a symbolic link pointing to the `original` path.

This is an async version of [`std::os::unix::fs::symlink`]."""
async def symlink(original: object, link: object) -> object: ...

"""Creates a new, empty directory at the provided path.

This is an async version of [`std::fs::create_dir`].

# Platform-specific behavior

This function currently corresponds to the `mkdir` function on Unix
and the `CreateDirectory` function on Windows.
Note that, this [may change in the future][changes].

[changes]: https://doc.rust-lang.org/std/io/index.html#platform-specific-behavior

**NOTE**: If a parent of the given path doesn't exist, this function will
return an error. To create a directory and all its missing parents at the
same time, use the [`create_dir_all`] function.

# Errors

This function will return an error in the following situations, but is not
limited to just these cases:

* User lacks permissions to create directory at `path`.
* A parent of the given path doesn't exist. (To create a directory and all
its missing parents at the same time, use the [`create_dir_all`]
function.)
* `path` already exists.

[`create_dir_all`]: super::create_dir_all()

# Examples

```no_run
use tokio::fs;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
fs::create_dir("/some/dir").await?;
Ok(())
}
```"""
async def create_dir(path: object) -> object: ...

"""Removes a file from the filesystem.

Note that there is no guarantee that the file is immediately deleted (e.g.
depending on platform, other open file descriptors may prevent immediate
removal).

This is an async version of [`std::fs::remove_file`]."""
async def remove_file(path: object) -> object: ...

"""Creates a future that will open a file for writing and write the entire
contents of `contents` to it.

This is the async equivalent of [`std::fs::write`][std].

This operation is implemented by running the equivalent blocking operation
on a separate thread pool using [`spawn_blocking`].

[`spawn_blocking`]: crate::task::spawn_blocking
[std]: fn@std::fs::write

# Examples

```no_run
use tokio::fs;

# async fn dox() -> std::io::Result<()> {
fs::write("foo.txt", b"Hello world!").await?;
# Ok(())
# }
```"""
async def write(path: object, contents: object) -> object: ...

"""Renames a file or directory to a new name, replacing the original file if
`to` already exists.

This will not work if the new name is on a different mount point.

This is an async version of [`std::fs::rename`]."""
async def rename(from_: object, to: object) -> object: ...

"""Reads the entire contents of a file into a bytes vector.

This is an async version of [`std::fs::read`].

This is a convenience function for using [`File::open`] and [`read_to_end`]
with fewer imports and without an intermediate variable. It pre-allocates a
buffer based on the file size when available, so it is generally faster than
reading into a vector created with `Vec::new()`.

This operation is implemented by running the equivalent blocking operation
on a separate thread pool using [`spawn_blocking`].

[`File::open`]: super::File::open
[`read_to_end`]: crate::io::AsyncReadExt::read_to_end
[`spawn_blocking`]: crate::task::spawn_blocking

# Errors

This function will return an error if `path` does not already exist.
Other errors may also be returned according to [`OpenOptions::open`].

[`OpenOptions::open`]: super::OpenOptions::open

It will also return an error if it encounters while reading an error
of a kind other than [`ErrorKind::Interrupted`].

[`ErrorKind::Interrupted`]: std::io::ErrorKind::Interrupted

# io_uring support

On Linux, you can also use io_uring for executing system calls. To enable
io_uring, you need to specify the `--cfg tokio_unstable` flag at compile time,
enable the io-uring cargo feature, and set the `Builder::enable_io_uring`
runtime option.

Support for io_uring is currently experimental, so its behavior may change
or it may be removed in future versions.

# Examples

```no_run
use tokio::fs;
use std::net::SocketAddr;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + 'static>> {
let contents = fs::read("address.txt").await?;
let foo: SocketAddr = String::from_utf8_lossy(&contents).parse()?;
Ok(())
}
```"""
async def read(path: object) -> list[int]: ...

"""Copies the contents of one file to another. This function will also copy the permission bits
of the original file to the destination file.
This function will overwrite the contents of to.

This is the async equivalent of [`std::fs::copy`].

# Examples

```no_run
use tokio::fs;

# async fn dox() -> std::io::Result<()> {
fs::copy("foo.txt", "bar.txt").await?;
# Ok(())
# }
```"""
async def copy(from_: object, to: object) -> int: ...

"""Reads a symbolic link, returning the file that the link points to.

This is an async version of [`std::fs::read_link`]."""
async def read_link(path: object) -> PathBuf: ...

"""Recursively creates a directory and all of its parent components if they
are missing.

This is an async version of [`std::fs::create_dir_all`].

# Platform-specific behavior

This function currently corresponds to the `mkdir` function on Unix
and the `CreateDirectory` function on Windows.
Note that, this [may change in the future][changes].

[changes]: https://doc.rust-lang.org/std/io/index.html#platform-specific-behavior

# Errors

This function will return an error in the following situations, but is not
limited to just these cases:

* If any directory in the path specified by `path` does not already exist
and it could not be created otherwise. The specific error conditions for
when a directory is being created (after it is determined to not exist) are
outlined by [`fs::create_dir`].

Notable exception is made for situations where any of the directories
specified in the `path` could not be created as it was being created concurrently.
Such cases are considered to be successful. That is, calling `create_dir_all`
concurrently from multiple threads or processes is guaranteed not to fail
due to a race condition with itself.

[`fs::create_dir`]: std::fs::create_dir

# Examples

```no_run
use tokio::fs;

#[tokio::main]
async fn main() -> std::io::Result<()> {
fs::create_dir_all("/some/dir").await?;
Ok(())
}
```"""
async def create_dir_all(path: object) -> object: ...

"""Changes the permissions found on a file or a directory.

This is an async version of [`std::fs::set_permissions`][std]

[std]: fn@std::fs::set_permissions"""
async def set_permissions(path: object, perm: Permissions) -> object: ...

"""Creates a new file symbolic link on the filesystem.

The `link` path will be a file symbolic link pointing to the `original`
path.

This is an async version of [`std::os::windows::fs::symlink_file`][std]

[std]: https://doc.rust-lang.org/std/os/windows/fs/fn.symlink_file.html"""
async def symlink_file(original: object, link: object) -> object: ...

"""Returns `Ok(true)` if the path points at an existing entity.

This function will traverse symbolic links to query information about the
destination file. In case of broken symbolic links this will return `Ok(false)`.

This is the async equivalent of [`std::path::Path::try_exists`][std].

[std]: fn@std::path::Path::try_exists

# Examples

```no_run
use tokio::fs;

# async fn dox() -> std::io::Result<()> {
fs::try_exists("foo.txt").await?;
# Ok(())
# }
```"""
async def try_exists(path: object) -> bool: ...

"""Creates a new hard link on the filesystem.

This is an async version of [`std::fs::hard_link`].

The `link` path will be a link pointing to the `original` path. Note that systems
often require these two paths to both be located on the same filesystem.

# Platform-specific behavior

This function currently corresponds to the `link` function on Unix
and the `CreateHardLink` function on Windows.
Note that, this [may change in the future][changes].

[changes]: https://doc.rust-lang.org/std/io/index.html#platform-specific-behavior

# Errors

This function will return an error in the following situations, but is not
limited to just these cases:

* The `original` path is not a file or doesn't exist.

# Examples

```no_run
use tokio::fs;

#[tokio::main]
async fn main() -> std::io::Result<()> {
fs::hard_link("a.txt", "b.txt").await?; // Hard link a.txt to b.txt
Ok(())
}
```"""
async def hard_link(original: object, link: object) -> object: ...

"""Removes a directory at this path, after removing all its contents. Use carefully!

This is an async version of [`std::fs::remove_dir_all`][std]

[std]: fn@std::fs::remove_dir_all"""
async def remove_dir_all(path: object) -> object: ...

"""Creates new [`Interval`] that yields with interval of `period`. The first
tick completes immediately. The default [`MissedTickBehavior`] is
[`Burst`](MissedTickBehavior::Burst), but this can be configured
by calling [`set_missed_tick_behavior`](Interval::set_missed_tick_behavior).

An interval will tick indefinitely. At any time, the [`Interval`] value can
be dropped. This cancels the interval.

This function is equivalent to
[`interval_at(Instant::now(), period)`](interval_at).

# Panics

This function panics if `period` is zero.

# Examples

```
use tokio::time::{self, Duration};

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let mut interval = time::interval(Duration::from_millis(10));

interval.tick().await; // ticks immediately
interval.tick().await; // ticks after 10ms
interval.tick().await; // ticks after 10ms

// approximately 20ms have elapsed.
# }
```

A simple example using `interval` to execute a task every two seconds.

The difference between `interval` and [`sleep`] is that an [`Interval`]
measures the time since the last tick, which means that [`.tick().await`]
may wait for a shorter time than the duration specified for the interval
if some time has passed between calls to [`.tick().await`].

If the tick in the example below was replaced with [`sleep`], the task
would only be executed once every three seconds, and not every two
seconds.

```
use tokio::time;

async fn task_that_takes_a_second() {
println!("hello");
time::sleep(time::Duration::from_secs(1)).await
}

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let mut interval = time::interval(time::Duration::from_secs(2));
for _i in 0..5 {
interval.tick().await;
task_that_takes_a_second().await;
}
# }
```

[`sleep`]: crate::time::sleep()
[`.tick().await`]: Interval::tick"""
def interval(period: Duration) -> Interval: ...

"""Creates new [`Interval`] that yields with interval of `period` with the
first tick completing at `start`. The default [`MissedTickBehavior`] is
[`Burst`](MissedTickBehavior::Burst), but this can be configured
by calling [`set_missed_tick_behavior`](Interval::set_missed_tick_behavior).

An interval will tick indefinitely. At any time, the [`Interval`] value can
be dropped. This cancels the interval.

# Panics

This function panics if `period` is zero.

# Examples

```
use tokio::time::{interval_at, Duration, Instant};

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
let start = Instant::now() + Duration::from_millis(50);
let mut interval = interval_at(start, Duration::from_millis(10));

interval.tick().await; // ticks after 50ms
interval.tick().await; // ticks after 10ms
interval.tick().await; // ticks after 10ms

// approximately 70ms have elapsed.
# }
```"""
def interval_at(start: Instant, period: Duration) -> Interval: ...

"""Requires a `Future` to complete before the specified duration has elapsed.

If the future completes before the duration has elapsed, then the completed
value is returned. Otherwise, an error is returned and the future is
canceled.

Note that the timeout is checked before polling the future, so if the future
does not yield during execution then it is possible for the future to complete
and exceed the timeout _without_ returning an error.

This function returns a future whose return type is [`Result`]`<T,`[`Elapsed`]`>`, where `T` is the
return type of the provided future.

If the provided future completes immediately, then the future returned from
this function is guaranteed to complete immediately with an [`Ok`] variant
no matter the provided duration.

[`Ok`]: std::result::Result::Ok
[`Result`]: std::result::Result
[`Elapsed`]: crate::time::error::Elapsed

# Cancellation

Cancelling a timeout is done by dropping the future. No additional cleanup
or other work is required.

The original future may be obtained by calling [`Timeout::into_inner`]. This
consumes the `Timeout`.

# Examples

Create a new `Timeout` set to expire in 10 milliseconds.

```rust
use tokio::time::timeout;
use tokio::sync::oneshot;

use std::time::Duration;

# async fn dox() {
let (tx, rx) = oneshot::channel();
# tx.send(()).unwrap();

// Wrap the future with a `Timeout` set to expire in 10 milliseconds.
if let Err(_) = timeout(Duration::from_millis(10), rx).await {
println!("did not receive value within 10 ms");
}
# }
```

# Panics

This function panics if there is no current timer set.

It can be triggered when [`Builder::enable_time`] or
[`Builder::enable_all`] are not included in the builder.

It can also panic whenever a timer is created outside of a
Tokio runtime. That is why `rt.block_on(sleep(...))` will panic,
since the function is executed outside of the runtime.
Whereas `rt.block_on(async {sleep(...).await})` doesn't panic.
And this is because wrapping the function on an async makes it lazy,
and so gets executed inside the runtime successfully without
panicking.

[`Builder::enable_time`]: crate::runtime::Builder::enable_time
[`Builder::enable_all`]: crate::runtime::Builder::enable_all"""
def timeout(duration: Duration, future: F) -> object: ...

"""Requires a `Future` to complete before the specified instant in time.

If the future completes before the instant is reached, then the completed
value is returned. Otherwise, an error is returned.

This function returns a future whose return type is [`Result`]`<T,`[`Elapsed`]`>`, where `T` is the
return type of the provided future.

If the provided future completes immediately, then the future returned from
this function is guaranteed to complete immediately with an [`Ok`] variant
no matter the provided deadline.

[`Ok`]: std::result::Result::Ok
[`Result`]: std::result::Result
[`Elapsed`]: crate::time::error::Elapsed

# Cancellation

Cancelling a timeout is done by dropping the future. No additional cleanup
or other work is required.

The original future may be obtained by calling [`Timeout::into_inner`]. This
consumes the `Timeout`.

# Examples

Create a new `Timeout` set to expire in 10 milliseconds.

```rust
use tokio::time::{Instant, timeout_at};
use tokio::sync::oneshot;

use std::time::Duration;

# async fn dox() {
let (tx, rx) = oneshot::channel();
# tx.send(()).unwrap();

// Wrap the future with a `Timeout` set to expire 10 milliseconds into the
// future.
if let Err(_) = timeout_at(Instant::now() + Duration::from_millis(10), rx).await {
println!("did not receive value within 10 ms");
}
# }
```"""
def timeout_at(deadline: Instant, future: F) -> object: ...

"""Waits until `deadline` is reached.

No work is performed while awaiting on the sleep future to complete. `Sleep`
operates at millisecond granularity and should not be used for tasks that
require high-resolution timers.

To run something regularly on a schedule, see [`interval`].

# Cancellation

Canceling a sleep instance is done by dropping the returned future. No additional
cleanup work is required.

# Examples

Wait 100ms and print "100 ms have elapsed".

```
use tokio::time::{sleep_until, Instant, Duration};

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
sleep_until(Instant::now() + Duration::from_millis(100)).await;
println!("100 ms have elapsed");
# }
```

See the documentation for the [`Sleep`] type for more examples.

# Panics

This function panics if there is no current timer set.

It can be triggered when [`Builder::enable_time`] or
[`Builder::enable_all`] are not included in the builder.

It can also panic whenever a timer is created outside of a
Tokio runtime. That is why `rt.block_on(sleep(...))` will panic,
since the function is executed outside of the runtime.
Whereas `rt.block_on(async {sleep(...).await})` doesn't panic.
And this is because wrapping the function on an async makes it lazy,
and so gets executed inside the runtime successfully without
panicking.

[`Sleep`]: struct@crate::time::Sleep
[`interval`]: crate::time::interval()
[`Builder::enable_time`]: crate::runtime::Builder::enable_time
[`Builder::enable_all`]: crate::runtime::Builder::enable_all"""
def sleep_until(deadline: Instant) -> Sleep: ...

"""Waits until `duration` has elapsed.

Equivalent to `sleep_until(Instant::now() + duration)`. An asynchronous
analog to `std::thread::sleep`.

No work is performed while awaiting on the sleep future to complete. `Sleep`
operates at millisecond granularity and should not be used for tasks that
require high-resolution timers. The implementation is platform specific,
and some platforms (specifically Windows) will provide timers with a
larger resolution than 1 ms.

To run something regularly on a schedule, see [`interval`].

# Cancellation

Canceling a sleep instance is done by dropping the returned future. No additional
cleanup work is required.

# Examples

Wait 100ms and print "100 ms have elapsed".

```
use tokio::time::{sleep, Duration};

# #[tokio::main(flavor = "current_thread")]
# async fn main() {
sleep(Duration::from_millis(100)).await;
println!("100 ms have elapsed");
# }
```

See the documentation for the [`Sleep`] type for more examples.

# Panics

This function panics if there is no current timer set.

It can be triggered when [`Builder::enable_time`] or
[`Builder::enable_all`] are not included in the builder.

It can also panic whenever a timer is created outside of a
Tokio runtime. That is why `rt.block_on(sleep(...))` will panic,
since the function is executed outside of the runtime.
Whereas `rt.block_on(async {sleep(...).await})` doesn't panic.
And this is because wrapping the function on an async makes it lazy,
and so gets executed inside the runtime successfully without
panicking.

[`Sleep`]: struct@crate::time::Sleep
[`interval`]: crate::time::interval()
[`Builder::enable_time`]: crate::runtime::Builder::enable_time
[`Builder::enable_all`]: crate::runtime::Builder::enable_all"""
def sleep(duration: Duration) -> Sleep: ...

"""Yields execution back to the Tokio runtime.

A task yields by awaiting on `yield_now()`, and may resume when that future
completes (with no output.) The current task will be re-added as a pending
task at the _back_ of the pending queue. Any other pending tasks will be
scheduled. No other waking is required for the task to continue.

See also the usage example in the [task module](index.html#yield_now).

## Non-guarantees

This function may not yield all the way up to the executor if there are any
special combinators above it in the call stack. For example, if a
[`tokio::select!`] has another branch complete during the same poll as the
`yield_now()`, then the yield is not propagated all the way up to the
runtime.

It is generally not guaranteed that the runtime behaves like you expect it
to when deciding which task to schedule next after a call to `yield_now()`.
In particular, the runtime may choose to poll the task that just ran
`yield_now()` again immediately without polling any other tasks first. For
example, the runtime will not drive the IO driver between every poll of a
task, and this could result in the runtime polling the current task again
immediately even if there is another task that could make progress if that
other task is waiting for a notification from the IO driver.

In general, changes to the order in which the runtime polls tasks is not
considered a breaking change, and your program should be correct no matter
which order the runtime polls your tasks in.

[`tokio::select!`]: macro@crate::select"""
async def yield_now() -> None: ...

"""Turn off cooperative scheduling for a future. The future will never be forced to yield by
Tokio. Using this exposes your service to starvation if the unconstrained future never yields
otherwise.

See also the usage example in the [task module](index.html#unconstrained)."""
def unconstrained(inner: F) -> object: ...

"""Returns `true` if there is still budget left on the task.

# Examples

This example defines a `Timeout` future that requires a given `future` to complete before the
specified duration elapses. If it does, its result is returned; otherwise, an error is returned
and the future is canceled.

Note that the future could exhaust the budget before we evaluate the timeout. Using `has_budget_remaining`,
we can detect this scenario and ensure the timeout is always checked.

```
# use std::future::Future;
# use std::pin::{pin, Pin};
# use std::task::{ready, Context, Poll};
# use tokio::task::coop;
# use tokio::time::Sleep;
pub struct Timeout<T> {
future: T,
delay: Pin<Box<Sleep>>,
}

impl<T> Future for Timeout<T>
where
T: Future + Unpin,
{
type Output = Result<T::Output, ()>;

fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
let this = Pin::into_inner(self);
let future = Pin::new(&mut this.future);
let delay = Pin::new(&mut this.delay);

// check if the future is ready
let had_budget_before = coop::has_budget_remaining();
if let Poll::Ready(v) = future.poll(cx) {
return Poll::Ready(Ok(v));
}
let has_budget_now = coop::has_budget_remaining();

// evaluate the timeout
if let (true, false) = (had_budget_before, has_budget_now) {
// it is the underlying future that exhausted the budget
ready!(pin!(coop::unconstrained(delay)).poll(cx));
} else {
ready!(delay.poll(cx));
}
return Poll::Ready(Err(()));
}
}
```"""
def has_budget_remaining() -> bool: ...

"""Consumes a unit of budget and returns the execution back to the Tokio
runtime *if* the task's coop budget was exhausted.

The task will only yield if its entire coop budget has been exhausted.
This function can be used in order to insert optional yield points into long
computations that do not use Tokio resources like sockets or semaphores,
without redundantly yielding to the runtime each time.

# Examples

Make sure that a function which returns a sum of (potentially lots of)
iterated values is cooperative.

```
async fn sum_iterator(input: &mut impl std::iter::Iterator<Item=i64>) -> i64 {
let mut sum: i64 = 0;
while let Some(i) = input.next() {
sum += i;
tokio::task::consume_budget().await
}
sum
}
```"""
async def consume_budget() -> None: ...

__all__: list[str] = ["duplex", "simplex", "copy_bidirectional", "copy_bidirectional_with_sizes", "join", "fuzz_linked_list", "channel", "channel", "channel", "unbounded_channel", "channel", "pipe", "maybe_done", "signal", "ctrl_c", "ctrl_c", "ctrl_break", "ctrl_close", "ctrl_shutdown", "ctrl_logoff", "id", "try_id", "symlink_dir", "symlink_metadata", "metadata", "read_dir", "canonicalize", "remove_dir", "read_to_string", "symlink", "create_dir", "remove_file", "write", "rename", "read", "copy", "read_link", "create_dir_all", "set_permissions", "symlink_file", "try_exists", "hard_link", "remove_dir_all", "interval", "interval_at", "timeout", "timeout_at", "sleep_until", "sleep", "yield_now", "unconstrained", "has_budget_remaining", "consume_budget", "spawn", "spawn_blocking", "mpsc_channel", "mpsc_unbounded_channel", "Duration", "Instant", "MpscSender", "MpscReceiver", "Arc", "Mutex", "RwLock", "AsyncFd", "AsyncFdReadyGuard", "AsyncFdReadyMutGuard", "TryIoError", "AsyncFdTryNewError", "DuplexStream", "SimplexStream", "ReadBuf", "Aio", "AioEvent", "Interest", "Ready", "RngSeed", "SetOnce", "SetOnceError", "OwnedRwLockReadGuard", "RwLockWriteGuard", "RwLockMappedWriteGuard", "RwLockReadGuard", "OwnedRwLockWriteGuard", "OwnedRwLockMappedWriteGuard", "Sender", "Receiver", "RecvError", "RwLock", "Notify", "Notified", "OwnedNotified", "Receiver", "Sender", "Ref", "SendError", "RecvError", "Barrier", "BarrierWaitResult", "Sender", "WeakSender", "Permit", "PermitIterator", "OwnedPermit", "Receiver", "UnboundedSender", "WeakUnboundedSender", "UnboundedReceiver", "SendError", "RecvError", "Mutex", "MutexGuard", "OwnedMutexGuard", "MappedMutexGuard", "OwnedMappedMutexGuard", "TryLockError", "Semaphore", "SemaphorePermit", "OwnedSemaphorePermit", "Sender", "WeakSender", "Receiver", "SendError", "AcquireError", "OnceCell", "NamedPipeServer", "NamedPipeClient", "ServerOptions", "ClientOptions", "PipeInfo", "SocketAddr", "ReadHalf", "WriteHalf", "UCred", "OwnedReadHalf", "OwnedWriteHalf", "ReuniteError", "OpenOptions", "Sender", "Receiver", "ReadHalf", "WriteHalf", "OwnedReadHalf", "OwnedWriteHalf", "ReuniteError", "Internal", "Command", "Child", "ChildStdin", "ChildStdout", "ChildStderr", "SelectNormal", "SelectBiased", "Rotator", "BiasedRotator", "SignalKind", "Signal", "CtrlC", "CtrlBreak", "CtrlClose", "CtrlShutdown", "CtrlLogoff", "Handle", "EnterGuard", "TryCurrentError", "Runtime", "LocalOptions", "LocalRuntime", "Dump", "Tasks", "Task", "BacktraceSymbol", "BacktraceFrame", "Backtrace", "Trace", "RuntimeMetrics", "LogHistogram", "LogHistogramBuilder", "Builder", "Id", "AbortHandle", "Id", "TaskMeta", "ReadDir", "DirEntry", "OpenOptions", "File", "DirBuilder", "Instant", "Interval", "Error", "Elapsed", "LocalEnterGuard", "Builder", "JoinSet", "Builder", "LocalKey", "AccessError", "TryRecvError", "TrySendError", "TryRecvError", "RecvError", "TryRecvError", "TryAcquireError", "SetError", "NotDefinedHere", "PipeMode", "PipeEnd", "RuntimeFlavor", "InvalidHistogramConfiguration", "MissedTickBehavior"]
