"""Example 5: Create multiple root certificate stores."""
from spicycrab_rustls import RootCertStore


def main() -> None:
    # Create first store
    store1: RootCertStore = RootCertStore.empty()
    print(f"Store 1 is empty: {store1.is_empty()}")

    # Create second store
    store2: RootCertStore = RootCertStore.empty()
    print(f"Store 2 is empty: {store2.is_empty()}")

    print("Created two empty RootCertStores successfully")
