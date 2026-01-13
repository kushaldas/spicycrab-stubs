"""JWT with Custom Claims.

Demonstrates:
- Adding custom claims to JWT payload
- Using set_claim for arbitrary claim data
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    HS256,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Create a JWT with custom claims."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("custom-user")
    payload.set_issuer("custom.example.com")

    # 32-byte key for HS256
    key = b"0123456789ABCDEF0123456789ABCDEF"

    # Sign the JWT
    signer = HS256.signer_from_bytes(key)
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"Custom Claims JWT: {jwt}")

    # Verify
    verifier = HS256.verifier_from_bytes(key)
    decoded = decode_with_verifier(jwt, verifier)
    print("Custom claims JWT verified!")
