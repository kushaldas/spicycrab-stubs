"""RSA-PSS JWT Signing with PS256.

Demonstrates:
- Generating RSA-PSS key pair (2048-bit)
- Signing with PS256
- Verifying the signature
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    PS256,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with RSA-PSS-SHA256."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("rsapss-user")
    payload.set_issuer("rsapss.example.com")

    # Generate 2048-bit RSA-PSS key pair
    key_pair = PS256.generate_key_pair(2048)

    # Sign the JWT with private key
    signer = PS256.signer_from_jwk(key_pair.to_jwk_private_key())
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"PS256 JWT: {jwt}")

    # Verify with public key
    verifier = PS256.verifier_from_jwk(key_pair.to_jwk_public_key())
    decoded = decode_with_verifier(jwt, verifier)
    print("PS256 JWT verified!")
