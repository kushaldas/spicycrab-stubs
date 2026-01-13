"""Example 1: Create an empty RootCertStore and check its properties."""
from spicycrab_rustls import RootCertStore


def main() -> None:
    # Create an empty certificate store
    store: RootCertStore = RootCertStore.empty()

    # Check if the store is empty
    is_empty: bool = store.is_empty()
    print(f"Store is empty: {is_empty}")
