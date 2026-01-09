"""Example 05: Sharing data between tasks with Arc.

Demonstrates:
- Creating Arc (Atomically Reference Counted) pointers
- Cloning Arc for sharing between spawned tasks
- Using Arc::strong_count to track references

Arc allows multiple tasks to share ownership of the same data.
Each Arc.clone() increments the reference count, and when the
last Arc is dropped, the data is deallocated.

Usage:
    ./tokio_arc
"""

from spicycrab_tokio import spawn, sleep, Duration, Arc
from spicycrab.types import Result


async def print_config(config: Arc[str], task_id: int) -> None:
    """A worker task that reads shared config data."""
    print(f"Task {task_id}: Starting with config")
    await sleep(Duration.from_millis(50))
    # In Rust, Arc<T> auto-derefs to T, so we can use the value directly
    # For this example, we just show that we have access to the Arc
    count: int = Arc.strong_count(config)
    print(f"Task {task_id}: Done. Strong count = {count}")


async def main() -> None:
    """Main function demonstrating Arc usage."""
    # Create shared config data wrapped in Arc
    config: Arc[str] = Arc.new("shared configuration data")

    print(f"Initial strong count: {Arc.strong_count(config)}")

    # Clone the Arc for each task (this increments the reference count)
    config1: Arc[str] = Arc.clone(config)
    config2: Arc[str] = Arc.clone(config)
    config3: Arc[str] = Arc.clone(config)

    print(f"After cloning: strong count = {Arc.strong_count(config)}")

    # Spawn tasks that share the config
    handle1 = spawn(print_config(config1, 1))
    handle2 = spawn(print_config(config2, 2))
    handle3 = spawn(print_config(config3, 3))

    # Wait for all tasks to complete
    Result.unwrap(await handle1)
    Result.unwrap(await handle2)
    Result.unwrap(await handle3)

    print(f"After tasks complete: strong count = {Arc.strong_count(config)}")
    print("All tasks completed!")
