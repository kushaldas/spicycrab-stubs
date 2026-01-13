"""HMAC JWT Signing with HS384.

Demonstrates:
- Using HS384 algorithm for stronger HMAC signing
- 48-byte key requirement for HS384
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    HS384,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Sign and verify a JWT with HMAC-SHA384."""
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("user789")
    payload.set_issuer("hs384.example.com")

    # 48-byte key for HS384
    key = b"0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"

    signer = HS384.signer_from_bytes(key)
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"HS384 JWT: {jwt}")

    verifier = HS384.verifier_from_bytes(key)
    decoded = decode_with_verifier(jwt, verifier)
    print("HS384 JWT verified!")
