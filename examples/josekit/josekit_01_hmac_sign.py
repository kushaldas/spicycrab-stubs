"""HMAC JWT Signing example (HS256).

Demonstrates:
- Creating a JWS header and JWT payload
- Signing with HMAC-SHA256
- Verifying the signature
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    HS256,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with HMAC-SHA256."""
    # Create header
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    # Create payload
    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("user123")
    payload.set_issuer("example.com")

    # 32-byte key for HS256
    key = b"0123456789ABCDEF0123456789ABCDEF"

    # Sign the JWT
    signer = HS256.signer_from_bytes(key)
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"Signed JWT: {jwt}")

    # Verify the JWT
    verifier = HS256.verifier_from_bytes(key)
    decoded = decode_with_verifier(jwt, verifier)
    print("JWT verified successfully!")
