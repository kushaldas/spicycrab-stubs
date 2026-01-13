"""AES Key Wrap JWE Encryption with A128KW.

Demonstrates:
- AES Key Wrap key management algorithm
- Encrypting JWT with A128KW
- Decrypting the JWE
"""

from spicycrab_josekit import (
    JweHeader,
    JwtPayload,
    A128KW,
    encode_with_encrypter,
    decode_with_decrypter,
)


def main() -> None:
    """Encrypt and decrypt a JWT with AES Key Wrap."""
    header: JweHeader = JweHeader.new()
    header.set_token_type("JWT")
    header.set_content_encryption("A128GCM")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("aeskw-user")
    payload.set_issuer("aeskw.example.com")

    # 16-byte key for A128KW
    key = b"0123456789ABCDEF"

    # Encrypt the JWT
    encrypter = A128KW.encrypter_from_bytes(key)
    jwe: str = encode_with_encrypter(payload, header, encrypter)
    print(f"A128KW Encrypted JWT: {jwe}")

    # Decrypt the JWT
    decrypter = A128KW.decrypter_from_bytes(key)
    decoded = decode_with_decrypter(jwe, decrypter)
    print("A128KW JWE decrypted successfully!")
