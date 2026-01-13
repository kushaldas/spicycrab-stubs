"""RSA-PSS JWT Signing with PS512.

Demonstrates:
- PS512 algorithm (RSA-PSS with SHA-512)
- 2048-bit RSA key pair
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    PS512,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with RSA-PSS-SHA512."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("ps512-user")
    payload.set_issuer("ps512.example.com")

    # Generate 2048-bit RSA-PSS key pair
    key_pair = PS512.generate_key_pair(2048)

    # Sign the JWT with private key
    signer = PS512.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"PS512 JWT: {jwt}")

    # Verify with public key
    verifier = PS512.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("PS512 JWT verified!")
