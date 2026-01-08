"""Example 10: Working with FixedOffset timezones.

Demonstrates:
- Creating fixed offset timezones (e.g., UTC+5:30)
- Getting offset in seconds
- Converting between UTC and local

Usage:
    ./fixed_offset
"""
from spicycrab_chrono import FixedOffset


def main() -> None:
    # Create UTC+5:30 (India Standard Time) - 5*3600 + 30*60 = 19800 seconds
    ist: FixedOffset | None = FixedOffset.east_opt(19800)

    if ist is not None:
        # Get offset from UTC
        offset_secs: int = ist.local_minus_utc()
        hours: int = offset_secs // 3600
        mins: int = (offset_secs % 3600) // 60
        print(f"IST offset: +{hours}:{mins}")

    # Create UTC-5 (EST) - 5*3600 = 18000 seconds west
    est: FixedOffset | None = FixedOffset.west_opt(18000)

    if est is not None:
        offset_secs2: int = est.local_minus_utc()
        hours2: int = offset_secs2 // 3600
        print(f"EST offset: {hours2} hours")

    # Create UTC+0
    utc: FixedOffset | None = FixedOffset.east_opt(0)

    if utc is not None:
        utc_offset: int = utc.local_minus_utc()
        print(f"UTC offset: {utc_offset} seconds")
