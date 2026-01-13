"""Example 7: Demonstrate empty store creation pattern."""
from spicycrab_rustls import RootCertStore


def main() -> None:
    # Pattern for creating server-side certificate store
    # Server needs to verify client certs (mTLS) or can skip verification

    # For mTLS: create a store and add trusted client CA certs
    client_trust_store: RootCertStore = RootCertStore.empty()
    print(f"Client trust store ready: empty={client_trust_store.is_empty()}")

    # For standard TLS without mTLS, no client cert store needed
    print("Standard TLS: no client certificate verification required")
