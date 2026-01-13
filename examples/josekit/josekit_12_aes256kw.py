"""AES Key Wrap JWE Encryption with A256KW.

Demonstrates:
- AES-256 Key Wrap key management algorithm
- 32-byte key for A256KW
- Encrypting JWT with A256GCM content encryption
"""

from spicycrab_josekit import (
    JweHeader,
    JwtPayload,
    A256KW,
    encode_with_encrypter,
    decode_with_decrypter,
)


def main() -> None:
    """Encrypt and decrypt a JWT with AES-256 Key Wrap."""
    header: JweHeader = JweHeader.new()
    header.set_token_type("JWT")
    header.set_content_encryption("A256GCM")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("aes256kw-user")
    payload.set_issuer("aes256kw.example.com")

    # 32-byte key for A256KW
    key = b"0123456789ABCDEF0123456789ABCDEF"

    # Encrypt the JWT
    encrypter = A256KW.encrypter_from_bytes(key)
    jwe: str = encode_with_encrypter(payload, header, encrypter)
    print(f"A256KW Encrypted JWT: {jwe}")

    # Decrypt the JWT
    decrypter = A256KW.decrypter_from_bytes(key)
    decoded = decode_with_decrypter(jwe, decrypter)
    print("A256KW JWE decrypted successfully!")
