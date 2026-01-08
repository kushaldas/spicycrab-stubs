"""Example 01: Creating and using NaiveDate.

Demonstrates:
- Creating dates with from_ymd_opt
- Accessing year, month, day components
- Checking for leap years

Usage:
    ./naive_date
"""
from spicycrab_chrono import NaiveDate


def main() -> None:
    # Create a date: July 4, 2024
    date: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 7, 4)

    if date is not None:
        # Use i32 for year (chrono returns i32)
        year: int = date.year()
        # Use u32 for month, day (chrono returns u32)
        month: int = date.month()
        day: int = date.day()
        print(f"Date: {year}-{month}-{day}")

        # Check if it's a leap year
        is_leap: bool = date.leap_year()
        if is_leap:
            print("2024 is a leap year")

        # Get the day of year (ordinal) - returns u32
        ordinal: int = date.ordinal()
        print(f"Day of year: {ordinal}")
