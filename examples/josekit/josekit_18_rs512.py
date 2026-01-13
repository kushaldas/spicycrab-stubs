"""RSA JWT Signing with RS512.

Demonstrates:
- RS512 algorithm (RSA with SHA-512)
- 2048-bit RSA key pair
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    RS512,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with RSA-SHA512."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("rs512-user")
    payload.set_issuer("rs512.example.com")

    # Generate 2048-bit RSA key pair
    key_pair = RS512.generate_key_pair(2048)

    # Sign the JWT with private key
    signer = RS512.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"RS512 JWT: {jwt}")

    # Verify with public key
    verifier = RS512.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("RS512 JWT verified!")
