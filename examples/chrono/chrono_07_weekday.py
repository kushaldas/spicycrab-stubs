"""Example 07: Working with Weekday.

Demonstrates:
- Using Weekday enum values
- Getting day number from Monday/Sunday
- Getting next/previous weekday

Usage:
    ./weekday
"""
from spicycrab_chrono import NaiveDate, Weekday


def main() -> None:
    # Get weekday from a date
    date: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 7, 4)  # July 4, 2024 is Thursday

    if date is not None:
        day = date.weekday()
        print("July 4, 2024 is a weekday")

        # Get day number (1-7 from Monday) - let Rust infer u32
        num_mon = day.number_from_monday()
        print(f"Number from Monday: {num_mon}")

        # Get day number (1-7 from Sunday) - let Rust infer u32
        num_sun = day.number_from_sunday()
        print(f"Number from Sunday: {num_sun}")

        # Get next weekday
        next_day = day.succ()
        print(f"Next day number from Monday: {next_day.number_from_monday()}")

        # Get previous weekday
        prev_day = day.pred()
        print(f"Previous day number from Monday: {prev_day.number_from_monday()}")
