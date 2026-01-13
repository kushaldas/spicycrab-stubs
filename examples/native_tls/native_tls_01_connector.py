"""Example 1: Create a TLS connector using the builder pattern."""
from spicycrab_native_tls import TlsConnector, TlsConnectorBuilder


def main() -> None:
    # Create a TLS connector builder
    builder: TlsConnectorBuilder = TlsConnector.builder()
    print("Created TlsConnectorBuilder")

    # Build the connector (using default settings)
    connector: TlsConnector = builder.build()
    print("Built TlsConnector successfully")
