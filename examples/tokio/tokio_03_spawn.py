"""Example 03: Spawning concurrent tasks with tokio."""

from spicycrab_tokio import spawn, sleep, Duration
from spicycrab.types import Result


async def do_work(task_id: int) -> int:
    """Simulate some async work."""
    print(f"Task {task_id} starting...")
    await sleep(Duration.from_millis(100))
    print(f"Task {task_id} finished!")
    return task_id * 10


async def main() -> None:
    """Main function demonstrating concurrent task spawning."""
    print("Spawning tasks...")

    # Spawn multiple tasks
    handle1 = spawn(do_work(1))
    handle2 = spawn(do_work(2))
    handle3 = spawn(do_work(3))

    # Wait for all tasks to complete - JoinHandle yields Result<T, JoinError>
    result1: int = Result.unwrap(await handle1)
    result2: int = Result.unwrap(await handle2)
    result3: int = Result.unwrap(await handle3)

    print(f"Results: {result1}, {result2}, {result3}")
    print("All tasks completed!")
