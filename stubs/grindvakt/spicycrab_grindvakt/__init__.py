"""Python stubs for the grindvakt Rust crate.

Install with: cookcrab install grindvakt
"""

from __future__ import annotations

from typing import Self, TypeVar, Generic

T = TypeVar('T')
E = TypeVar('E')


class Result(Generic[T, E]):
    """A Result type alias for grindvakt.

    Maps to grindvakt::Result which is an alias for std::result::Result<T,Error>.
    """

    @staticmethod
    def Ok(value: T) -> "Result[T, E]":
        """Create a successful result."""
        ...

    @staticmethod
    def Err(error: E) -> "Result[T, E]":
        """Create an error result."""
        ...

class OAuthError:
    """An OAuth2 error with an optional human-readable description."""

    @staticmethod
    def new(code: OAuthErrorCode, description: object) -> "OAuthError": ...

    @staticmethod
    def bare(code: OAuthErrorCode) -> "OAuthError": ...

    def with_state(self, state: str | None) -> Self: ...

    @staticmethod
    def invalid_request(msg: object) -> "OAuthError": ...

    @staticmethod
    def invalid_client(msg: object) -> "OAuthError": ...

    @staticmethod
    def invalid_grant(msg: object) -> "OAuthError": ...

    @staticmethod
    def invalid_dpop_proof(msg: object) -> "OAuthError": ...

    def to_response(self) -> Response: ...

    def to_redirect(self, redirect_uri: str) -> Response: ...

    def fmt(self, f: Formatter) -> Result: ...

class TokenLifetimes:
    """Configuration knobs for token lifetimes."""

    @staticmethod
    def default() -> "TokenLifetimes": ...

class Provider:
    """The OpenID Provider engine.

Construct with [`Provider::new`]; the token-use store is installed via
[`Provider::with_token_use_store`] rather than a public field so adding
stores later does not break struct-literal construction downstream."""

    @staticmethod
    def new(metadata: ProviderMetadata, signing_key: SigningKey, clients: object, codec: TokenCodec, lifetimes: TokenLifetimes) -> "Provider": ...

    def with_token_use_store(self, store: object) -> Self: ...

    def discovery_document(self) -> Value: ...

    def jwks_document(self) -> JwkSet: ...

    def validate_authorization_request(self, req: AuthorizationRequest) -> Client: ...

    def authorization_redirect(self, req: AuthorizationRequest, sub: str, external_claims: object, acr: str | None) -> Response: ...

    def handle_token_request(self, form: object, auth_header: object, token_url: str, dpop: object) -> TokenResponse: ...

    def userinfo(self, access_token: str, presented_jkt: object) -> Value: ...

    def authenticate_client(self, form: object, auth_header: object, token_url: str) -> Client: ...

class TokenResponse:
    """The token endpoint success response."""
    pass

class InMemoryTokenUseStore:
    """Single-process [`TokenUseStore`] implementation."""

    @staticmethod
    def new() -> "InMemoryTokenUseStore": ...

    def consume(self, token_hash: str, ttl_secs: int) -> bool: ...

class RedisStore:
    """Redis-backed [`TokenUseStore`] implementation for multi-process deployments.

Values are written with `SET key 1 NX EX ttl`, so the first consumer wins and
Redis expires the replay marker after the original token lifetime.

Commands run over a shared async [`redis::aio::ConnectionManager`]
(multiplexed, reconnecting), so consuming a token never blocks the async
executor and does not open a new connection per call. The `redis` feature
enables the tokio-backed transport of the `redis` crate."""

    @staticmethod
    def new(redis_url: str) -> object: ...

    @staticmethod
    def from_client(client: Client) -> object: ...

    def with_key_prefix(self, key_prefix: object) -> Self: ...

    def consume(self, token_hash: str, ttl_secs: int) -> bool: ...

class SigningKey:
    """A loaded signing key: the signer that performs the cryptographic operation,
plus the algorithm, key id, and cached public JWK used for publication.

The signer is held behind an [`Arc`] so cloning a `SigningKey` is cheap and
the same backing key (software or HSM) is shared. The private material is
never exposed; only [`public_jwk`](Self::public_jwk) is available.

A `SigningKey` is immutable after construction: `alg`/`kid` are read-only
accessors so the signer, the headers, and the cached public JWK can never
drift out of agreement."""

    def signer(self) -> Signer: ...

    def alg(self) -> JwsAlgorithm: ...

    def kid(self) -> object: ...

    def public_jwk(self) -> Jwk: ...

    def to_public_jwks(self) -> JwkSet: ...

class Pkcs11KeyConfig:
    """Configuration identifying a signing key on a PKCS#11 token.

The token is selected through kryptering's default provider selection
for `module_path`, which accepts exactly one initialized token; the key
pair is selected by its `CKA_LABEL`."""
    pass

class ProviderMetadata:
    """OpenID Provider metadata. Serializes to the `.well-known/openid-configuration`
document and is reused (under `metadata.openid_provider`) in federation
entity statements."""

    @staticmethod
    def new(issuer: object, base: str) -> "ProviderMetadata": ...

    def to_json(self) -> Value: ...

class DpopConfig:
    """Configuration knobs for DPoP validation (replaces authc's `AppConfig`)."""

    @staticmethod
    def default() -> "DpopConfig": ...

class DpopProof:
    """The outcome of validating a DPoP proof."""
    pass

class NoReplayStore:
    """A no-op [`ReplayStore`] for the stateless-nonce-only mode: every `jti` is
treated as fresh.

**Security caveat:** with this store a captured proof can be replayed for the
whole `proof_max_age_secs` window *unless* `require_nonce` is also enabled —
the HMAC nonce challenge is then the only thing bounding the replay window.
Do not pair `NoReplayStore` with `require_nonce = false` on an internet-facing
deployment; prefer a real (shared) [`ReplayStore`]. The in-tree frontends use
a cache-backed store, never this."""

    def record(self, _jti: str, _ttl_secs: int) -> bool: ...

class HttpRequestData:
    """A parsed inbound HTTP request, normalized for the proxy flow."""

    def param(self, key: str) -> object: ...

    def authorization(self) -> object: ...

    def bearer_token(self) -> object: ...

class Response:
    """A framework-agnostic HTTP response produced by a handler."""

    @staticmethod
    def new(status: int) -> "Response": ...

    def with_header(self, name: object, value: object) -> Self: ...

    def with_body(self, body: object) -> Self: ...

    @staticmethod
    def redirect(location: object) -> "Response": ...

    @staticmethod
    def html(body: object) -> "Response": ...

    @staticmethod
    def json(value: T) -> object: ...

    @staticmethod
    def json_status(status: int, value: T) -> object: ...

    @staticmethod
    def text(status: int, body: object) -> "Response": ...

class HttpFetchResponse:
    """The result of an outbound fetch."""

    def text(self) -> str: ...

    def json(self) -> T: ...

class Client:
    """A registered relying party."""

    def allows_redirect(self, uri: str) -> bool: ...

    def allows_response_type(self, rt: str) -> bool: ...

class InMemoryClientStore:
    """In-memory client store with optional per-entry TTL (for federation)."""

    @staticmethod
    def new() -> "InMemoryClientStore": ...

    @staticmethod
    def with_clients(clients: list[Client]) -> "InMemoryClientStore": ...

    def get(self, client_id: str) -> Client | None: ...

    def put(self, client: Client) -> None: ...

    def put_with_ttl(self, client: Client, ttl: int) -> None: ...

class AuthorizationRequest:
    """A parsed OIDC authorization request."""

    @staticmethod
    def from_params(params: object) -> object: ...

    def scopes(self) -> object: ...

    def is_oidc(self) -> bool: ...

    def wants_code(self) -> bool: ...

    def wants_id_token(self) -> bool: ...

    def use_fragment(self) -> bool: ...

    def validate_response_type(self) -> None: ...

class ThirdPartyInitiatedLogin:
    """A parsed and validated Third-Party Initiated Login request (OpenID Connect
Core 1.0 §4), as received at the RP's `initiate_login_uri`."""
    pass

class SelfPublishedRp:
    """A verified self-published relying party: the full `metadata` claims object
from its entity configuration plus the statement's lifetime."""
    pass

class ResolvedEntity:
    """A successful resolve response, bound to a configured trust anchor."""
    pass

class EntityStatement:
    """The decoded claims of an entity statement, as a JSON object."""

    def iss(self) -> object: ...

    def sub(self) -> object: ...

    def jwks(self) -> JwkSet: ...

    def metadata(self, kind: str) -> Value | None: ...

    def authority_hints(self) -> list[str]: ...

class CollectionEntity:
    """One entity returned by a trust anchor's collection (listing) endpoint, with
its UI presentation already flattened for a discovery page."""
    pass

class ProviderInfo:
    """Minimal upstream provider info the RP needs."""

    @staticmethod
    def from_(m: ProviderMetadata) -> "ProviderInfo": ...

class RpClient:
    """RP client configuration."""
    pass

class TokenSet:
    """The result of a successful token exchange."""
    pass

class AuthCodePayload:
    """The payload sealed inside an authorization code."""
    pass

class AccessTokenPayload:
    """The payload sealed inside an access token."""
    pass

class RefreshTokenPayload:
    """The payload sealed inside a refresh token (RFC 6749 §6).

It carries everything needed to re-mint an access token and id_token on
refresh without a server lookup: the subject, the granted scope, the released
claims, the original `auth_time`/`nonce`/`acr` so a refreshed id_token stays
faithful to the initial authentication, and any DPoP confirmation thumbprint
that sender-constrains the refresh token. Refresh tokens are rotated on each
use, but — like every other token here — they are stateless, so they cannot
be revoked before their own `exp` (no server-side store to consult)."""
    pass

class TokenCodec:
    """Seals/opens authorization codes, access tokens, and refresh tokens."""

    @staticmethod
    def new(secret: str) -> "TokenCodec": ...

    def with_previous_secrets(self, secrets: object) -> Self: ...

    def seal_code(self, payload: AuthCodePayload) -> str: ...

    def open_code(self, token: str) -> AuthCodePayload: ...

    def seal_access_token(self, payload: AccessTokenPayload) -> str: ...

    def open_access_token(self, token: str) -> AccessTokenPayload: ...

    def seal_refresh_token(self, payload: RefreshTokenPayload) -> str: ...

    def open_refresh_token(self, token: str) -> RefreshTokenPayload: ...

class OAuthErrorCode:
    """A standard OAuth2 error code."""
    InvalidRequest: "OAuthErrorCode"
    InvalidClient: "OAuthErrorCode"
    InvalidGrant: "OAuthErrorCode"
    UnauthorizedClient: "OAuthErrorCode"
    UnsupportedGrantType: "OAuthErrorCode"
    UnsupportedResponseType: "OAuthErrorCode"
    InvalidScope: "OAuthErrorCode"
    AccessDenied: "OAuthErrorCode"
    LoginRequired: "OAuthErrorCode"
    ServerError: "OAuthErrorCode"
    TemporarilyUnavailable: "OAuthErrorCode"
    InvalidDpopProof: "OAuthErrorCode"

    def as_str(self) -> object: ...

    def http_status(self) -> int: ...

class DpopError:
    """Why DPoP validation failed. The web layer maps these onto the right HTTP
response (a `use_dpop_nonce` challenge vs. an `invalid_dpop_proof` error)."""
    Invalid: "DpopError"
    Replay: "DpopError"
    NonceRequired: "DpopError"
    Server: "DpopError"

    def fmt(self, f: Formatter) -> Result: ...

class Error:
    """Top-level error type. Carries enough structure to be mapped onto an HTTP
response by the binary layer (see [`Error::status_hint`])."""
    NoBoundEndpoint: "Error"
    UnknownModule: "Error"
    BadRequest: "Error"
    Authn: "Error"
    State: "Error"
    Config: "Error"
    Crypto: "Error"
    Attribute: "Error"
    Jose: "Error"
    Json: "Error"
    Internal: "Error"

    def status_hint(self) -> int: ...

class ClientAuth:
    """How the RP authenticates to the upstream token endpoint."""
    None_: "ClientAuth"
    ClientSecretBasic: "ClientAuth"
    ClientSecretPost: "ClientAuth"
    PrivateKeyJwt: "ClientAuth"

def flatten_claims(external: object) -> object: ...

"""Load a signing key from a JWK JSON string."""
def signing_key_from_jwk_json(json: str, alg_override: object, kid_override: object) -> SigningKey: ...

"""Load a signing key from a PEM (or DER) file's bytes."""
def signing_key_from_pem(bytes: object, alg_override: object, kid_override: object) -> SigningKey: ...

"""Load a signing key whose private material lives on a PKCS#11 token."""
def signing_key_from_pkcs11(cfg: Pkcs11KeyConfig) -> SigningKey: ...

"""Validate a DPoP proof for a token-endpoint request.

* `htm` / `htu` — the HTTP method and the absolute request URI the proof
must be bound to (query and fragment stripped before comparison).
* On success the proof's `jti` has been recorded via `store`, so a replay of
the same proof now returns [`DpopError::Replay`]."""
async def validate_proof(store: dynReplayStore, config: DpopConfig, proof: str, htm: str, htu: str) -> DpopProof: ...

"""Validate a DPoP proof for a **resource** request (e.g. userinfo), additionally
binding it to `access_token` via the `ath` claim (RFC 9449 §4.3/§7.1). The
caller must still check that the returned [`DpopProof::jkt`] equals the access
token's `cnf.jkt` confirmation."""
async def validate_resource_proof(store: dynReplayStore, config: DpopConfig, proof: str, htm: str, htu: str, access_token: str) -> DpopProof: ...

"""Issue a fresh DPoP nonce: `base64url( ts_be(8) || HMAC-SHA256(secret, ts)[..16] )`.
Stateless — validated by recomputing the MAC and checking the age, so no
nonce store is required."""
def issue_nonce(config: DpopConfig) -> str: ...

"""Validate an OpenID Federation Entity Identifier as accepted on a wire
parameter (`entity_id`, `iss`, `hint`): an https URL with a host and no
query or fragment."""
def validate_entity_id(s: str) -> None: ...

"""Build the URL an RP redirects the browser to in order to start home
organization discovery (the *outgoing call*):
`<discovery_endpoint>?entity_id=<rp>[&hint=<op>][&target_link_uri=<uri>]`.

`discovery_endpoint` is the discovery service's absolute endpoint URL.
`rp_entity_id` is the RP's own entity identifier; `op_hint` optionally
names a preferred OP; `target_link_uri` lets the RP learn where to send the
user after login without keeping a session (the discovery service must
return it verbatim)."""
def discovery_request_url(discovery_endpoint: str, rp_entity_id: str, op_hint: object, target_link_uri: object) -> str: ...

"""Parse the query parameters arriving at an RP's `initiate_login_uri` into a
[`ThirdPartyInitiatedLogin`]. `iss` is required and must be a valid https
entity identifier."""
def parse_third_party_initiated_login(params: object) -> ThirdPartyInitiatedLogin: ...

"""Extract a verified RP's `initiate_login_uri` from its resolved metadata
(`metadata.openid_relying_party.initiate_login_uri`). The URI must be https
without a fragment — it is the only place a discovery service ever sends a
user, so anything weaker would turn the service into an open redirector."""
def initiate_login_uri(metadata: Value) -> str: ...

"""[`initiate_login_uri`] over a [`ResolvedEntity`] from
[`crate::federation::resolve_via_trust_anchors`]."""
def initiate_login_uri_from_resolved(entity: ResolvedEntity) -> str: ...

"""Fetch and verify an RP's *self-published* entity configuration
(`<entity_id>/.well-known/openid-federation`, self-signed) and return its
metadata and lifetime.

For discovery services running in an open mode: the RP is not required to
chain up to a trust anchor, but anything taken from the result is still
limited to what the entity itself publishes under its own identifier -
never caller-supplied data."""
async def self_published_rp(http: object, rp_entity_id: str) -> SelfPublishedRp: ...

"""[`self_published_rp`] reduced to the validated `initiate_login_uri`."""
async def self_published_initiate_login_uri(http: object, rp_entity_id: str) -> str: ...

"""Build the third-party initiated login URL the user is sent to after
selecting an OP (the *return call*):
`<initiate_login_uri>?iss=<op>[&login_hint=…][&target_link_uri=…]`.

`target_link_uri` is attached verbatim (it is only ever appended to a
verified `initiate_login_uri`, never used as a redirect target itself)."""
def third_party_login_url(initiate_login_uri: str, op_entity_id: str, login_hint: object, target_link_uri: object) -> str: ...

"""If `hint` names one of the entities, move it to the front of the list — the
discovery flow requires a matching OP hint to become the default choice.
Returns whether `hint` matched any entity."""
def promote_hint(entities: list[CollectionEntity], hint: str) -> bool: ...

"""Build and sign a self-issued Entity Configuration JWT
(`iss == sub == entity_id`)."""
def build_entity_configuration(key: SigningKey, entity_id: str, public_jwks: JwkSet, authority_hints: object, metadata: Value, trust_marks: object, lifetime: int) -> str: ...

"""Decode an entity statement without verifying its signature (inspection only)."""
def decode_unverified(token: str) -> EntityStatement: ...

"""Verify an entity statement's signature against a JWKS and its `typ`, then
return the decoded claims."""
def verify(token: str, jwks: JwkSet) -> EntityStatement: ...

"""Verify a trust-anchor-signed JWT against a JWKS, requiring a specific `typ`
header. Entity statements and resolve responses are both TA-signed but carry
different `typ` values."""
def verify_typed(token: str, jwks: JwkSet, typ: str) -> EntityStatement: ...

"""Verify a self-issued Entity Configuration using the keys it carries
(`iss == sub`, signature validates against the embedded `jwks`)."""
def verify_self_signed(token: str) -> EntityStatement: ...

"""Fetch an entity's configuration JWT from its `.well-known/openid-federation`."""
async def fetch_entity_configuration(http: object, entity_id: str) -> str: ...

"""Resolve a subject entity's metadata by delegating to each configured trust
anchor's `federation_resolve_endpoint` (OpenID Federation 1.0 §10). Returns
the resolved `metadata` object from the first trust anchor that succeeds."""
async def resolve_via_trust_anchors(http: object, sub: str, trust_anchors: TrustAnchors) -> ResolvedEntity: ...

"""Resolve an Entity Type key set using the representations from OpenID
Federation 1.1 §5.2.1."""
async def entity_metadata_jwks(http: object, metadata: Value, subject_entity_id: str, subject_fed_jwks: JwkSet) -> JwkSet: ...

"""Fetch and verify a signed JWK Set document referenced by `signed_jwks_uri`."""
async def fetch_signed_jwks(http: object, signed_jwks_uri: str, subject_entity_id: str, subject_fed_jwks: JwkSet) -> JwkSet: ...

"""Fetch a list of federation entities of a given type from a trust anchor's
collection endpoint (e.g. a SUNET/inmor `…/collection`), flattening their
UI info for a discovery page. `entity_type` is the federation entity-type
filter, e.g. `"openid_provider"`.

The endpoint is expected to answer with
`{"entities": [{"entity_id": "...", "ui_infos": {"openid_provider": {...},
"federation_entity": {...}}}, ...]}`."""
async def fetch_collection(http: object, collection_endpoint: str, entity_type: str) -> list[CollectionEntity]: ...

"""Parse a collection-endpoint response body into [`CollectionEntity`] list.
Separated from the fetch so it can be unit-tested without HTTP. Entries
without an `entity_id`, or that do not advertise `entity_type`, are skipped."""
def parse_collection(body: Value, entity_type: str) -> list[CollectionEntity]: ...

"""Apply a metadata policy object to a metadata object in place. Supports the
`value`, `default`, `add`, `one_of`, `subset_of`, `superset_of` and
`essential` operators."""
def apply_policy(metadata: object, policy: object) -> None: ...

"""Sign a set of claims into a compact JWS using a [`SigningKey`], setting the
`alg`, `kid` and (optionally) a custom `typ` header."""
def sign(key: SigningKey, claims: Claims, typ: object) -> str: ...

"""Verify and validate a compact JWS against a JWK Set."""
def verify_with_jwks(jwks: JwkSet, token: str, validation: Validation) -> Claims: ...

"""Verify and validate a compact JWS against a single JWK."""
def verify_with_jwk(jwk: Jwk, token: str, validation: Validation) -> Claims: ...

"""Read the protected header of a compact JWS without verifying it (used to peek
at `kid`/`typ` before key selection)."""
def peek_header(token: str) -> JoseHeader: ...

"""Decode the claims of a JWS without verifying its signature. DANGEROUS — only
for inspection (e.g. reading `iss`/`client_id` to pick a verification key)."""
def peek_claims_unverified(token: str) -> Claims: ...

"""Compute HMAC-SHA256 over `data` with `key`."""
def hmac_sha256(key: object, data: object) -> list[int]: ...

"""Compute a plain SHA-256 digest of `data`. Used for the DPoP `ath`
access-token hash (RFC 9449 §4.3)."""
def sha256(data: object) -> list[int]: ...

"""Constant-time equality (no early return on first mismatching byte). Returns
false for differing lengths."""
def constant_time_eq(a: object, b: object) -> bool: ...

"""Build the authorization request URL (redirect the user here)."""
def authorization_url(provider: ProviderInfo, client: RpClient, state: str, nonce: str, code_challenge: object, extra: object) -> str: ...

"""Build a signed request object (RFC 9101, "JAR") carrying the
authorization-request parameters as JWT claims.

OpenID Federation **automatic registration** needs this: a federation OP
authenticates the RP at the authorization endpoint by verifying the
request object against the keys published in the RP's resolved
`openid_relying_party` metadata, and implementations (e.g. the Shibboleth
OIDC OP plugin) use its presence as the trigger to resolve the RP's trust
chain on the fly. Pass the result as the `request` parameter — typically
via [`authorization_url`]'s `extra` — alongside the plain parameters so
OPs that ignore request objects keep working.

`key` must be (one of) the RP's published client keys; for a federation
RP that is the `private_key_jwt` key from its entity configuration."""
def signed_request_object(provider: ProviderInfo, client: RpClient, key: SigningKey, state: str, nonce: str, code_challenge: object) -> str: ...

"""Discover provider metadata from an issuer."""
async def discover(http: object, issuer: str) -> ProviderMetadata: ...

"""Fetch a JWKS document."""
async def fetch_jwks(http: object, jwks_uri: str) -> JwkSet: ...

"""Exchange an authorization code for tokens."""
async def exchange_code(http: object, provider: ProviderInfo, client: RpClient, code: str, code_verifier: object) -> TokenSet: ...

"""Verify an id_token against the provider JWKS, issuer, audience and nonce."""
def verify_id_token(jwks: JwkSet, id_token: str, issuer: str, client_id: str, expected_nonce: object) -> Claims: ...

"""Fetch userinfo with a Bearer access token."""
async def fetch_userinfo(http: object, userinfo_endpoint: str, access_token: str) -> Value: ...

"""Build a `private_key_jwt` client assertion (RFC 7523) for token-endpoint auth."""
def build_client_assertion(key: SigningKey, client_id: str, audience: str) -> str: ...

"""Convert a userinfo / id_token claims object into the proxy's external
attribute map shape (`name -> [values]`)."""
def claims_to_attributes(claims: Value) -> object: ...

"""Current Unix time in seconds."""
def now_secs() -> int: ...

"""RFC 3339 timestamp for "now" (used in InternalData auth_info)."""
def now_rfc3339() -> str: ...

"""Generate a URL-safe random token of `n` bytes of entropy (base64url, no pad)."""
def random_token(n: int) -> str: ...

"""Compute the S256 code challenge for a verifier."""
def s256_challenge(verifier: str) -> str: ...

"""Verify a `code_verifier` against a stored `code_challenge` + method.

`method` defaults to `plain` when absent (RFC 7636 §4.3)."""
def verify(verifier: str, challenge: str, method: object) -> bool: ...

__all__: list[str] = ["flatten_claims", "signing_key_from_jwk_json", "signing_key_from_pem", "signing_key_from_pkcs11", "validate_proof", "validate_resource_proof", "issue_nonce", "validate_entity_id", "discovery_request_url", "parse_third_party_initiated_login", "initiate_login_uri", "initiate_login_uri_from_resolved", "self_published_rp", "self_published_initiate_login_uri", "third_party_login_url", "promote_hint", "build_entity_configuration", "decode_unverified", "verify", "verify_typed", "verify_self_signed", "fetch_entity_configuration", "resolve_via_trust_anchors", "entity_metadata_jwks", "fetch_signed_jwks", "fetch_collection", "parse_collection", "apply_policy", "sign", "verify_with_jwks", "verify_with_jwk", "peek_header", "peek_claims_unverified", "hmac_sha256", "sha256", "constant_time_eq", "authorization_url", "signed_request_object", "discover", "fetch_jwks", "exchange_code", "verify_id_token", "fetch_userinfo", "build_client_assertion", "claims_to_attributes", "now_secs", "now_rfc3339", "random_token", "s256_challenge", "verify", "Result", "OAuthError", "TokenLifetimes", "Provider", "TokenResponse", "InMemoryTokenUseStore", "RedisStore", "SigningKey", "Pkcs11KeyConfig", "ProviderMetadata", "DpopConfig", "DpopProof", "NoReplayStore", "HttpRequestData", "Response", "HttpFetchResponse", "Client", "InMemoryClientStore", "AuthorizationRequest", "ThirdPartyInitiatedLogin", "SelfPublishedRp", "ResolvedEntity", "EntityStatement", "CollectionEntity", "ProviderInfo", "RpClient", "TokenSet", "AuthCodePayload", "AccessTokenPayload", "RefreshTokenPayload", "TokenCodec", "OAuthErrorCode", "DpopError", "Error", "ClientAuth"]
