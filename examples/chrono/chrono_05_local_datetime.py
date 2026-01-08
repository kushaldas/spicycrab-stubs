"""Example 05: Working with Local DateTime.

Demonstrates:
- Getting current local time with Local.now()
- Accessing timezone offset
- Getting naive local time

Usage:
    ./local_datetime
"""
from spicycrab_chrono import DateTime, Local, NaiveDateTime


def main() -> None:
    # Get current local time
    now = Local.now()
    # Use to_rfc3339 for formatted output
    rfc_now: str = now.to_rfc3339()
    print(f"Current local: {rfc_now}")

    # Get the naive local datetime (without timezone info)
    naive: NaiveDateTime = now.naive_local()
    print(f"Naive local: {naive.year()}-{naive.month()}-{naive.day()}")

    # Get timestamp
    ts: int = now.timestamp()
    print(f"Unix timestamp: {ts}")
