"""Example 6: Create a client-certificate verifier builder."""
from spicycrab_rustls import ClientCertVerifierBuilder, RootCertStore, WebPkiClientVerifier


def main() -> None:
    roots: RootCertStore = RootCertStore.empty()
    _builder: ClientCertVerifierBuilder = WebPkiClientVerifier.builder_from_store(roots)
    print("Created a WebPkiClientVerifier builder")
    print("Add trusted client CAs before calling builder.build()")
