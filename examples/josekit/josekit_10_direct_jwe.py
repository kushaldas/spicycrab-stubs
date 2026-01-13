"""Direct JWE Encryption with A128GCM.

Demonstrates:
- Direct encryption using shared secret
- Creating JWE header
- Encrypting and decrypting payload
"""

from spicycrab_josekit import (
    JweHeader,
    JwtPayload,
    Dir,
    encode_with_encrypter,
    decode_with_decrypter,
)


def main() -> None:
    """Encrypt and decrypt a JWT with direct encryption."""
    header: JweHeader = JweHeader.new()
    header.set_token_type("JWT")
    header.set_content_encryption("A128GCM")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("encrypted-user")
    payload.set_issuer("jwe.example.com")

    # 16-byte key for A128GCM content encryption
    key = b"0123456789ABCDEF"

    # Encrypt the JWT
    encrypter = Dir.encrypter_from_bytes(key)
    jwe: str = encode_with_encrypter(payload, header, encrypter)
    print(f"Encrypted JWT: {jwe}")

    # Decrypt the JWT
    decrypter = Dir.decrypter_from_bytes(key)
    decoded = decode_with_decrypter(jwe, decrypter)
    print("JWE decrypted successfully!")
