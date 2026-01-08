"""Example 5: Chaining multiple Result-returning operations.

Demonstrates how errors propagate through a chain of operations.
"""

from spicycrab_anyhow import Error, Result


def step1(value: int) -> Result[int, Error]:
    """First step: double the value."""
    if value < 0:
        return Result.Err(Error.msg("step1: value must be non-negative"))
    return Result.Ok(value * 2)


def step2(value: int) -> Result[int, Error]:
    """Second step: add 10."""
    if value > 1000:
        return Result.Err(Error.msg("step2: value too large"))
    return Result.Ok(value + 10)


def step3(value: int) -> Result[int, Error]:
    """Third step: divide by 2."""
    return Result.Ok(value // 2)


def process_pipeline(input_val: int) -> Result[int, Error]:
    """Process value through all steps.

    Each step can fail, and errors propagate via ?.
    """
    after_step1: int = step1(input_val)
    after_step2: int = step2(after_step1)
    after_step3: int = step3(after_step2)
    return Result.Ok(after_step3)


def run() -> Result[int, Error]:
    """Run the pipeline with a valid input."""
    result: int = process_pipeline(5)
    # 5 -> 10 -> 20 -> 10
    print(f"Pipeline result: {result}")
    return Result.Ok(result)


def main() -> None:
    result: Result[int, Error] = run()
    if Result.is_ok(result):
        print("Pipeline completed successfully")
    else:
        print("Pipeline failed")
