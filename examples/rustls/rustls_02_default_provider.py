"""Example 2: Get the default cryptographic provider."""
from spicycrab_rustls import default_provider, CryptoProvider


def main() -> None:
    # Get the default cryptographic provider
    provider: CryptoProvider = default_provider()
    print("Got default crypto provider")
