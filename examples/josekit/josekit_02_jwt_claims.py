"""JWT with various claims example.

Demonstrates:
- Setting expiration (exp), issued-at (iat), not-before (nbf)
- Setting audience and JWT ID claims
- Verifying the complete token
"""

from spicycrab_josekit import (
    JwsHeader,
    JwtPayload,
    HS256,
    encode_with_signer,
    decode_with_verifier,
)


def main() -> None:
    """Create a JWT with multiple standard claims."""
    # Create header
    header: JwsHeader = JwsHeader.new()
    header.set_token_type("JWT")

    # Create payload with various claims
    payload: JwtPayload = JwtPayload.new()
    payload.set_subject("user456")
    payload.set_issuer("auth.example.com")
    payload.set_audience(["api.example.com", "web.example.com"])
    payload.set_jwt_id("unique-token-id-123")

    # Set time-based claims using helper methods
    # These methods use SystemTime internally
    payload.set_issued_at_now()  # Sets iat to current time
    payload.set_expires_at_hours(1)  # Expires in 1 hour

    # Sign with HMAC-SHA256
    key = b"supersecretkey32byteslong1234567"
    signer = HS256.signer_from_bytes(key)
    jwt: str = encode_with_signer(payload, header, signer)
    print(f"JWT with claims: {jwt}")

    # Verify and decode
    verifier = HS256.verifier_from_bytes(key)
    decoded = decode_with_verifier(jwt, verifier)
    print("JWT verified with all claims!")
