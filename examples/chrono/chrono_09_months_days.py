"""Example 09: Adding months and days using Months and Days types.

Demonstrates:
- Creating Months and Days duration types
- Adding months to dates (calendar-aware)
- Adding days to dates

Usage:
    ./months_days
"""
from spicycrab_chrono import Days, Months, NaiveDate


def main() -> None:
    # Start date
    start: NaiveDate | None = NaiveDate.from_ymd_opt(2024, 1, 31)

    if start is not None:
        print(f"Start: {start.year()}-{start.month()}-{start.day()}")

        # Add 1 month (handles end-of-month correctly)
        one_month: Months = Months.new(1)
        next_month: NaiveDate | None = start.checked_add_months(one_month)

        if next_month is not None:
            print(f"Plus 1 month: {next_month.year()}-{next_month.month()}-{next_month.day()}")

        # Add 3 months
        three_months: Months = Months.new(3)
        later: NaiveDate | None = start.checked_add_months(three_months)

        if later is not None:
            print(f"Plus 3 months: {later.year()}-{later.month()}-{later.day()}")

        # Add days using Days type
        seven_days: Days = Days.new(7)
        week_later: NaiveDate | None = start.checked_add_days(seven_days)

        if week_later is not None:
            print(f"Plus 7 days: {week_later.year()}-{week_later.month()}-{week_later.day()}")

        # Subtract months
        six_months: Months = Months.new(6)
        earlier: NaiveDate | None = start.checked_sub_months(six_months)

        if earlier is not None:
            print(f"Minus 6 months: {earlier.year()}-{earlier.month()}-{earlier.day()}")
