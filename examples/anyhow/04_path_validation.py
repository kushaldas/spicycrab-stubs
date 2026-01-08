"""Example 4: Path validation with Result.

Demonstrates validating paths and returning descriptive errors.
"""

from spicycrab_anyhow import Error, Result


def validate_filename(name: str) -> Result[str, Error]:
    """Validate a filename."""
    if len(name) == 0:
        return Result.Err(Error.msg("filename cannot be empty"))

    if len(name) > 255:
        return Result.Err(Error.msg("filename too long"))

    # Check for invalid characters (simplified check)
    if name.find("/") >= 0:
        return Result.Err(Error.msg("filename contains slash"))
    if name.find("\\") >= 0:
        return Result.Err(Error.msg("filename contains backslash"))

    return Result.Ok(name)


def run() -> Result[str, Error]:
    """Test filename validation."""
    # Valid filename
    name1: str = validate_filename("document.txt")
    print(f"Valid filename: {name1}")

    # Another valid filename
    name2: str = validate_filename("my_file_2024.pdf")
    print(f"Valid filename: {name2}")

    return Result.Ok(name2)


def main() -> None:
    result: Result[str, Error] = run()
    if Result.is_ok(result):
        print("All filenames are valid")
    else:
        print("Invalid filename detected")
