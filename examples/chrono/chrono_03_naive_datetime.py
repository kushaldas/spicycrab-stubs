"""Example 03: Creating and using NaiveDateTime.

Demonstrates:
- Combining NaiveDate and NaiveTime
- Creating datetime from timestamp
- Getting date and time components

Usage:
    ./naive_datetime
"""
from spicycrab_chrono import NaiveDate, NaiveDateTime, NaiveTime


def main() -> None:
    # Create date and time separately
    date: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 12, 25)
    time: NaiveTime | None = NaiveTime.from_hms_opt(10, 30, 0)

    if date is not None:
        if time is not None:
            # Combine into datetime using instance method
            dt: NaiveDateTime = date.and_time(time)
            print(f"Christmas morning: {dt.year()}-{dt.month()}-{dt.day()} {dt.hour()}:{dt.minute()}")

    # Create from Unix timestamp (seconds since epoch)
    ts_dt: NaiveDateTime | None = NaiveDateTime.from_timestamp_opt(1704067200, 0)
    if ts_dt is not None:
        print(f"From timestamp: {ts_dt.year()}-{ts_dt.month()}-{ts_dt.day()}")

        # Get the timestamp back
        ts: int = ts_dt.timestamp()
        print(f"Timestamp: {ts}")
