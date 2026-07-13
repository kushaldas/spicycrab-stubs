# spicycrab-stubs justfile
# Commands for managing stub packages and version tags

# Resolve paths from the repository root, including when this file is invoked
# with `just --justfile /path/to/spicycrab-stubs/justfile ...`.
repo_root := justfile_directory()

# Default recipe - list available commands
default:
    @just --justfile "{{ repo_root }}/justfile" --list

# Create a version tag for a stub package
# Usage: just tag <crate> <version>
# Example: just tag clap 4.5.0
tag crate version:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{ repo_root }}"

    TAG="{{ crate }}-{{ version }}"
    STUB_DIR="stubs/{{ crate }}"

    # Verify the crate directory exists
    if [ ! -d "$STUB_DIR" ]; then
        echo "Error: Stub directory '$STUB_DIR' not found"
        exit 1
    fi

    # Verify pyproject.toml exists
    if [ ! -f "$STUB_DIR/pyproject.toml" ]; then
        echo "Error: $STUB_DIR/pyproject.toml not found"
        exit 1
    fi

    # Check version in pyproject.toml matches
    TOML_VERSION=$(grep -E '^[[:space:]]*version[[:space:]]*=' "$STUB_DIR/pyproject.toml" | head -1 | sed 's/.*"\(.*\)".*/\1/')
    if [ "$TOML_VERSION" != "{{ version }}" ]; then
        echo "Warning: pyproject.toml version ($TOML_VERSION) doesn't match tag version ({{ version }})"
        read -p "Continue anyway? [y/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi

    # Check if tag already exists
    if git rev-parse --verify "refs/tags/$TAG" >/dev/null 2>&1; then
        echo "Error: Tag '$TAG' already exists"
        echo "To update, delete it first: git tag -d $TAG && git push origin :refs/tags/$TAG"
        exit 1
    fi

    # Create and push tag
    echo "Creating tag: $TAG"
    git add -- "$STUB_DIR"
    # Commit only this stub package. Unrelated staged work remains staged.
    git commit --only --allow-empty -m "{{ crate }}: version {{ version }}" -- "$STUB_DIR"
    git tag -a "$TAG" -m "{{ crate }} version {{ version }}"

    echo ""
    echo "Tag '$TAG' created locally."
    echo "To push: git push origin main && git push origin $TAG"

# List all existing tags
tags:
    @git -C "{{ repo_root }}" tag -l | sort -V

# List tags for a specific crate
# Usage: just tags-for <crate>
tags-for crate:
    @git -C "{{ repo_root }}" tag -l "{{ crate }}-*" | sort -V

# List stub crates with staged, unstaged, or untracked changes and their versions
changed:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{ repo_root }}"

    mapfile -d '' CRATES < <(
        {
            git diff --name-only --no-renames -z -- stubs/
            git diff --cached --name-only --no-renames -z -- stubs/
            git ls-files --others --exclude-standard -z -- stubs/
        } |
            while IFS= read -r -d '' PATHNAME; do
                case "$PATHNAME" in
                    stubs/*/*)
                        CRATE="${PATHNAME#stubs/}"
                        printf '%s\0' "${CRATE%%/*}"
                        ;;
                esac
            done |
            sort -zu
    )

    if [ "${#CRATES[@]}" -eq 0 ]; then
        echo "No stub crates have uncommitted changes."
        exit 0
    fi

    printf '%-28s %s\n' "CRATE" "VERSION"
    printf '%-28s %s\n' "----------------------------" "----------------"
    for CRATE in "${CRATES[@]}"; do
        PYPROJECT="stubs/$CRATE/pyproject.toml"
        if [ ! -f "$PYPROJECT" ]; then
            VERSION="<missing pyproject.toml>"
        else
            VERSION=$(awk -F'"' '/^[[:space:]]*version[[:space:]]*=/{print $2; exit}' "$PYPROJECT")
            if [ -z "$VERSION" ]; then
                VERSION="<missing version>"
            fi
        fi
        printf '%-28s %s\n' "$CRATE" "$VERSION"
    done

# Validate a stub package
# Usage: just validate <crate>
validate crate:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{ repo_root }}"

    STUB_DIR="stubs/{{ crate }}"
    PKG_NAME="spicycrab_$(echo "{{ crate }}" | tr '-' '_')"
    PKG_DIR="$STUB_DIR/$PKG_NAME"

    if [ ! -d "$STUB_DIR" ]; then
        echo "Error: Stub directory '$STUB_DIR' not found"
        exit 1
    fi

    echo "Validating {{ crate }}..."

    # Check required files
    ERRORS=0

    if [ ! -f "$STUB_DIR/pyproject.toml" ]; then
        echo "  [FAIL] Missing pyproject.toml"
        ERRORS=$((ERRORS + 1))
    else
        echo "  [OK] pyproject.toml"
    fi

    if [ ! -d "$PKG_DIR" ]; then
        echo "  [FAIL] Missing package directory: $PKG_DIR"
        ERRORS=$((ERRORS + 1))
    else
        echo "  [OK] Package directory: $(basename $PKG_DIR)"

        if [ ! -f "$PKG_DIR/__init__.py" ]; then
            echo "  [FAIL] Missing __init__.py"
            ERRORS=$((ERRORS + 1))
        else
            echo "  [OK] __init__.py"
        fi

        if [ ! -f "$PKG_DIR/_spicycrab.toml" ]; then
            echo "  [FAIL] Missing _spicycrab.toml"
            ERRORS=$((ERRORS + 1))
        else
            echo "  [OK] _spicycrab.toml"
        fi
    fi

    echo ""
    if [ $ERRORS -eq 0 ]; then
        echo "Validation PASSED"
    else
        echo "Validation FAILED with $ERRORS error(s)"
        exit 1
    fi

# Build a stub package wheel
# Usage: just build <crate>
build crate:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{ repo_root }}"

    STUB_DIR="stubs/{{ crate }}"

    if [ ! -d "$STUB_DIR" ]; then
        echo "Error: Stub directory '$STUB_DIR' not found"
        exit 1
    fi

    echo "Building wheel for {{ crate }}..."
    if command -v uv >/dev/null 2>&1; then
        uv run --quiet --with build python -m build --wheel "$STUB_DIR"
    elif python3 -c 'import build' >/dev/null 2>&1; then
        python3 -m build --wheel "$STUB_DIR"
    else
        echo "Error: building requires either uv or the Python 'build' package" >&2
        echo "Install one with: python3 -m pip install build" >&2
        exit 1
    fi
    echo ""
    echo "Wheel built in $STUB_DIR/dist/"

# Create a new stub package scaffold
# Usage: just new <crate> <version>
new crate version:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{ repo_root }}"

    STUB_DIR="stubs/{{ crate }}"
    PKG_NAME="spicycrab_$(echo "{{ crate }}" | tr '-' '_')"
    RUST_CRATE_NAME="$(echo "{{ crate }}" | tr '-' '_')"

    if [ -d "$STUB_DIR" ]; then
        echo "Error: Directory '$STUB_DIR' already exists"
        exit 1
    fi

    echo "Creating stub scaffold for {{ crate }}..."

    mkdir -p "$STUB_DIR/$PKG_NAME"

    # Create pyproject.toml
    cat > "$STUB_DIR/pyproject.toml" << 'PYPROJECT'
    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [project]
    name = "spicycrab-{{ crate }}"
    version = "{{ version }}"
    description = "spicycrab type stubs for the {{ crate }} Rust crate"
    requires-python = ">=3.11"
    dependencies = []

    [project.entry-points."spicycrab.stubs"]
    {{ crate }} = "PKG_NAME"

    [tool.hatch.build.targets.wheel]
    packages = ["PKG_NAME"]
    PYPROJECT

    # Fix the PKG_NAME placeholder
    sed -i "s/PKG_NAME/$PKG_NAME/g" "$STUB_DIR/pyproject.toml"
    # Remove leading spaces from heredoc
    sed -i 's/^    //' "$STUB_DIR/pyproject.toml"

    # Create __init__.py
    cat > "$STUB_DIR/$PKG_NAME/__init__.py" << 'INIT'
    """Python stubs for the {{ crate }} Rust crate.

    Install with: cookcrab install {{ crate }}
    """

    from __future__ import annotations

    # TODO: Add type stubs here

    __all__: list[str] = []
    INIT
    sed -i 's/^    //' "$STUB_DIR/$PKG_NAME/__init__.py"

    # Create _spicycrab.toml
    cat > "$STUB_DIR/$PKG_NAME/_spicycrab.toml" << 'TOML'
    [package]
    name = "{{ crate }}"
    rust_crate = "RUST_CRATE_NAME"
    rust_version = "{{ version }}"
    python_module = "PKG_NAME"

    [cargo.dependencies]
    {{ crate }} = "{{ version }}"

    # TODO: Add function mappings
    # [[mappings.functions]]
    # python = "{{ crate }}.SomeType.new"
    # rust_code = "RUST_CRATE_NAME::SomeType::new({arg0})"
    # rust_imports = ["RUST_CRATE_NAME::SomeType"]
    # needs_result = false

    # TODO: Add method mappings
    # [[mappings.methods]]
    # python = "SomeType.method"
    # rust_code = "{self}.method({arg0})"
    # rust_imports = []
    # needs_result = false

    # TODO: Add type mappings
    # [[mappings.types]]
    # python = "SomeType"
    # rust = "RUST_CRATE_NAME::SomeType"
    TOML
    sed -i "s/PKG_NAME/$PKG_NAME/g" "$STUB_DIR/$PKG_NAME/_spicycrab.toml"
    sed -i "s/RUST_CRATE_NAME/$RUST_CRATE_NAME/g" "$STUB_DIR/$PKG_NAME/_spicycrab.toml"
    sed -i 's/^    //' "$STUB_DIR/$PKG_NAME/_spicycrab.toml"

    # Create README.md
    cat > "$STUB_DIR/README.md" << 'README'
    # spicycrab-{{ crate }}

    Python type stubs for the [{{ crate }}](https://crates.io/crates/{{ crate }}) Rust crate.

    **Install with cookcrab, NOT pip:**

    ```bash
    cookcrab install {{ crate }}
    ```

    ## Usage

    ```python
    from PKG_NAME import ...

    # TODO: Add usage example
    ```
    README
    sed -i "s/PKG_NAME/$PKG_NAME/g" "$STUB_DIR/README.md"
    sed -i 's/^    //' "$STUB_DIR/README.md"

    echo ""
    echo "Scaffold created at $STUB_DIR/"
    echo ""
    echo "Next steps:"
    echo "  1. Edit $STUB_DIR/$PKG_NAME/__init__.py - add Python stubs"
    echo "  2. Edit $STUB_DIR/$PKG_NAME/_spicycrab.toml - add mappings"
    echo "  3. Validate: just validate {{ crate }}"
    echo "  4. Tag: just tag {{ crate }} {{ version }}"

# Delete a tag (local and remote)
# Usage: just delete-tag <crate> <version>
delete-tag crate version:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{ repo_root }}"

    TAG="{{ crate }}-{{ version }}"

    echo "Deleting tag: $TAG"

    # Delete local tag
    git tag -d "$TAG" 2>/dev/null || echo "Local tag not found"

    # Delete remote tag
    git push origin ":refs/tags/$TAG" 2>/dev/null || echo "Remote tag not found"

    echo "Tag '$TAG' deleted"
