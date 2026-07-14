"""Example 5: Create a server-certificate verifier builder."""
from spicycrab_rustls import RootCertStore, ServerCertVerifierBuilder, WebPkiServerVerifier


def main() -> None:
    roots: RootCertStore = RootCertStore.empty()
    _builder: ServerCertVerifierBuilder = WebPkiServerVerifier.builder_from_store(roots)
    print("Created a WebPkiServerVerifier builder")
    print("Add trusted roots before calling builder.build()")
