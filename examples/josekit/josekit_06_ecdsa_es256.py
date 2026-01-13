"""ECDSA JWT Signing with ES256.

Demonstrates:
- Generating EC key pair (P-256 curve)
- Signing with ES256
- Verifying the signature
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    ES256,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with ECDSA-SHA256."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("ecdsa-user")
    payload.set_issuer("ecdsa.example.com")

    # Generate EC key pair (P-256 curve)
    key_pair = ES256.generate_key_pair()

    # Sign the JWT with private key
    signer = ES256.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"ES256 JWT: {jwt}")

    # Verify with public key
    verifier = ES256.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("ES256 JWT verified!")
