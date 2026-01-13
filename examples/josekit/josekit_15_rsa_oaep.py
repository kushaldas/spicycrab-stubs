"""RSA-OAEP JWE Encryption.

Demonstrates:
- RSA-OAEP key management algorithm
- Generating RSA key pair for encryption
- Encrypting with public key, decrypting with private key
"""

from spicycrab_josekit import (
    JweHeader,
    JwtPayload,
    RSA_OAEP,
    encode_with_encrypter,
    decode_with_decrypter,
)


def main() -> None:
    """Encrypt and decrypt a JWT with RSA-OAEP."""
    header: JweHeader = JweHeader.new()
    header.set_token_type("JWT")
    header.set_content_encryption("A256GCM")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("rsa-oaep-user")
    payload.set_issuer("rsa-oaep.example.com")

    # Generate 2048-bit RSA key pair
    key_pair = RSA_OAEP.generate_key_pair(2048)

    # Encrypt with public key
    encrypter = RSA_OAEP.encrypter_from_jwk(key_pair.to_jwk_public_key())
    jwe: str = encode_with_encrypter(payload, header, encrypter)
    print(f"RSA-OAEP Encrypted JWT: {jwe}")

    # Decrypt with private key
    decrypter = RSA_OAEP.decrypter_from_jwk(key_pair.to_jwk_private_key())
    decoded = decode_with_decrypter(jwe, decrypter)
    print("RSA-OAEP JWE decrypted successfully!")
