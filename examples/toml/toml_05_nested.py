"""Parse deeply nested TOML example.

Demonstrates:
- Parsing complex nested TOML
"""

from spicycrab_toml import from_str, Value


def main() -> None:
    """Parse deeply nested TOML."""
    toml_str: str = '[server]\nhost = "localhost"\nport = 8080\n\n[server.tls]\nenabled = true'
    value: Value = from_str(toml_str)
    print(f"Parsed nested TOML: {value}")
