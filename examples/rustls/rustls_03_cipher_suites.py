"""Example 3: Inspect the default provider's cipher suites."""
from spicycrab_rustls import CryptoProvider, default_provider


def main() -> None:
    provider: CryptoProvider = default_provider()
    count: int = provider.cipher_suite_count()
    print(f"The default provider offers {count} cipher suites")
    print(f"All provider components are FIPS enabled: {provider.fips()}")
