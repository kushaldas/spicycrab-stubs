"""Example 4: Create a KeyLogFile for TLS debugging."""
from spicycrab_rustls import KeyLogFile


def main() -> None:
    # Create a key log file for debugging TLS connections
    # This is useful for debugging with Wireshark
    key_log: KeyLogFile = KeyLogFile.new()
    print("Created KeyLogFile for TLS key logging")
    print("Key logs can be used with Wireshark to decrypt TLS traffic")
