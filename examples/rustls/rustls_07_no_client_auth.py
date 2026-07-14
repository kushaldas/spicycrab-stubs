"""Example 7: Disable client-certificate authentication."""
from spicycrab_rustls import ClientCertVerifier, WebPkiClientVerifier


def main() -> None:
    # Rustls returns an Arc<dyn ClientCertVerifier>.  The verifier is retained
    # by the generated Rust even though Python has no useful concrete type for it.
    _verifier: ClientCertVerifier = WebPkiClientVerifier.no_client_auth()
    print("Created the standard no-client-auth verifier")
