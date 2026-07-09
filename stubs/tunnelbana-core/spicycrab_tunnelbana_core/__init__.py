"""Python stubs for the tunnelbana-core Rust crate."""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")

KEY_AUTHN_CONTEXT_CLASS_REF: str
KEY_TARGET_AUTHN_CONTEXT_CLASS_REF: str
KEY_TARGET_ENTITYID: str
KEY_ERROR_REDIRECT: str


class Result(Generic[T, E]):
    @staticmethod
    def Ok(value: T) -> "Result[T, E]": ...

    @staticmethod
    def Err(error: E) -> "Result[T, E]": ...


class Error:
    @staticmethod
    def Config(message: str) -> "Error": ...

    @staticmethod
    def Authn(message: str) -> "Error": ...

    @staticmethod
    def Internal(message: str) -> "Error": ...

    @staticmethod
    def BadRequest(message: str) -> "Error": ...


class SubjectType:
    Persistent: "SubjectType"
    Transient: "SubjectType"
    Public: "SubjectType"
    Pairwise: "SubjectType"


class AuthenticationInformation:
    auth_class_ref: str | None
    timestamp: str | None
    issuer: str | None


class InternalData:
    auth_info: AuthenticationInformation
    requester: str | None
    requester_name: list[str]
    subject_id: str | None
    subject_type: SubjectType
    attributes: dict[str, list[str]]
    extensions: dict[str, object]

    @staticmethod
    def request(requester: str) -> "InternalData": ...

    def attr_first(self, name: str) -> str | None: ...

    def set_attr(self, name: str, value: str) -> None: ...

    def set_extension(self, name: str, value: object) -> None: ...

    def extension(self, name: str) -> object | None: ...


class HttpRequestData:
    path: str
    method: str
    uri: str
    query: dict[str, str]
    form: dict[str, str]
    body: bytes
    headers: dict[str, str]
    cookies: dict[str, str]


class State:
    def get_str(self, namespace: str, key: str) -> str | None: ...

    def set_str(self, namespace: str, key: str, value: str) -> None: ...

    def get_value(self, namespace: str, key: str) -> object | None: ...

    def set_value(self, namespace: str, key: str, value: object) -> None: ...

    def clear_namespace(self, namespace: str) -> None: ...


class Context:
    request: HttpRequestData
    target_backend: str | None
    target_frontend: str | None
    state: State
    decorations: dict[str, object]

    def path(self) -> str: ...

    def decorate(self, key: str, value: object) -> None: ...

    def decoration(self, key: str) -> object | None: ...

    def requester(self) -> str | None: ...


class Response:
    @staticmethod
    def new(status: int) -> "Response": ...

    @staticmethod
    def text(status: int, body: str) -> "Response": ...

    @staticmethod
    def redirect(url: str) -> "Response": ...

    def with_header(self, key: str, value: str) -> "Response": ...

    def with_body(self, body: bytes) -> "Response": ...


class Route:
    @staticmethod
    def new(pattern: str, id: str) -> "Route": ...


class BuildContext:
    name: str
    base_url: str
    config: object
    secret: str
    previous_secrets: list[str]


class Registry:
    def register_microservice(self, kind: str, ctor: object) -> None: ...


class MicroService:
    def name(self) -> str: ...

    async def process_request(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]: ...

    async def process_response(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]: ...

    def register_endpoints(self) -> list[Route]: ...

    async def handle_endpoint(self, ctx: Context, route_id: str) -> Result[Response, Error]: ...


class Frontend:
    pass


class Backend:
    pass
