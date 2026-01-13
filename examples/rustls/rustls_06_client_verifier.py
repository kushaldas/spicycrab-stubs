"""Example 6: Check certificate store state."""
from spicycrab_rustls import RootCertStore


def main() -> None:
    # Create an empty root certificate store
    store: RootCertStore = RootCertStore.empty()

    # Check various properties
    empty: bool = store.is_empty()
    print(f"Store is empty: {empty}")

    # The store can be used for TLS verification
    print("RootCertStore ready for use with TLS configurations")
