"""Example 3: Working with TLS 1.3 cipher suites."""
from spicycrab_rustls import Tls13CipherSuite, SupportedCipherSuite


def main() -> None:
    # Check if cipher suites support FIPS
    # Note: This example demonstrates the type structure
    print("Rustls cipher suite types available")
    print("- Tls13CipherSuite: For TLS 1.3 cipher suites")
    print("- SupportedCipherSuite: Generic cipher suite wrapper")
