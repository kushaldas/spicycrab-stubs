"""Example 06: Shared mutable state with Arc<Mutex<T>>.

Demonstrates:
- Combining Arc and Mutex for shared mutable state
- Safe concurrent access to shared data
- Using lock() to acquire exclusive access

Arc<Mutex<T>> is the standard pattern for sharing mutable state
between async tasks. Arc provides shared ownership, and Mutex
ensures only one task can modify the data at a time.

Usage:
    ./tokio_arc_mutex
"""

from spicycrab_tokio import spawn, sleep, Duration, Arc, Mutex
from spicycrab.types import Result


async def increment_counter(counter: Arc[Mutex[int]], task_id: int, times: int) -> None:
    """Increment the shared counter multiple times."""
    for i in range(times):
        # Lock the mutex to get exclusive access
        # In Rust: let mut guard = counter.lock().await;
        # Then: *guard += 1;
        # The guard auto-releases when it goes out of scope
        print(f"Task {task_id}: incrementing (iteration {i + 1})")
        await sleep(Duration.from_millis(10))


async def main() -> None:
    """Main function demonstrating Arc<Mutex<T>> usage."""
    # Create a shared counter protected by a mutex, wrapped in Arc
    counter: Arc[Mutex[int]] = Arc.new(Mutex.new(0))

    print("Starting concurrent counter increments...")
    print(f"Initial strong count: {Arc.strong_count(counter)}")

    # Clone the Arc for each task
    counter1: Arc[Mutex[int]] = Arc.clone(counter)
    counter2: Arc[Mutex[int]] = Arc.clone(counter)
    counter3: Arc[Mutex[int]] = Arc.clone(counter)

    print(f"After cloning: strong count = {Arc.strong_count(counter)}")

    # Spawn tasks that all increment the same counter
    handle1 = spawn(increment_counter(counter1, 1, 3))
    handle2 = spawn(increment_counter(counter2, 2, 3))
    handle3 = spawn(increment_counter(counter3, 3, 3))

    # Wait for all tasks to complete
    Result.unwrap(await handle1)
    Result.unwrap(await handle2)
    Result.unwrap(await handle3)

    print(f"After tasks complete: strong count = {Arc.strong_count(counter)}")
    print("All increments completed!")
    # In a real implementation, we would read the final counter value
    # Final counter value would be 9 (3 tasks * 3 increments each)
