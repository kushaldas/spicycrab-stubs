"""Example 9: Create a KeyLogFile for TLS debugging with Wireshark."""
from spicycrab_rustls import KeyLogFile


def main() -> None:
    # Create a key log file
    # This reads from SSLKEYLOGFILE environment variable
    key_log: KeyLogFile = KeyLogFile.new()
    print("Created KeyLogFile")
    print("Set SSLKEYLOGFILE env var to enable TLS key logging")
    print("Useful for debugging TLS traffic with Wireshark")
