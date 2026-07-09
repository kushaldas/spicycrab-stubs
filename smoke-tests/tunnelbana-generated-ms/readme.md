# Tunnelbana Generated Microservice Smoke Harness

This harness validates that spicycrab can generate a Tunnelbana
`MicroService`, build it as a Rust crate, register it through
`tunnelbana_core::Registry`, and run it inside a cloned Tunnelbana workspace.

The harness intentionally works in a temporary clone of Tunnelbana. It does not
modify the live checkout under `/home/kdas/code/xml/tunnelbana`.

## Files

- `generated_marker.py`: the Python microservice source transpiled by
  spicycrab.
- `registry_smoke.rs`: a Rust integration test copied into the generated crate.
- `run.sh`: end-to-end automation for clone, transpile, workspace wiring, and
  tests.

## What It Tests

`GeneratedMarker` is a generated `MicroService` with two hooks:

- `process_request`: writes `request_seen = "yes"` into Tunnelbana state under
  the service name.
- `process_response`: writes the `generated-marker` attribute from an owned
  `self.marker_value` field.

The Rust smoke test registers a constructor with `Registry`, builds the service
through `Registry::build_microservice`, runs both hooks, and asserts both
mutations. The `self.marker_value` use is deliberate: it catches ownership bugs
where generated Rust tries to move a `String` field out of `&self` instead of
cloning it.

## Prerequisites

Default paths assumed by `run.sh`:

- Tunnelbana repo: `/home/kdas/code/xml/tunnelbana`
- spicycrab repo: `/home/kdas/code/pyexp/spicycrab`
- this harness: `/home/kdas/code/pyexp/spicycrab-stubs/smoke-tests/tunnelbana-generated-ms`

The spicycrab environment must have the local Tunnelbana stubs installed. From
`/home/kdas/code/pyexp/spicycrab`:

```bash
uv pip install \
  -e /home/kdas/code/pyexp/spicycrab-stubs/stubs/tunnelbana-core \
  -e /home/kdas/code/pyexp/spicycrab-stubs/stubs/tunnelbana-plugins \
  -e /home/kdas/code/pyexp/spicycrab-stubs/stubs/grindvakt
```

You also need Rust/Cargo, Git, Perl, and `uv`.

## Run The Harness

From this directory:

```bash
./run.sh
```

The script creates and keeps a temp directory like:

```text
/tmp/tunnelbana-spicycrab-smoke.XXXXXX/tunnelbana
```

It prints the exact temp clone and Cargo target directory at the end.

## Useful Environment Variables

Override repo paths:

```bash
TUNNELBANA_REPO=/path/to/tunnelbana \
SPICYCRAB_REPO=/path/to/spicycrab \
./run.sh
```

Reuse or choose a work directory:

```bash
WORK_ROOT=/tmp/my-tunnelbana-smoke ./run.sh
```

Choose a Cargo target directory:

```bash
CARGO_TARGET_DIR=/tmp/tunnelbana-smoke-target ./run.sh
```

Skip the baseline workspace check before adding the generated crate:

```bash
RUN_BASELINE_CHECK=0 ./run.sh
```

Skip the final full workspace test run while still running the generated crate
test and `cargo check --workspace`:

```bash
RUN_FULL_WORKSPACE_TESTS=0 ./run.sh
```

## Manual Steps

These are the operations performed by `run.sh`.

1. Clone Tunnelbana into a temp directory:

```bash
workdir="$(mktemp -d /tmp/tunnelbana-spicycrab-smoke.XXXXXX)"
git clone /home/kdas/code/xml/tunnelbana "$workdir/tunnelbana"
```

2. Optionally verify the clean clone first:

```bash
CARGO_TARGET_DIR="$workdir/target" cargo check \
  --workspace \
  --manifest-path "$workdir/tunnelbana/Cargo.toml"
```

3. Copy the Python source into the clone:

```bash
mkdir -p "$workdir/tunnelbana/generated-sources"
cp generated_marker.py "$workdir/tunnelbana/generated-sources/generated_marker.py"
```

4. Transpile it into a new crate:

```bash
cd /home/kdas/code/pyexp/spicycrab
uv run crabpy transpile \
  "$workdir/tunnelbana/generated-sources/generated_marker.py" \
  -o "$workdir/tunnelbana/crates/spicycrab-generated-ms" \
  --name spicycrab-generated-ms \
  --no-format
```

5. Add the crate to the cloned workspace `Cargo.toml`:

```toml
members = [
    "crates/spicycrab-generated-ms",
    "crates/tunnelbana-core",
    "crates/tunnelbana-oidc",
    "crates/tunnelbana-plugins",
    "crates/tunnelbana",
]
```

6. Change the generated crate dependency to point at the cloned core crate:

```toml
tunnelbana-core = { path = "../tunnelbana-core" }

[dev-dependencies]
tokio = { workspace = true }
```

7. Copy the Rust integration test:

```bash
mkdir -p "$workdir/tunnelbana/crates/spicycrab-generated-ms/tests"
cp registry_smoke.rs \
  "$workdir/tunnelbana/crates/spicycrab-generated-ms/tests/registry_smoke.rs"
```

8. Confirm generated Rust clones the owned self field:

```bash
grep 'self.marker_value.clone()' \
  "$workdir/tunnelbana/crates/spicycrab-generated-ms/src/lib.rs"
```

9. Format and test:

```bash
CARGO_TARGET_DIR="$workdir/target" cargo fmt \
  --all \
  --manifest-path "$workdir/tunnelbana/Cargo.toml"

CARGO_TARGET_DIR="$workdir/target" cargo test \
  --manifest-path "$workdir/tunnelbana/Cargo.toml" \
  -p spicycrab-generated-ms \
  --test registry_smoke \
  -- --nocapture

CARGO_TARGET_DIR="$workdir/target" cargo check \
  --workspace \
  --manifest-path "$workdir/tunnelbana/Cargo.toml"

CARGO_TARGET_DIR="$workdir/target" cargo test \
  --workspace \
  --manifest-path "$workdir/tunnelbana/Cargo.toml"
```

## Expected Result

The generated crate test should include:

```text
test generated_microservice_builds_and_runs_through_registry ... ok
```

The full workspace test run should pass all Tunnelbana tests plus the generated
crate smoke test.

One warning is currently expected:

```text
warning: unused variable: `ctx`
```

That comes from generated `process_response` methods whose Python source does
not use `ctx`.

## Cleanup

The script keeps the temp clone so failures can be inspected. Remove it when
done:

```bash
rm -rf /tmp/tunnelbana-spicycrab-smoke.*
```
