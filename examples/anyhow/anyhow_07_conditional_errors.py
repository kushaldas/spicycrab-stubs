"""Example 7: Conditional error handling.

Demonstrates checking Result status and handling errors conditionally.
"""

from spicycrab_anyhow import Error, Result


def risky_operation(value: int) -> Result[int, Error]:
    """An operation that may fail based on input."""
    if value < 0:
        return Result.Err(Error.msg("negative value not allowed"))
    if value == 0:
        return Result.Err(Error.msg("zero value not allowed"))
    if value > 100:
        return Result.Err(Error.msg("value too large"))
    return Result.Ok(value * 2)


def safe_operation(value: int) -> int:
    """Try risky operation, return default on error."""
    result: Result[int, Error] = risky_operation(value)
    if Result.is_ok(result):
        return Result.unwrap_or(result, 0)
    else:
        return -1


def main() -> None:
    # Test with valid value
    result1: int = safe_operation(25)
    print(f"safe_operation(25) = {result1}")

    # Test with zero (error case)
    result2: int = safe_operation(0)
    print(f"safe_operation(0) = {result2}")

    # Test with large value (error case)
    result3: int = safe_operation(200)
    print(f"safe_operation(200) = {result3}")

    # Test with valid value again
    result4: int = safe_operation(50)
    print(f"safe_operation(50) = {result4}")

    print("Conditional error handling complete")
