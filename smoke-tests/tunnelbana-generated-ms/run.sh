#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

TUNNELBANA_REPO="${TUNNELBANA_REPO:-/home/kdas/code/xml/tunnelbana}"
SPICYCRAB_REPO="${SPICYCRAB_REPO:-/home/kdas/code/pyexp/spicycrab}"
WORK_ROOT="${WORK_ROOT:-$(mktemp -d /tmp/tunnelbana-spicycrab-smoke.XXXXXX)}"
CLONE_DIR="${WORK_ROOT}/tunnelbana"
TARGET_DIR="${CARGO_TARGET_DIR:-${WORK_ROOT}/target}"
RUN_BASELINE_CHECK="${RUN_BASELINE_CHECK:-1}"
RUN_FULL_WORKSPACE_TESTS="${RUN_FULL_WORKSPACE_TESTS:-1}"

if [[ ! -d "${TUNNELBANA_REPO}/.git" ]]; then
    echo "TUNNELBANA_REPO is not a git checkout: ${TUNNELBANA_REPO}" >&2
    exit 2
fi

if [[ ! -d "${SPICYCRAB_REPO}/.git" ]]; then
    echo "SPICYCRAB_REPO is not a git checkout: ${SPICYCRAB_REPO}" >&2
    exit 2
fi

if [[ -e "${CLONE_DIR}" ]]; then
    echo "Refusing to reuse existing clone directory: ${CLONE_DIR}" >&2
    exit 2
fi

echo "==> Cloning tunnelbana"
echo "    from: ${TUNNELBANA_REPO}"
echo "      to: ${CLONE_DIR}"
git clone --quiet "${TUNNELBANA_REPO}" "${CLONE_DIR}"

if [[ "${RUN_BASELINE_CHECK}" != "0" ]]; then
    echo "==> Baseline cargo check --workspace"
    CARGO_TARGET_DIR="${TARGET_DIR}" cargo check --workspace --manifest-path "${CLONE_DIR}/Cargo.toml"
fi

echo "==> Copying Python source into temp clone"
mkdir -p "${CLONE_DIR}/generated-sources"
cp "${SCRIPT_DIR}/generated_marker.py" "${CLONE_DIR}/generated-sources/generated_marker.py"

echo "==> Transpiling generated_marker.py into crates/spicycrab-generated-ms"
(
    cd "${SPICYCRAB_REPO}"
    uv run crabpy transpile \
        "${CLONE_DIR}/generated-sources/generated_marker.py" \
        -o "${CLONE_DIR}/crates/spicycrab-generated-ms" \
        --name spicycrab-generated-ms \
        --no-format
)

echo "==> Wiring generated crate into the cloned tunnelbana workspace"
perl -0pi -e 's/(members = \[\n)/$1    "crates\/spicycrab-generated-ms",\n/' "${CLONE_DIR}/Cargo.toml"
perl -0pi -e 's#tunnelbana-core = \{ path = "[^"]+" \}#tunnelbana-core = { path = "../tunnelbana-core" }#' \
    "${CLONE_DIR}/crates/spicycrab-generated-ms/Cargo.toml"

if ! grep -q '^\[dev-dependencies\]' "${CLONE_DIR}/crates/spicycrab-generated-ms/Cargo.toml"; then
    {
        printf '\n[dev-dependencies]\n'
        printf 'tokio = { workspace = true }\n'
    } >> "${CLONE_DIR}/crates/spicycrab-generated-ms/Cargo.toml"
fi

mkdir -p "${CLONE_DIR}/crates/spicycrab-generated-ms/tests"
cp "${SCRIPT_DIR}/registry_smoke.rs" "${CLONE_DIR}/crates/spicycrab-generated-ms/tests/registry_smoke.rs"

echo "==> Checking generated Rust ownership shape"
grep -q 'self.marker_value.clone()' "${CLONE_DIR}/crates/spicycrab-generated-ms/src/lib.rs"

echo "==> Formatting workspace"
CARGO_TARGET_DIR="${TARGET_DIR}" cargo fmt --all --manifest-path "${CLONE_DIR}/Cargo.toml"

echo "==> Running generated microservice registry smoke test"
CARGO_TARGET_DIR="${TARGET_DIR}" cargo test \
    --manifest-path "${CLONE_DIR}/Cargo.toml" \
    -p spicycrab-generated-ms \
    --test registry_smoke \
    -- --nocapture

echo "==> Running cargo check --workspace with generated crate"
CARGO_TARGET_DIR="${TARGET_DIR}" cargo check --workspace --manifest-path "${CLONE_DIR}/Cargo.toml"

if [[ "${RUN_FULL_WORKSPACE_TESTS}" != "0" ]]; then
    echo "==> Running cargo test --workspace with generated crate"
    CARGO_TARGET_DIR="${TARGET_DIR}" cargo test --workspace --manifest-path "${CLONE_DIR}/Cargo.toml"
else
    echo "==> Skipping full workspace tests because RUN_FULL_WORKSPACE_TESTS=0"
fi

echo "==> Smoke test complete"
echo "    temp clone: ${CLONE_DIR}"
echo "    target dir: ${TARGET_DIR}"
