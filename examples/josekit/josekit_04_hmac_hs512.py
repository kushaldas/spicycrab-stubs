"""HMAC JWT Signing with HS512.

Demonstrates:
- Using HS512 algorithm for strongest HMAC signing
- 64-byte key requirement for HS512
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    HS512,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with HMAC-SHA512."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("admin")
    payload.set_issuer("hs512.example.com")

    # 64-byte key for HS512
    key = b"0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"

    signer = HS512.signer_from_bytes(key)
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"HS512 JWT: {jwt}")

    verifier = HS512.verifier_from_bytes(key)
    decoded = decode_with_verifier(jwt, verifier)
    print("HS512 JWT verified!")
