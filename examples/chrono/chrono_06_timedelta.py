"""Example 06: Working with TimeDelta (durations).

Demonstrates:
- Creating durations with days, hours, minutes, seconds
- Getting duration components
- Checking if duration is zero

Usage:
    ./timedelta
"""
from spicycrab_chrono import TimeDelta


def main() -> None:
    # Create various durations
    one_day: TimeDelta = TimeDelta.days(1)
    two_hours: TimeDelta = TimeDelta.hours(2)
    thirty_mins: TimeDelta = TimeDelta.minutes(30)
    ten_secs: TimeDelta = TimeDelta.seconds(10)

    # Get duration in different units
    print(f"One day in hours: {one_day.num_hours()}")
    print(f"One day in minutes: {one_day.num_minutes()}")
    print(f"One day in seconds: {one_day.num_seconds()}")

    # Two hours in various units
    print(f"Two hours in minutes: {two_hours.num_minutes()}")
    print(f"Two hours in seconds: {two_hours.num_seconds()}")

    # Check zero duration
    zero: TimeDelta = TimeDelta.zero()
    is_zero: bool = zero.is_zero()
    if is_zero:
        print("Zero duration is zero")

    # Get absolute value (for negative durations)
    neg_day: TimeDelta = TimeDelta.days(-1)
    abs_day: TimeDelta = neg_day.abs()
    print(f"Absolute of -1 day: {abs_day.num_days()} days")
