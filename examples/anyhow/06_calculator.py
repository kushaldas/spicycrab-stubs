"""Example 6: Simple calculator with Result error handling.

Demonstrates handling different error conditions in arithmetic operations.
"""

from spicycrab_anyhow import Error, Result


def add(a: int, b: int) -> Result[int, Error]:
    """Add two numbers with overflow check."""
    result: int = a + b
    # Simple overflow check for demo
    if a > 0 and b > 0 and result < 0:
        return Result.Err(Error.msg("addition overflow"))
    return Result.Ok(result)


def subtract(a: int, b: int) -> Result[int, Error]:
    """Subtract two numbers."""
    return Result.Ok(a - b)


def multiply(a: int, b: int) -> Result[int, Error]:
    """Multiply two numbers with overflow check."""
    result: int = a * b
    if a != 0 and result // a != b:
        return Result.Err(Error.msg("multiplication overflow"))
    return Result.Ok(result)


def divide(a: int, b: int) -> Result[int, Error]:
    """Divide two numbers."""
    if b == 0:
        return Result.Err(Error.msg("division by zero"))
    return Result.Ok(a // b)


def run() -> Result[int, Error]:
    """Run calculator operations."""
    sum_result: int = add(10, 20)
    print(f"10 + 20 = {sum_result}")

    diff_result: int = subtract(50, 30)
    print(f"50 - 30 = {diff_result}")

    prod_result: int = multiply(6, 7)
    print(f"6 * 7 = {prod_result}")

    quot_result: int = divide(100, 4)
    print(f"100 / 4 = {quot_result}")

    return Result.Ok(quot_result)


def main() -> None:
    result: Result[int, Error] = run()
    if Result.is_ok(result):
        print("All calculations completed")
    else:
        print("Calculation error")
