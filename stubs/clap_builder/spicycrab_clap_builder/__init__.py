"""Python stubs for the clap_builder Rust crate.

Install with: cookcrab install clap_builder
"""

from __future__ import annotations

from typing import Self

class ArgAction:
    """Behavior of arguments when they are encountered while parsing.

    Maps to clap::builder::ArgAction in Rust.

    Common variants:
    - SetTrue: Flag that sets to true when present
    - SetFalse: Flag that sets to false when present
    - Set: Store a single value (default)
    - Append: Collect multiple values
    - Count: Count occurrences

    Example:
        cmd.arg(Arg.new("verbose").short("v").action(ArgAction.SetTrue()))
    """

    @staticmethod
    def SetTrue() -> "ArgAction":
        """Flag that sets to true when present."""
        ...

    @staticmethod
    def SetFalse() -> "ArgAction":
        """Flag that sets to false when present."""
        ...

    @staticmethod
    def Set() -> "ArgAction":
        """Store a single value (default behavior)."""
        ...

    @staticmethod
    def Append() -> "ArgAction":
        """Collect multiple occurrences into a Vec."""
        ...

    @staticmethod
    def Count() -> "ArgAction":
        """Count the number of occurrences."""
        ...

    @staticmethod
    def Help() -> "ArgAction":
        """Print help and exit."""
        ...

    @staticmethod
    def Version() -> "ArgAction":
        """Print version and exit."""
        ...


class ValueHint:
    """Provide shell completion hints for argument values.

    Maps to clap::builder::ValueHint in Rust.

    Example:
        cmd.arg(Arg.new("file").value_hint(ValueHint.FilePath()))
    """

    @staticmethod
    def Unknown() -> "ValueHint":
        """Unknown hint (default)."""
        ...

    @staticmethod
    def Other() -> "ValueHint":
        """Other type."""
        ...

    @staticmethod
    def AnyPath() -> "ValueHint":
        """Any path (file or directory)."""
        ...

    @staticmethod
    def FilePath() -> "ValueHint":
        """Path to a file."""
        ...

    @staticmethod
    def DirPath() -> "ValueHint":
        """Path to a directory."""
        ...

    @staticmethod
    def ExecutablePath() -> "ValueHint":
        """Path to an executable."""
        ...

    @staticmethod
    def CommandName() -> "ValueHint":
        """Command name."""
        ...

    @staticmethod
    def CommandString() -> "ValueHint":
        """Command string."""
        ...

    @staticmethod
    def CommandWithArguments() -> "ValueHint":
        """Command with arguments."""
        ...

    @staticmethod
    def Username() -> "ValueHint":
        """Username."""
        ...

    @staticmethod
    def Hostname() -> "ValueHint":
        """Hostname."""
        ...

    @staticmethod
    def Url() -> "ValueHint":
        """URL."""
        ...

    @staticmethod
    def EmailAddress() -> "ValueHint":
        """Email address."""
        ...


class AnyValueId:

    def eq(self, other: Self) -> bool: ...

    def partial_cmp(self, other: Self) -> Ordering | None: ...

    def eq(self, other: TypeId) -> bool: ...

    def cmp(self, other: Self) -> Ordering: ...

    def hash(self, state: H) -> None: ...

    def fmt(self, f: Formatter) -> None: ...

    @staticmethod
    def from_(_: object) -> "AnyValueId": ...

class Id:
    """[`Arg`][crate::Arg] or [`ArgGroup`][crate::ArgGroup] identifier

This is used for accessing the value in [`ArgMatches`][crate::ArgMatches] or defining
relationships between `Arg`s and `ArgGroup`s with functions like
[`Arg::conflicts_with`][crate::Arg::conflicts_with]."""

    def as_str(self) -> str: ...

    @staticmethod
    def from_(id: object) -> "Id": ...

    @staticmethod
    def from_(name: Str) -> "Id": ...

    @staticmethod
    def from_(name: object) -> "Id": ...

    @staticmethod
    def from_(name: str) -> "Id": ...

    @staticmethod
    def from_(name: object) -> "Id": ...

    @staticmethod
    def from_(name: object) -> "Id": ...

    @staticmethod
    def from_(name: object) -> "Id": ...

    @staticmethod
    def from_(name: object) -> "Id": ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def as_ref(self) -> str: ...

    def borrow(self) -> str: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: Str) -> bool: ...

    def eq(self, other: str) -> bool: ...

class ReadmeDoctests:
    pass

class ArgMatches:
    """Container for parse results.

Used to get information about the arguments that were supplied to the program at runtime by
the user. New instances of this struct are obtained by using the [`Command::get_matches`] family of
methods.

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::parser::ValueSource;
let matches = Command::new("MyApp")
.arg(Arg::new("out")
.long("output")
.required(true)
.action(ArgAction::Set)
.default_value("-"))
.arg(Arg::new("cfg")
.short('c')
.action(ArgAction::Set))
.get_matches(); // builds the instance of ArgMatches

// to get information about the "cfg" argument we created, such as the value supplied we use
// various ArgMatches methods, such as [ArgMatches::get_one]
if let Some(c) = matches.get_one::<String>("cfg") {
println!("Value for -c: {c}");
}

// The ArgMatches::get_one method returns an Option because the user may not have supplied
// that argument at runtime. But if we specified that the argument was "required" as we did
// with the "out" argument, we can safely unwrap because `clap` verifies that was actually
// used at runtime.
println!("Value for --output: {}", matches.get_one::<String>("out").unwrap());

// You can check the presence of an argument's values
if matches.contains_id("out") {
// However, if you want to know where the value came from
if matches.value_source("out").expect("checked contains_id") == ValueSource::CommandLine {
println!("`out` set by user");
} else {
println!("`out` is defaulted");
}
}
```
[`Command::get_matches`]: crate::Command::get_matches()"""

    def get_one(self, id: str) -> object: ...

    def get_count(self, id: str) -> int: ...

    def get_flag(self, id: str) -> bool: ...

    def get_many(self, id: str) -> object: ...

    def get_occurrences(self, id: str) -> object: ...

    def get_raw(self, id: str) -> RawValues | None: ...

    def get_raw_occurrences(self, id: str) -> RawOccurrences | None: ...

    def remove_one(self, id: str) -> T | None: ...

    def remove_many(self, id: str) -> object | None: ...

    def remove_occurrences(self, id: str) -> object | None: ...

    def contains_id(self, id: str) -> bool: ...

    def ids(self) -> IdsRef: ...

    def args_present(self) -> bool: ...

    def value_source(self, id: str) -> ValueSource | None: ...

    def index_of(self, id: str) -> int | None: ...

    def indices_of(self, id: str) -> Indices | None: ...

    def subcommand(self) -> object | None: ...

    def remove_subcommand(self) -> object | None: ...

    def subcommand_matches(self, name: str) -> object: ...

    def subcommand_name(self) -> object: ...

    def is_valid_subcommand(self, _name: str) -> bool: ...

    def try_get_one(self, id: str) -> object: ...

    def try_get_many(self, id: str) -> object: ...

    def try_get_occurrences(self, id: str) -> object: ...

    def try_get_raw(self, id: str) -> RawValues | None: ...

    def try_get_raw_occurrences(self, id: str) -> RawOccurrences | None: ...

    def try_remove_one(self, id: str) -> T | None: ...

    def try_remove_many(self, id: str) -> object | None: ...

    def try_remove_occurrences(self, id: str) -> object | None: ...

    def try_contains_id(self, id: str) -> bool: ...

    def try_clear_id(self, id: str) -> bool: ...

class IdsRef:
    """Iterate over [`Arg`][crate::Arg] and [`ArgGroup`][crate::ArgGroup] [`Id`]s via [`ArgMatches::ids`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};

let m = Command::new("myprog")
.arg(arg!(--color <when>)
.value_parser(["auto", "always", "never"]))
.arg(arg!(--config <path>)
.value_parser(value_parser!(std::path::PathBuf)))
.get_matches_from(["myprog", "--config=config.toml", "--color=auto"]);
assert_eq!(
m.ids()
.map(|id| id.as_str())
.collect::<Vec<_>>(),
["config", "color"]
);
```"""

    def next(self) -> object: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> object: ...

class Values:
    """Iterate over multiple values for an argument via [`ArgMatches::remove_many`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let mut m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.action(ArgAction::Append))
.get_matches_from(vec!["myapp", "-o", "val1", "-o", "val2"]);

let mut values = m.remove_many::<String>("output")
.unwrap();

assert_eq!(values.next(), Some(String::from("val1")));
assert_eq!(values.next(), Some(String::from("val2")));
assert_eq!(values.next(), None);
```"""

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

    @staticmethod
    def default() -> "Values": ...

class ValuesRef:
    """Iterate over multiple values for an argument via [`ArgMatches::get_many`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.action(ArgAction::Append))
.get_matches_from(vec!["myapp", "-o", "val1", "-o", "val2"]);

let mut values = m.get_many::<String>("output")
.unwrap()
.map(|s| s.as_str());

assert_eq!(values.next(), Some("val1"));
assert_eq!(values.next(), Some("val2"));
assert_eq!(values.next(), None);
```"""

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

    @staticmethod
    def default() -> "ValuesRef": ...

class RawValues:
    """Iterate over raw argument values via [`ArgMatches::get_raw`].

# Examples

```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};
use std::ffi::OsString;
use std::os::unix::ffi::{OsStrExt,OsStringExt};

let m = Command::new("utf8")
.arg(arg!(<arg> "some arg")
.value_parser(value_parser!(OsString)))
.get_matches_from(vec![OsString::from("myprog"),
// "Hi {0xe9}!"
OsString::from_vec(vec![b'H', b'i', b' ', 0xe9, b'!'])]);
assert_eq!(
&*m.get_raw("arg")
.unwrap()
.next().unwrap()
.as_bytes(),
[b'H', b'i', b' ', 0xe9, b'!']
);
# }
```"""

    def next(self) -> object: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> object: ...

    @staticmethod
    def default() -> "RawValues": ...

class Occurrences:

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

    @staticmethod
    def default() -> "Occurrences": ...

class OccurrenceValues:

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

class OccurrencesRef:

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

    @staticmethod
    def default() -> "OccurrencesRef": ...

class OccurrenceValuesRef:

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

class RawOccurrences:

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

    @staticmethod
    def default() -> "RawOccurrences": ...

class RawOccurrenceValues:

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> Item | None: ...

class Indices:
    """Iterate over indices for where an argument appeared when parsing, via [`ArgMatches::indices_of`]

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.num_args(1..)
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-o", "val1", "val2"]);

let mut indices = m.indices_of("output").unwrap();

assert_eq!(indices.next(), Some(2));
assert_eq!(indices.next(), Some(3));
assert_eq!(indices.next(), None);
```
[`ArgMatches::indices_of`]: ArgMatches::indices_of()"""

    def next(self) -> int | None: ...

    def size_hint(self) -> object: ...

    def next_back(self) -> int | None: ...

    @staticmethod
    def default() -> "Indices": ...

class ValueRange:
    """Values per occurrence for an argument"""

    @staticmethod
    def new(range: object) -> "ValueRange": ...

    def min_values(self) -> int: ...

    def max_values(self) -> int: ...

    def takes_values(self) -> bool: ...

    def start_bound(self) -> object: ...

    def end_bound(self) -> object: ...

    @staticmethod
    def default() -> "ValueRange": ...

    @staticmethod
    def from_(fixed: int) -> "ValueRange": ...

    @staticmethod
    def from_(range: object) -> "ValueRange": ...

    @staticmethod
    def from_(_: object) -> "ValueRange": ...

    @staticmethod
    def from_(range: object) -> "ValueRange": ...

    @staticmethod
    def from_(range: object) -> "ValueRange": ...

    @staticmethod
    def from_(range: object) -> "ValueRange": ...

    @staticmethod
    def from_(range: object) -> "ValueRange": ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class Str:
    """A UTF-8-encoded fixed string

<div class="warning">

**NOTE:** To support dynamic values (i.e. `String`), enable the `string`
feature

</div>"""

    @staticmethod
    def from_(name: Id) -> "Str": ...

    def eq(self, other: Id) -> bool: ...

    def as_str(self) -> str: ...

    @staticmethod
    def from_(id: object) -> "Str": ...

    @staticmethod
    def from_(name: str) -> "Str": ...

    @staticmethod
    def from_(name: object) -> "Str": ...

    @staticmethod
    def from_(name: object) -> "Str": ...

    @staticmethod
    def from_(name: object) -> "Str": ...

    @staticmethod
    def from_(cow: object) -> "Str": ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def deref(self) -> str: ...

    def as_ref(self) -> str: ...

    def as_ref(self) -> object: ...

    def as_ref(self) -> OsStr: ...

    def as_ref(self) -> Path: ...

    def borrow(self) -> str: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: OsStr) -> bool: ...

    def eq(self, other: OsStr) -> bool: ...

    def eq(self, other: str) -> bool: ...

class Arg:
    """The abstract representation of a command line argument. Used to set all the options and
relationships that define a valid argument for the program.

There are two methods for constructing [`Arg`]s, using the builder pattern and setting options
manually, or using a usage string which is far less verbose but has fewer options. You can also
use a combination of the two methods to achieve the best of both worlds.

- [Basic API][crate::Arg#basic-api]
- [Value Handling][crate::Arg#value-handling]
- [Help][crate::Arg#help-1]
- [Advanced Argument Relations][crate::Arg#advanced-argument-relations]
- [Reflection][crate::Arg#reflection]

# Examples

```rust
# use clap_builder as clap;
# use clap::{Arg, arg, ArgAction};
// Using the traditional builder pattern and setting each option manually
let cfg = Arg::new("config")
.short('c')
.long("config")
.action(ArgAction::Set)
.value_name("FILE")
.help("Provides a config file to myprog");
// Using a usage string (setting a similar argument to the one above)
let input = arg!(-i --input <FILE> "Provides an input file to the program");
```"""

    @staticmethod
    def new(id: object) -> "Arg": ...

    def id(self, id: object) -> Self: ...

    def short(self, s: object) -> Self: ...

    def long(self, l: object) -> Self: ...

    def alias(self, name: object) -> Self: ...

    def short_alias(self, name: object) -> Self: ...

    def aliases(self, names: object) -> Self: ...

    def short_aliases(self, names: object) -> Self: ...

    def visible_alias(self, name: object) -> Self: ...

    def visible_short_alias(self, name: object) -> Self: ...

    def visible_aliases(self, names: object) -> Self: ...

    def visible_short_aliases(self, names: object) -> Self: ...

    def index(self, idx: object) -> Self: ...

    def trailing_var_arg(self, yes: bool) -> Self: ...

    def last(self, yes: bool) -> Self: ...

    def required(self, yes: bool) -> Self: ...

    def requires(self, arg_id: object) -> Self: ...

    def exclusive(self, yes: bool) -> Self: ...

    def global_(self, yes: bool) -> Self: ...

    def add(self, tagged: T) -> Self: ...

    def action(self, action: object) -> Self: ...

    def value_parser(self, parser: object) -> Self: ...

    def num_args(self, qty: object) -> Self: ...

    def number_of_values(self, qty: int) -> Self: ...

    def value_name(self, name: object) -> Self: ...

    def value_names(self, names: object) -> Self: ...

    def value_hint(self, value_hint: object) -> Self: ...

    def ignore_case(self, yes: bool) -> Self: ...

    def allow_hyphen_values(self, yes: bool) -> Self: ...

    def allow_negative_numbers(self, yes: bool) -> Self: ...

    def require_equals(self, yes: bool) -> Self: ...

    def use_value_delimiter(self, yes: bool) -> Self: ...

    def value_delimiter(self, d: object) -> Self: ...

    def value_terminator(self, term: object) -> Self: ...

    def raw(self, yes: bool) -> Self: ...

    def default_value(self, val: object) -> Self: ...

    def default_value_os(self, val: object) -> Self: ...

    def default_values(self, vals: object) -> Self: ...

    def default_values_os(self, vals: object) -> Self: ...

    def default_missing_value(self, val: object) -> Self: ...

    def default_missing_value_os(self, val: object) -> Self: ...

    def default_missing_values(self, vals: object) -> Self: ...

    def default_missing_values_os(self, vals: object) -> Self: ...

    def env(self, name: object) -> Self: ...

    def env_os(self, name: object) -> Self: ...

    def help(self, h: object) -> Self: ...

    def long_help(self, h: object) -> Self: ...

    def display_order(self, ord: object) -> Self: ...

    def help_heading(self, heading: object) -> Self: ...

    def next_line_help(self, yes: bool) -> Self: ...

    def hide(self, yes: bool) -> Self: ...

    def hide_possible_values(self, yes: bool) -> Self: ...

    def hide_default_value(self, yes: bool) -> Self: ...

    def hide_env(self, yes: bool) -> Self: ...

    def hide_env_values(self, yes: bool) -> Self: ...

    def hide_short_help(self, yes: bool) -> Self: ...

    def hide_long_help(self, yes: bool) -> Self: ...

    def group(self, group_id: object) -> Self: ...

    def groups(self, group_ids: object) -> Self: ...

    def default_value_if(self, arg_id: object, predicate: object, default: object) -> Self: ...

    def default_values_if(self, arg_id: object, predicate: object, defaults: object) -> Self: ...

    def default_value_if_os(self, arg_id: object, predicate: object, default: object) -> Self: ...

    def default_value_ifs(self, ifs: object) -> Self: ...

    def default_values_ifs(self, ifs: object) -> Self: ...

    def default_value_ifs_os(self, ifs: object) -> Self: ...

    def required_unless_present(self, arg_id: object) -> Self: ...

    def required_unless_present_all(self, names: object) -> Self: ...

    def required_unless_present_any(self, names: object) -> Self: ...

    def required_if_eq(self, arg_id: object, val: object) -> Self: ...

    def required_if_eq_any(self, ifs: object) -> Self: ...

    def required_if_eq_all(self, ifs: object) -> Self: ...

    def requires_if(self, val: object, arg_id: object) -> Self: ...

    def requires_ifs(self, ifs: object) -> Self: ...

    def requires_all(self, ids: object) -> Self: ...

    def conflicts_with(self, arg_id: object) -> Self: ...

    def conflicts_with_all(self, names: object) -> Self: ...

    def overrides_with(self, arg_id: object) -> Self: ...

    def overrides_with_all(self, names: object) -> Self: ...

    def get_id(self) -> Id: ...

    def get_help(self) -> object: ...

    def get_long_help(self) -> object: ...

    def get_display_order(self) -> int: ...

    def get_help_heading(self) -> object: ...

    def get_short(self) -> str | None: ...

    def get_visible_short_aliases(self) -> list[str] | None: ...

    def get_all_short_aliases(self) -> list[str] | None: ...

    def get_short_and_visible_aliases(self) -> list[str] | None: ...

    def get_long(self) -> object: ...

    def get_visible_aliases(self) -> object: ...

    def get_all_aliases(self) -> object: ...

    def get_long_and_visible_aliases(self) -> object: ...

    def get_aliases(self) -> object: ...

    def get_possible_values(self) -> list[PossibleValue]: ...

    def get_value_names(self) -> object: ...

    def get_num_args(self) -> ValueRange | None: ...

    def get_value_delimiter(self) -> str | None: ...

    def get_value_terminator(self) -> object: ...

    def get_index(self) -> int | None: ...

    def get_value_hint(self) -> ValueHint: ...

    def get_env(self) -> object: ...

    def get_default_values(self) -> object: ...

    def is_positional(self) -> bool: ...

    def is_required_set(self) -> bool: ...

    def is_allow_hyphen_values_set(self) -> bool: ...

    def is_allow_negative_numbers_set(self) -> bool: ...

    def get_action(self) -> ArgAction: ...

    def get_value_parser(self) -> ValueParser: ...

    def is_global_set(self) -> bool: ...

    def is_next_line_help_set(self) -> bool: ...

    def is_hide_set(self) -> bool: ...

    def is_hide_default_value_set(self) -> bool: ...

    def is_hide_possible_values_set(self) -> bool: ...

    def is_hide_env_set(self) -> bool: ...

    def is_hide_env_values_set(self) -> bool: ...

    def is_hide_short_help_set(self) -> bool: ...

    def is_hide_long_help_set(self) -> bool: ...

    def is_require_equals_set(self) -> bool: ...

    def is_exclusive_set(self) -> bool: ...

    def is_trailing_var_arg_set(self) -> bool: ...

    def is_last_set(self) -> bool: ...

    def is_ignore_case_set(self) -> bool: ...

    def get(self) -> object: ...

    def remove(self) -> T | None: ...

    @staticmethod
    def from_(a: Arg) -> "Arg": ...

    def eq(self, other: Arg) -> bool: ...

    def partial_cmp(self, other: Self) -> Ordering | None: ...

    def cmp(self, other: Arg) -> Ordering: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> None: ...

class ArgGroup:
    """Specifies a logical group of [arguments]

You can use this for
- applying validation to an entire group, like [`ArgGroup::multiple`]
- validate relationships between an argument and a group, like [conflicts] or [requirements]
- check which argument in a group was specified on the command-line

For visually grouping arguments in help, see instead
[`Arg::help_heading`][crate::Arg::help_heading].

# Examples

The following example demonstrates using an `ArgGroup` to ensure that one, and only one, of
the arguments from the specified group is present at runtime.

```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup, error::ErrorKind};
let result = Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually"))
.arg(arg!(--major           "auto increase major"))
.arg(arg!(--minor           "auto increase minor"))
.arg(arg!(--patch           "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor", "patch"])
.required(true))
.try_get_matches_from(vec!["cmd", "--major", "--patch"]);
// Because we used two args in the group it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```

This next example shows a passing parse of the same scenario
```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup, Id};
let result = Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually"))
.arg(arg!(--major           "auto increase major"))
.arg(arg!(--minor           "auto increase minor"))
.arg(arg!(--patch           "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true))
.try_get_matches_from(vec!["cmd", "--major"]);
assert!(result.is_ok());
let matches = result.unwrap();
// We may not know which of the args was used, so we can test for the group...
assert!(matches.contains_id("vers"));
// We can also ask the group which arg was used
assert_eq!(matches
.get_one::<Id>("vers")
.expect("`vers` is required")
.as_str(),
"major"
);
// we could also alternatively check each arg individually (not shown here)
```
[arguments]: crate::Arg
[conflicts]: crate::Arg::conflicts_with()
[requirements]: crate::Arg::requires()"""

    @staticmethod
    def new(id: object) -> "ArgGroup": ...

    def id(self, id: object) -> Self: ...

    def arg(self, arg_id: object) -> Self: ...

    def args(self, ns: object) -> Self: ...

    def get_args(self) -> object: ...

    def multiple(self, yes: bool) -> Self: ...

    def is_multiple(self) -> bool: ...

    def required(self, yes: bool) -> Self: ...

    def requires(self, id: object) -> Self: ...

    def requires_all(self, ns: object) -> Self: ...

    def conflicts_with(self, id: object) -> Self: ...

    def conflicts_with_all(self, ns: object) -> Self: ...

    def get_id(self) -> Id: ...

    def is_required_set(self) -> bool: ...

    @staticmethod
    def from_(g: ArgGroup) -> "ArgGroup": ...

class ValueParser:
    """Parse/validate argument values

Specified with [`Arg::value_parser`][crate::Arg::value_parser].

`ValueParser` defines how to convert a raw argument value into a validated and typed value for
use within an application.

See
- [`value_parser!`][crate::value_parser] for automatically selecting an implementation for a given type
- [`ValueParser::new`] for additional [`TypedValueParser`] that can be used

# Example

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(["always", "auto", "never"])
.default_value("auto")
)
.arg(
clap::Arg::new("hostname")
.long("hostname")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.action(clap::ArgAction::Set)
.required(true)
)
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--hostname", "rust-lang.org", "--port", "3001"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "auto");

let hostname: &String = m.get_one("hostname")
.expect("required");
assert_eq!(hostname, "rust-lang.org");

let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```"""

    @staticmethod
    def new(other: P) -> "ValueParser": ...

    @staticmethod
    def bool() -> "ValueParser": ...

    @staticmethod
    def string() -> "ValueParser": ...

    @staticmethod
    def os_string() -> "ValueParser": ...

    @staticmethod
    def path_buf() -> "ValueParser": ...

    def type_id(self) -> AnyValueId: ...

    def possible_values(self) -> object | None: ...

    @staticmethod
    def from_(p: P) -> "ValueParser": ...

    @staticmethod
    def from_(p: _AnonymousValueParser) -> "ValueParser": ...

    @staticmethod
    def from_(value: object) -> "ValueParser": ...

    @staticmethod
    def from_(value: object) -> "ValueParser": ...

    @staticmethod
    def from_(value: object) -> "ValueParser": ...

    @staticmethod
    def from_(value: object) -> "ValueParser": ...

    @staticmethod
    def from_(value: object) -> "ValueParser": ...

    @staticmethod
    def from_(value: object) -> "ValueParser": ...

    @staticmethod
    def from_(values: object) -> "ValueParser": ...

    @staticmethod
    def from_(values: list[P]) -> "ValueParser": ...

    def fmt(self, f: Formatter) -> None: ...

    def clone(self) -> Self: ...

class StringValueParser:
    """Implementation for [`ValueParser::string`]

Useful for composing new [`TypedValueParser`]s"""

    @staticmethod
    def new() -> "StringValueParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def parse(self, cmd: Command, _arg: object, value: OsString) -> Value: ...

    @staticmethod
    def default() -> "StringValueParser": ...

class OsStringValueParser:
    """Implementation for [`ValueParser::os_string`]

Useful for composing new [`TypedValueParser`]s"""

    @staticmethod
    def new() -> "OsStringValueParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def parse(self, _cmd: Command, _arg: object, value: OsString) -> Value: ...

    @staticmethod
    def default() -> "OsStringValueParser": ...

class PathBufValueParser:
    """Implementation for [`ValueParser::path_buf`]

Useful for composing new [`TypedValueParser`]s"""

    @staticmethod
    def new() -> "PathBufValueParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def parse(self, cmd: Command, arg: object, value: OsString) -> Value: ...

    @staticmethod
    def default() -> "PathBufValueParser": ...

class EnumValueParser:
    """Parse an [`ValueEnum`][crate::ValueEnum] value.

See also:
- [`PossibleValuesParser`]

# Example

```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::ColorChoice;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;

// Usage
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.value_parser(clap::builder::EnumValueParser::<ColorChoice>::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let port: ColorChoice = *m.get_one("color")
.expect("required");
assert_eq!(port, ColorChoice::Always);

// Semantics
let value_parser = clap::builder::EnumValueParser::<ColorChoice>::new();
// or
let value_parser = clap::value_parser!(ColorChoice);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("always")).unwrap(), ColorChoice::Always);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("auto")).unwrap(), ColorChoice::Auto);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("never")).unwrap(), ColorChoice::Never);
```"""

    @staticmethod
    def new() -> "EnumValueParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def possible_values(self) -> object | None: ...

    @staticmethod
    def default() -> "EnumValueParser": ...

class PossibleValuesParser:
    """Verify the value is from an enumerated set of [`PossibleValue`][crate::builder::PossibleValue].

See also:
- [`EnumValueParser`] for directly supporting [`ValueEnum`][crate::ValueEnum] types
- [`TypedValueParser::map`] for adapting values to a more specialized type, like an external
enums that can't implement [`ValueEnum`][crate::ValueEnum]

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.value_parser(clap::builder::PossibleValuesParser::new(["always", "auto", "never"]))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let port: &String = m.get_one("color")
.expect("required");
assert_eq!(port, "always");
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::PossibleValuesParser::new(["always", "auto", "never"]);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("always")).unwrap(), "always");
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("auto")).unwrap(), "auto");
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("never")).unwrap(), "never");
```"""

    @staticmethod
    def new(values: object) -> "PossibleValuesParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def parse(self, cmd: Command, arg: object, value: OsString) -> str: ...

    def possible_values(self) -> object | None: ...

    @staticmethod
    def from_(values: I) -> "PossibleValuesParser": ...

class RangedI64ValueParser:
    """Parse number that fall within a range of values

<div class="warning">

**NOTE:** To capture negative values, you will also need to set
[`Arg::allow_negative_numbers`][crate::Arg::allow_negative_numbers] or
[`Arg::allow_hyphen_values`][crate::Arg::allow_hyphen_values].

</div>

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::RangedI64ValueParser::<i32>::new().range(-1..200);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-200")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("300")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("-1")).unwrap(), -1);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), 0);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("50")).unwrap(), 50);
```"""

    @staticmethod
    def new() -> "RangedI64ValueParser": ...

    def range(self, range: B) -> Self: ...

    def parse_ref(self, cmd: Command, arg: object, raw_value: OsStr) -> Value: ...

    @staticmethod
    def from_(range: B) -> "RangedI64ValueParser": ...

    @staticmethod
    def default() -> "RangedI64ValueParser": ...

class RangedU64ValueParser:
    """Parse number that fall within a range of values

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u64).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: u64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::RangedU64ValueParser::<u32>::new().range(0..200);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-200")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("300")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-1")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), 0);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("50")).unwrap(), 50);
```"""

    @staticmethod
    def new() -> "RangedU64ValueParser": ...

    def range(self, range: B) -> Self: ...

    def parse_ref(self, cmd: Command, arg: object, raw_value: OsStr) -> Value: ...

    @staticmethod
    def from_(range: B) -> "RangedU64ValueParser": ...

    @staticmethod
    def default() -> "RangedU64ValueParser": ...

class BoolValueParser:
    """Implementation for [`ValueParser::bool`]

Useful for composing new [`TypedValueParser`]s"""

    @staticmethod
    def new() -> "BoolValueParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def possible_values(self) -> object | None: ...

    @staticmethod
    def default() -> "BoolValueParser": ...

class FalseyValueParser:
    """Parse false-like string values, everything else is `true`

See also:
- [`ValueParser::bool`] for assuming non-false is true
- [`BoolishValueParser`] for different human readable bool representations

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::FalseyValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("append")
.expect("required");
assert_eq!(port, true);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::FalseyValueParser::new();
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("false")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("No")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oFF")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), false);
```"""

    @staticmethod
    def new() -> "FalseyValueParser": ...

    def parse_ref(self, cmd: Command, _arg: object, value: OsStr) -> Value: ...

    def possible_values(self) -> object | None: ...

    @staticmethod
    def default() -> "FalseyValueParser": ...

class BoolishValueParser:
    """Parse bool-like string values

See also:
- [`ValueParser::bool`] for different human readable bool representations
- [`FalseyValueParser`] for assuming non-false is true

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::BoolishValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("append")
.expect("required");
assert_eq!(port, true);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::BoolishValueParser::new();
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("true")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("Yes")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oN")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("1")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("false")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("No")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oFF")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), false);
```"""

    @staticmethod
    def new() -> "BoolishValueParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def possible_values(self) -> object | None: ...

    @staticmethod
    def default() -> "BoolishValueParser": ...

class NonEmptyStringValueParser:
    """Parse non-empty string values

See also:
- [`ValueParser::string`]

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: &String = m.get_one("append")
.expect("required");
assert_eq!(port, "true");
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::NonEmptyStringValueParser::new();
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).unwrap(), "random");
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
```"""

    @staticmethod
    def new() -> "NonEmptyStringValueParser": ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    @staticmethod
    def default() -> "NonEmptyStringValueParser": ...

class MapValueParser:
    """Adapt a `TypedValueParser` from one value to another

See [`TypedValueParser::map`]"""

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def parse(self, cmd: Command, arg: object, value: OsString) -> Value: ...

    def possible_values(self) -> object | None: ...

class TryMapValueParser:
    """Adapt a `TypedValueParser` from one value to another

See [`TypedValueParser::try_map`]"""

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def possible_values(self) -> object | None: ...

class UnknownArgumentValueParser:
    """When encountered, report [`ErrorKind::UnknownArgument`][crate::error::ErrorKind::UnknownArgument]

Useful to help users migrate, either from old versions or similar tools.

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.args([
Arg::new("current-dir")
.short('C'),
Arg::new("current-dir-unknown")
.long("cwd")
.aliases(["current-dir", "directory", "working-directory", "root"])
.value_parser(clap::builder::UnknownArgumentValueParser::suggest_arg("-C"))
.hide(true),
]);

// Use a supported version of the argument
let matches = cmd.clone().try_get_matches_from(["mycmd", "-C", ".."]).unwrap();
assert!(matches.contains_id("current-dir"));
assert_eq!(
matches.get_many::<String>("current-dir").unwrap_or_default().map(|v| v.as_str()).collect::<Vec<_>>(),
vec![".."]
);

// Use one of the invalid versions
let err = cmd.try_get_matches_from(["mycmd", "--cwd", ".."]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::UnknownArgument);
```"""

    @staticmethod
    def suggest_arg(arg: object) -> "UnknownArgumentValueParser": ...

    @staticmethod
    def suggest(text: object) -> "UnknownArgumentValueParser": ...

    def and_suggest(self, text: object) -> Self: ...

    def parse_ref(self, cmd: Command, arg: object, value: OsStr) -> Value: ...

    def parse_ref_(self, cmd: Command, arg: object, _value: OsStr, source: ValueSource) -> Value: ...

class _infer_ValueParser_for:

    @staticmethod
    def new() -> "_infer_ValueParser_for": ...

    def value_parser(self) -> _AnonymousValueParser: ...

class _AnonymousValueParser:
    """Unstable [`ValueParser`]

Implementation may change to more specific instance in the future"""
    pass

class StyledStr:
    """Terminal-styling container

Styling may be encoded as [ANSI Escape Code](https://en.wikipedia.org/wiki/ANSI_escape_code)

# Examples

```rust
# use clap_builder as clap;
// `cstr!` converts tags to ANSI codes
let after_help: &'static str = color_print::cstr!(
r#"<bold><underline>Examples</underline></bold>

<dim>$</dim> <bold>mybin --input file.toml</bold>
"#);

let cmd = clap::Command::new("mybin")
.after_help(after_help)  // The `&str` gets converted into a `StyledStr`
// ...
#   ;
```"""

    @staticmethod
    def new() -> "StyledStr": ...

    def ansi(self) -> object: ...

    def push_str(self, msg: str) -> None: ...

    @staticmethod
    def from_(name: str) -> "StyledStr": ...

    @staticmethod
    def from_(name: object) -> "StyledStr": ...

    @staticmethod
    def from_(name: object) -> "StyledStr": ...

    @staticmethod
    def from_(name: object) -> "StyledStr": ...

    @staticmethod
    def from_(cow: object) -> "StyledStr": ...

    def write_str(self, s: str) -> None: ...

    def write_char(self, c: str) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

class Styles:
    """Terminal styling definitions

See also [`Command::styles`][crate::Command::styles].

# Example

clap v3 styling
```rust
# use clap_builder as clap;
# use clap::builder::styling::*;
let styles = Styles::styled()
.header(AnsiColor::Yellow.on_default())
.usage(AnsiColor::Green.on_default())
.literal(AnsiColor::Green.on_default())
.placeholder(AnsiColor::Green.on_default());
```"""

    @staticmethod
    def plain() -> "Styles": ...

    @staticmethod
    def styled() -> "Styles": ...

    def header(self, style: Style) -> Self: ...

    def error(self, style: Style) -> Self: ...

    def usage(self, style: Style) -> Self: ...

    def literal(self, style: Style) -> Self: ...

    def placeholder(self, style: Style) -> Self: ...

    def valid(self, style: Style) -> Self: ...

    def invalid(self, style: Style) -> Self: ...

    def context(self, style: Style) -> Self: ...

    def context_value(self, style: Style) -> Self: ...

    def get_header(self) -> Style: ...

    def get_error(self) -> Style: ...

    def get_usage(self) -> Style: ...

    def get_literal(self) -> Style: ...

    def get_placeholder(self) -> Style: ...

    def get_valid(self) -> Style: ...

    def get_invalid(self) -> Style: ...

    def get_context(self) -> Style: ...

    def get_context_value(self) -> Style: ...

    @staticmethod
    def default() -> "Styles": ...

class OsStr:
    """A UTF-8-encoded fixed string

<div class="warning">

**NOTE:** To support dynamic values (i.e. `OsString`), enable the `string`
feature

</div>"""

    def eq(self, other: Str) -> bool: ...

    def as_os_str(self) -> OsStr: ...

    def to_os_string(self) -> OsString: ...

    @staticmethod
    def from_(id: object) -> "OsStr": ...

    @staticmethod
    def from_(id: Str) -> "OsStr": ...

    @staticmethod
    def from_(id: Str) -> "OsStr": ...

    @staticmethod
    def from_(id: object) -> "OsStr": ...

    @staticmethod
    def from_(name: OsString) -> "OsStr": ...

    @staticmethod
    def from_(name: OsString) -> "OsStr": ...

    @staticmethod
    def from_(name: str) -> "OsStr": ...

    @staticmethod
    def from_(name: object) -> "OsStr": ...

    @staticmethod
    def from_(name: OsStr) -> "OsStr": ...

    @staticmethod
    def from_(name: OsStr) -> "OsStr": ...

    @staticmethod
    def from_(name: object) -> "OsStr": ...

    @staticmethod
    def from_(name: object) -> "OsStr": ...

    @staticmethod
    def from_(cow: object) -> "OsStr": ...

    def fmt(self, f: Formatter) -> Result: ...

    def deref(self) -> OsStr: ...

    def as_ref(self) -> OsStr: ...

    def as_ref(self) -> Path: ...

    def borrow(self) -> OsStr: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: OsStr) -> bool: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: OsString) -> bool: ...

class Command:
    """Build a command-line interface.

This includes defining arguments, subcommands, parser behavior, and help output.
Once all configuration is complete,
the [`Command::get_matches`] family of methods starts the runtime-parsing
process. These methods then return information about the user supplied
arguments (or lack thereof).

When deriving a [`Parser`][crate::Parser], you can use
[`CommandFactory::command`][crate::CommandFactory::command] to access the
`Command`.

- [Basic API][crate::Command#basic-api]
- [Application-wide Settings][crate::Command#application-wide-settings]
- [Command-specific Settings][crate::Command#command-specific-settings]
- [Subcommand-specific Settings][crate::Command#subcommand-specific-settings]
- [Reflection][crate::Command#reflection]

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("My Program")
.author("Me, me@mail.com")
.version("1.0.2")
.about("Explains in brief what the program does")
.arg(
Arg::new("in_file")
)
.after_help("Longer explanation to appear after the options when \\
displaying the help information from --help or -h")
.get_matches();

// Your program logic starts here...
```
[`Command::get_matches`]: Command::get_matches()"""

    @staticmethod
    def new(name: object) -> "Command": ...

    def arg(self, a: object) -> Self: ...

    def args(self, args: object) -> Self: ...

    def mut_arg(self, arg_id: object, f: F) -> Self: ...

    def mut_args(self, f: F) -> Self: ...

    def mut_group(self, arg_id: object, f: F) -> Self: ...

    def mut_subcommand(self, name: object, f: F) -> Self: ...

    def mut_subcommands(self, f: F) -> Self: ...

    def group(self, group: object) -> Self: ...

    def groups(self, groups: object) -> Self: ...

    def subcommand(self, subcmd: object) -> Self: ...

    def subcommands(self, subcmds: object) -> Self: ...

    def defer(self, deferred: object) -> Self: ...

    def debug_assert(self) -> None: ...

    def error(self, kind: ErrorKind, message: object) -> Exception: ...

    def get_matches(self) -> ArgMatches: ...

    def get_matches_mut(self) -> ArgMatches: ...

    def try_get_matches(self) -> object: ...

    def get_matches_from(self, itr: I) -> ArgMatches: ...

    def try_get_matches_from(self, itr: I) -> object: ...

    def try_get_matches_from_mut(self, itr: I) -> object: ...

    def print_help(self) -> object: ...

    def print_long_help(self) -> object: ...

    def render_help(self) -> StyledStr: ...

    def render_long_help(self) -> StyledStr: ...

    def write_help(self, w: W) -> object: ...

    def write_long_help(self, w: W) -> object: ...

    def render_version(self) -> str: ...

    def render_long_version(self) -> str: ...

    def render_usage(self) -> StyledStr: ...

    def add(self, tagged: T) -> Self: ...

    def no_binary_name(self, yes: bool) -> Self: ...

    def ignore_errors(self, yes: bool) -> Self: ...

    def args_override_self(self, yes: bool) -> Self: ...

    def dont_delimit_trailing_values(self, yes: bool) -> Self: ...

    def color(self, color: ColorChoice) -> Self: ...

    def styles(self, styles: Styles) -> Self: ...

    def term_width(self, width: int) -> Self: ...

    def max_term_width(self, width: int) -> Self: ...

    def disable_version_flag(self, yes: bool) -> Self: ...

    def propagate_version(self, yes: bool) -> Self: ...

    def next_line_help(self, yes: bool) -> Self: ...

    def disable_help_flag(self, yes: bool) -> Self: ...

    def disable_help_subcommand(self, yes: bool) -> Self: ...

    def disable_colored_help(self, yes: bool) -> Self: ...

    def help_expected(self, yes: bool) -> Self: ...

    def dont_collapse_args_in_usage(self, _yes: bool) -> Self: ...

    def hide_possible_values(self, yes: bool) -> Self: ...

    def infer_long_args(self, yes: bool) -> Self: ...

    def infer_subcommands(self, yes: bool) -> Self: ...

    def name(self, name: object) -> Self: ...

    def bin_name(self, name: object) -> Self: ...

    def display_name(self, name: object) -> Self: ...

    def author(self, author: object) -> Self: ...

    def about(self, about: object) -> Self: ...

    def long_about(self, long_about: object) -> Self: ...

    def after_help(self, help: object) -> Self: ...

    def after_long_help(self, help: object) -> Self: ...

    def before_help(self, help: object) -> Self: ...

    def before_long_help(self, help: object) -> Self: ...

    def version(self, ver: object) -> Self: ...

    def long_version(self, ver: object) -> Self: ...

    def override_usage(self, usage: object) -> Self: ...

    def override_help(self, help: object) -> Self: ...

    def help_template(self, s: object) -> Self: ...

    def flatten_help(self, yes: bool) -> Self: ...

    def next_help_heading(self, heading: object) -> Self: ...

    def next_display_order(self, disp_ord: object) -> Self: ...

    def arg_required_else_help(self, yes: bool) -> Self: ...

    def allow_hyphen_values(self, yes: bool) -> Self: ...

    def allow_negative_numbers(self, yes: bool) -> Self: ...

    def trailing_var_arg(self, yes: bool) -> Self: ...

    def allow_missing_positional(self, yes: bool) -> Self: ...

    def short_flag(self, short: object) -> Self: ...

    def long_flag(self, long: object) -> Self: ...

    def alias(self, name: object) -> Self: ...

    def short_flag_alias(self, name: object) -> Self: ...

    def long_flag_alias(self, name: object) -> Self: ...

    def aliases(self, names: object) -> Self: ...

    def short_flag_aliases(self, names: object) -> Self: ...

    def long_flag_aliases(self, names: object) -> Self: ...

    def visible_alias(self, name: object) -> Self: ...

    def visible_short_flag_alias(self, name: object) -> Self: ...

    def visible_long_flag_alias(self, name: object) -> Self: ...

    def visible_aliases(self, names: object) -> Self: ...

    def visible_short_flag_aliases(self, names: object) -> Self: ...

    def visible_long_flag_aliases(self, names: object) -> Self: ...

    def display_order(self, ord: object) -> Self: ...

    def hide(self, yes: bool) -> Self: ...

    def subcommand_required(self, yes: bool) -> Self: ...

    def allow_external_subcommands(self, yes: bool) -> Self: ...

    def external_subcommand_value_parser(self, parser: object) -> Self: ...

    def args_conflicts_with_subcommands(self, yes: bool) -> Self: ...

    def subcommand_precedence_over_arg(self, yes: bool) -> Self: ...

    def subcommand_negates_reqs(self, yes: bool) -> Self: ...

    def multicall(self, yes: bool) -> Self: ...

    def subcommand_value_name(self, value_name: object) -> Self: ...

    def subcommand_help_heading(self, heading: object) -> Self: ...

    def get_display_name(self) -> object: ...

    def get_bin_name(self) -> object: ...

    def set_bin_name(self, name: object) -> None: ...

    def get_name(self) -> str: ...

    def get_name_and_visible_aliases(self) -> object: ...

    def get_version(self) -> object: ...

    def get_long_version(self) -> object: ...

    def get_display_order(self) -> int: ...

    def get_author(self) -> object: ...

    def get_short_flag(self) -> str | None: ...

    def get_long_flag(self) -> object: ...

    def get_about(self) -> object: ...

    def get_long_about(self) -> object: ...

    def is_flatten_help_set(self) -> bool: ...

    def get_next_help_heading(self) -> object: ...

    def get_visible_aliases(self) -> object: ...

    def get_visible_short_flag_aliases(self) -> object: ...

    def get_visible_long_flag_aliases(self) -> object: ...

    def get_all_aliases(self) -> object: ...

    def get_all_short_flag_aliases(self) -> object: ...

    def get_all_long_flag_aliases(self) -> object: ...

    def get_aliases(self) -> object: ...

    def get_color(self) -> ColorChoice: ...

    def get_styles(self) -> Styles: ...

    def get_subcommands(self) -> object: ...

    def get_subcommands_mut(self) -> object: ...

    def has_subcommands(self) -> bool: ...

    def get_subcommand_help_heading(self) -> object: ...

    def get_subcommand_value_name(self) -> object: ...

    def get_before_help(self) -> object: ...

    def get_before_long_help(self) -> object: ...

    def get_after_help(self) -> object: ...

    def get_after_long_help(self) -> object: ...

    def find_subcommand(self, name: object) -> object: ...

    def find_subcommand_mut(self, name: object) -> object: ...

    def get_groups(self) -> object: ...

    def get_arguments(self) -> object: ...

    def get_positionals(self) -> object: ...

    def get_opts(self) -> object: ...

    def get_arg_conflicts_with(self, arg: Arg) -> object: ...

    def is_no_binary_name_set(self) -> bool: ...

    def is_dont_delimit_trailing_values_set(self) -> bool: ...

    def is_disable_version_flag_set(self) -> bool: ...

    def is_propagate_version_set(self) -> bool: ...

    def is_next_line_help_set(self) -> bool: ...

    def is_disable_help_flag_set(self) -> bool: ...

    def is_disable_help_subcommand_set(self) -> bool: ...

    def is_disable_colored_help_set(self) -> bool: ...

    def is_dont_collapse_args_in_usage_set(self) -> bool: ...

    def is_arg_required_else_help_set(self) -> bool: ...

    def is_allow_negative_numbers_set(self) -> bool: ...

    def is_trailing_var_arg_set(self) -> bool: ...

    def is_allow_missing_positional_set(self) -> bool: ...

    def is_hide_set(self) -> bool: ...

    def is_subcommand_required_set(self) -> bool: ...

    def is_allow_external_subcommands_set(self) -> bool: ...

    def get_external_subcommand_value_parser(self) -> object: ...

    def is_args_conflicts_with_subcommands_set(self) -> bool: ...

    def is_args_override_self(self) -> bool: ...

    def is_subcommand_precedence_over_arg_set(self) -> bool: ...

    def is_subcommand_negates_reqs_set(self) -> bool: ...

    def is_multicall_set(self) -> bool: ...

    def get(self) -> object: ...

    def remove(self) -> T | None: ...

    def build(self) -> None: ...

    @staticmethod
    def default() -> "Command": ...

    def index(self, key: Id) -> Output: ...

    @staticmethod
    def from_(cmd: object) -> "Command": ...

    def fmt(self, f: Formatter) -> Result: ...

class PossibleValue:
    """A possible value of an argument.

This is used for specifying [possible values] of [Args].

See also [`PossibleValuesParser`][crate::builder::PossibleValuesParser]

<div class="warning">

**NOTE:** Most likely you can use strings, rather than `PossibleValue` as it is only required
to [hide] single values from help messages and shell completions or to attach [help] to
possible values.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Arg, builder::PossibleValue, ArgAction};
let cfg = Arg::new("config")
.action(ArgAction::Set)
.value_name("FILE")
.value_parser([
PossibleValue::new("fast"),
PossibleValue::new("slow").help("slower than fast"),
PossibleValue::new("secret speed").hide(true)
]);
```

[Args]: crate::Arg
[possible values]: crate::builder::ValueParser::possible_values
[hide]: PossibleValue::hide()
[help]: PossibleValue::help()"""

    @staticmethod
    def new(name: object) -> "PossibleValue": ...

    def help(self, help: object) -> Self: ...

    def hide(self, yes: bool) -> Self: ...

    def alias(self, name: object) -> Self: ...

    def aliases(self, names: object) -> Self: ...

    def get_name(self) -> str: ...

    def get_help(self) -> object: ...

    def is_hide_set(self) -> bool: ...

    def get_name_and_aliases(self) -> object: ...

    def matches(self, value: str, ignore_case: bool) -> bool: ...

    @staticmethod
    def from_(s: S) -> "PossibleValue": ...

class KindFormatter:
    """Report [`ErrorKind`]

No context is included.

<div class="warning">

**NOTE:** Consider removing the `error-context` default feature if using this to remove all
overhead for [`RichFormatter`].

</div>"""

    @staticmethod
    def format_error(error: object) -> StyledStr: ...

class RichFormatter:
    """Richly formatted error context

This follows the [rustc diagnostic style guide](https://rustc-dev-guide.rust-lang.org/diagnostics.html#suggestion-style-guide)."""

    @staticmethod
    def format_error(error: object) -> StyledStr: ...

class Error:
    """Command Line Argument Parser Error

See [`Command::error`] to create an error.

[`Command::error`]: crate::Command::error"""

    @staticmethod
    def raw(kind: ErrorKind, message: object) -> "Error": ...

    def format(self, cmd: Command) -> Self: ...

    @staticmethod
    def new(kind: ErrorKind) -> "Error": ...

    def with_cmd(self, cmd: Command) -> Self: ...

    def apply(self) -> object: ...

    def kind(self) -> ErrorKind: ...

    def context(self) -> object: ...

    def get(self, kind: ContextKind) -> object: ...

    def insert(self, kind: ContextKind, value: ContextValue) -> ContextValue | None: ...

    def remove(self, kind: ContextKind) -> ContextValue | None: ...

    def use_stderr(self) -> bool: ...

    def exit_code(self) -> int: ...

    def exit(self) -> object: ...

    def print(self) -> object: ...

    def render(self) -> StyledStr: ...

    @staticmethod
    def from_(e: Exception) -> "Error": ...

    @staticmethod
    def from_(e: Exception) -> "Error": ...

    def fmt(self, f: Formatter) -> None: ...

    def source(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class ColorChoice:
    """Represents the color preferences for program output"""
    Auto: "ColorChoice"
    Always: "ColorChoice"
    Never: "ColorChoice"

    @staticmethod
    def possible_values() -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    @staticmethod
    def value_variants() -> object: ...

    def to_possible_value(self) -> PossibleValue | None: ...

class MatchesError:
    """Violation of [`ArgMatches`][crate::ArgMatches] assumptions"""
    Downcast: "MatchesError"
    UnknownArgument: "MatchesError"

    def fmt(self, f: Formatter) -> Result: ...

class ValueSource:
    """Origin of the argument's value"""
    DefaultValue: "ValueSource"
    EnvVariable: "ValueSource"
    CommandLine: "ValueSource"

class Resettable:
    """Clearable builder value

This allows a builder function to both accept any value that can [`Into::into`] `T` (like
`&str` into `OsStr`) as well as `None` to reset it to the default.  This is needed to
workaround a limitation where you can't have a function argument that is `impl Into<Option<T>>`
where `T` is `impl Into<S>` accept `None` as its type is ambiguous.

# Example

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
fn common() -> Command {
Command::new("cli")
.arg(Arg::new("input").short('i').long("input"))
}
let mut command = common();
command.mut_arg("input", |arg| arg.short(None));
```"""
    Value: "Resettable"
    Reset: "Resettable"

    @staticmethod
    def from_(other: T) -> "Resettable": ...

    @staticmethod
    def from_(other: T | None) -> "Resettable": ...

    def into_resettable(self) -> object: ...

class ArgAction:
    """Behavior of arguments when they are encountered while parsing

# Examples

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("special-help")
.short('?')
.action(clap::ArgAction::Help)
);

// Existing help still exists
let err = cmd.clone().try_get_matches_from(["mycmd", "-h"]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::DisplayHelp);

// New help available
let err = cmd.try_get_matches_from(["mycmd", "-?"]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::DisplayHelp);
# }
```"""
    Set: "ArgAction"
    Append: "ArgAction"
    SetTrue: "ArgAction"
    SetFalse: "ArgAction"
    Count: "ArgAction"
    Help: "ArgAction"
    HelpShort: "ArgAction"
    HelpLong: "ArgAction"
    Version: "ArgAction"

    def into_resettable(self) -> object: ...

    def takes_values(self) -> bool: ...

class ArgPredicate:
    """Operations to perform on argument values

These do not apply to [`ValueSource::DefaultValue`][crate::parser::ValueSource::DefaultValue]"""
    IsPresent: "ArgPredicate"
    Equals: "ArgPredicate"

    @staticmethod
    def from_(other: S) -> "ArgPredicate": ...

class ValueHint:
    """Provide shell with hint on how to complete an argument.

See [`Arg::value_hint`][crate::Arg::value_hint] to set this on an argument.

See the `clap_complete` crate for completion script generation.

Overview of which hints are supported by which shell:

| Hint                   | zsh | fish[^1] | dynamic |
| ---------------------- | --- | ---------|---------|
| `AnyPath`              | Yes | Yes      | Yes     |
| `FilePath`             | Yes | Yes      | Yes     |
| `DirPath`              | Yes | Yes      | Yes     |
| `ExecutablePath`       | Yes | Partial  | Yes     |
| `CommandName`          | Yes | Yes      | No      |
| `CommandString`        | Yes | Partial  | No      |
| `CommandWithArguments` | Yes |          | No      |
| `Username`             | Yes | Yes      | No      |
| `Hostname`             | Yes | Yes      | No      |
| `Url`                  | Yes |          | No      |
| `EmailAddress`         | Yes |          | No      |

[^1]: fish completions currently only support named arguments (e.g. -o or --opt), not
positional arguments."""
    Unknown: "ValueHint"
    Other: "ValueHint"
    AnyPath: "ValueHint"
    FilePath: "ValueHint"
    DirPath: "ValueHint"
    ExecutablePath: "ValueHint"
    CommandName: "ValueHint"
    CommandString: "ValueHint"
    CommandWithArguments: "ValueHint"
    Username: "ValueHint"
    Hostname: "ValueHint"
    Url: "ValueHint"
    EmailAddress: "ValueHint"

    def into_resettable(self) -> object: ...

    @staticmethod
    def from_str(s: str) -> object: ...

class ContextKind:
    """Semantics for a piece of error information"""
    InvalidSubcommand: "ContextKind"
    InvalidArg: "ContextKind"
    PriorArg: "ContextKind"
    ValidSubcommand: "ContextKind"
    ValidValue: "ContextKind"
    InvalidValue: "ContextKind"
    ActualNumValues: "ContextKind"
    ExpectedNumValues: "ContextKind"
    MinValues: "ContextKind"
    SuggestedCommand: "ContextKind"
    SuggestedSubcommand: "ContextKind"
    SuggestedArg: "ContextKind"
    SuggestedValue: "ContextKind"
    TrailingArg: "ContextKind"
    Suggested: "ContextKind"
    Usage: "ContextKind"
    Custom: "ContextKind"

    def as_str(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class ContextValue:
    """A piece of error information"""
    None_: "ContextValue"
    Bool: "ContextValue"
    String: "ContextValue"
    Strings: "ContextValue"
    StyledStr: "ContextValue"
    StyledStrs: "ContextValue"
    Number: "ContextValue"

    def fmt(self, f: Formatter) -> Result: ...

class ErrorKind:
    """Command line argument parser kind of error"""
    InvalidValue: "ErrorKind"
    UnknownArgument: "ErrorKind"
    InvalidSubcommand: "ErrorKind"
    NoEquals: "ErrorKind"
    ValueValidation: "ErrorKind"
    TooManyValues: "ErrorKind"
    TooFewValues: "ErrorKind"
    WrongNumberOfValues: "ErrorKind"
    ArgumentConflict: "ErrorKind"
    MissingRequiredArgument: "ErrorKind"
    MissingSubcommand: "ErrorKind"
    InvalidUtf8: "ErrorKind"
    DisplayHelp: "ErrorKind"
    DisplayHelpOnMissingArgumentOrSubcommand: "ErrorKind"
    DisplayVersion: "ErrorKind"
    Io: "ErrorKind"
    Format: "ErrorKind"

    def as_str(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

__all__: list[str] = ["ArgAction", "ValueHint", "AnyValueId", "Id", "ReadmeDoctests", "ArgMatches", "IdsRef", "Values", "ValuesRef", "RawValues", "Occurrences", "OccurrenceValues", "OccurrencesRef", "OccurrenceValuesRef", "RawOccurrences", "RawOccurrenceValues", "Indices", "ValueRange", "Str", "Arg", "ArgGroup", "ValueParser", "StringValueParser", "OsStringValueParser", "PathBufValueParser", "EnumValueParser", "PossibleValuesParser", "RangedI64ValueParser", "RangedU64ValueParser", "BoolValueParser", "FalseyValueParser", "BoolishValueParser", "NonEmptyStringValueParser", "MapValueParser", "TryMapValueParser", "UnknownArgumentValueParser", "_infer_ValueParser_for", "_AnonymousValueParser", "StyledStr", "Styles", "OsStr", "Command", "PossibleValue", "KindFormatter", "RichFormatter", "Error", "ColorChoice", "MatchesError", "ValueSource", "Resettable", "ArgAction", "ArgPredicate", "ValueHint", "ContextKind", "ContextValue", "ErrorKind"]
