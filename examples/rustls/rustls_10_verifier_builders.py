"""Example 10: Create separate stores for client and server verification."""
from spicycrab_rustls import RootCertStore


def main() -> None:
    # Create certificate stores for different purposes

    # Store for verifying server certificates (client-side)
    server_roots: RootCertStore = RootCertStore.empty()
    print(f"Server trust store: empty={server_roots.is_empty()}")

    # Store for verifying client certificates (server-side, for mTLS)
    client_roots: RootCertStore = RootCertStore.empty()
    print(f"Client trust store: empty={client_roots.is_empty()}")

    print("Both certificate stores ready for TLS configuration")
