"""Python stubs for the oidfed_metadata_policy Rust crate.

Install with: cookcrab install oidfed_metadata_policy
"""

from __future__ import annotations

from typing import Self

"""Merges a Trust Anchor's (TA) policy on top of an Intermediate Authority's (IA) policy
according to the OpenID Federation policy merging rules.

This function implements the policy merge algorithm defined in
[Section 6.1.3](https://openid.net/specs/openid-federation-1_0.html#section-6.1.3)
of the OpenID Federation specification.

# Arguments

* `ta_policies_in` - The Trust Anchor's metadata policy as a JSON value
* `ia_policies_in` - The Intermediate Authority's metadata policy as a JSON value

# Returns

Returns `Ok(Map<String, Value>)` containing the merged policy, or an `Err` if
the policies cannot be merged due to conflicts.

# Example

```rust
use serde_json::json;

let ta_policy = json!({
"openid_relying_party": {
"grant_types": {
"subset_of": ["authorization_code", "implicit"]
}
}
});

let ia_policy = json!({
"openid_relying_party": {
"grant_types": {
"subset_of": ["authorization_code", "implicit", "client_credentials"]
}
}
});

let merged = oidfed_metadata_policy::merge_policies(&ta_policy, &ia_policy).unwrap();
// The merged policy will have the intersection of subset_of values
```"""
def merge_policies(ta_policies_in: Value, ia_policies_in: Value) -> object: ...

"""Merges metadata policies for a single entity type from Trust Anchor and Intermediate Authority.

This function handles the detailed merging logic for individual policy operators such as
`value`, `default`, `add`, `one_of`, `subset_of`, `superset_of`, and `essential`.

The merge follows the rules defined in
[Section 6.1.3.1](https://openid.net/specs/openid-federation-1_0.html#section-6.1.3.1)
of the OpenID Federation specification.

# Arguments

* `ta_policies_in` - The Trust Anchor's policy for one entity type
* `ia_policies_in` - The Intermediate Authority's policy for the same entity type

# Returns

Returns `Ok(Map<String, Value>)` with the merged policy, or `Err` if policies conflict.

# Errors

Returns an error if:
- `value` or `default` operators have different values in TA and IA
- `one_of` in IA contains values not present in TA's `one_of`
- `superset_of` in TA is not a subset of IA's `superset_of`
- Combined operators violate policy constraints

# Example

```rust
use serde_json::json;

let ta_policy = json!({
"grant_types": {
"subset_of": ["authorization_code", "implicit"]
}
});

let ia_policy = json!({
"grant_types": {
"default": ["authorization_code"]
}
});

let merged = oidfed_metadata_policy::merge_one_type_policy(&ta_policy, &ia_policy).unwrap();
```"""
def merge_one_type_policy(ta_policies_in: Value, ia_policies_in: Value) -> object: ...

"""Returns an ordered array by merging items from Trust Anchor and Intermediate Authority.

This helper function maintains the order of items when merging policy values,
prioritizing items from the Trust Anchor's order first, then adding remaining
items from the Intermediate Authority.

# Arguments

* `ta_orderd_items` - Ordered slice of values from the Trust Anchor
* `ia_orderd_items` - Ordered slice of values from the Intermediate Authority
* `added_items` - Set of items that should be included in the result

# Returns

A JSON array value containing the ordered merged items.

# Example

```rust
use serde_json::{json, Value};
use std::collections::HashSet;

let ta_items = vec![json!("a"), json!("b")];
let ia_items = vec![json!("b"), json!("c")];
let a = json!("a");
let b = json!("b");
let c = json!("c");
let added: HashSet<&Value> = [&a, &b, &c].into_iter().collect();

let result = oidfed_metadata_policy::get_ordered_array(&ta_items, &ia_items, &added);
// Result: ["a", "b", "c"] - TA order preserved, then IA items added
```"""
def get_ordered_array(ta_orderd_items: object, ia_orderd_items: object, added_items: object) -> Value: ...

"""Converts a JSON value into a `HashSet` of values.

If the input is an array, each element becomes a set member.
If the input is a single value, it becomes the only member of the set.

# Arguments

* `values` - A JSON value (array or single value)

# Returns

A `HashSet<Value>` containing the values.

# Example

```rust
use serde_json::json;

let array = json!(["a", "b", "c"]);
let set = oidfed_metadata_policy::get_hashset_from_values(&array);
assert_eq!(set.len(), 3);

let single = json!("a");
let set = oidfed_metadata_policy::get_hashset_from_values(&single);
assert_eq!(set.len(), 1);
```"""
def get_hashset_from_values(values: Value) -> object: ...

"""Checks if the first value is a subset of the second value.

Both values are converted to sets before comparison. Works with both
single values and arrays.

# Arguments

* `val` - The value to check if it's a subset
* `val2` - The value to check against (superset candidate)

# Returns

`true` if `val` is a subset of `val2`, `false` otherwise.

# Example

```rust
use serde_json::json;

let subset = json!(["a", "b"]);
let superset = json!(["a", "b", "c"]);

assert!(oidfed_metadata_policy::is_subset_of(&subset, &superset));
assert!(!oidfed_metadata_policy::is_subset_of(&superset, &subset));
```"""
def is_subset_of(val: Value, val2: Value) -> bool: ...

"""Checks if the first value is a superset of the second value.

Both values are converted to sets before comparison. Works with both
single values and arrays.

# Arguments

* `val` - The value to check if it's a superset
* `val2` - The value to check against (subset candidate)

# Returns

`true` if `val` is a superset of `val2`, `false` otherwise.

# Example

```rust
use serde_json::json;

let superset = json!(["a", "b", "c"]);
let subset = json!(["a", "b"]);

assert!(oidfed_metadata_policy::is_superset_of(&superset, &subset));
assert!(!oidfed_metadata_policy::is_superset_of(&subset, &superset));
```"""
def is_superset_of(val: Value, val2: Value) -> bool: ...

"""Computes the intersection of two JSON values as sets.

Both values are converted to sets and the intersection is returned.

# Arguments

* `val` - First JSON value
* `val2` - Second JSON value

# Returns

`Some(HashSet<Value>)` containing the intersection of both values.

# Example

```rust
use serde_json::json;

let v1 = json!(["a", "b", "c"]);
let v2 = json!(["b", "c", "d"]);

let result = oidfed_metadata_policy::intersection_of(&v1, &v2).unwrap();
assert_eq!(result.len(), 2); // Contains "b" and "c"
```"""
def intersection_of(val: Value, val2: Value) -> object | None: ...

"""Extracts only the names (keys) from a JSON value into a `HashSet`.

For objects, extracts the keys. For arrays, extracts the elements.
For single values, creates a set with just that value.

# Arguments

* `values` - A JSON value (object, array, or single value)

# Returns

A `HashSet<Value>` containing the names/keys.

# Example

```rust
use serde_json::json;

let obj = json!({"key1": "value1", "key2": "value2"});
let names = oidfed_metadata_policy::get_hashset_from_only_names(&obj);
assert_eq!(names.len(), 2);
assert!(names.contains(&json!("key1")));
```"""
def get_hashset_from_only_names(values: Value) -> object: ...

"""Resolves metadata according to a given policy.

This function applies policy operators to metadata values and returns the
resolved metadata. It handles operators like `value`, `add`, `default`,
`one_of`, `subset_of`, `superset_of`, and `essential`.

# Arguments

* `policy` - The metadata policy containing operators for each metadata field
* `metadata` - The original metadata to apply the policy to

# Returns

Returns `Ok(Value)` with the resolved metadata, or `Err` if the metadata
violates the policy constraints.

# Errors

Returns an error if:
- A value is not in the `one_of` list
- A value is not a superset of `superset_of` requirement
- An essential field is missing or has an empty value

# Example

```rust
use serde_json::{json, Map, Value};

let policy: Map<String, Value> = json!({
"grant_types": {
"default": ["authorization_code"]
}
}).as_object().unwrap().clone();

let metadata: Map<String, Value> = json!({
"client_name": "My App"
}).as_object().unwrap().clone();

let resolved = oidfed_metadata_policy::resolve_metadata_policy(&policy, &metadata).unwrap();
// grant_types will have the default value since it wasn't in metadata
```"""
def resolve_metadata_policy(policy: object, metadata: object) -> Value: ...

"""Checks if two JSON values are equal using unordered set comparison.

This function compares two JSON objects by checking if they have the same keys
and if the values for each key are equal when treated as sets (order-independent).

# Arguments

* `v1` - First JSON value to compare (must be an object)
* `v2` - Second JSON value to compare (must be an object)

# Returns

`true` if both values have the same keys and equal values (as sets), `false` otherwise.

# Panics

Panics if either value is not a JSON object.

# Example

```rust
use serde_json::json;

let v1 = json!({
"grant_types": ["authorization_code", "implicit"],
"application_type": "web"
});

let v2 = json!({
"application_type": "web",
"grant_types": ["implicit", "authorization_code"]  // Different order, same values
});

assert!(oidfed_metadata_policy::check_equal(&v1, &v2));

let v3 = json!({
"grant_types": ["authorization_code"],
"application_type": "web"
});

assert!(!oidfed_metadata_policy::check_equal(&v1, &v3));
```"""
def check_equal(v1: Value, v2: Value) -> bool: ...

"""Applies a full policy document on the raw metadata of a given entity.

This function processes a complete policy document (containing `metadata_policy` and
optional `metadata` for forced values) and applies it to entity metadata. It handles
multiple entity types including `openid_relying_party`, `openid_provider`,
`federation_entity`, `oauth_client`, `oauth_authorization_server`, and `oauth_resource`.

The function first applies any forced metadata values, then applies the metadata policy
constraints for each entity type present in the input metadata.

# Arguments

* `full_policy` - The complete policy document containing:
- `metadata_policy`: Policy operators for each entity type
- `metadata`: Forced metadata values to override (optional)
* `metadata` - The original entity metadata organized by entity type

# Returns

Returns `Ok(Map<String, Value>)` containing the resolved metadata for all entity types,
or `Err` if policy constraints are violated.

# Errors

Returns an error if:
- No known entity type is found in the metadata
- Policy constraints (e.g., `superset_of`, `one_of`) are violated

# Example

```rust
use serde_json::json;

let metadata = json!({
"openid_relying_party": {
"application_type": "web",
"grant_types": ["authorization_code", "implicit"]
}
});

let full_policy = json!({
"metadata_policy": {
"openid_relying_party": {
"grant_types": {
"subset_of": ["authorization_code", "implicit", "client_credentials"]
}
}
},
"metadata": {
"openid_relying_party": {
"application_type": "native"  // Force this value
}
}
});

let result = oidfed_metadata_policy::apply_policy_document_on_metadata(
full_policy.as_object().unwrap(),
metadata.as_object().unwrap()
).unwrap();

// application_type is now "native" (forced)
assert_eq!(result["openid_relying_party"]["application_type"], "native");
```

# Additional Examples

See the integration tests in [`tests/apply_policy.rs`] for more comprehensive examples:

- `test_apply_blank_policy` - Applying empty policy with forced metadata
- `test_apply_policy_superset_failure` - Error handling when `superset_of` constraint fails
- `test_apply_policy_subset_of_without_metadata` - Using `subset_of` without forced metadata
- `test_apply_policy_subset_of_with_metadata` - Combining `subset_of` with forced metadata

[`tests/apply_policy.rs`]: https://github.com/user/oidfed_metadata_policy/blob/main/tests/apply_policy.rs"""
def apply_policy_document_on_metadata(full_policy: object, metadata: object) -> object: ...

"""Applies a metadata policy to metadata for a single entity type.

This is a wrapper around [`resolve_metadata_policy`] that handles the
resolution and returns the result as a `Map<String, Value>`.

# Arguments

* `policy` - The metadata policy containing operators for each metadata field
* `metadata` - The entity's metadata to apply the policy to

# Returns

Returns `Ok(Map<String, Value>)` with the resolved metadata, or `Err` if
policy constraints are violated.

# Errors

Returns an error if the metadata violates policy constraints.

# Example

```rust
use serde_json::{json, Map, Value};

let policy: Map<String, Value> = json!({
"grant_types": {
"default": ["authorization_code"],
"subset_of": ["authorization_code", "implicit"]
}
}).as_object().unwrap().clone();

let metadata: Map<String, Value> = json!({
"application_type": "web"
}).as_object().unwrap().clone();

let result = oidfed_metadata_policy::apply_policy_on_metadata(policy, &metadata).unwrap();

// grant_types will have the default value ["authorization_code"]
```"""
def apply_policy_on_metadata(policy: object, metadata: object) -> object: ...

__all__: list[str] = ["merge_policies", "merge_one_type_policy", "get_ordered_array", "get_hashset_from_values", "is_subset_of", "is_superset_of", "intersection_of", "get_hashset_from_only_names", "resolve_metadata_policy", "check_equal", "apply_policy_document_on_metadata", "apply_policy_on_metadata"]
