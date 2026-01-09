"""Python stubs for the chrono Rust crate.

Install with: cookcrab install chrono
"""

from __future__ import annotations

from typing import Self

class SecondsTimestampVisitor:

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

class NanoSecondsTimestampVisitor:

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

class MicroSecondsTimestampVisitor:

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

class MilliSecondsTimestampVisitor:

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

    def expecting(self, formatter: Formatter) -> Result: ...

    def visit_i64(self, value: int) -> Value: ...

    def visit_u64(self, value: int) -> Value: ...

class DateTime:
    """ISO 8601 combined date and time with time zone.

There are some constructors implemented here (the `from_*` methods), but
the general-purpose constructors are all via the methods on the
[`TimeZone`](./offset/trait.TimeZone.html) implementations."""

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def from_naive_utc_and_offset(datetime: NaiveDateTime, offset: Offset) -> object: ...

    @staticmethod
    def from_utc(datetime: NaiveDateTime, offset: Offset) -> object: ...

    @staticmethod
    def from_local(datetime: NaiveDateTime, offset: Offset) -> object: ...

    def date(self) -> object: ...

    def date_naive(self) -> NaiveDate: ...

    def time(self) -> NaiveTime: ...

    def timestamp(self) -> int: ...

    def timestamp_millis(self) -> int: ...

    def timestamp_micros(self) -> int: ...

    def timestamp_nanos(self) -> int: ...

    def timestamp_nanos_opt(self) -> int | None: ...

    def timestamp_subsec_millis(self) -> int: ...

    def timestamp_subsec_micros(self) -> int: ...

    def timestamp_subsec_nanos(self) -> int: ...

    def offset(self) -> Offset: ...

    def timezone(self) -> Tz: ...

    def with_timezone(self, tz: Tz2) -> object: ...

    def fixed_offset(self) -> object: ...

    def to_utc(self) -> object: ...

    def checked_add_signed(self, rhs: TimeDelta) -> object | None: ...

    def checked_add_months(self, months: Months) -> object | None: ...

    def checked_sub_signed(self, rhs: TimeDelta) -> object | None: ...

    def checked_sub_months(self, months: Months) -> object | None: ...

    def checked_add_days(self, days: Days) -> object: ...

    def checked_sub_days(self, days: Days) -> object: ...

    def signed_duration_since(self, rhs: object) -> TimeDelta: ...

    def naive_utc(self) -> NaiveDateTime: ...

    def naive_local(self) -> NaiveDateTime: ...

    def years_since(self, base: Self) -> int | None: ...

    def to_rfc2822(self) -> str: ...

    def to_rfc3339(self) -> str: ...

    def to_rfc3339_opts(self, secform: SecondsFormat, use_z: bool) -> str: ...

    def with_time(self, time: NaiveTime) -> object: ...

    @staticmethod
    def from_timestamp_secs(secs: int) -> object: ...

    @staticmethod
    def from_timestamp(secs: int, nsecs: int) -> object: ...

    @staticmethod
    def from_timestamp_millis(millis: int) -> object: ...

    @staticmethod
    def from_timestamp_micros(micros: int) -> object: ...

    @staticmethod
    def from_timestamp_nanos(nanos: int) -> "DateTime": ...

    @staticmethod
    def default() -> "DateTime": ...

    @staticmethod
    def default() -> "DateTime": ...

    @staticmethod
    def default() -> "DateTime": ...

    @staticmethod
    def from_(src: object) -> "DateTime": ...

    @staticmethod
    def from_(src: object) -> "DateTime": ...

    @staticmethod
    def from_(src: object) -> "DateTime": ...

    @staticmethod
    def from_(src: object) -> "DateTime": ...

    @staticmethod
    def from_(src: object) -> "DateTime": ...

    @staticmethod
    def from_(src: object) -> "DateTime": ...

    @staticmethod
    def parse_from_rfc2822(s: str) -> object: ...

    @staticmethod
    def parse_from_rfc3339(s: str) -> object: ...

    @staticmethod
    def parse_from_str(s: str, fmt: str) -> object: ...

    @staticmethod
    def parse_and_remainder(s: object, fmt: str) -> object: ...

    def format_with_items(self, items: I) -> object: ...

    def format(self, fmt: object) -> object: ...

    def format_localized_with_items(self, items: I, locale: Locale) -> object: ...

    def format_localized(self, fmt: object, locale: Locale) -> object: ...

    def year(self) -> int: ...

    def month(self) -> int: ...

    def month0(self) -> int: ...

    def day(self) -> int: ...

    def day0(self) -> int: ...

    def ordinal(self) -> int: ...

    def ordinal0(self) -> int: ...

    def weekday(self) -> Weekday: ...

    def iso_week(self) -> IsoWeek: ...

    def with_year(self, year: int) -> object | None: ...

    def with_month(self, month: int) -> object | None: ...

    def with_month0(self, month0: int) -> object | None: ...

    def with_day(self, day: int) -> object | None: ...

    def with_day0(self, day0: int) -> object | None: ...

    def with_ordinal(self, ordinal: int) -> object | None: ...

    def with_ordinal0(self, ordinal0: int) -> object | None: ...

    def hour(self) -> int: ...

    def minute(self) -> int: ...

    def second(self) -> int: ...

    def nanosecond(self) -> int: ...

    def with_hour(self, hour: int) -> object | None: ...

    def with_minute(self, min: int) -> object | None: ...

    def with_second(self, sec: int) -> object | None: ...

    def with_nanosecond(self, nano: int) -> object | None: ...

    def eq(self, other: object) -> bool: ...

    def partial_cmp(self, other: object) -> Ordering | None: ...

    def cmp(self, other: object) -> Ordering: ...

    def hash(self, state: H) -> None: ...

    def add(self, rhs: TimeDelta) -> object: ...

    def add(self, rhs: Duration) -> object: ...

    def add_assign(self, rhs: TimeDelta) -> None: ...

    def add_assign(self, rhs: Duration) -> None: ...

    def add(self, rhs: FixedOffset) -> object: ...

    def add(self, rhs: Months) -> Output: ...

    def sub(self, rhs: TimeDelta) -> object: ...

    def sub(self, rhs: Duration) -> object: ...

    def sub_assign(self, rhs: TimeDelta) -> None: ...

    def sub_assign(self, rhs: Duration) -> None: ...

    def sub(self, rhs: FixedOffset) -> object: ...

    def sub(self, rhs: Months) -> Output: ...

    def sub(self, rhs: object) -> TimeDelta: ...

    def sub(self, rhs: object) -> TimeDelta: ...

    def add(self, days: Days) -> Output: ...

    def sub(self, days: Days) -> Output: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    @staticmethod
    def from_(t: SystemTime) -> object: ...

    @staticmethod
    def from_(t: SystemTime) -> object: ...

    @staticmethod
    def from_(date: Date) -> object: ...

    @staticmethod
    def from_(date: Date) -> object: ...

    @staticmethod
    def arbitrary(u: Unstructured) -> object: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    def duration_round(self, duration: TimeDelta) -> object: ...

    def duration_trunc(self, duration: TimeDelta) -> object: ...

    def duration_round_up(self, duration: TimeDelta) -> object: ...

class ParseWeekdayError:
    """An error resulting from reading `Weekday` value with `FromStr`."""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class Months:
    """A duration in calendar months"""

    @staticmethod
    def new(num: int) -> "Months": ...

    def as_u32(self) -> int: ...

class ParseMonthError:
    """An error resulting from reading `<Month>` value with `FromStr`."""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class StrftimeItems:
    """Parsing iterator for `strftime`-like format strings.

See the [`format::strftime` module](crate::format::strftime) for supported formatting
specifiers.

`StrftimeItems` is used in combination with more low-level methods such as [`format::parse()`]
or [`format_with_items`].

If formatting or parsing date and time values is not performance-critical, the methods
[`parse_from_str`] and [`format`] on types such as [`DateTime`](crate::DateTime) are easier to
use.

[`format`]: crate::DateTime::format
[`format_with_items`]: crate::DateTime::format
[`parse_from_str`]: crate::DateTime::parse_from_str
[`DateTime`]: crate::DateTime
[`format::parse()`]: crate::format::parse()"""

    @staticmethod
    def new(s: object) -> "StrftimeItems": ...

    @staticmethod
    def new_lenient(s: object) -> "StrftimeItems": ...

    @staticmethod
    def new_with_locale(s: object, locale: Locale) -> "StrftimeItems": ...

    def parse(self) -> list[Item]: ...

    def parse_to_owned(self) -> list[Item]: ...

    def next(self) -> Item | None: ...

class DelayedFormat:
    """A *temporary* object which can be used as an argument to `format!` or others.
This is normally constructed via `format` methods of each date and time type."""

    @staticmethod
    def new(date: NaiveDate | None, time: NaiveTime | None, items: I) -> object: ...

    @staticmethod
    def new_with_offset(date: NaiveDate | None, time: NaiveTime | None, offset: Off, items: I) -> object: ...

    @staticmethod
    def new_with_locale(date: NaiveDate | None, time: NaiveTime | None, items: I, locale: Locale) -> object: ...

    @staticmethod
    def new_with_offset_and_locale(date: NaiveDate | None, time: NaiveTime | None, offset: Off, items: I, locale: Locale) -> object: ...

    def write_to(self, w: object) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class InternalNumeric:
    """An opaque type representing numeric item types for internal uses only."""

    def fmt(self, f: Formatter) -> Result: ...

class InternalFixed:
    """An opaque type representing fixed-format item types for internal uses only."""
    pass

class OffsetFormat:
    """Type for specifying the format of UTC offsets."""
    pass

class ParseError:
    """An error from the `parse` function."""

    def kind(self) -> ParseErrorKind: ...

    def fmt(self, f: Formatter) -> Result: ...

    def description(self) -> str: ...

class Parsed:
    """A type to hold parsed fields of date and time that can check all fields are consistent.

There are three classes of methods:

- `set_*` methods to set fields you have available. They do a basic range check, and if the
same field is set more than once it is checked for consistency.

- `to_*` methods try to make a concrete date and time value out of set fields.
They fully check that all fields are consistent and whether the date/datetime exists.

- Methods to inspect the parsed fields.

`Parsed` is used internally by all parsing functions in chrono. It is a public type so that it
can be used to write custom parsers that reuse the resolving algorithm, or to inspect the
results of a string parsed with chrono without converting it to concrete types.

# Resolving algorithm

Resolving date/time parts is littered with lots of corner cases, which is why common date/time
parsers do not implement it correctly.

Chrono provides a complete resolution algorithm that checks all fields for consistency via the
`Parsed` type.

As an easy example, consider RFC 2822. The [RFC 2822 date and time format] has a day of the week
part, which should be consistent with the other date parts. But a `strptime`-based parse would
happily accept inconsistent input:

```python
>>> import time
>>> time.strptime('Wed, 31 Dec 2014 04:26:40 +0000',
'%a, %d %b %Y %H:%M:%S +0000')
time.struct_time(tm_year=2014, tm_mon=12, tm_mday=31,
tm_hour=4, tm_min=26, tm_sec=40,
tm_wday=2, tm_yday=365, tm_isdst=-1)
>>> time.strptime('Thu, 31 Dec 2014 04:26:40 +0000',
'%a, %d %b %Y %H:%M:%S +0000')
time.struct_time(tm_year=2014, tm_mon=12, tm_mday=31,
tm_hour=4, tm_min=26, tm_sec=40,
tm_wday=3, tm_yday=365, tm_isdst=-1)
```

[RFC 2822 date and time format]: https://tools.ietf.org/html/rfc2822#section-3.3

# Example

Let's see how `Parsed` correctly detects the second RFC 2822 string from before is inconsistent.

```
# #[cfg(feature = "alloc")] {
use chrono::format::{ParseErrorKind, Parsed};
use chrono::Weekday;

let mut parsed = Parsed::new();
parsed.set_weekday(Weekday::Wed)?;
parsed.set_day(31)?;
parsed.set_month(12)?;
parsed.set_year(2014)?;
parsed.set_hour(4)?;
parsed.set_minute(26)?;
parsed.set_second(40)?;
parsed.set_offset(0)?;
let dt = parsed.to_datetime()?;
assert_eq!(dt.to_rfc2822(), "Wed, 31 Dec 2014 04:26:40 +0000");

let mut parsed = Parsed::new();
parsed.set_weekday(Weekday::Thu)?; // changed to the wrong day
parsed.set_day(31)?;
parsed.set_month(12)?;
parsed.set_year(2014)?;
parsed.set_hour(4)?;
parsed.set_minute(26)?;
parsed.set_second(40)?;
parsed.set_offset(0)?;
let result = parsed.to_datetime();

assert!(result.is_err());
if let Err(error) = result {
assert_eq!(error.kind(), ParseErrorKind::Impossible);
}
# }
# Ok::<(), chrono::ParseError>(())
```

The same using chrono's built-in parser for RFC 2822 (the [RFC2822 formatting item]) and
[`format::parse()`] showing how to inspect a field on failure.

[RFC2822 formatting item]: crate::format::Fixed::RFC2822
[`format::parse()`]: crate::format::parse()

```
# #[cfg(feature = "alloc")] {
use chrono::format::{parse, Fixed, Item, Parsed};
use chrono::Weekday;

let rfc_2822 = [Item::Fixed(Fixed::RFC2822)];

let mut parsed = Parsed::new();
parse(&mut parsed, "Wed, 31 Dec 2014 04:26:40 +0000", rfc_2822.iter())?;
let dt = parsed.to_datetime()?;

assert_eq!(dt.to_rfc2822(), "Wed, 31 Dec 2014 04:26:40 +0000");

let mut parsed = Parsed::new();
parse(&mut parsed, "Thu, 31 Dec 2014 04:26:40 +0000", rfc_2822.iter())?;
let result = parsed.to_datetime();

assert!(result.is_err());
if result.is_err() {
// What is the weekday?
assert_eq!(parsed.weekday(), Some(Weekday::Thu));
}
# }
# Ok::<(), chrono::ParseError>(())
```"""

    @staticmethod
    def new() -> "Parsed": ...

    def set_year(self, value: int) -> object: ...

    def set_year_div_100(self, value: int) -> object: ...

    def set_year_mod_100(self, value: int) -> object: ...

    def set_isoyear(self, value: int) -> object: ...

    def set_isoyear_div_100(self, value: int) -> object: ...

    def set_isoyear_mod_100(self, value: int) -> object: ...

    def set_quarter(self, value: int) -> object: ...

    def set_month(self, value: int) -> object: ...

    def set_week_from_sun(self, value: int) -> object: ...

    def set_week_from_mon(self, value: int) -> object: ...

    def set_isoweek(self, value: int) -> object: ...

    def set_weekday(self, value: Weekday) -> object: ...

    def set_ordinal(self, value: int) -> object: ...

    def set_day(self, value: int) -> object: ...

    def set_ampm(self, value: bool) -> object: ...

    def set_hour12(self, value: int) -> object: ...

    def set_hour(self, value: int) -> object: ...

    def set_minute(self, value: int) -> object: ...

    def set_second(self, value: int) -> object: ...

    def set_nanosecond(self, value: int) -> object: ...

    def set_timestamp(self, value: int) -> object: ...

    def set_offset(self, value: int) -> object: ...

    def to_naive_date(self) -> object: ...

    def to_naive_time(self) -> object: ...

    def to_naive_datetime_with_offset(self, offset: int) -> object: ...

    def to_fixed_offset(self) -> object: ...

    def to_datetime(self) -> object: ...

    def to_datetime_with_timezone(self, tz: Tz) -> object: ...

    def year(self) -> int | None: ...

    def year_div_100(self) -> int | None: ...

    def year_mod_100(self) -> int | None: ...

    def isoyear(self) -> int | None: ...

    def isoyear_div_100(self) -> int | None: ...

    def isoyear_mod_100(self) -> int | None: ...

    def quarter(self) -> int | None: ...

    def month(self) -> int | None: ...

    def week_from_sun(self) -> int | None: ...

    def week_from_mon(self) -> int | None: ...

    def isoweek(self) -> int | None: ...

    def weekday(self) -> Weekday | None: ...

    def ordinal(self) -> int | None: ...

    def day(self) -> int | None: ...

    def hour_div_12(self) -> int | None: ...

    def hour_mod_12(self) -> int | None: ...

    def minute(self) -> int | None: ...

    def second(self) -> int | None: ...

    def nanosecond(self) -> int | None: ...

    def timestamp(self) -> int | None: ...

    def offset(self) -> int | None: ...

class OutOfRange:
    """Out of range error type used in various converting APIs"""

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class FixedOffset:
    """The time zone with fixed offset, from UTC-23:59:59 to UTC+23:59:59.

Using the [`TimeZone`](./trait.TimeZone.html) methods
on a `FixedOffset` struct is the preferred way to construct
`DateTime<FixedOffset>` instances. See the [`east_opt`](#method.east_opt) and
[`west_opt`](#method.west_opt) methods for examples."""

    @staticmethod
    def east(secs: int) -> "FixedOffset": ...

    @staticmethod
    def east_opt(secs: int) -> FixedOffset | None: ...

    @staticmethod
    def west(secs: int) -> "FixedOffset": ...

    @staticmethod
    def west_opt(secs: int) -> FixedOffset | None: ...

    def local_minus_utc(self) -> int: ...

    def utc_minus_local(self) -> int: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    @staticmethod
    def from_offset(offset: FixedOffset) -> "FixedOffset": ...

    def offset_from_local_date(self, _local: NaiveDate) -> object: ...

    def offset_from_local_datetime(self, _local: NaiveDateTime) -> object: ...

    def offset_from_utc_date(self, _utc: NaiveDate) -> FixedOffset: ...

    def offset_from_utc_datetime(self, _utc: NaiveDateTime) -> FixedOffset: ...

    def fix(self) -> FixedOffset: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def arbitrary(u: Unstructured) -> "FixedOffset": ...

class Utc:
    """The UTC time zone. This is the most efficient time zone when you don't need the local time.
It is also used as an offset (which is also a dummy type).

Using the [`TimeZone`](./trait.TimeZone.html) methods
on the UTC struct is the preferred way to construct `DateTime<Utc>`
instances.

# Example

```
use chrono::{DateTime, TimeZone, Utc};

let dt = DateTime::from_timestamp(61, 0).unwrap();

assert_eq!(Utc.timestamp_opt(61, 0).unwrap(), dt);
assert_eq!(Utc.with_ymd_and_hms(1970, 1, 1, 0, 1, 1).unwrap(), dt);
```"""

    @staticmethod
    def today() -> object: ...

    @staticmethod
    def now() -> object: ...

    @staticmethod
    def now() -> object: ...

    @staticmethod
    def from_offset(_state: Utc) -> "Utc": ...

    def offset_from_local_date(self, _local: NaiveDate) -> object: ...

    def offset_from_local_datetime(self, _local: NaiveDateTime) -> object: ...

    def offset_from_utc_date(self, _utc: NaiveDate) -> Utc: ...

    def offset_from_utc_datetime(self, _utc: NaiveDateTime) -> Utc: ...

    def fix(self) -> FixedOffset: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class DYNAMIC_TIME_ZONE_INFORMATION:

    @staticmethod
    def default() -> "DYNAMIC_TIME_ZONE_INFORMATION": ...

class FILETIME:
    pass

class SYSTEMTIME:
    pass

class TIME_ZONE_INFORMATION:

    @staticmethod
    def default() -> "TIME_ZONE_INFORMATION": ...

class Local:
    """The local timescale.

Using the [`TimeZone`](./trait.TimeZone.html) methods
on the Local struct is the preferred way to construct `DateTime<Local>`
instances.

# Example

```
use chrono::{DateTime, Local, TimeZone};

let dt1: DateTime<Local> = Local::now();
let dt2: DateTime<Local> = Local.timestamp_opt(0, 0).unwrap();
assert!(dt1 >= dt2);
```"""

    @staticmethod
    def today() -> object: ...

    @staticmethod
    def now() -> object: ...

    @staticmethod
    def from_offset(_offset: FixedOffset) -> "Local": ...

    def offset_from_local_date(self, local: NaiveDate) -> object: ...

    def offset_from_local_datetime(self, local: NaiveDateTime) -> object: ...

    def offset_from_utc_date(self, utc: NaiveDate) -> FixedOffset: ...

    def offset_from_utc_datetime(self, utc: NaiveDateTime) -> FixedOffset: ...

class Date:
    """ISO 8601 calendar date with time zone.

You almost certainly want to be using a [`NaiveDate`] instead of this type.

This type primarily exists to aid in the construction of DateTimes that
have a timezone by way of the [`TimeZone`] datelike constructors (e.g.
[`TimeZone::ymd`]).

This type should be considered ambiguous at best, due to the inherent lack
of precision required for the time zone resolution.

There are some guarantees on the usage of `Date<Tz>`:

- If properly constructed via [`TimeZone::ymd`] and others without an error,
the corresponding local date should exist for at least a moment.
(It may still have a gap from the offset changes.)

- The `TimeZone` is free to assign *any* [`Offset`](crate::offset::Offset) to the
local date, as long as that offset did occur in given day.

For example, if `2015-03-08T01:59-08:00` is followed by `2015-03-08T03:00-07:00`,
it may produce either `2015-03-08-08:00` or `2015-03-08-07:00`
but *not* `2015-03-08+00:00` and others.

- Once constructed as a full `DateTime`, [`DateTime::date`] and other associated
methods should return those for the original `Date`. For example, if `dt =
tz.ymd_opt(y,m,d).unwrap().hms(h,n,s)` were valid, `dt.date() == tz.ymd_opt(y,m,d).unwrap()`.

- The date is timezone-agnostic up to one day (i.e. practically always),
so the local date and UTC date should be equal for most cases
even though the raw calculation between `NaiveDate` and `TimeDelta` may not."""

    @staticmethod
    def from_(date: object) -> "Date": ...

    @staticmethod
    def from_utc(date: NaiveDate, offset: Offset) -> object: ...

    def and_time(self, time: NaiveTime) -> object | None: ...

    def and_hms(self, hour: int, min: int, sec: int) -> object: ...

    def and_hms_opt(self, hour: int, min: int, sec: int) -> object | None: ...

    def and_hms_milli(self, hour: int, min: int, sec: int, milli: int) -> object: ...

    def and_hms_milli_opt(self, hour: int, min: int, sec: int, milli: int) -> object | None: ...

    def and_hms_micro(self, hour: int, min: int, sec: int, micro: int) -> object: ...

    def and_hms_micro_opt(self, hour: int, min: int, sec: int, micro: int) -> object | None: ...

    def and_hms_nano(self, hour: int, min: int, sec: int, nano: int) -> object: ...

    def and_hms_nano_opt(self, hour: int, min: int, sec: int, nano: int) -> object | None: ...

    def succ(self) -> object: ...

    def succ_opt(self) -> object | None: ...

    def pred(self) -> object: ...

    def pred_opt(self) -> object | None: ...

    def offset(self) -> Offset: ...

    def timezone(self) -> Tz: ...

    def with_timezone(self, tz: Tz2) -> object: ...

    def checked_add_signed(self, rhs: TimeDelta) -> object | None: ...

    def checked_sub_signed(self, rhs: TimeDelta) -> object | None: ...

    def signed_duration_since(self, rhs: object) -> TimeDelta: ...

    def naive_utc(self) -> NaiveDate: ...

    def naive_local(self) -> NaiveDate: ...

    def years_since(self, base: Self) -> int | None: ...

    def format_with_items(self, items: I) -> object: ...

    def format(self, fmt: object) -> object: ...

    def format_localized_with_items(self, items: I, locale: Locale) -> object: ...

    def format_localized(self, fmt: object, locale: Locale) -> object: ...

    def year(self) -> int: ...

    def month(self) -> int: ...

    def month0(self) -> int: ...

    def day(self) -> int: ...

    def day0(self) -> int: ...

    def ordinal(self) -> int: ...

    def ordinal0(self) -> int: ...

    def weekday(self) -> Weekday: ...

    def iso_week(self) -> IsoWeek: ...

    def with_year(self, year: int) -> object | None: ...

    def with_month(self, month: int) -> object | None: ...

    def with_month0(self, month0: int) -> object | None: ...

    def with_day(self, day: int) -> object | None: ...

    def with_day0(self, day0: int) -> object | None: ...

    def with_ordinal(self, ordinal: int) -> object | None: ...

    def with_ordinal0(self, ordinal0: int) -> object | None: ...

    def eq(self, other: object) -> bool: ...

    def partial_cmp(self, other: object) -> Ordering | None: ...

    def cmp(self, other: object) -> Ordering: ...

    def hash(self, state: H) -> None: ...

    def add(self, rhs: TimeDelta) -> object: ...

    def add_assign(self, rhs: TimeDelta) -> None: ...

    def sub(self, rhs: TimeDelta) -> object: ...

    def sub_assign(self, rhs: TimeDelta) -> None: ...

    def sub(self, rhs: object) -> TimeDelta: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def arbitrary(u: Unstructured) -> object: ...

class NaiveDateTime:
    """ISO 8601 combined date and time without timezone.

# Example

`NaiveDateTime` is commonly created from [`NaiveDate`].

```
use chrono::{NaiveDate, NaiveDateTime};

let dt: NaiveDateTime =
NaiveDate::from_ymd_opt(2016, 7, 8).unwrap().and_hms_opt(9, 10, 11).unwrap();
# let _ = dt;
```

You can use typical [date-like](Datelike) and [time-like](Timelike) methods,
provided that relevant traits are in the scope.

```
# use chrono::{NaiveDate, NaiveDateTime};
# let dt: NaiveDateTime = NaiveDate::from_ymd_opt(2016, 7, 8).unwrap().and_hms_opt(9, 10, 11).unwrap();
use chrono::{Datelike, Timelike, Weekday};

assert_eq!(dt.weekday(), Weekday::Fri);
assert_eq!(dt.num_seconds_from_midnight(), 33011);
```"""

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def new(date: NaiveDate, time: NaiveTime) -> "NaiveDateTime": ...

    @staticmethod
    def from_timestamp(secs: int, nsecs: int) -> "NaiveDateTime": ...

    @staticmethod
    def from_timestamp_millis(millis: int) -> NaiveDateTime | None: ...

    @staticmethod
    def from_timestamp_micros(micros: int) -> NaiveDateTime | None: ...

    @staticmethod
    def from_timestamp_nanos(nanos: int) -> NaiveDateTime | None: ...

    @staticmethod
    def from_timestamp_opt(secs: int, nsecs: int) -> NaiveDateTime | None: ...

    @staticmethod
    def parse_from_str(s: str, fmt: str) -> object: ...

    @staticmethod
    def parse_and_remainder(s: object, fmt: str) -> object: ...

    def date(self) -> NaiveDate: ...

    def time(self) -> NaiveTime: ...

    def timestamp(self) -> int: ...

    def timestamp_millis(self) -> int: ...

    def timestamp_micros(self) -> int: ...

    def timestamp_nanos(self) -> int: ...

    def timestamp_nanos_opt(self) -> int | None: ...

    def timestamp_subsec_millis(self) -> int: ...

    def timestamp_subsec_micros(self) -> int: ...

    def timestamp_subsec_nanos(self) -> int: ...

    def checked_add_signed(self, rhs: TimeDelta) -> NaiveDateTime | None: ...

    def checked_add_months(self, rhs: Months) -> NaiveDateTime | None: ...

    def checked_add_offset(self, rhs: FixedOffset) -> NaiveDateTime | None: ...

    def checked_sub_offset(self, rhs: FixedOffset) -> NaiveDateTime | None: ...

    def checked_sub_signed(self, rhs: TimeDelta) -> NaiveDateTime | None: ...

    def checked_sub_months(self, rhs: Months) -> NaiveDateTime | None: ...

    def checked_add_days(self, days: Days) -> object: ...

    def checked_sub_days(self, days: Days) -> object: ...

    def signed_duration_since(self, rhs: NaiveDateTime) -> TimeDelta: ...

    def format_with_items(self, items: I) -> object: ...

    def format(self, fmt: object) -> object: ...

    def and_local_timezone(self, tz: Tz) -> object: ...

    def and_utc(self) -> object: ...

    @staticmethod
    def from_(date: NaiveDate) -> "NaiveDateTime": ...

    def year(self) -> int: ...

    def month(self) -> int: ...

    def month0(self) -> int: ...

    def day(self) -> int: ...

    def day0(self) -> int: ...

    def ordinal(self) -> int: ...

    def ordinal0(self) -> int: ...

    def weekday(self) -> Weekday: ...

    def iso_week(self) -> IsoWeek: ...

    def with_year(self, year: int) -> NaiveDateTime | None: ...

    def with_month(self, month: int) -> NaiveDateTime | None: ...

    def with_month0(self, month0: int) -> NaiveDateTime | None: ...

    def with_day(self, day: int) -> NaiveDateTime | None: ...

    def with_day0(self, day0: int) -> NaiveDateTime | None: ...

    def with_ordinal(self, ordinal: int) -> NaiveDateTime | None: ...

    def with_ordinal0(self, ordinal0: int) -> NaiveDateTime | None: ...

    def hour(self) -> int: ...

    def minute(self) -> int: ...

    def second(self) -> int: ...

    def nanosecond(self) -> int: ...

    def with_hour(self, hour: int) -> NaiveDateTime | None: ...

    def with_minute(self, min: int) -> NaiveDateTime | None: ...

    def with_second(self, sec: int) -> NaiveDateTime | None: ...

    def with_nanosecond(self, nano: int) -> NaiveDateTime | None: ...

    def add(self, rhs: TimeDelta) -> NaiveDateTime: ...

    def add(self, rhs: Duration) -> NaiveDateTime: ...

    def add_assign(self, rhs: TimeDelta) -> None: ...

    def add_assign(self, rhs: Duration) -> None: ...

    def add(self, rhs: FixedOffset) -> NaiveDateTime: ...

    def add(self, rhs: Months) -> Output: ...

    def sub(self, rhs: TimeDelta) -> NaiveDateTime: ...

    def sub(self, rhs: Duration) -> NaiveDateTime: ...

    def sub_assign(self, rhs: TimeDelta) -> None: ...

    def sub_assign(self, rhs: Duration) -> None: ...

    def sub(self, rhs: FixedOffset) -> NaiveDateTime: ...

    def sub(self, rhs: Months) -> Output: ...

    def sub(self, rhs: NaiveDateTime) -> TimeDelta: ...

    def add(self, days: Days) -> Output: ...

    def sub(self, days: Days) -> Output: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    @staticmethod
    def default() -> "NaiveDateTime": ...

    def duration_round(self, duration: TimeDelta) -> object: ...

    def duration_trunc(self, duration: TimeDelta) -> object: ...

    def duration_round_up(self, duration: TimeDelta) -> object: ...

class NaiveDate:
    """ISO 8601 calendar date without timezone.
Allows for every [proleptic Gregorian date] from Jan 1, 262145 BCE to Dec 31, 262143 CE.
Also supports the conversion from ISO 8601 ordinal and week date.

# Calendar Date

The ISO 8601 **calendar date** follows the proleptic Gregorian calendar.
It is like a normal civil calendar but note some slight differences:

* Dates before the Gregorian calendar's inception in 1582 are defined via the extrapolation.
Be careful, as historical dates are often noted in the Julian calendar and others
and the transition to Gregorian may differ across countries (as late as early 20C).

(Some example: Both Shakespeare from Britain and Cervantes from Spain seemingly died
on the same calendar date---April 23, 1616---but in the different calendar.
Britain used the Julian calendar at that time, so Shakespeare's death is later.)

* ISO 8601 calendars have the year 0, which is 1 BCE (a year before 1 CE).
If you need a typical BCE/BC and CE/AD notation for year numbers,
use the [`Datelike::year_ce`] method.

# Week Date

The ISO 8601 **week date** is a triple of year number, week number
and [day of the week](Weekday) with the following rules:

* A week consists of Monday through Sunday, and is always numbered within some year.
The week number ranges from 1 to 52 or 53 depending on the year.

* The week 1 of given year is defined as the first week containing January 4 of that year,
or equivalently, the first week containing four or more days in that year.

* The year number in the week date may *not* correspond to the actual Gregorian year.
For example, January 3, 2016 (Sunday) was on the last (53rd) week of 2015.

Chrono's date types default to the ISO 8601 [calendar date](#calendar-date), but
[`Datelike::iso_week`] and [`Datelike::weekday`] methods can be used to get the corresponding
week date.

# Ordinal Date

The ISO 8601 **ordinal date** is a pair of year number and day of the year ("ordinal").
The ordinal number ranges from 1 to 365 or 366 depending on the year.
The year number is the same as that of the [calendar date](#calendar-date).

This is currently the internal format of Chrono's date types.

[proleptic Gregorian date]: crate::NaiveDate#calendar-date"""

    @staticmethod
    def arbitrary(u: Unstructured) -> "NaiveDate": ...

    @staticmethod
    def from_ymd(year: int, month: int, day: int) -> "NaiveDate": ...

    @staticmethod
    def from_ymd_opt(year: int, month: int, day: int) -> NaiveDate | None: ...

    @staticmethod
    def from_yo(year: int, ordinal: int) -> "NaiveDate": ...

    @staticmethod
    def from_yo_opt(year: int, ordinal: int) -> NaiveDate | None: ...

    @staticmethod
    def from_isoywd(year: int, week: int, weekday: Weekday) -> "NaiveDate": ...

    @staticmethod
    def from_isoywd_opt(year: int, week: int, weekday: Weekday) -> NaiveDate | None: ...

    @staticmethod
    def from_num_days_from_ce(days: int) -> "NaiveDate": ...

    @staticmethod
    def from_num_days_from_ce_opt(days: int) -> NaiveDate | None: ...

    @staticmethod
    def from_epoch_days(days: int) -> NaiveDate | None: ...

    @staticmethod
    def from_weekday_of_month(year: int, month: int, weekday: Weekday, n: int) -> "NaiveDate": ...

    @staticmethod
    def from_weekday_of_month_opt(year: int, month: int, weekday: Weekday, n: int) -> NaiveDate | None: ...

    @staticmethod
    def parse_from_str(s: str, fmt: str) -> object: ...

    @staticmethod
    def parse_and_remainder(s: object, fmt: str) -> object: ...

    def checked_add_months(self, months: Months) -> object: ...

    def checked_sub_months(self, months: Months) -> object: ...

    def checked_add_days(self, days: Days) -> object: ...

    def checked_sub_days(self, days: Days) -> object: ...

    def and_time(self, time: NaiveTime) -> NaiveDateTime: ...

    def and_hms(self, hour: int, min: int, sec: int) -> NaiveDateTime: ...

    def and_hms_opt(self, hour: int, min: int, sec: int) -> NaiveDateTime | None: ...

    def and_hms_milli(self, hour: int, min: int, sec: int, milli: int) -> NaiveDateTime: ...

    def and_hms_milli_opt(self, hour: int, min: int, sec: int, milli: int) -> NaiveDateTime | None: ...

    def and_hms_micro(self, hour: int, min: int, sec: int, micro: int) -> NaiveDateTime: ...

    def and_hms_micro_opt(self, hour: int, min: int, sec: int, micro: int) -> NaiveDateTime | None: ...

    def and_hms_nano(self, hour: int, min: int, sec: int, nano: int) -> NaiveDateTime: ...

    def and_hms_nano_opt(self, hour: int, min: int, sec: int, nano: int) -> NaiveDateTime | None: ...

    def succ(self) -> NaiveDate: ...

    def succ_opt(self) -> NaiveDate | None: ...

    def pred(self) -> NaiveDate: ...

    def pred_opt(self) -> NaiveDate | None: ...

    def checked_add_signed(self, rhs: TimeDelta) -> NaiveDate | None: ...

    def checked_sub_signed(self, rhs: TimeDelta) -> NaiveDate | None: ...

    def signed_duration_since(self, rhs: NaiveDate) -> TimeDelta: ...

    def years_since(self, base: Self) -> int | None: ...

    def format_with_items(self, items: I) -> object: ...

    def format(self, fmt: object) -> object: ...

    def format_localized_with_items(self, items: I, locale: Locale) -> object: ...

    def format_localized(self, fmt: object, locale: Locale) -> object: ...

    def iter_days(self) -> NaiveDateDaysIterator: ...

    def iter_weeks(self) -> NaiveDateWeeksIterator: ...

    def week(self, start: Weekday) -> NaiveWeek: ...

    def leap_year(self) -> bool: ...

    def to_epoch_days(self) -> int: ...

    def year(self) -> int: ...

    def month(self) -> int: ...

    def month0(self) -> int: ...

    def day(self) -> int: ...

    def day0(self) -> int: ...

    def ordinal(self) -> int: ...

    def ordinal0(self) -> int: ...

    def weekday(self) -> Weekday: ...

    def iso_week(self) -> IsoWeek: ...

    def with_year(self, year: int) -> NaiveDate | None: ...

    def with_month(self, month: int) -> NaiveDate | None: ...

    def with_month0(self, month0: int) -> NaiveDate | None: ...

    def with_day(self, day: int) -> NaiveDate | None: ...

    def with_day0(self, day0: int) -> NaiveDate | None: ...

    def with_ordinal(self, ordinal: int) -> NaiveDate | None: ...

    def with_ordinal0(self, ordinal0: int) -> NaiveDate | None: ...

    def add(self, rhs: TimeDelta) -> NaiveDate: ...

    def add_assign(self, rhs: TimeDelta) -> None: ...

    def add(self, months: Months) -> Output: ...

    def sub(self, months: Months) -> Output: ...

    def add(self, days: Days) -> Output: ...

    def sub(self, days: Days) -> Output: ...

    def sub(self, rhs: TimeDelta) -> NaiveDate: ...

    def sub_assign(self, rhs: TimeDelta) -> None: ...

    def sub(self, rhs: NaiveDate) -> TimeDelta: ...

    @staticmethod
    def from_(naive_datetime: NaiveDateTime) -> "NaiveDate": ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    @staticmethod
    def default() -> "NaiveDate": ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

class NaiveDateDaysIterator:
    """Iterator over `NaiveDate` with a step size of one day."""

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

class NaiveDateWeeksIterator:
    """Iterator over `NaiveDate` with a step size of one week."""

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

class YearFlags:
    """Year flags (aka the dominical letter).

`YearFlags` are used as the last four bits of `NaiveDate`, `Mdf` and `IsoWeek`.

There are 14 possible classes of year in the Gregorian calendar:
common and leap years starting with Monday through Sunday.

The `YearFlags` stores this information into 4 bits `LWWW`. `L` is the leap year flag, with `1`
for the common year (this simplifies validating an ordinal in `NaiveDate`). `WWW` is a non-zero
`Weekday` of the last day in the preceding year."""

    @staticmethod
    def from_year(year: int) -> "YearFlags": ...

    def fmt(self, f: Formatter) -> Result: ...

class NaiveWeek:
    """A week represented by a [`NaiveDate`] and a [`Weekday`] which is the first
day of the week."""

    def first_day(self) -> NaiveDate: ...

    def checked_first_day(self) -> NaiveDate | None: ...

    def last_day(self) -> NaiveDate: ...

    def checked_last_day(self) -> NaiveDate | None: ...

    def days(self) -> object: ...

    def checked_days(self) -> object | None: ...

    def eq(self, other: Self) -> bool: ...

    def hash(self, state: H) -> None: ...

class Days:
    """A duration in calendar days.

This is useful because when using `TimeDelta` it is possible that adding `TimeDelta::days(1)`
doesn't increment the day value as expected due to it being a fixed number of seconds. This
difference applies only when dealing with `DateTime<TimeZone>` data types and in other cases
`TimeDelta::days(n)` and `Days::new(n)` are equivalent."""

    @staticmethod
    def new(num: int) -> "Days": ...

class NaiveTime:
    """ISO 8601 time without timezone.
Allows for the nanosecond precision and optional leap second representation.

# Leap Second Handling

Since 1960s, the manmade atomic clock has been so accurate that
it is much more accurate than Earth's own motion.
It became desirable to define the civil time in terms of the atomic clock,
but that risks the desynchronization of the civil time from Earth.
To account for this, the designers of the Coordinated Universal Time (UTC)
made that the UTC should be kept within 0.9 seconds of the observed Earth-bound time.
When the mean solar day is longer than the ideal (86,400 seconds),
the error slowly accumulates and it is necessary to add a **leap second**
to slow the UTC down a bit.
(We may also remove a second to speed the UTC up a bit, but it never happened.)
The leap second, if any, follows 23:59:59 of June 30 or December 31 in the UTC.

Fast forward to the 21st century,
we have seen 26 leap seconds from January 1972 to December 2015.
Yes, 26 seconds. Probably you can read this paragraph within 26 seconds.
But those 26 seconds, and possibly more in the future, are never predictable,
and whether to add a leap second or not is known only before 6 months.
Internet-based clocks (via NTP) do account for known leap seconds,
but the system API normally doesn't (and often can't, with no network connection)
and there is no reliable way to retrieve leap second information.

Chrono does not try to accurately implement leap seconds; it is impossible.
Rather, **it allows for leap seconds but behaves as if there are *no other* leap seconds.**
Various operations will ignore any possible leap second(s)
except when any of the operands were actually leap seconds.

If you cannot tolerate this behavior,
you must use a separate `TimeZone` for the International Atomic Time (TAI).
TAI is like UTC but has no leap seconds, and thus slightly differs from UTC.
Chrono does not yet provide such implementation, but it is planned.

## Representing Leap Seconds

The leap second is indicated via fractional seconds more than 1 second.
This makes possible to treat a leap second as the prior non-leap second
if you don't care about sub-second accuracy.
You should use the proper formatting to get the raw leap second.

All methods accepting fractional seconds will accept such values.

```
use chrono::{NaiveDate, NaiveTime};

let t = NaiveTime::from_hms_milli_opt(8, 59, 59, 1_000).unwrap();

let dt1 = NaiveDate::from_ymd_opt(2015, 7, 1)
.unwrap()
.and_hms_micro_opt(8, 59, 59, 1_000_000)
.unwrap();

let dt2 = NaiveDate::from_ymd_opt(2015, 6, 30)
.unwrap()
.and_hms_nano_opt(23, 59, 59, 1_000_000_000)
.unwrap()
.and_utc();
# let _ = (t, dt1, dt2);
```

Note that the leap second can happen anytime given an appropriate time zone;
2015-07-01 01:23:60 would be a proper leap second if UTC+01:24 had existed.
Practically speaking, though, by the time of the first leap second on 1972-06-30,
every time zone offset around the world has standardized to the 5-minute alignment.

## Date And Time Arithmetic

As a concrete example, let's assume that `03:00:60` and `04:00:60` are leap seconds.
In reality, of course, leap seconds are separated by at least 6 months.
We will also use some intuitive concise notations for the explanation.

`Time + TimeDelta`
(short for [`NaiveTime::overflowing_add_signed`](#method.overflowing_add_signed)):

- `03:00:00 + 1s = 03:00:01`.
- `03:00:59 + 60s = 03:01:59`.
- `03:00:59 + 61s = 03:02:00`.
- `03:00:59 + 1s = 03:01:00`.
- `03:00:60 + 1s = 03:01:00`.
Note that the sum is identical to the previous.
- `03:00:60 + 60s = 03:01:59`.
- `03:00:60 + 61s = 03:02:00`.
- `03:00:60.1 + 0.8s = 03:00:60.9`.

`Time - TimeDelta`
(short for [`NaiveTime::overflowing_sub_signed`](#method.overflowing_sub_signed)):

- `03:00:00 - 1s = 02:59:59`.
- `03:01:00 - 1s = 03:00:59`.
- `03:01:00 - 60s = 03:00:00`.
- `03:00:60 - 60s = 03:00:00`.
Note that the result is identical to the previous.
- `03:00:60.7 - 0.4s = 03:00:60.3`.
- `03:00:60.7 - 0.9s = 03:00:59.8`.

`Time - Time`
(short for [`NaiveTime::signed_duration_since`](#method.signed_duration_since)):

- `04:00:00 - 03:00:00 = 3600s`.
- `03:01:00 - 03:00:00 = 60s`.
- `03:00:60 - 03:00:00 = 60s`.
Note that the difference is identical to the previous.
- `03:00:60.6 - 03:00:59.4 = 1.2s`.
- `03:01:00 - 03:00:59.8 = 0.2s`.
- `03:01:00 - 03:00:60.5 = 0.5s`.
Note that the difference is larger than the previous,
even though the leap second clearly follows the previous whole second.
- `04:00:60.9 - 03:00:60.1 =
(04:00:60.9 - 04:00:00) + (04:00:00 - 03:01:00) + (03:01:00 - 03:00:60.1) =
60.9s + 3540s + 0.9s = 3601.8s`.

In general,

- `Time + TimeDelta` unconditionally equals to `TimeDelta + Time`.

- `Time - TimeDelta` unconditionally equals to `Time + (-TimeDelta)`.

- `Time1 - Time2` unconditionally equals to `-(Time2 - Time1)`.

- Associativity does not generally hold, because
`(Time + TimeDelta1) - TimeDelta2` no longer equals to `Time + (TimeDelta1 - TimeDelta2)`
for two positive durations.

- As a special case, `(Time + TimeDelta) - TimeDelta` also does not equal to `Time`.

- If you can assume that all durations have the same sign, however,
then the associativity holds:
`(Time + TimeDelta1) + TimeDelta2` equals to `Time + (TimeDelta1 + TimeDelta2)`
for two positive durations.

## Reading And Writing Leap Seconds

The "typical" leap seconds on the minute boundary are
correctly handled both in the formatting and parsing.
The leap second in the human-readable representation
will be represented as the second part being 60, as required by ISO 8601.

```
use chrono::NaiveDate;

let dt = NaiveDate::from_ymd_opt(2015, 6, 30)
.unwrap()
.and_hms_milli_opt(23, 59, 59, 1_000)
.unwrap()
.and_utc();
assert_eq!(format!("{:?}", dt), "2015-06-30T23:59:60Z");
```

There are hypothetical leap seconds not on the minute boundary nevertheless supported by Chrono.
They are allowed for the sake of completeness and consistency; there were several "exotic" time
zone offsets with fractional minutes prior to UTC after all.
For such cases the human-readable representation is ambiguous and would be read back to the next
non-leap second.

A `NaiveTime` with a leap second that is not on a minute boundary can only be created from a
[`DateTime`](crate::DateTime) with fractional minutes as offset, or using
[`Timelike::with_nanosecond()`].

```
use chrono::{FixedOffset, NaiveDate, TimeZone};

let paramaribo_pre1945 = FixedOffset::east_opt(-13236).unwrap(); // -03:40:36
let leap_sec_2015 =
NaiveDate::from_ymd_opt(2015, 6, 30).unwrap().and_hms_milli_opt(23, 59, 59, 1_000).unwrap();
let dt1 = paramaribo_pre1945.from_utc_datetime(&leap_sec_2015);
assert_eq!(format!("{:?}", dt1), "2015-06-30T20:19:24-03:40:36");
assert_eq!(format!("{:?}", dt1.time()), "20:19:24");

let next_sec = NaiveDate::from_ymd_opt(2015, 7, 1).unwrap().and_hms_opt(0, 0, 0).unwrap();
let dt2 = paramaribo_pre1945.from_utc_datetime(&next_sec);
assert_eq!(format!("{:?}", dt2), "2015-06-30T20:19:24-03:40:36");
assert_eq!(format!("{:?}", dt2.time()), "20:19:24");

assert!(dt1.time() != dt2.time());
assert!(dt1.time().to_string() == dt2.time().to_string());
```

Since Chrono alone cannot determine any existence of leap seconds,
**there is absolutely no guarantee that the leap second read has actually happened**."""

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def arbitrary(u: Unstructured) -> "NaiveTime": ...

    @staticmethod
    def from_hms(hour: int, min: int, sec: int) -> "NaiveTime": ...

    @staticmethod
    def from_hms_opt(hour: int, min: int, sec: int) -> NaiveTime | None: ...

    @staticmethod
    def from_hms_milli(hour: int, min: int, sec: int, milli: int) -> "NaiveTime": ...

    @staticmethod
    def from_hms_milli_opt(hour: int, min: int, sec: int, milli: int) -> NaiveTime | None: ...

    @staticmethod
    def from_hms_micro(hour: int, min: int, sec: int, micro: int) -> "NaiveTime": ...

    @staticmethod
    def from_hms_micro_opt(hour: int, min: int, sec: int, micro: int) -> NaiveTime | None: ...

    @staticmethod
    def from_hms_nano(hour: int, min: int, sec: int, nano: int) -> "NaiveTime": ...

    @staticmethod
    def from_hms_nano_opt(hour: int, min: int, sec: int, nano: int) -> NaiveTime | None: ...

    @staticmethod
    def from_num_seconds_from_midnight(secs: int, nano: int) -> "NaiveTime": ...

    @staticmethod
    def from_num_seconds_from_midnight_opt(secs: int, nano: int) -> NaiveTime | None: ...

    @staticmethod
    def parse_from_str(s: str, fmt: str) -> object: ...

    @staticmethod
    def parse_and_remainder(s: object, fmt: str) -> object: ...

    def overflowing_add_signed(self, rhs: TimeDelta) -> object: ...

    def overflowing_sub_signed(self, rhs: TimeDelta) -> object: ...

    def signed_duration_since(self, rhs: NaiveTime) -> TimeDelta: ...

    def format_with_items(self, items: I) -> object: ...

    def format(self, fmt: object) -> object: ...

    def hour(self) -> int: ...

    def minute(self) -> int: ...

    def second(self) -> int: ...

    def nanosecond(self) -> int: ...

    def with_hour(self, hour: int) -> NaiveTime | None: ...

    def with_minute(self, min: int) -> NaiveTime | None: ...

    def with_second(self, sec: int) -> NaiveTime | None: ...

    def with_nanosecond(self, nano: int) -> NaiveTime | None: ...

    def num_seconds_from_midnight(self) -> int: ...

    def add(self, rhs: TimeDelta) -> NaiveTime: ...

    def add_assign(self, rhs: TimeDelta) -> None: ...

    def add(self, rhs: Duration) -> NaiveTime: ...

    def add_assign(self, rhs: Duration) -> None: ...

    def add(self, rhs: FixedOffset) -> NaiveTime: ...

    def sub(self, rhs: TimeDelta) -> NaiveTime: ...

    def sub_assign(self, rhs: TimeDelta) -> None: ...

    def sub(self, rhs: Duration) -> NaiveTime: ...

    def sub_assign(self, rhs: Duration) -> None: ...

    def sub(self, rhs: FixedOffset) -> NaiveTime: ...

    def sub(self, rhs: NaiveTime) -> TimeDelta: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    @staticmethod
    def default() -> "NaiveTime": ...

class IsoWeek:
    """ISO 8601 week.

This type, combined with [`Weekday`](../enum.Weekday.html),
constitutes the ISO 8601 [week date](./struct.NaiveDate.html#week-date).
One can retrieve this type from the existing [`Datelike`](../trait.Datelike.html) types
via the [`Datelike::iso_week`](../trait.Datelike.html#tymethod.iso_week) method."""

    def year(self) -> int: ...

    def week(self) -> int: ...

    def week0(self) -> int: ...

    def fmt(self, f: Formatter) -> Result: ...

class TimeDelta:
    """Time duration with nanosecond precision.

This also allows for negative durations; see individual methods for details.

A `TimeDelta` is represented internally as a complement of seconds and
nanoseconds. The range is restricted to that of `i64` milliseconds, with the
minimum value notably being set to `-i64::MAX` rather than allowing the full
range of `i64::MIN`. This is to allow easy flipping of sign, so that for
instance `abs()` can be called without any checks."""

    @staticmethod
    def new(secs: int, nanos: int) -> TimeDelta | None: ...

    @staticmethod
    def weeks(weeks: int) -> "TimeDelta": ...

    @staticmethod
    def try_weeks(weeks: int) -> TimeDelta | None: ...

    @staticmethod
    def days(days: int) -> "TimeDelta": ...

    @staticmethod
    def try_days(days: int) -> TimeDelta | None: ...

    @staticmethod
    def hours(hours: int) -> "TimeDelta": ...

    @staticmethod
    def try_hours(hours: int) -> TimeDelta | None: ...

    @staticmethod
    def minutes(minutes: int) -> "TimeDelta": ...

    @staticmethod
    def try_minutes(minutes: int) -> TimeDelta | None: ...

    @staticmethod
    def seconds(seconds: int) -> "TimeDelta": ...

    @staticmethod
    def try_seconds(seconds: int) -> TimeDelta | None: ...

    @staticmethod
    def milliseconds(milliseconds: int) -> "TimeDelta": ...

    @staticmethod
    def try_milliseconds(milliseconds: int) -> TimeDelta | None: ...

    @staticmethod
    def microseconds(microseconds: int) -> "TimeDelta": ...

    @staticmethod
    def nanoseconds(nanos: int) -> "TimeDelta": ...

    def num_weeks(self) -> int: ...

    def num_days(self) -> int: ...

    def num_hours(self) -> int: ...

    def num_minutes(self) -> int: ...

    def num_seconds(self) -> int: ...

    def as_seconds_f64(self) -> float: ...

    def as_seconds_f32(self) -> float: ...

    def num_milliseconds(self) -> int: ...

    def subsec_millis(self) -> int: ...

    def num_microseconds(self) -> int | None: ...

    def subsec_micros(self) -> int: ...

    def num_nanoseconds(self) -> int | None: ...

    def subsec_nanos(self) -> int: ...

    def checked_add(self, rhs: TimeDelta) -> TimeDelta | None: ...

    def checked_sub(self, rhs: TimeDelta) -> TimeDelta | None: ...

    def checked_mul(self, rhs: int) -> TimeDelta | None: ...

    def checked_div(self, rhs: int) -> TimeDelta | None: ...

    def abs(self) -> TimeDelta: ...

    @staticmethod
    def min_value() -> "TimeDelta": ...

    @staticmethod
    def max_value() -> "TimeDelta": ...

    @staticmethod
    def zero() -> "TimeDelta": ...

    def is_zero(self) -> bool: ...

    @staticmethod
    def from_std(duration: Duration) -> "TimeDelta": ...

    def to_std(self) -> Duration: ...

    def neg(self) -> TimeDelta: ...

    def add(self, rhs: TimeDelta) -> TimeDelta: ...

    def sub(self, rhs: TimeDelta) -> TimeDelta: ...

    def add_assign(self, rhs: TimeDelta) -> None: ...

    def sub_assign(self, rhs: TimeDelta) -> None: ...

    def mul(self, rhs: int) -> TimeDelta: ...

    def div(self, rhs: int) -> TimeDelta: ...

    @staticmethod
    def sum(iter: I) -> "TimeDelta": ...

    @staticmethod
    def sum(iter: I) -> "TimeDelta": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def arbitrary(u: Unstructured) -> "TimeDelta": ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

class OutOfRangeError:
    """Represents error when converting `TimeDelta` to/from a standard library
implementation

The `std::time::Duration` supports a range from zero to `u64::MAX`
*seconds*, while this module supports signed range of up to
`i64::MAX` of *milliseconds*."""

    def fmt(self, f: Formatter) -> Result: ...

    def description(self) -> str: ...

class WeekdaySet:
    """A collection of [`Weekday`]s stored as a single byte.

This type is `Copy` and provides efficient set-like and slice-like operations.
Many operations are `const` as well.

Implemented as a bitmask where bits 1-7 correspond to Monday-Sunday."""

    @staticmethod
    def from_array(days: object) -> "WeekdaySet": ...

    @staticmethod
    def single(weekday: Weekday) -> "WeekdaySet": ...

    def single_day(self) -> Weekday | None: ...

    def insert(self, day: Weekday) -> bool: ...

    def remove(self, day: Weekday) -> bool: ...

    def is_subset(self, other: Self) -> bool: ...

    def intersection(self, other: Self) -> Self: ...

    def union(self, other: Self) -> Self: ...

    def symmetric_difference(self, other: Self) -> Self: ...

    def difference(self, other: Self) -> Self: ...

    def first(self) -> Weekday | None: ...

    def last(self) -> Weekday | None: ...

    def iter(self, start: Weekday) -> WeekdaySetIter: ...

    def contains(self, day: Weekday) -> bool: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_iter(iter: T) -> "WeekdaySet": ...

class WeekdaySetIter:
    """An iterator over a collection of weekdays, starting from a given day.

See [`WeekdaySet::iter()`]."""

    def next(self) -> Item | None: ...

    def next_back(self) -> Item | None: ...

    def len(self) -> int: ...

class Weekday:
    """The day of week.

The order of the days of week depends on the context.
(This is why this type does *not* implement `PartialOrd` or `Ord` traits.)
One should prefer `*_from_monday` or `*_from_sunday` methods to get the correct result.

# Example
```
use chrono::Weekday;

let monday = "Monday".parse::<Weekday>().unwrap();
assert_eq!(monday, Weekday::Mon);

let sunday = Weekday::try_from(6).unwrap();
assert_eq!(sunday, Weekday::Sun);

assert_eq!(sunday.num_days_from_monday(), 6); // starts counting with Monday = 0
assert_eq!(sunday.number_from_monday(), 7); // starts counting with Monday = 1
assert_eq!(sunday.num_days_from_sunday(), 0); // starts counting with Sunday = 0
assert_eq!(sunday.number_from_sunday(), 1); // starts counting with Sunday = 1

assert_eq!(sunday.succ(), monday);
assert_eq!(sunday.pred(), Weekday::Sat);
```"""
    Mon: "Weekday"
    Tue: "Weekday"
    Wed: "Weekday"
    Thu: "Weekday"
    Fri: "Weekday"
    Sat: "Weekday"
    Sun: "Weekday"

    def succ(self) -> Weekday: ...

    def pred(self) -> Weekday: ...

    def number_from_monday(self) -> int: ...

    def number_from_sunday(self) -> int: ...

    def num_days_from_monday(self) -> int: ...

    def num_days_from_sunday(self) -> int: ...

    def days_since(self, other: Weekday) -> int: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def try_from(value: int) -> object: ...

    @staticmethod
    def from_i64(n: int) -> Weekday | None: ...

    @staticmethod
    def from_u64(n: int) -> Weekday | None: ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def from_str(s: str) -> object: ...

class Month:
    """The month of the year.

This enum is just a convenience implementation.
The month in dates created by DateLike objects does not return this enum.

It is possible to convert from a date to a month independently
```
use chrono::prelude::*;
let date = Utc.with_ymd_and_hms(2019, 10, 28, 9, 10, 11).unwrap();
// `2019-10-28T09:10:11Z`
let month = Month::try_from(u8::try_from(date.month()).unwrap()).ok();
assert_eq!(month, Some(Month::October))
```
Or from a Month to an integer usable by dates
```
# use chrono::prelude::*;
let month = Month::January;
let dt = Utc.with_ymd_and_hms(2019, month.number_from_month(), 28, 9, 10, 11).unwrap();
assert_eq!((dt.year(), dt.month(), dt.day()), (2019, 1, 28));
```
Allows mapping from and to month, from 1-January to 12-December.
Can be Serialized/Deserialized with serde"""
    January: "Month"
    February: "Month"
    March: "Month"
    April: "Month"
    May: "Month"
    June: "Month"
    July: "Month"
    August: "Month"
    September: "Month"
    October: "Month"
    November: "Month"
    December: "Month"

    def succ(self) -> Month: ...

    def pred(self) -> Month: ...

    def number_from_month(self) -> int: ...

    def name(self) -> object: ...

    def num_days(self, year: int) -> int | None: ...

    @staticmethod
    def try_from(value: int) -> object: ...

    @staticmethod
    def from_u64(n: int) -> Month | None: ...

    @staticmethod
    def from_i64(n: int) -> Month | None: ...

    @staticmethod
    def from_u32(n: int) -> Month | None: ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def from_str(s: str) -> object: ...

class SecondsFormat:
    """Specific formatting options for seconds. This may be extended in the
future, so exhaustive matching in external code is not recommended.

See the `TimeZone::to_rfc3339_opts` function for usage."""
    Secs: "SecondsFormat"
    Millis: "SecondsFormat"
    Micros: "SecondsFormat"
    Nanos: "SecondsFormat"
    AutoSi: "SecondsFormat"
    __NonExhaustive: "SecondsFormat"

class Pad:
    """Padding characters for numeric items."""
    None_: "Pad"
    Zero: "Pad"
    Space: "Pad"

class Numeric:
    """Numeric item types.
They have associated formatting width (FW) and parsing width (PW).

The **formatting width** is the minimal width to be formatted.
If the number is too short, and the padding is not [`Pad::None`](./enum.Pad.html#variant.None),
then it is left-padded.
If the number is too long or (in some cases) negative, it is printed as is.

The **parsing width** is the maximal width to be scanned.
The parser only tries to consume from one to given number of digits (greedily).
It also trims the preceding whitespace if any.
It cannot parse the negative number, so some date and time cannot be formatted then
parsed with the same formatting items."""
    Year: "Numeric"
    YearDiv100: "Numeric"
    YearMod100: "Numeric"
    IsoYear: "Numeric"
    IsoYearDiv100: "Numeric"
    IsoYearMod100: "Numeric"
    Quarter: "Numeric"
    Month: "Numeric"
    Day: "Numeric"
    WeekFromSun: "Numeric"
    WeekFromMon: "Numeric"
    IsoWeek: "Numeric"
    NumDaysFromSun: "Numeric"
    WeekdayFromMon: "Numeric"
    Ordinal: "Numeric"
    Hour: "Numeric"
    Hour12: "Numeric"
    Minute: "Numeric"
    Second: "Numeric"
    Nanosecond: "Numeric"
    Timestamp: "Numeric"
    Internal: "Numeric"

class Fixed:
    """Fixed-format item types.

They have their own rules of formatting and parsing.
Otherwise noted, they print in the specified cases but parse case-insensitively."""
    ShortMonthName: "Fixed"
    LongMonthName: "Fixed"
    ShortWeekdayName: "Fixed"
    LongWeekdayName: "Fixed"
    LowerAmPm: "Fixed"
    UpperAmPm: "Fixed"
    Nanosecond: "Fixed"
    Nanosecond3: "Fixed"
    Nanosecond6: "Fixed"
    Nanosecond9: "Fixed"
    TimezoneName: "Fixed"
    TimezoneOffsetColon: "Fixed"
    TimezoneOffsetDoubleColon: "Fixed"
    TimezoneOffsetTripleColon: "Fixed"
    TimezoneOffsetColonZ: "Fixed"
    TimezoneOffset: "Fixed"
    TimezoneOffsetZ: "Fixed"
    RFC2822: "Fixed"
    RFC3339: "Fixed"
    Internal: "Fixed"

class OffsetPrecision:
    """The precision of an offset from UTC formatting item."""
    Hours: "OffsetPrecision"
    Minutes: "OffsetPrecision"
    Seconds: "OffsetPrecision"
    OptionalMinutes: "OffsetPrecision"
    OptionalSeconds: "OffsetPrecision"
    OptionalMinutesAndSeconds: "OffsetPrecision"

class Colons:
    """The separator between hours and minutes in an offset."""
    None_: "Colons"
    Colon: "Colons"
    Maybe: "Colons"

class Item:
    """A single formatting item. This is used for both formatting and parsing."""
    Literal: "Item"
    OwnedLiteral: "Item"
    Space: "Item"
    OwnedSpace: "Item"
    Numeric: "Item"
    Fixed: "Item"
    Error: "Item"

    def to_owned(self) -> Item: ...

class ParseErrorKind:
    """The category of parse error"""
    OutOfRange: "ParseErrorKind"
    Impossible: "ParseErrorKind"
    NotEnough: "ParseErrorKind"
    Invalid: "ParseErrorKind"
    TooShort: "ParseErrorKind"
    TooLong: "ParseErrorKind"
    BadFormat: "ParseErrorKind"
    __Nonexhaustive: "ParseErrorKind"

class LocalResult:
    """Old name of [`MappedLocalTime`]. See that type for more documentation."""
    Single: "LocalResult"
    Ambiguous: "LocalResult"
    None_: "LocalResult"

class RoundingError:
    """An error from rounding by `TimeDelta`

See: [`DurationRound`]"""
    DurationExceedsTimestamp: "RoundingError"
    DurationExceedsLimit: "RoundingError"
    TimestampExceedsLimit: "RoundingError"

    def fmt(self, f: Formatter) -> Result: ...

    def description(self) -> str: ...

    def description(self) -> str: ...

"""Serialize a UTC datetime into an integer number of nanoseconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Errors

An `i64` with nanosecond precision can span a range of ~584 years. This function returns an
error on an out of range `DateTime`.

The dates that can be represented as nanoseconds are between 1677-09-21T00:12:44.0 and
2262-04-11T23:47:16.854775804.

# Example:

```rust
# use chrono::{DateTime, Utc, NaiveDate};
# use serde_derive::Serialize;
use chrono::serde::ts_nanoseconds::serialize as to_nano_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_nano_ts")]
time: DateTime<Utc>,
}

let my_s = S {
time: NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_nano_opt(02, 04, 59, 918355733)
.unwrap()
.and_utc(),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355733}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: object, serializer: S) -> Ok: ...

"""Deserialize a [`DateTime`] from a nanosecond timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, TimeZone, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_nanoseconds::deserialize as from_nano_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_nano_ts")]
time: DateTime<Utc>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355733 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(1526522699, 918355733).unwrap() });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(-1, 999_999_999).unwrap() });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object: ...

"""Serialize a UTC datetime into an integer number of nanoseconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Errors

An `i64` with nanosecond precision can span a range of ~584 years. This function returns an
error on an out of range `DateTime`.

The dates that can be represented as nanoseconds are between 1677-09-21T00:12:44.0 and
2262-04-11T23:47:16.854775804.

# Example:

```rust
# use chrono::{DateTime, Utc, NaiveDate};
# use serde_derive::Serialize;
use chrono::serde::ts_nanoseconds_option::serialize as to_nano_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_nano_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s = S {
time: Some(
NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_nano_opt(02, 04, 59, 918355733)
.unwrap()
.and_utc(),
),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355733}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: object | None, serializer: S) -> Ok: ...

"""Deserialize a `DateTime` from a nanosecond timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, TimeZone, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_nanoseconds_option::deserialize as from_nano_tsopt;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_nano_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355733 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(1526522699, 918355733).single() });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object | None: ...

"""Serialize a UTC datetime into an integer number of microseconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, Utc, NaiveDate};
# use serde_derive::Serialize;
use chrono::serde::ts_microseconds::serialize as to_micro_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_micro_ts")]
time: DateTime<Utc>,
}

let my_s = S {
time: NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_micro_opt(02, 04, 59, 918355)
.unwrap()
.and_utc(),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: object, serializer: S) -> Ok: ...

"""Deserialize a `DateTime` from a microsecond timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, TimeZone, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_microseconds::deserialize as from_micro_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_micro_ts")]
time: DateTime<Utc>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(1526522699, 918355000).unwrap() });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(-1, 999_999_000).unwrap() });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object: ...

"""Serialize a UTC datetime into an integer number of microseconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, Utc, NaiveDate};
# use serde_derive::Serialize;
use chrono::serde::ts_microseconds_option::serialize as to_micro_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_micro_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s = S {
time: Some(
NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_micro_opt(02, 04, 59, 918355)
.unwrap()
.and_utc(),
),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: object | None, serializer: S) -> Ok: ...

"""Deserialize a `DateTime` from a microsecond timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, TimeZone, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_microseconds_option::deserialize as from_micro_tsopt;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_micro_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(1526522699, 918355000).single() });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object | None: ...

"""Serialize a UTC datetime into an integer number of milliseconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, Utc, NaiveDate};
# use serde_derive::Serialize;
use chrono::serde::ts_milliseconds::serialize as to_milli_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_milli_ts")]
time: DateTime<Utc>,
}

let my_s = S {
time: NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_milli_opt(02, 04, 59, 918)
.unwrap()
.and_utc(),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: object, serializer: S) -> Ok: ...

"""Deserialize a `DateTime` from a millisecond timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, TimeZone, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_milliseconds::deserialize as from_milli_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_milli_ts")]
time: DateTime<Utc>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(1526522699, 918000000).unwrap() });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(-1, 999_000_000).unwrap() });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object: ...

"""Serialize a UTC datetime into an integer number of milliseconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, Utc, NaiveDate};
# use serde_derive::Serialize;
use chrono::serde::ts_milliseconds_option::serialize as to_milli_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_milli_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s = S {
time: Some(
NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_milli_opt(02, 04, 59, 918)
.unwrap()
.and_utc(),
),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: object | None, serializer: S) -> Ok: ...

"""Deserialize a `DateTime` from a millisecond timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{TimeZone, DateTime, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_milliseconds_option::deserialize as from_milli_tsopt;

#[derive(Deserialize, PartialEq, Debug)]
#[serde(untagged)]
enum E<T> {
V(T),
}

#[derive(Deserialize, PartialEq, Debug)]
struct S {
#[serde(default, deserialize_with = "from_milli_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s: E<S> = serde_json::from_str(r#"{ "time": 1526522699918 }"#)?;
assert_eq!(my_s, E::V(S { time: Some(Utc.timestamp_opt(1526522699, 918000000).unwrap()) }));
let s: E<S> = serde_json::from_str(r#"{ "time": null }"#)?;
assert_eq!(s, E::V(S { time: None }));
let t: E<S> = serde_json::from_str(r#"{}"#)?;
assert_eq!(t, E::V(S { time: None }));
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object | None: ...

"""Serialize a UTC datetime into an integer number of seconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{TimeZone, DateTime, Utc};
# use serde_derive::Serialize;
use chrono::serde::ts_seconds::serialize as to_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_ts")]
time: DateTime<Utc>,
}

let my_s = S { time: Utc.with_ymd_and_hms(2015, 5, 15, 10, 0, 0).unwrap() };
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1431684000}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: object, serializer: S) -> Ok: ...

"""Deserialize a `DateTime` from a seconds timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, TimeZone, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_seconds::deserialize as from_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_ts")]
time: DateTime<Utc>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1431684000 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(1431684000, 0).unwrap() });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object: ...

"""Serialize a UTC datetime into an integer number of seconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{TimeZone, DateTime, Utc};
# use serde_derive::Serialize;
use chrono::serde::ts_seconds_option::serialize as to_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s = S { time: Some(Utc.with_ymd_and_hms(2015, 5, 15, 10, 0, 0).unwrap()) };
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1431684000}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: object | None, serializer: S) -> Ok: ...

"""Deserialize a `DateTime` from a seconds timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, TimeZone, Utc};
# use serde_derive::Deserialize;
use chrono::serde::ts_seconds_option::deserialize as from_tsopt;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_tsopt")]
time: Option<DateTime<Utc>>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1431684000 }"#)?;
assert_eq!(my_s, S { time: Utc.timestamp_opt(1431684000, 0).single() });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> object | None: ...

"""Tries to format given arguments with given formatting items.
Internally used by `DelayedFormat`."""
def format(w: Formatter, date: object, time: object, off: object, items: I) -> Result: ...

"""Formats single formatting item"""
def format_item(w: Formatter, date: object, time: object, off: object, item: Item) -> Result: ...

"""Tries to parse given string into `parsed` with given formatting items.
Returns `Ok` when the entire string has been parsed (otherwise `parsed` should not be used).
There should be no trailing string after parsing;
use a stray [`Item::Space`](./enum.Item.html#variant.Space) to trim whitespaces.

This particular date and time parser is:

- Greedy. It will consume the longest possible prefix.
For example, `April` is always consumed entirely when the long month name is requested;
it equally accepts `Apr`, but prefers the longer prefix in this case.

- Padding-agnostic (for numeric items).
The [`Pad`](./enum.Pad.html) field is completely ignored,
so one can prepend any number of whitespace then any number of zeroes before numbers.

- (Still) obeying the intrinsic parsing width. This allows, for example, parsing `HHMMSS`."""
def parse(parsed: Parsed, s: str, items: I) -> object: ...

"""Tries to parse given string into `parsed` with given formatting items.
Returns `Ok` with a slice of the unparsed remainder.

This particular date and time parser is:

- Greedy. It will consume the longest possible prefix.
For example, `April` is always consumed entirely when the long month name is requested;
it equally accepts `Apr`, but prefers the longer prefix in this case.

- Padding-agnostic (for numeric items).
The [`Pad`](./enum.Pad.html) field is completely ignored,
so one can prepend any number of zeroes before numbers.

- (Still) obeying the intrinsic parsing width. This allows, for example, parsing `HHMMSS`."""
def parse_and_remainder(parsed: Parsed, s: object, items: I) -> object: ...

"""Serialize a datetime into an integer number of nanoseconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Errors

An `i64` with nanosecond precision can span a range of ~584 years. This function returns an
error on an out of range `DateTime`.

The dates that can be represented as nanoseconds are between 1677-09-21T00:12:44.0 and
2262-04-11T23:47:16.854775804.

# Example:

```rust
# use chrono::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_nanoseconds::serialize as to_nano_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_nano_ts")]
time: NaiveDateTime,
}

let my_s = S {
time: NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_nano_opt(02, 04, 59, 918355733)
.unwrap(),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355733}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: NaiveDateTime, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a nanoseconds timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_nanoseconds::deserialize as from_nano_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_nano_ts")]
time: NaiveDateTime,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355733 }"#)?;
let expected = DateTime::from_timestamp(1526522699, 918355733).unwrap().naive_utc();
assert_eq!(my_s, S { time: expected });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
let expected = DateTime::from_timestamp(-1, 999_999_999).unwrap().naive_utc();
assert_eq!(my_s, S { time: expected });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime: ...

"""Serialize a datetime into an integer number of nanoseconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Errors

An `i64` with nanosecond precision can span a range of ~584 years. This function returns an
error on an out of range `DateTime`.

The dates that can be represented as nanoseconds are between 1677-09-21T00:12:44.0 and
2262-04-11T23:47:16.854775804.

# Example:

```rust
# use chrono::naive::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_nanoseconds_option::serialize as to_nano_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_nano_tsopt")]
time: Option<NaiveDateTime>,
}

let my_s = S {
time: Some(
NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_nano_opt(02, 04, 59, 918355733)
.unwrap(),
),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355733}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: NaiveDateTime | None, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a nanosecond timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_nanoseconds_option::deserialize as from_nano_tsopt;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_nano_tsopt")]
time: Option<NaiveDateTime>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355733 }"#)?;
let expected = DateTime::from_timestamp(1526522699, 918355733).unwrap().naive_utc();
assert_eq!(my_s, S { time: Some(expected) });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
let expected = DateTime::from_timestamp(-1, 999_999_999).unwrap().naive_utc();
assert_eq!(my_s, S { time: Some(expected) });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime | None: ...

"""Serialize a datetime into an integer number of microseconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_microseconds::serialize as to_micro_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_micro_ts")]
time: NaiveDateTime,
}

let my_s = S {
time: NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_micro_opt(02, 04, 59, 918355)
.unwrap(),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: NaiveDateTime, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a microseconds timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_microseconds::deserialize as from_micro_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_micro_ts")]
time: NaiveDateTime,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355 }"#)?;
let expected = DateTime::from_timestamp(1526522699, 918355000).unwrap().naive_utc();
assert_eq!(my_s, S { time: expected });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
let expected = DateTime::from_timestamp(-1, 999_999_000).unwrap().naive_utc();
assert_eq!(my_s, S { time: expected });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime: ...

"""Serialize a datetime into an integer number of microseconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::naive::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_microseconds_option::serialize as to_micro_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_micro_tsopt")]
time: Option<NaiveDateTime>,
}

let my_s = S {
time: Some(
NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_micro_opt(02, 04, 59, 918355)
.unwrap(),
),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918355}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: NaiveDateTime | None, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a nanosecond timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_microseconds_option::deserialize as from_micro_tsopt;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_micro_tsopt")]
time: Option<NaiveDateTime>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918355 }"#)?;
let expected = DateTime::from_timestamp(1526522699, 918355000).unwrap().naive_utc();
assert_eq!(my_s, S { time: Some(expected) });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
let expected = DateTime::from_timestamp(-1, 999_999_000).unwrap().naive_utc();
assert_eq!(my_s, S { time: Some(expected) });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime | None: ...

"""Serialize a datetime into an integer number of milliseconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_milliseconds::serialize as to_milli_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_milli_ts")]
time: NaiveDateTime,
}

let my_s = S {
time: NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_milli_opt(02, 04, 59, 918)
.unwrap(),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: NaiveDateTime, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a milliseconds timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_milliseconds::deserialize as from_milli_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_milli_ts")]
time: NaiveDateTime,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918 }"#)?;
let expected = DateTime::from_timestamp(1526522699, 918000000).unwrap().naive_utc();
assert_eq!(my_s, S { time: expected });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
let expected = DateTime::from_timestamp(-1, 999_000_000).unwrap().naive_utc();
assert_eq!(my_s, S { time: expected });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime: ...

"""Serialize a datetime into an integer number of milliseconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::naive::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_milliseconds_option::serialize as to_milli_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_milli_tsopt")]
time: Option<NaiveDateTime>,
}

let my_s = S {
time: Some(
NaiveDate::from_ymd_opt(2018, 5, 17)
.unwrap()
.and_hms_milli_opt(02, 04, 59, 918)
.unwrap(),
),
};
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699918}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: NaiveDateTime | None, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a millisecond timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_milliseconds_option::deserialize as from_milli_tsopt;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_milli_tsopt")]
time: Option<NaiveDateTime>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1526522699918 }"#)?;
let expected = DateTime::from_timestamp(1526522699, 918000000).unwrap().naive_utc();
assert_eq!(my_s, S { time: Some(expected) });

let my_s: S = serde_json::from_str(r#"{ "time": -1 }"#)?;
let expected = DateTime::from_timestamp(-1, 999_000_000).unwrap().naive_utc();
assert_eq!(my_s, S { time: Some(expected) });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime | None: ...

"""Serialize a datetime into an integer number of seconds since the epoch

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_seconds::serialize as to_ts;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_ts")]
time: NaiveDateTime,
}

let my_s =
S { time: NaiveDate::from_ymd_opt(2015, 5, 15).unwrap().and_hms_opt(10, 0, 0).unwrap() };
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1431684000}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(dt: NaiveDateTime, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a seconds timestamp

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_seconds::deserialize as from_ts;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_ts")]
time: NaiveDateTime,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1431684000 }"#)?;
let expected = DateTime::from_timestamp_secs(1431684000).unwrap().naive_utc();
assert_eq!(my_s, S { time: expected });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime: ...

"""Serialize a datetime into an integer number of seconds since the epoch or none

Intended for use with `serde`s `serialize_with` attribute.

# Example:

```rust
# use chrono::naive::{NaiveDate, NaiveDateTime};
# use serde_derive::Serialize;
use chrono::naive::serde::ts_seconds_option::serialize as to_tsopt;
#[derive(Serialize)]
struct S {
#[serde(serialize_with = "to_tsopt")]
time: Option<NaiveDateTime>,
}

let expected = NaiveDate::from_ymd_opt(2018, 5, 17).unwrap().and_hms_opt(02, 04, 59).unwrap();
let my_s = S { time: Some(expected) };
let as_string = serde_json::to_string(&my_s)?;
assert_eq!(as_string, r#"{"time":1526522699}"#);
# Ok::<(), serde_json::Error>(())
```"""
def serialize(opt: NaiveDateTime | None, serializer: S) -> Ok: ...

"""Deserialize a `NaiveDateTime` from a second timestamp or none

Intended for use with `serde`s `deserialize_with` attribute.

# Example:

```rust
# use chrono::{DateTime, NaiveDateTime};
# use serde_derive::Deserialize;
use chrono::naive::serde::ts_seconds_option::deserialize as from_tsopt;
#[derive(Debug, PartialEq, Deserialize)]
struct S {
#[serde(deserialize_with = "from_tsopt")]
time: Option<NaiveDateTime>,
}

let my_s: S = serde_json::from_str(r#"{ "time": 1431684000 }"#)?;
let expected = DateTime::from_timestamp_secs(1431684000).unwrap().naive_utc();
assert_eq!(my_s, S { time: Some(expected) });
# Ok::<(), serde_json::Error>(())
```"""
def deserialize(d: D) -> NaiveDateTime | None: ...

__all__: list[str] = ["serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "format", "format_item", "parse", "parse_and_remainder", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "serialize", "deserialize", "SecondsTimestampVisitor", "NanoSecondsTimestampVisitor", "MicroSecondsTimestampVisitor", "MilliSecondsTimestampVisitor", "DateTime", "ParseWeekdayError", "Months", "ParseMonthError", "StrftimeItems", "DelayedFormat", "InternalNumeric", "InternalFixed", "OffsetFormat", "ParseError", "Parsed", "OutOfRange", "FixedOffset", "Utc", "DYNAMIC_TIME_ZONE_INFORMATION", "FILETIME", "SYSTEMTIME", "TIME_ZONE_INFORMATION", "Local", "Date", "NaiveDateTime", "NaiveDate", "NaiveDateDaysIterator", "NaiveDateWeeksIterator", "YearFlags", "NaiveWeek", "Days", "NaiveTime", "IsoWeek", "TimeDelta", "OutOfRangeError", "WeekdaySet", "WeekdaySetIter", "Weekday", "Month", "SecondsFormat", "Pad", "Numeric", "Fixed", "OffsetPrecision", "Colons", "Item", "ParseErrorKind", "LocalResult", "RoundingError"]
