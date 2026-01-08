"""Example 8: Batch processing with error collection.

Demonstrates processing multiple items and tracking successes/failures.
"""

from spicycrab_anyhow import Error, Result


def process_item(value: int) -> Result[int, Error]:
    """Process a single item - fails if not divisible by 2."""
    if value % 2 != 0:
        return Result.Err(Error.msg("value must be even"))
    return Result.Ok(value // 2)


def main() -> None:
    # Process a batch of values
    values: list[int] = [2, 4, 6, 8, 10]
    success_count: int = 0
    total_sum: int = 0

    i: int = 0
    while i < len(values):
        value: int = values[i]
        result: Result[int, Error] = process_item(value)
        if Result.is_ok(result):
            processed: int = Result.unwrap_or(result, 0)
            total_sum = total_sum + processed
            success_count = success_count + 1
            print(f"Processed {value} -> {processed}")
        else:
            print(f"Failed to process {value}")
        i = i + 1

    print(f"Successfully processed {success_count} items")
    print(f"Total sum: {total_sum}")
