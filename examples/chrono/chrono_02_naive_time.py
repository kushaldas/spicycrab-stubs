"""Example 02: Creating and using NaiveTime.

Demonstrates:
- Creating times with from_hms_opt
- Accessing hour, minute, second components
- Getting seconds from midnight

Usage:
    ./naive_time
"""
from spicycrab_chrono import NaiveTime


def main() -> None:
    # Create a time: 14:30:45
    time: NaiveTime | None = NaiveTime.from_hms_opt(14, 30, 45)

    if time is not None:
        hour: int = time.hour()
        minute: int = time.minute()
        second: int = time.second()
        print(f"Time: {hour}:{minute}:{second}")

        # Get total seconds from midnight
        secs: int = time.num_seconds_from_midnight()
        print(f"Seconds from midnight: {secs}")

    # Create time with milliseconds
    time_ms: NaiveTime | None = NaiveTime.from_hms_milli_opt(10, 20, 30, 500)
    if time_ms is not None:
        nano: int = time_ms.nanosecond()
        print(f"Nanoseconds: {nano}")
