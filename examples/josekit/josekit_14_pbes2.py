"""PBES2 Password-Based JWE Encryption.

Demonstrates:
- Password-based encryption (PBES2-HS256+A128KW)
- Password-derived key encryption
"""

from spicycrab_josekit import (
    JweHeader,
    JwtPayload,
    PBES2_HS256_A128KW,
    encode_with_encrypter,
    decode_with_decrypter,
)


def main() -> None:
    """Encrypt and decrypt a JWT with password-based encryption."""
    header: JweHeader = JweHeader.new()
    header.set_token_type("JWT")
    header.set_content_encryption("A128GCM")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("pbes2-user")
    payload.set_issuer("pbes2.example.com")

    # Password for PBES2
    password = b"my-secret-password"

    # Encrypt the JWT
    encrypter = PBES2_HS256_A128KW.encrypter_from_bytes(password)
    jwe: str = encode_with_encrypter(payload, header, encrypter)
    print(f"PBES2 Encrypted JWT: {jwe}")

    # Decrypt the JWT
    decrypter = PBES2_HS256_A128KW.decrypter_from_bytes(password)
    decoded = decode_with_decrypter(jwe, decrypter)
    print("PBES2 JWE decrypted successfully!")
