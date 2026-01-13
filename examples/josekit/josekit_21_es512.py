"""ECDSA JWT Signing with ES512.

Demonstrates:
- ES512 algorithm (ECDSA with P-521 curve)
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    ES512,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with ECDSA-SHA512."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("es512-user")
    payload.set_issuer("es512.example.com")

    # Generate EC key pair (P-521 curve)
    key_pair = ES512.generate_key_pair()

    # Sign the JWT with private key
    signer = ES512.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"ES512 JWT: {jwt}")

    # Verify with public key
    verifier = ES512.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("ES512 JWT verified!")
