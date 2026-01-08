"""Example 08: Date arithmetic with TimeDelta.

Demonstrates:
- Adding/subtracting days from dates
- Calculating duration between dates
- Checking for valid date operations

Usage:
    ./date_arithmetic
"""
from spicycrab_chrono import NaiveDate, TimeDelta


def main() -> None:
    # Start with a date
    start: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 1, 15)

    if start is not None:
        print(f"Start date: {start.year()}-{start.month()}-{start.day()}")

        # Add 30 days
        delta: TimeDelta = TimeDelta.days(30)
        future: NaiveDate | None = start.checked_add_signed(delta)

        if future is not None:
            print(f"30 days later: {future.year()}-{future.month()}-{future.day()}")

        # Subtract 10 days
        past_delta: TimeDelta = TimeDelta.days(10)
        past: NaiveDate | None = start.checked_sub_signed(past_delta)

        if past is not None:
            print(f"10 days before: {past.year()}-{past.month()}-{past.day()}")

    # Calculate duration between two dates
    date1: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 1, 1)
    if date1 is not None:
        date2: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 12, 31)
        if date2 is not None:
            diff = date2.signed_duration_since(date1)
            days: int = diff.num_days()
            print(f"Days in 2024: {days}")
