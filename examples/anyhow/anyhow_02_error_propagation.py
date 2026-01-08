"""Example 2: Error propagation with the ? operator.

When a function returns Result, calls to other Result-returning
functions automatically get the ? operator for early return on error.
"""

from spicycrab_anyhow import Error, Result


def parse_positive(s: str) -> Result[int, Error]:
    """Parse a string as a positive integer."""
    if not s.isdigit():
        return Result.Err(Error.msg("not a valid number"))
    value: int = int(s)
    if value <= 0:
        return Result.Err(Error.msg("number must be positive"))
    return Result.Ok(value)


def compute_ratio(a_str: str, b_str: str) -> Result[int, Error]:
    """Parse two strings and compute their ratio.

    The ? operator propagates errors from parse_positive automatically.
    """
    a: int = parse_positive(a_str)  # ? applied here
    b: int = parse_positive(b_str)  # ? applied here
    if b == 0:
        return Result.Err(Error.msg("divisor cannot be zero"))
    return Result.Ok(a // b)


def run() -> Result[int, Error]:
    """Run the computation."""
    result: int = compute_ratio("100", "5")
    print(f"100 / 5 = {result}")
    return Result.Ok(result)


def main() -> None:
    result: Result[int, Error] = run()
    if Result.is_ok(result):
        print("Success!")
    else:
        print("Error occurred")
