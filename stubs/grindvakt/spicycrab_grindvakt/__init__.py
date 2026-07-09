"""Python stubs for the grindvakt Rust crate."""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Error:
    def status_hint(self) -> int: ...


class Result(Generic[T]):  # noqa: UP046
    pass


class HttpRequestData:
    path: str
    method: str
    uri: str
    query: dict[str, str]
    form: dict[str, str]
    body: bytes
    headers: dict[str, str]
    cookies: dict[str, str]

    def param(self, key: str) -> str | None: ...

    def authorization(self) -> str | None: ...

    def bearer_token(self) -> str | None: ...


class Response:
    status: int
    headers: list[tuple[str, str]]
    body: bytes

    @staticmethod
    def new(status: int) -> Response: ...

    @staticmethod
    def redirect(location: str) -> Response: ...

    @staticmethod
    def html(body: str) -> Response: ...

    @staticmethod
    def json(value: object) -> Result[Response]: ...

    @staticmethod
    def json_status(status: int, value: object) -> Result[Response]: ...

    @staticmethod
    def text(status: int, body: str) -> Response: ...

    def with_header(self, name: str, value: str) -> Response: ...

    def with_body(self, body: bytes) -> Response: ...


class HttpFetchResponse:
    status: int
    body: bytes
    content_type: str | None

    def text(self) -> str: ...

    def json(self) -> object: ...


class HttpClient:
    async def get(self, url: str) -> HttpFetchResponse: ...

    async def post_form(
        self,
        url: str,
        form: list[tuple[str, str]],
        headers: list[tuple[str, str]],
    ) -> HttpFetchResponse: ...


class SigningKey:
    def kid(self) -> str | None: ...

    def public_jwk(self) -> object: ...

    def to_public_jwks(self) -> object: ...


class ProviderMetadata:
    issuer: str
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: str
    jwks_uri: str
    registration_endpoint: str | None

    @staticmethod
    def new(issuer: str, base: str) -> ProviderMetadata: ...

    def to_json(self) -> object: ...


def signing_key_from_jwk_json(
    json: str,
    alg_override: str | None = None,
    kid_override: str | None = None,
) -> Result[SigningKey]: ...


def signing_key_from_pem(
    bytes_: bytes,
    alg_override: str | None = None,
    kid_override: str | None = None,
) -> Result[SigningKey]: ...


def hmac_sha256(key: bytes, data: bytes) -> bytes: ...


def sha256(data: bytes) -> bytes: ...


def constant_time_eq(a: bytes, b: bytes) -> bool: ...


def s256_challenge(verifier: str) -> str: ...


def verify_pkce(verifier: str, challenge: str, method: str | None = None) -> bool: ...
