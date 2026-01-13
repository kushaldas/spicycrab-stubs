"""ECDSA JWT Signing with ES384.

Demonstrates:
- Generating EC key pair (P-384 curve)
- Signing with ES384
- Verifying the signature
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    ES384,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with ECDSA-SHA384."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("ecdsa384-user")
    payload.set_issuer("ecdsa384.example.com")

    # Generate EC key pair (P-384 curve)
    key_pair = ES384.generate_key_pair()

    # Sign the JWT with private key
    signer = ES384.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"ES384 JWT: {jwt}")

    # Verify with public key
    verifier = ES384.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("ES384 JWT verified!")
