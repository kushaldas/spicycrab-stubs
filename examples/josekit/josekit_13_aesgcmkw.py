"""AES-GCM Key Wrap JWE Encryption with A128GCMKW.

Demonstrates:
- AES-GCM Key Wrap key management algorithm
- 16-byte key for A128GCMKW
"""

from spicycrab_josekit import (
    JweHeader,
    JwtPayload,
    A128GCMKW,
    encode_with_encrypter,
    decode_with_decrypter,
)


def main() -> None:
    """Encrypt and decrypt a JWT with AES-GCM Key Wrap."""
    header: JweHeader = JweHeader.new()
    header.set_token_type("JWT")
    header.set_content_encryption("A128GCM")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("aesgcmkw-user")
    payload.set_issuer("aesgcmkw.example.com")

    # 16-byte key for A128GCMKW
    key = b"0123456789ABCDEF"

    # Encrypt the JWT
    encrypter = A128GCMKW.encrypter_from_bytes(key)
    jwe: str = encode_with_encrypter(payload, header, encrypter)
    print(f"A128GCMKW Encrypted JWT: {jwe}")

    # Decrypt the JWT
    decrypter = A128GCMKW.decrypter_from_bytes(key)
    decoded = decode_with_decrypter(jwe, decrypter)
    print("A128GCMKW JWE decrypted successfully!")
