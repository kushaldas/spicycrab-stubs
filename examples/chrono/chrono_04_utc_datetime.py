"""Example 04: Working with UTC DateTime.

Demonstrates:
- Getting current UTC time with Utc.now()
- Creating DateTime from timestamp
- Converting to RFC3339 format

Usage:
    ./utc_datetime
"""
from spicycrab_chrono import DateTime, Utc


def main() -> None:
    # Get current UTC time
    now = Utc.now()
    # Use to_rfc3339 for formatted output (avoids trait method issues)
    rfc_now: str = now.to_rfc3339()
    print(f"Current UTC: {rfc_now}")

    # Get Unix timestamp
    ts: int = now.timestamp()
    print(f"Unix timestamp: {ts}")

    # Create from timestamp (returns DateTime<Utc>)
    dt = DateTime.from_timestamp(1704067200, 0)
    if dt is not None:
        # Convert to RFC3339 string format
        rfc: str = dt.to_rfc3339()
        print(f"RFC3339: {rfc}")
