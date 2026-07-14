"""Example 10: Create both WebPKI verifier builders."""
from spicycrab_rustls import (
    ClientCertVerifierBuilder,
    RootCertStore,
    ServerCertVerifierBuilder,
    WebPkiClientVerifier,
    WebPkiServerVerifier,
)


def main() -> None:
    server_roots: RootCertStore = RootCertStore.empty()
    _server_builder: ServerCertVerifierBuilder = WebPkiServerVerifier.builder_from_store(server_roots)

    client_roots: RootCertStore = RootCertStore.empty()
    _client_builder: ClientCertVerifierBuilder = WebPkiClientVerifier.builder_from_store(client_roots)

    print("Created server- and client-certificate verifier builders")
    print("Both builders need non-empty trust stores before build()")
