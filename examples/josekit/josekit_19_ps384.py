"""RSA-PSS JWT Signing with PS384.

Demonstrates:
- PS384 algorithm (RSA-PSS with SHA-384)
- 2048-bit RSA key pair
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    PS384,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with RSA-PSS-SHA384."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("ps384-user")
    payload.set_issuer("ps384.example.com")

    # Generate 2048-bit RSA-PSS key pair
    key_pair = PS384.generate_key_pair(2048)

    # Sign the JWT with private key
    signer = PS384.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"PS384 JWT: {jwt}")

    # Verify with public key
    verifier = PS384.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("PS384 JWT verified!")
