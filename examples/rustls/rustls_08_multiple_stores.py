"""Example 8: Multiple root certificate stores."""
from spicycrab_rustls import RootCertStore


def main() -> None:
    # Create multiple certificate stores for different purposes
    server_roots: RootCertStore = RootCertStore.empty()
    client_roots: RootCertStore = RootCertStore.empty()

    print(f"Server roots empty: {server_roots.is_empty()}")
    print(f"Client roots empty: {client_roots.is_empty()}")
    print(f"Server roots count: {server_roots.len()}")
    print(f"Client roots count: {client_roots.len()}")
