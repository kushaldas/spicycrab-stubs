"""Example 1: Basic Result usage with anyhow.

Demonstrates returning Ok and Err from a function.
"""

from spicycrab_anyhow import Error, Result


def divide(a: int, b: int) -> Result[int, Error]:
    """Divide two integers, returning an error if divisor is zero."""
    if b == 0:
        return Result.Err(Error.msg("cannot divide by zero"))
    return Result.Ok(a // b)


def main() -> None:
    # Test successful division
    result1: Result[int, Error] = divide(10, 2)
    if Result.is_ok(result1):
        print("10 / 2 = 5")

    # Test division by zero
    result2: Result[int, Error] = divide(10, 0)
    if Result.is_err(result2):
        print("Division by zero caught!")
