"""RSA JWT Signing with RS256.

Demonstrates:
- Generating RSA key pair (2048-bit)
- Signing with RS256
- Verifying the signature
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    RS256,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with RSA-SHA256."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("rsa-user")
    payload.set_issuer("rsa.example.com")

    # Generate 2048-bit RSA key pair
    key_pair = RS256.generate_key_pair(2048)

    # Sign the JWT with private key
    signer = RS256.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"RS256 JWT: {jwt}")

    # Verify with public key
    verifier = RS256.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("RS256 JWT verified!")
