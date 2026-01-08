"""Example 3: Parsing and validating input.

Demonstrates using Result for input validation with descriptive errors.
"""

from spicycrab_anyhow import Error, Result


def parse_age(input_str: str) -> Result[int, Error]:
    """Parse and validate an age from string input."""
    if not input_str.isdigit():
        return Result.Err(Error.msg("age must be a number"))

    age: int = int(input_str)

    if age < 0:
        return Result.Err(Error.msg("age cannot be negative"))

    if age > 150:
        return Result.Err(Error.msg("age seems unrealistic"))

    return Result.Ok(age)


def run() -> Result[int, Error]:
    """Test age parsing."""
    # Valid age
    age1: int = parse_age("25")
    print(f"Parsed age: {age1}")

    # Another valid age
    age2: int = parse_age("100")
    print(f"Parsed age: {age2}")

    return Result.Ok(age2)


def main() -> None:
    result: Result[int, Error] = run()
    if Result.is_ok(result):
        print("All ages parsed successfully")
    else:
        print("Failed to parse ages")
