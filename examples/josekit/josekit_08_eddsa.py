"""EdDSA JWT Signing with Ed25519.

Demonstrates:
- Generating Ed25519 key pair
- Signing with EdDSA
- Verifying the signature
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    EdDSA,
    EdCurve,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with EdDSA."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("eddsa-user")
    payload.set_issuer("eddsa.example.com")

    # Generate Ed25519 key pair
    key_pair = EdDSA.generate_key_pair(EdCurve.Ed25519)

    # Sign the JWT with private key
    signer = EdDSA.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"EdDSA JWT: {jwt}")

    # Verify with public key
    verifier = EdDSA.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("EdDSA JWT verified!")
