"""Python stubs for the actix-web Rust crate.

Install with: cookcrab install actix-web
"""

from __future__ import annotations

from typing import Self, TypeVar, Generic

T = TypeVar('T')
E = TypeVar('E')


class Result(Generic[T, E]):
    """A Result type alias for actix-web.

    Maps to actix-web::Result which is an alias for std::result::Result<T,E>.
    """

    @staticmethod
    def Ok(value: T) -> "Result[T, E]":
        """Create a successful result."""
        ...

    @staticmethod
    def Err(error: E) -> "Result[T, E]":
        """Create an error result."""
        ...

class HttpResponse:
    """HTTP response type.

    Use the static methods to create responses with specific status codes,
    then chain builder methods to set body, headers, etc.

    Maps to actix_web::HttpResponse in Rust.

    Example:
        return HttpResponse.Ok().body("Hello World!")
        return HttpResponse.Ok().json({"key": "value"})
        return HttpResponse.NotFound().body("Not found")
    """

    @staticmethod
    def Ok() -> "HttpResponseBuilder":
        """Creates a 200 OK response builder."""
        ...

    @staticmethod
    def Created() -> "HttpResponseBuilder":
        """Creates a 201 Created response builder."""
        ...

    @staticmethod
    def Accepted() -> "HttpResponseBuilder":
        """Creates a 202 Accepted response builder."""
        ...

    @staticmethod
    def NoContent() -> "HttpResponseBuilder":
        """Creates a 204 No Content response builder."""
        ...

    @staticmethod
    def BadRequest() -> "HttpResponseBuilder":
        """Creates a 400 Bad Request response builder."""
        ...

    @staticmethod
    def Unauthorized() -> "HttpResponseBuilder":
        """Creates a 401 Unauthorized response builder."""
        ...

    @staticmethod
    def Forbidden() -> "HttpResponseBuilder":
        """Creates a 403 Forbidden response builder."""
        ...

    @staticmethod
    def NotFound() -> "HttpResponseBuilder":
        """Creates a 404 Not Found response builder."""
        ...

    @staticmethod
    def InternalServerError() -> "HttpResponseBuilder":
        """Creates a 500 Internal Server Error response builder."""
        ...


class HttpResponseBuilder:
    """Builder for constructing HTTP responses.

    Returned by HttpResponse status methods. Chain methods to configure
    the response body, headers, and content type.
    """

    def body(self, data: str) -> "HttpResponse":
        """Set the response body as a string."""
        ...

    def json(self, data: object) -> "HttpResponse":
        """Set the response body as JSON."""
        ...

    def content_type(self, ct: str) -> "HttpResponseBuilder":
        """Set the Content-Type header."""
        ...

    def insert_header(self, header: tuple[str, str]) -> "HttpResponseBuilder":
        """Insert a custom header."""
        ...

    def finish(self) -> "HttpResponse":
        """Finish building and return the response."""
        ...


class App:
    """Application builder for configuring actix-web services.

    Create with App.new(), then chain methods to add routes, middleware,
    and application data.

    Maps to actix_web::App in Rust.

    Example:
        app = App.new().app_data(Data.new(state)).service(handler)
    """

    @staticmethod
    def new() -> "App":
        """Create a new application builder."""
        ...

    def app_data(self, data: object) -> "App":
        """Set application-wide shared data.

        Data is wrapped in web::Data<T> and can be extracted in handlers.
        """
        ...

    def service(self, handler: object) -> "App":
        """Register an HTTP service (handler function)."""
        ...

    def route(self, path: str, route: object) -> "App":
        """Configure a route for a specific path and method."""
        ...

    def wrap(self, middleware: object) -> "App":
        """Wrap the application with middleware."""
        ...

    def configure(self, f: object) -> "App":
        """Run external configuration as part of application building."""
        ...


class HttpServer:
    """HTTP server that manages worker threads and connections.

    Create with HttpServer.new() passing an App factory, then configure
    bindings and run the server.

    Maps to actix_web::HttpServer in Rust.

    Example:
        HttpServer.new(lambda: App.new().service(index))
            .bind("127.0.0.1:8080")
            .run()
    """

    @staticmethod
    def new(factory: object) -> "HttpServer":
        """Create a new HTTP server with an application factory.

        The factory is called for each worker thread to create the App.
        """
        ...

    def bind(self, addr: str) -> "HttpServer":
        """Bind to a socket address (e.g., "127.0.0.1:8080")."""
        ...

    def bind_rustls(self, addr: str, config: object) -> "HttpServer":
        """Bind with TLS using rustls."""
        ...

    def workers(self, num: int) -> "HttpServer":
        """Set the number of worker threads (default: number of CPUs)."""
        ...

    async def run(self) -> None:
        """Start the server and wait for it to finish."""
        ...


class Data(Generic[T]):
    """Shared application state extractor.

    Wraps data in Arc for thread-safe sharing between handlers.
    Register with App.app_data() and extract in handler parameters.

    Maps to actix_web::web::Data<T> in Rust.

    Example:
        # In main:
        state = Data.new(AppState())
        app = App.new().app_data(state)

        # In handler:
        async def index(data: Data[AppState]) -> HttpResponse:
            return HttpResponse.Ok().body(data.app_name)
    """

    @staticmethod
    def new(value: T) -> "Data[T]":
        """Create new shared application data."""
        ...


class Query(Generic[T]):
    """Query string parameter extractor.

    Extracts typed data from the URL query string.
    The type T must implement serde::Deserialize.

    Maps to actix_web::web::Query<T> in Rust.

    Example:
        @dataclass
        class Params:
            name: str
            page: int

        async def search(params: Query[Params]) -> HttpResponse:
            return HttpResponse.Ok().body(f"Searching for {params.name}")
    """
    pass


class Json(Generic[T]):
    """JSON extractor and responder.

    As extractor: Deserializes JSON request body into type T.
    As responder: Serializes type T to JSON response.

    Maps to actix_web::web::Json<T> in Rust.

    Example:
        @dataclass
        class User:
            name: str
            email: str

        async def create_user(user: Json[User]) -> Json[User]:
            # user.name, user.email are accessible
            return Json(user)
    """

    def __init__(self, value: T) -> None:
        """Create a JSON response from a value."""
        ...


class Form(Generic[T]):
    """URL-encoded form data extractor.

    Extracts typed data from application/x-www-form-urlencoded request body.
    The type T must implement serde::Deserialize.

    Maps to actix_web::web::Form<T> in Rust.

    Example:
        @dataclass
        class LoginForm:
            username: str
            password: str

        async def login(form: Form[LoginForm]) -> HttpResponse:
            # form.username, form.password are accessible
            return HttpResponse.Ok().body("Logged in")
    """
    pass


class Path(Generic[T]):
    """Path parameter extractor.

    Extracts typed data from URL path segments.
    The type T must implement serde::Deserialize.

    Maps to actix_web::web::Path<T> in Rust.

    Example:
        # Route: /users/{user_id}
        async def get_user(path: Path[int]) -> HttpResponse:
            user_id = path.into_inner()
            return HttpResponse.Ok().body(f"User {user_id}")

        # Multiple params: /users/{user_id}/posts/{post_id}
        @dataclass
        class PathParams:
            user_id: int
            post_id: int

        async def get_post(path: Path[PathParams]) -> HttpResponse:
            return HttpResponse.Ok().body(f"Post {path.post_id}")
    """

    def into_inner(self) -> T:
        """Extract the inner value."""
        ...


class HttpRequest:
    """HTTP request type.

    Contains request metadata like method, URI, headers, etc.
    Can be extracted in handlers when you need low-level access.

    Maps to actix_web::HttpRequest in Rust.

    Example:
        async def handler(req: HttpRequest) -> HttpResponse:
            method = req.method()
            path = req.path()
            return HttpResponse.Ok().body(f"{method} {path}")
    """

    def method(self) -> str:
        """Get the HTTP method."""
        ...

    def uri(self) -> str:
        """Get the request URI."""
        ...

    def path(self) -> str:
        """Get the URL path."""
        ...

    def query_string(self) -> str:
        """Get the raw query string."""
        ...

    def headers(self) -> object:
        """Get request headers."""
        ...


class Route:
    """Route configuration for HTTP method handlers.

    Created by web::get(), web::post(), etc. functions.
    Use .to() to attach a handler function.

    Maps to actix_web::web::Route in Rust.

    Example:
        # Register a GET route
        app = App.new().route("/", get().to(index))

        # Register a POST route
        app = App.new().route("/submit", post().to(submit_handler))
    """

    def to(self, handler: object) -> "Route":
        """Attach a handler function to this route.

        The handler must be an async function that returns an HttpResponse
        or impl Responder.
        """
        ...


def ErrorBadRequest(msg: str) -> object:
    """Create a 400 Bad Request error.

    Use in handlers to return an error response.

    Example:
        if not valid:
            return Err(ErrorBadRequest("Invalid input"))
    """
    ...


def ErrorUnauthorized(msg: str) -> object:
    """Create a 401 Unauthorized error."""
    ...


def ErrorForbidden(msg: str) -> object:
    """Create a 403 Forbidden error."""
    ...


def ErrorNotFound(msg: str) -> object:
    """Create a 404 Not Found error."""
    ...


def ErrorInternalServerError(msg: str) -> object:
    """Create a 500 Internal Server Error."""
    ...


def get() -> object:
    """Create a GET route configuration.

    Use with App.route() to configure a GET endpoint.

    Example:
        App.new().route("/", get().to(handler))
    """
    ...


def post() -> object:
    """Create a POST route configuration."""
    ...


def put() -> object:
    """Create a PUT route configuration."""
    ...


def delete() -> object:
    """Create a DELETE route configuration."""
    ...


def patch() -> object:
    """Create a PATCH route configuration."""
    ...


class Person:
    pass

class TestRequest:
    """Test `Request` builder.

For unit testing, actix provides a request builder type and a simple handler runner. TestRequest implements a builder-like pattern.
You can generate various types of request via TestRequest's methods:
- [`TestRequest::to_request`] creates an [`actix_http::Request`](Request).
- [`TestRequest::to_srv_request`] creates a [`ServiceRequest`], which is used for testing middlewares and chain adapters.
- [`TestRequest::to_srv_response`] creates a [`ServiceResponse`].
- [`TestRequest::to_http_request`] creates an [`HttpRequest`], which is used for testing handlers.

```
use actix_web::{test, HttpRequest, HttpResponse, HttpMessage};
use actix_web::http::{header, StatusCode};

async fn handler(req: HttpRequest) -> HttpResponse {
if let Some(hdr) = req.headers().get(header::CONTENT_TYPE) {
HttpResponse::Ok().into()
} else {
HttpResponse::BadRequest().into()
}
}

#[actix_web::test]
# // force rustdoc to display the correct thing and also compile check the test
# async fn _test() {}
async fn test_index() {
let req = test::TestRequest::default()
.insert_header(header::ContentType::plaintext())
.to_http_request();

let resp = handler(req).await;
assert_eq!(resp.status(), StatusCode::OK);

let req = test::TestRequest::default().to_http_request();
let resp = handler(req).await;
assert_eq!(resp.status(), StatusCode::BAD_REQUEST);
}
```"""

    @staticmethod
    def default() -> "TestRequest": ...

    @staticmethod
    def with_uri(uri: str) -> "TestRequest": ...

    @staticmethod
    def get() -> "TestRequest": ...

    @staticmethod
    def post() -> "TestRequest": ...

    @staticmethod
    def put() -> "TestRequest": ...

    @staticmethod
    def patch() -> "TestRequest": ...

    @staticmethod
    def delete() -> "TestRequest": ...

    def version(self, ver: Version) -> Self: ...

    def method(self, meth: Method) -> Self: ...

    def uri(self, path: str) -> Self: ...

    def insert_header(self, header: object) -> Self: ...

    def append_header(self, header: object) -> Self: ...

    def cookie(self, cookie: Cookie) -> Self: ...

    def param(self, name: object, value: object) -> Self: ...

    def peer_addr(self, addr: SocketAddr) -> Self: ...

    def set_payload(self, data: object) -> Self: ...

    def set_form(self, data: object) -> Self: ...

    def set_json(self, data: object) -> Self: ...

    def app_data(self, data: T) -> Self: ...

    def data(self, data: T) -> Self: ...

    def to_request(self) -> Request: ...

    def to_srv_request(self) -> ServiceRequest: ...

    def to_srv_response(self, res: object) -> object: ...

    def to_http_request(self) -> HttpRequest: ...

    def to_http_parts(self) -> object: ...

    def send_request(self, app: S) -> Response: ...

    def set_server_hostname(self, host: str) -> None: ...

class ThinData:
    """Application data wrapper and extractor for cheaply-cloned types.

Similar to the [`Data`] wrapper but for `Clone`/`Copy` types that are already an `Arc` internally,
share state using some other means when cloned, or is otherwise static data that is very cheap
to clone.

Unlike `Data`, this wrapper clones `T` during extraction. Therefore, it is the user's
responsibility to ensure that clones of `T` do actually share the same state, otherwise state
may be unexpectedly different across multiple requests.

Note that if your type is literally an `Arc<T>` then it's recommended to use the
[`Data::from(arc)`][data_from_arc] conversion instead.

# Examples

```
use actix_web::{
web::{self, ThinData},
App, HttpResponse, Responder,
};

// Use the `ThinData<T>` extractor to access a database connection pool.
async fn index(ThinData(db_pool): ThinData<DbPool>) -> impl Responder {
// database action ...

HttpResponse::Ok()
}

# type DbPool = ();
let db_pool = DbPool::default();

App::new()
.app_data(ThinData(db_pool.clone()))
.service(web::resource("/").get(index))
# ;
```

[`Data`]: crate::web::Data
[data_from_arc]: crate::web::Data#impl-From<Arc<T>>-for-Data<T>"""

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class ReqData:
    """Request-local data extractor.

Request-local data is arbitrary data attached to an individual request, usually
by middleware. It can be set via `extensions_mut` on [`HttpRequest`][htr_ext_mut]
or [`ServiceRequest`][srv_ext_mut].

Unlike app data, request data is dropped when the request has finished processing. This makes it
useful as a kind of messaging system between middleware and request handlers. It uses the same
types-as-keys storage system as app data.

# Mutating Request Data
Note that since extractors must output owned data, only types that `impl Clone` can use this
extractor. A clone is taken of the required request data and can, therefore, not be directly
mutated in-place. To mutate request data, continue to use [`HttpRequest::extensions_mut`] or
re-insert the cloned data back into the extensions map. A `DerefMut` impl is intentionally not
provided to make this potential foot-gun more obvious.

# Examples
```no_run
# use actix_web::{web, HttpResponse, HttpRequest, Responder, HttpMessage as _};
#[derive(Debug, Clone, PartialEq)]
struct FlagFromMiddleware(String);

/// Use the `ReqData<T>` extractor to access request data in a handler.
async fn handler(
req: HttpRequest,
opt_flag: Option<web::ReqData<FlagFromMiddleware>>,
) -> impl Responder {
// use an option extractor if middleware is not guaranteed to add this type of req data
if let Some(flag) = opt_flag {
assert_eq!(&flag.into_inner(), req.extensions().get::<FlagFromMiddleware>().unwrap());
}

HttpResponse::Ok()
}
```

[htr_ext_mut]: crate::HttpRequest::extensions_mut
[srv_ext_mut]: crate::dev::ServiceRequest::extensions_mut"""

    def into_inner(self) -> T: ...

    def deref(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class Resource:
    """A collection of [`Route`]s that respond to the same path pattern.

Resource in turn has at least one route. Route consists of an handlers objects and list of
guards (objects that implement `Guard` trait). Resources and routes uses builder-like pattern
for configuration. During request handling, the resource object iterates through all routes
and checks guards for the specific route, if the request matches all the guards, then the route
is considered matched and the route handler gets called.

# Examples
```
use actix_web::{web, App, HttpResponse};

let app = App::new().service(
web::resource("/")
.get(|| HttpResponse::Ok())
.post(|| async { "Hello World!" })
);
```

If no matching route is found, an empty 405 response is returned which includes an
[appropriate Allow header][RFC 9110 §15.5.6]. This default behavior can be overridden using
[`default_service()`](Self::default_service).

[RFC 9110 §15.5.6]: https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.6"""

    @staticmethod
    def new(path: T) -> "Resource": ...

    def name(self, name: str) -> Self: ...

    def guard(self, guard: G) -> Self: ...

    def route(self, route: Route) -> Self: ...

    def app_data(self, data: U) -> Self: ...

    def data(self, data: U) -> Self: ...

    def to(self, handler: F) -> Self: ...

    def wrap(self, mw: M) -> object: ...

    def wrap_fn(self, mw: F) -> object: ...

    def default_service(self, f: F) -> Self: ...

    def register(self, config: AppService) -> None: ...

class ResourceFactory:

    def new_service(self, _: None) -> Future: ...

class ResourceService:

    def call(self, req: ServiceRequest) -> Future: ...

class ResourceEndpoint:

    def new_service(self, _: None) -> Future: ...

class HttpServer:
    """An HTTP Server.

Create new HTTP server with application factory.

# Automatic HTTP Version Selection

There are two ways to select the HTTP version of an incoming connection:

- One is to rely on the ALPN information that is provided when using a TLS (HTTPS); both
versions are supported automatically when using either of the `.bind_rustls()` or
`.bind_openssl()` methods.
- The other is to read the first few bytes of the TCP stream. This is the only viable approach
for supporting H2C, which allows the HTTP/2 protocol to work over plaintext connections. Use
the `.bind_auto_h2c()` method to enable this behavior.

# Examples

```no_run
use actix_web::{web, App, HttpResponse, HttpServer};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
HttpServer::new(|| {
App::new()
.service(web::resource("/").to(|| async { "hello world" }))
})
.bind(("127.0.0.1", 8080))?
.run()
.await
}
```"""

    @staticmethod
    def new(factory: F) -> "HttpServer": ...

    def workers(self, num: int) -> Self: ...

    def keep_alive(self, val: T) -> Self: ...

    def backlog(self, backlog: int) -> Self: ...

    def max_connections(self, num: int) -> Self: ...

    def max_connection_rate(self, num: int) -> Self: ...

    def worker_max_blocking_threads(self, num: int) -> Self: ...

    def client_request_timeout(self, dur: Duration) -> Self: ...

    def client_timeout(self, dur: Duration) -> Self: ...

    def client_disconnect_timeout(self, dur: Duration) -> Self: ...

    def tls_handshake_timeout(self, dur: Duration) -> Self: ...

    def client_shutdown(self, dur: int) -> Self: ...

    def h1_allow_half_closed(self, allow: bool) -> Self: ...

    def on_connect(self, f: CB) -> object: ...

    def server_hostname(self, val: T) -> Self: ...

    def system_exit(self) -> Self: ...

    def disable_signals(self) -> Self: ...

    def shutdown_signal(self, shutdown_signal: Fut) -> Self: ...

    def shutdown_timeout(self, sec: int) -> Self: ...

    def addrs(self) -> list[SocketAddr]: ...

    def addrs_with_scheme(self) -> list[object]: ...

    def bind(self, addrs: A) -> object: ...

    def bind_auto_h2c(self, addrs: A) -> object: ...

    def bind_rustls(self, addrs: A, config: ServerConfig) -> object: ...

    def bind_rustls_021(self, addrs: A, config: ServerConfig) -> object: ...

    def bind_rustls_0_22(self, addrs: A, config: ServerConfig) -> object: ...

    def bind_rustls_0_23(self, addrs: A, config: ServerConfig) -> object: ...

    def bind_openssl(self, addrs: A, builder: SslAcceptorBuilder) -> object: ...

    def listen(self, lst: TcpListener) -> object: ...

    def listen_auto_h2c(self, lst: TcpListener) -> object: ...

    def listen_rustls(self, lst: TcpListener, config: ServerConfig) -> object: ...

    def listen_rustls_0_21(self, lst: TcpListener, config: ServerConfig) -> object: ...

    def listen_rustls_0_22(self, lst: TcpListener, config: ServerConfig) -> object: ...

    def listen_rustls_0_23(self, lst: TcpListener, config: ServerConfig) -> object: ...

    def listen_openssl(self, lst: TcpListener, builder: SslAcceptorBuilder) -> object: ...

    def bind_uds(self, uds_path: A) -> object: ...

    def listen_uds(self, lst: UnixListener) -> object: ...

    def run(self) -> Server: ...

class Data:
    """Application data wrapper and extractor.

# Setting Data
Data is set using the `app_data` methods on `App`, `Scope`, and `Resource`. If data is wrapped
in this `Data` type for those calls, it can be used as an extractor.

Note that `Data` should be constructed _outside_ the `HttpServer::new` closure if shared,
potentially mutable state is desired. `Data` is cheap to clone; internally, it uses an `Arc`.

See also [`App::app_data`](crate::App::app_data), [`Scope::app_data`](crate::Scope::app_data),
and [`Resource::app_data`](crate::Resource::app_data).

# Extracting `Data`
Since the Actix Web router layers application data, the returned object will reference the
"closest" instance of the type. For example, if an `App` stores a `u32`, a nested `Scope`
also stores a `u32`, and the delegated request handler falls within that `Scope`, then
extracting a `web::Data<u32>` for that handler will return the `Scope`'s instance. However,
using the same router set up and a request that does not get captured by the `Scope`,
`web::<Data<u32>>` would return the `App`'s instance.

If route data is not set for a handler, using `Data<T>` extractor would cause a `500 Internal
Server Error` response.

See also [`HttpRequest::app_data`]
and [`ServiceRequest::app_data`](crate::dev::ServiceRequest::app_data).

# Unsized Data
For types that are unsized, most commonly `dyn T`, `Data` can wrap these types by first
constructing an `Arc<dyn T>` and using the `From` implementation to convert it.

```
# use std::{fmt::Display, sync::Arc};
# use actix_web::web::Data;
let displayable_arc: Arc<dyn Display> = Arc::new(42usize);
let displayable_data: Data<dyn Display> = Data::from(displayable_arc);
```

# Examples
```
use std::sync::Mutex;
use actix_web::{App, HttpRequest, HttpResponse, Responder, web::{self, Data}};

struct MyData {
counter: usize,
}

/// Use the `Data<T>` extractor to access data in a handler.
async fn index(data: Data<Mutex<MyData>>) -> impl Responder {
let mut my_data = data.lock().unwrap();
my_data.counter += 1;
HttpResponse::Ok()
}

/// Alternatively, use the `HttpRequest::app_data` method to access data in a handler.
async fn index_alt(req: HttpRequest) -> impl Responder {
let data = req.app_data::<Data<Mutex<MyData>>>().unwrap();
let mut my_data = data.lock().unwrap();
my_data.counter += 1;
HttpResponse::Ok()
}

let data = Data::new(Mutex::new(MyData { counter: 0 }));

let app = App::new()
// Store `MyData` in application storage.
.app_data(Data::clone(&data))
.route("/index.html", web::get().to(index))
.route("/index-alt.html", web::get().to(index_alt));
```"""

    @staticmethod
    def new(state: T) -> object: ...

    def get_ref(self) -> T: ...

    def into_inner(self) -> object: ...

    def deref(self) -> object: ...

    def clone(self) -> object: ...

    @staticmethod
    def from_(arc: object) -> "Data": ...

    @staticmethod
    def default() -> "Data": ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def deserialize(deserializer: D) -> object: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

    def create(self, extensions: Extensions) -> bool: ...

class AppService:
    """Application configuration"""

    def is_root(self) -> bool: ...

    def config(self) -> AppConfig: ...

    def default_service(self) -> object: ...

    def register_service(self, rdef: ResourceDef, guards: list[dynGuard] | None, factory: F, nested: object | None) -> None: ...

class AppConfig:
    """Application connection config."""

    @staticmethod
    def __priv_test_new(secure: bool, host: str, addr: SocketAddr) -> "AppConfig": ...

    def host(self) -> str: ...

    def secure(self) -> bool: ...

    def local_addr(self) -> SocketAddr: ...

    @staticmethod
    def default() -> "AppConfig": ...

class ServiceConfig:
    """Enables parts of app configuration to be declared separately from the app itself. Helpful for
modularizing large applications.

Merge a `ServiceConfig` into an app using [`App::configure`](crate::App::configure). Scope and
resources services have similar methods.

```
use actix_web::{web, App, HttpResponse};

// this function could be located in different module
fn config(cfg: &mut web::ServiceConfig) {
cfg.service(web::resource("/test")
.route(web::get().to(|| HttpResponse::Ok()))
.route(web::head().to(|| HttpResponse::MethodNotAllowed()))
);
}

// merge `/test` routes from config function to App
App::new().configure(config);
```"""

    def data(self, data: U) -> Self: ...

    def app_data(self, ext: U) -> Self: ...

    def default_service(self, f: F) -> Self: ...

    def configure(self, f: F) -> Self: ...

    def route(self, path: str, route: Route) -> Self: ...

    def service(self, factory: F) -> Self: ...

    def external_resource(self, name: N, url: U) -> Self: ...

class HostGuard:

    def scheme(self, scheme: H) -> HostGuard: ...

    def check(self, ctx: GuardContext) -> bool: ...

class Acceptable:
    """A guard that verifies that an `Accept` header is present and it contains a compatible MIME type.

An exception is that matching `*/*` must be explicitly enabled because most browsers send this
as part of their `Accept` header for almost every request.

# Examples
```
use actix_web::{guard::Acceptable, web, HttpResponse};

web::resource("/images")
.guard(Acceptable::new(mime::IMAGE_STAR))
.default_service(web::to(|| async {
HttpResponse::Ok().body("only called when images responses are acceptable")
}));
```"""

    @staticmethod
    def new(mime: Mime) -> "Acceptable": ...

    def match_star_star(self) -> Self: ...

    def check(self, ctx: GuardContext) -> bool: ...

class GuardContext:
    """Provides access to request parts that are useful during routing."""

    def head(self) -> RequestHead: ...

    def req_data(self) -> object: ...

    def req_data_mut(self) -> object: ...

    def header(self) -> H | None: ...

    def app_data(self) -> object: ...

class AnyGuard:
    """A collection of guards that match if the disjunction of their `check` outcomes is true.

That is, only one contained guard needs to match in order for the aggregate guard to match.

Construct an `AnyGuard` using [`Any`]."""

    def or_(self, guard: F) -> Self: ...

    def check(self, ctx: GuardContext) -> bool: ...

class AllGuard:
    """A collection of guards that match if the conjunction of their `check` outcomes is true.

That is, **all** contained guard needs to match in order for the aggregate guard to match.

Construct an `AllGuard` using [`All`]."""

    def and_(self, guard: F) -> Self: ...

    def check(self, ctx: GuardContext) -> bool: ...

class Not:
    """Wraps a guard and inverts the outcome of its `Guard` implementation.

# Examples
The handler below will be called for any request method apart from `GET`.
```
use actix_web::{guard, web, HttpResponse};

web::route()
.guard(guard::Not(guard::Get()))
.to(|| HttpResponse::Ok());
```"""

    def check(self, ctx: GuardContext) -> bool: ...

class AppInit:
    """Service factory to convert [`Request`] to a [`ServiceRequest<S>`].

It also executes data factories."""

    def new_service(self, config: AppConfig) -> Future: ...

class AppInitService:
    """The [`Service`] that is passed to `actix-http`'s server builder.

Wraps a service receiving a [`ServiceRequest`] into one receiving a [`Request`]."""

    def call(self, req: Request) -> Future: ...

    def drop(self) -> None: ...

class AppRoutingFactory:

    def new_service(self, _: None) -> Future: ...

class AppRouting:
    """The Actix Web router default entry point."""

    def call(self, req: ServiceRequest) -> Future: ...

class AppEntry:
    """Wrapper service for routing"""

    @staticmethod
    def new(factory: object) -> "AppEntry": ...

    def new_service(self, _: None) -> Future: ...

class ConnectionInfo:
    """HTTP connection information.

`ConnectionInfo` implements `FromRequest` and can be extracted in handlers.

# Examples
```
# use actix_web::{HttpResponse, Responder};
use actix_web::dev::ConnectionInfo;

async fn handler(conn: ConnectionInfo) -> impl Responder {
match conn.host() {
"actix.rs" => HttpResponse::Ok().body("Welcome!"),
"admin.actix.rs" => HttpResponse::Ok().body("Admin portal."),
_ => HttpResponse::NotFound().finish()
}
}
# let _svc = actix_web::web::to(handler);
```

# Implementation Notes
Parses `Forwarded` header information according to [RFC 7239][rfc7239] but does not try to
interpret the values for each property. As such, the getter methods on `ConnectionInfo` return
strings instead of IP addresses or other types to acknowledge that they may be
[obfuscated][rfc7239-63] or [unknown][rfc7239-62].

If the older, related headers are also present (eg. `X-Forwarded-For`), then `Forwarded`
is preferred.

[rfc7239]: https://datatracker.ietf.org/doc/html/rfc7239
[rfc7239-62]: https://datatracker.ietf.org/doc/html/rfc7239#section-6.2
[rfc7239-63]: https://datatracker.ietf.org/doc/html/rfc7239#section-6.3"""

    def realip_remote_addr(self) -> object: ...

    def peer_addr(self) -> object: ...

    def host(self) -> str: ...

    def scheme(self) -> str: ...

    def remote_addr(self) -> object: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class PeerAddr:
    """Extractor for peer's socket address.

Also see [`HttpRequest::peer_addr`] and [`ConnectionInfo::peer_addr`].

# Examples
```
# use actix_web::Responder;
use actix_web::dev::PeerAddr;

async fn handler(peer_addr: PeerAddr) -> impl Responder {
let socket_addr = peer_addr.0;
socket_addr.to_string()
}
# let _svc = actix_web::web::to(handler);
```"""

    def into_inner(self) -> SocketAddr: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class MissingPeerAddr:
    pass

class Route:
    """A request handler with [guards](guard).

Route uses a builder-like pattern for configuration. If handler is not set, a `404 Not Found`
handler is used."""

    @staticmethod
    def new() -> "Route": ...

    def wrap(self, mw: M) -> Route: ...

    def new_service(self, _: None) -> Future: ...

    def method(self, method: Method) -> Self: ...

    def guard(self, f: F) -> Self: ...

    def to(self, handler: F) -> Self: ...

    def service(self, service_factory: S) -> Self: ...

class RouteService:

    def check(self, req: ServiceRequest) -> bool: ...

    def call(self, req: ServiceRequest) -> Future: ...

class Redirect:
    """An HTTP service for redirecting one path to another path or URL.

By default, the "307 Temporary Redirect" status is used when responding. See [this MDN
article][mdn-redirects] on why 307 is preferred over 302.

# Examples
As service:
```
use actix_web::{web, App};

App::new()
// redirect "/duck" to DuckDuckGo
.service(web::redirect("/duck", "https://duck.com"))
.service(
// redirect "/api/old" to "/api/new"
web::scope("/api").service(web::redirect("/old", "/new"))
);
```

As responder:
```
use actix_web::{web::Redirect, Responder};

async fn handler() -> impl Responder {
// sends a permanent (308) redirect to duck.com
Redirect::to("https://duck.com").permanent()
}
# actix_web::web::to(handler);
```

[mdn-redirects]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections#temporary_redirections"""

    @staticmethod
    def new(from_: object, to: object) -> "Redirect": ...

    @staticmethod
    def to(to: object) -> "Redirect": ...

    def permanent(self) -> Self: ...

    def temporary(self) -> Self: ...

    def see_other(self) -> Self: ...

    def using_status_code(self, status: StatusCode) -> Self: ...

    def register(self, config: AppService) -> None: ...

    def respond_to(self, _req: HttpRequest) -> object: ...

class ResourceMap:

    @staticmethod
    def new(root: ResourceDef) -> "ResourceMap": ...

    def add(self, pattern: ResourceDef, nested: object | None) -> None: ...

    def url_for(self, req: HttpRequest, name: str, elements: U) -> Url: ...

    def has_resource(self, path: str) -> bool: ...

    def match_name(self, path: str) -> object: ...

    def match_pattern(self, path: str) -> str | None: ...

class HttpRequest:
    """An incoming request."""

    def head(self) -> RequestHead: ...

    def uri(self) -> Uri: ...

    def full_url(self) -> Url: ...

    def method(self) -> Method: ...

    def version(self) -> Version: ...

    def headers(self) -> HeaderMap: ...

    def path(self) -> str: ...

    def query_string(self) -> str: ...

    def match_info(self) -> object: ...

    def match_pattern(self) -> str | None: ...

    def match_name(self) -> object: ...

    def conn_data(self) -> object: ...

    def url_for(self, name: str, elements: U) -> Url: ...

    def url_for_static(self, name: str) -> Url: ...

    def resource_map(self) -> ResourceMap: ...

    def peer_addr(self) -> SocketAddr | None: ...

    def connection_info(self) -> object: ...

    def app_config(self) -> AppConfig: ...

    def app_data(self) -> object: ...

    def cookies(self) -> object: ...

    def cookie(self, name: str) -> Cookie | None: ...

    def headers(self) -> HeaderMap: ...

    def extensions(self) -> object: ...

    def extensions_mut(self) -> object: ...

    def take_payload(self) -> object: ...

    def drop(self) -> None: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

    def fmt(self, f: Formatter) -> Result: ...

class Scope:
    """A collection of [`Route`]s, [`Resource`]s, or other services that share a common path prefix.

The `Scope`'s path can contain [dynamic segments]. The dynamic segments can be extracted from
requests using the [`Path`](crate::web::Path) extractor or
with [`HttpRequest::match_info()`](crate::HttpRequest::match_info).

# Avoid Trailing Slashes
Avoid using trailing slashes in the scope prefix (e.g., `web::scope("/scope/")`). It will almost
certainly not have the expected behavior. See the [documentation on resource definitions][pat]
to understand why this is the case and how to correctly construct scope/prefix definitions.

# Examples
```
use actix_web::{web, App, HttpResponse};

let app = App::new().service(
web::scope("/{project_id}")
.service(web::resource("/path1").to(|| async { "OK" }))
.service(web::resource("/path2").route(web::get().to(|| HttpResponse::Ok())))
.service(web::resource("/path3").route(web::head().to(HttpResponse::MethodNotAllowed)))
);
```

In the above example three routes get registered:
- /{project_id}/path1 - responds to all HTTP methods
- /{project_id}/path2 - responds to `GET` requests
- /{project_id}/path3 - responds to `HEAD` requests

[pat]: crate::dev::ResourceDef#prefix-resources
[dynamic segments]: crate::dev::ResourceDef#dynamic-segments"""

    @staticmethod
    def new(path: str) -> "Scope": ...

    def guard(self, guard: G) -> Self: ...

    def app_data(self, data: U) -> Self: ...

    def data(self, data: U) -> Self: ...

    def configure(self, cfg_fn: F) -> Self: ...

    def service(self, factory: F) -> Self: ...

    def route(self, path: str, route: Route) -> Self: ...

    def default_service(self, f: F) -> Self: ...

    def wrap(self, mw: M) -> object: ...

    def wrap_fn(self, mw: F) -> object: ...

    def register(self, config: AppService) -> None: ...

class ScopeFactory:

    def new_service(self, _: None) -> Future: ...

class ScopeService:

    def call(self, req: ServiceRequest) -> Future: ...

class ScopeEndpoint:

    def new_service(self, _: None) -> Future: ...

class App:
    """The top-level builder for an Actix Web application."""

    @staticmethod
    def new() -> "App": ...

    def app_data(self, data: U) -> Self: ...

    def data(self, data: U) -> Self: ...

    def data_factory(self, data: F) -> Self: ...

    def configure(self, f: F) -> Self: ...

    def route(self, path: str, route: Route) -> Self: ...

    def service(self, factory: F) -> Self: ...

    def default_service(self, svc: F) -> Self: ...

    def external_resource(self, name: N, url: U) -> Self: ...

    def wrap(self, mw: M) -> object: ...

    def wrap_fn(self, mw: F) -> object: ...

    def into_factory(self) -> object: ...

class ContentDisposition:
    """`Content-Disposition` header.

It is compatible to be used either as [a response header for the main body][use_main_body]
as (re)defined in [RFC 6266], or as [a header for a multipart body][use_multipart] as
(re)defined in [RFC 7587].

In a regular HTTP response, the *Content-Disposition* response header is a header indicating if
the content is expected to be displayed *inline* in the browser, that is, as a Web page or as
part of a Web page, or as an attachment, that is downloaded and saved locally, and also can be
used to attach additional metadata, such as the filename to use when saving the response payload
locally.

In a *multipart/form-data* body, the HTTP *Content-Disposition* general header is a header that
can be used on the subpart of a multipart body to give information about the field it applies to.
The subpart is delimited by the boundary defined in the *Content-Type* header. Used on the body
itself, *Content-Disposition* has no effect.

# ABNF
```plain
content-disposition = "Content-Disposition" ":"
disposition-type *( ";" disposition-parm )

disposition-type    = "inline" | "attachment" | disp-ext-type
; case-insensitive

disp-ext-type       = token

disposition-parm    = filename-parm | disp-ext-parm

filename-parm       = "filename" "=" value
| "filename*" "=" ext-value

disp-ext-parm       = token "=" value
| ext-token "=" ext-value

ext-token           = <the characters in token, followed by "*">
```

# Note
*filename* is [not supposed](https://datatracker.ietf.org/doc/html/rfc6266#appendix-D) to
contain any non-ASCII characters when used in a *Content-Disposition* HTTP response header,
where filename* with charset UTF-8 may be used instead in case there are Unicode characters in
file names. Filename is [acceptable](https://datatracker.ietf.org/doc/html/rfc7578#section-4.2)
to be UTF-8 encoded directly in a *Content-Disposition* header for
*multipart/form-data*, though.

*filename* [must not](https://datatracker.ietf.org/doc/html/rfc7578#section-4.2) be used within
*multipart/form-data*.

# Examples
```
use actix_web::http::header::{
Charset, ContentDisposition, DispositionParam, DispositionType,
ExtendedValue,
};

let cd1 = ContentDisposition {
disposition: DispositionType::Attachment,
parameters: vec![DispositionParam::FilenameExt(ExtendedValue {
charset: Charset::Iso_8859_1, // The character set for the bytes of the filename
language_tag: None, // The optional language tag (see `language-tag` crate)
value: b"\\xA9 Ferris 2011.txt".to_vec(), // the actual bytes of the filename
})],
};
assert!(cd1.is_attachment());
assert!(cd1.get_filename_ext().is_some());

let cd2 = ContentDisposition {
disposition: DispositionType::FormData,
parameters: vec![
DispositionParam::Name(String::from("file")),
DispositionParam::Filename(String::from("bill.odt")),
],
};
assert_eq!(cd2.get_name(), Some("file")); // field name
assert_eq!(cd2.get_filename(), Some("bill.odt"));

// HTTP response header with Unicode characters in file names
let cd3 = ContentDisposition {
disposition: DispositionType::Attachment,
parameters: vec![
DispositionParam::FilenameExt(ExtendedValue {
charset: Charset::Ext(String::from("UTF-8")),
language_tag: None,
value: String::from("\\u{1f600}.svg").into_bytes(),
}),
// fallback for better compatibility
DispositionParam::Filename(String::from("Grinning-Face-Emoji.svg"))
],
};
assert_eq!(cd3.get_filename_ext().map(|ev| ev.value.as_ref()),
Some("\\u{1f600}.svg".as_bytes()));
```

# Security Note
If "filename" parameter is supplied, do not use the file name blindly, check and possibly
change to match local file system conventions if applicable, and do not use directory path
information that may be present.
See [RFC 2183 §2.3](https://datatracker.ietf.org/doc/html/rfc2183#section-2.3).

[use_main_body]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body
[RFC 6266]: https://datatracker.ietf.org/doc/html/rfc6266
[use_multipart]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_header_for_a_multipart_body
[RFC 7587]: https://datatracker.ietf.org/doc/html/rfc7578"""

    @staticmethod
    def attachment(filename: object) -> "ContentDisposition": ...

    @staticmethod
    def from_raw(hv: HeaderValue) -> object: ...

    def is_inline(self) -> bool: ...

    def is_attachment(self) -> bool: ...

    def is_form_data(self) -> bool: ...

    def is_ext(self, disp_type: object) -> bool: ...

    def get_name(self) -> object: ...

    def get_filename(self) -> object: ...

    def get_filename_ext(self) -> object: ...

    def get_unknown(self, name: object) -> object: ...

    def get_unknown_ext(self, name: object) -> object: ...

    def try_into_value(self) -> HeaderValue: ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: T) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class ContentLength:
    """`Content-Length` header, defined in [RFC 9110 §8.6].

The Content-Length

# ABNF

```plain
Content-Length = 1*DIGIT
```

# Example Values

- `0`
- `3495`

# Examples

```
use actix_web::{http::header::ContentLength, HttpResponse};

let res_empty = HttpResponse::Ok()
.insert_header(ContentLength(0));

let res_fake_cl = HttpResponse::Ok()
.insert_header(ContentLength(3_495));
```

[RFC 9110 §8.6]: https://www.rfc-editor.org/rfc/rfc9110#name-content-length"""

    def into_inner(self) -> int: ...

    @staticmethod
    def from_str(val: str) -> object: ...

    def try_into_value(self) -> HeaderValue: ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: M) -> object: ...

    @staticmethod
    def from_(len: int) -> "ContentLength": ...

    def eq(self, other: int) -> bool: ...

    def partial_cmp(self, other: int) -> Ordering | None: ...

class EntityTag:
    """An entity tag, defined in [RFC 7232 §2.3].

An entity tag consists of a string enclosed by two literal double quotes.
Preceding the first double quote is an optional weakness indicator,
which always looks like `W/`. Examples for valid tags are `"xyzzy"` and
`W/"xyzzy"`.

# ABNF
```plain
entity-tag = [ weak ] opaque-tag
weak       = %x57.2F ; "W/", case-sensitive
opaque-tag = DQUOTE *etagc DQUOTE
etagc      = %x21 / %x23-7E / obs-text
; VCHAR except double quotes, plus obs-text
```

# Comparison
To check if two entity tags are equivalent in an application always use the
`strong_eq` or `weak_eq` methods based on the context of the Tag. Only use
`==` to check if two tags are identical.

The example below shows the results for a set of entity-tag pairs and
both the weak and strong comparison function results:

| `ETag 1`| `ETag 2`| Strong Comparison | Weak Comparison |
|---------|---------|-------------------|-----------------|
| `W/"1"` | `W/"1"` | no match          | match           |
| `W/"1"` | `W/"2"` | no match          | no match        |
| `W/"1"` | `"1"`   | no match          | match           |
| `"1"`   | `"1"`   | match             | match           |

[RFC 7232 §2.3](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3)"""

    @staticmethod
    def new(weak: bool, tag: str) -> "EntityTag": ...

    @staticmethod
    def new_weak(tag: str) -> "EntityTag": ...

    @staticmethod
    def weak(tag: str) -> "EntityTag": ...

    @staticmethod
    def new_strong(tag: str) -> "EntityTag": ...

    @staticmethod
    def strong(tag: str) -> "EntityTag": ...

    def tag(self) -> str: ...

    def set_tag(self, tag: object) -> None: ...

    def strong_eq(self, other: EntityTag) -> bool: ...

    def weak_eq(self, other: EntityTag) -> bool: ...

    def strong_ne(self, other: EntityTag) -> bool: ...

    def weak_ne(self, other: EntityTag) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(slice: str) -> "EntityTag": ...

    def try_into_value(self) -> HeaderValue: ...

class InternalError:
    """Wraps errors to alter the generated response status code.

In following example, the `io::Error` is wrapped into `ErrorBadRequest` which will generate a
response with the 400 Bad Request status code instead of the usual status code generated by
an `io::Error`.

# Examples
```
# use std::io;
# use actix_web::{error, HttpRequest};
async fn handler_error() -> Result<String, actix_web::Error> {
let err = io::Error::new(io::ErrorKind::Other, "error");
Err(error::ErrorBadRequest(err))
}
```"""

    @staticmethod
    def new(cause: T, status: StatusCode) -> "InternalError": ...

    @staticmethod
    def from_response(cause: T, response: HttpResponse) -> "InternalError": ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def status_code(self) -> StatusCode: ...

    def error_response(self) -> HttpResponse: ...

    def respond_to(self, _: HttpRequest) -> object: ...

class BlockingError:
    """An error representing a problem running a blocking task on a thread pool."""
    pass

class Error:
    """General purpose Actix Web error.

An Actix Web error is used to carry errors from `std::error` through actix in a convenient way.
It can be created through converting errors with `into()`.

Whenever it is created from an external object a response error is created for it that can be
used to create an HTTP response from it this means that if you have access to an actix `Error`
you can always get a `ResponseError` reference from it."""

    def status_code(self) -> StatusCode: ...

    def status_code(self) -> StatusCode: ...

    def status_code(self) -> StatusCode: ...

    def error_response(self) -> object: ...

    def as_response_error(self) -> dynResponseError: ...

    def as_error(self) -> object: ...

    def error_response(self) -> HttpResponse: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    def source(self) -> object: ...

    @staticmethod
    def from_(err: T) -> Exception: ...

    @staticmethod
    def from_(value: dynResponseError) -> "Error": ...

    @staticmethod
    def from_(err: object) -> Exception: ...

class Identity:
    """A no-op middleware that passes through request and response untouched."""

    def new_transform(self, service: S) -> Future: ...

class IdentityMiddleware:

    def call(self, req: Req) -> Future: ...

class ErrorHandlers:
    """Middleware for registering custom status code based error handlers.

Register handlers with the [`ErrorHandlers::handler()`] method to register a custom error handler
for a given status code. Handlers can modify existing responses or create completely new ones.

To register a default handler, use the [`ErrorHandlers::default_handler()`] method. This
handler will be used only if a response has an error status code (400-599) that isn't covered by
a more specific handler (set with the [`handler()`][ErrorHandlers::handler] method). See examples
below.

To register a default for only client errors (400-499) or only server errors (500-599), use the
[`ErrorHandlers::default_handler_client()`] and [`ErrorHandlers::default_handler_server()`]
methods, respectively.

Any response with a status code that isn't covered by a specific handler or a default handler
will pass by unchanged by this middleware.

# Examples

Adding a header:

```
use actix_web::{
dev::ServiceResponse,
http::{header, StatusCode},
middleware::{ErrorHandlerResponse, ErrorHandlers},
web, App, HttpResponse, Result,
};

fn add_error_header<B>(mut res: ServiceResponse<B>) -> Result<ErrorHandlerResponse<B>> {
res.response_mut().headers_mut().insert(
header::CONTENT_TYPE,
header::HeaderValue::from_static("Error"),
);

// body is unchanged, map to "left" slot
Ok(ErrorHandlerResponse::Response(res.map_into_left_body()))
}

let app = App::new()
.wrap(ErrorHandlers::new().handler(StatusCode::INTERNAL_SERVER_ERROR, add_error_header))
.service(web::resource("/").route(web::get().to(HttpResponse::InternalServerError)));
```

Modifying response body:

```
use actix_web::{
dev::ServiceResponse,
http::{header, StatusCode},
middleware::{ErrorHandlerResponse, ErrorHandlers},
web, App, HttpResponse, Result,
};

fn add_error_body<B>(res: ServiceResponse<B>) -> Result<ErrorHandlerResponse<B>> {
// split service response into request and response components
let (req, res) = res.into_parts();

// set body of response to modified body
let res = res.set_body("An error occurred.");

// modified bodies need to be boxed and placed in the "right" slot
let res = ServiceResponse::new(req, res)
.map_into_boxed_body()
.map_into_right_body();

Ok(ErrorHandlerResponse::Response(res))
}

let app = App::new()
.wrap(ErrorHandlers::new().handler(StatusCode::INTERNAL_SERVER_ERROR, add_error_body))
.service(web::resource("/").route(web::get().to(HttpResponse::InternalServerError)));
```

Registering default handler:

```
# use actix_web::{
#     dev::ServiceResponse,
#     http::{header, StatusCode},
#     middleware::{ErrorHandlerResponse, ErrorHandlers},
#     web, App, HttpResponse, Result,
# };
fn add_error_header<B>(mut res: ServiceResponse<B>) -> Result<ErrorHandlerResponse<B>> {
res.response_mut().headers_mut().insert(
header::CONTENT_TYPE,
header::HeaderValue::from_static("Error"),
);

// body is unchanged, map to "left" slot
Ok(ErrorHandlerResponse::Response(res.map_into_left_body()))
}

fn handle_bad_request<B>(mut res: ServiceResponse<B>) -> Result<ErrorHandlerResponse<B>> {
res.response_mut().headers_mut().insert(
header::CONTENT_TYPE,
header::HeaderValue::from_static("Bad Request Error"),
);

// body is unchanged, map to "left" slot
Ok(ErrorHandlerResponse::Response(res.map_into_left_body()))
}

// Bad Request errors will hit `handle_bad_request()`, while all other errors will hit
// `add_error_header()`. The order in which the methods are called is not meaningful.
let app = App::new()
.wrap(
ErrorHandlers::new()
.default_handler(add_error_header)
.handler(StatusCode::BAD_REQUEST, handle_bad_request)
)
.service(web::resource("/").route(web::get().to(HttpResponse::InternalServerError)));
```

You can set default handlers for all client (4xx) or all server (5xx) errors:

```
# use actix_web::{
#     dev::ServiceResponse,
#     http::{header, StatusCode},
#     middleware::{ErrorHandlerResponse, ErrorHandlers},
#     web, App, HttpResponse, Result,
# };
# fn add_error_header<B>(mut res: ServiceResponse<B>) -> Result<ErrorHandlerResponse<B>> {
#     res.response_mut().headers_mut().insert(
#         header::CONTENT_TYPE,
#         header::HeaderValue::from_static("Error"),
#     );
#     Ok(ErrorHandlerResponse::Response(res.map_into_left_body()))
# }
# fn handle_bad_request<B>(mut res: ServiceResponse<B>) -> Result<ErrorHandlerResponse<B>> {
#     res.response_mut().headers_mut().insert(
#         header::CONTENT_TYPE,
#         header::HeaderValue::from_static("Bad Request Error"),
#     );
#     Ok(ErrorHandlerResponse::Response(res.map_into_left_body()))
# }
// Bad request errors will hit `handle_bad_request()`, other client errors will hit
// `add_error_header()`, and server errors will pass through unchanged
let app = App::new()
.wrap(
ErrorHandlers::new()
.default_handler_client(add_error_header) // or .default_handler_server
.handler(StatusCode::BAD_REQUEST, handle_bad_request)
)
.service(web::resource("/").route(web::get().to(HttpResponse::InternalServerError)));
```"""

    @staticmethod
    def default() -> "ErrorHandlers": ...

    @staticmethod
    def new() -> "ErrorHandlers": ...

    def handler(self, status: StatusCode, handler: F) -> Self: ...

    def default_handler(self, handler: F) -> Self: ...

    def default_handler_client(self, handler: F) -> Self: ...

    def default_handler_server(self, handler: F) -> Self: ...

    def new_transform(self, service: S) -> Future: ...

class ErrorHandlersMiddleware:

    def call(self, req: ServiceRequest) -> Future: ...

class Compat:
    """Middleware for enabling any middleware to be used in [`Resource::wrap`](crate::Resource::wrap),
and [`Condition`](super::Condition).

# Examples
```
use actix_web::middleware::{Logger, Compat};
use actix_web::{App, web};

let logger = Logger::default();

// this would not compile because of incompatible body types
// let app = App::new()
//     .service(web::scope("scoped").wrap(logger));

// by using this middleware we can use the logger on a scope
let app = App::new()
.service(web::scope("scoped").wrap(Compat::new(logger)));
```"""

    @staticmethod
    def new(middleware: T) -> "Compat": ...

    def new_transform(self, service: S) -> Future: ...

class CompatMiddleware:

    def call(self, req: Req) -> Future: ...

class Logger:
    """Middleware for logging request and response summaries to the terminal.

This middleware uses the `log` crate to output information. Enable `log`'s output for the
"actix_web" scope using [`env_logger`](https://docs.rs/env_logger) or similar crate.

# Default Format
The [`default`](Logger::default) Logger uses the following format:

```plain
%a "%r" %s %b "%{Referer}i" "%{User-Agent}i" %T

Example Output:
127.0.0.1:54278 "GET /test HTTP/1.1" 404 20 "-" "HTTPie/2.2.0" 0.001074
```

# Examples
```
use actix_web::{middleware::Logger, App};

// access logs are printed with the INFO level so ensure it is enabled by default
env_logger::init_from_env(env_logger::Env::new().default_filter_or("info"));

let app = App::new()
// .wrap(Logger::default())
.wrap(Logger::new("%a %{User-Agent}i"));
```

# Format
Variable | Description
-------- | -----------
`%%` | The percent sign
`%a` | Peer IP address (or IP address of reverse proxy if used)
`%t` | Time when the request started processing (in RFC 3339 format)
`%r` | First line of request (Example: `GET /test HTTP/1.1`)
`%s` | Response status code
`%b` | Size of response in bytes, including HTTP headers
`%T` | Time taken to serve the request, in seconds to 6 decimal places
`%D` | Time taken to serve the request, in milliseconds
`%U` | Request URL
`%{r}a` | "Real IP" remote address **\\***
`%{FOO}i` | `request.headers["FOO"]`
`%{FOO}o` | `response.headers["FOO"]`
`%{FOO}e` | `env_var["FOO"]`
`%{FOO}xi` | [Custom request replacement](Logger::custom_request_replace) labelled "FOO"
`%{FOO}xo` | [Custom response replacement](Logger::custom_response_replace) labelled "FOO"

# Security
**\\*** "Real IP" remote address is calculated using
[`ConnectionInfo::realip_remote_addr()`](crate::dev::ConnectionInfo::realip_remote_addr())

If you use this value, ensure that all requests come from trusted hosts. Otherwise, it is
trivial for the remote client to falsify their source IP address."""

    @staticmethod
    def new(format: str) -> "Logger": ...

    def exclude(self, path: T) -> Self: ...

    def exclude_regex(self, path: T) -> Self: ...

    def log_target(self, target: object) -> Self: ...

    def log_level(self, level: Level) -> Self: ...

    def custom_request_replace(self, label: str, f: object) -> Self: ...

    def custom_response_replace(self, label: str, f: object) -> Self: ...

    @staticmethod
    def default() -> "Logger": ...

    def new_transform(self, service: S) -> Future: ...

class LoggerMiddleware:
    """Logger middleware service."""

    def call(self, req: ServiceRequest) -> Future: ...

class NormalizePath:
    """Middleware for normalizing a request's path so that routes can be matched more flexibly.

# Normalization Steps
- Merges consecutive slashes into one. (For example, `/path//one` always becomes `/path/one`.)
- Appends a trailing slash if one is not present, removes one if present, or keeps trailing
slashes as-is, depending on which [`TrailingSlash`] variant is supplied
to [`new`](NormalizePath::new()).

# Default Behavior
The default constructor chooses to strip trailing slashes from the end of paths with them
([`TrailingSlash::Trim`]). The implication is that route definitions should be defined without
trailing slashes or else they will be inaccessible (or vice versa when using the
`TrailingSlash::Always` behavior), as shown in the example tests below.

# Examples
```
use actix_web::{web, middleware, App};

# actix_web::rt::System::new().block_on(async {
let app = App::new()
.wrap(middleware::NormalizePath::trim())
.route("/test", web::get().to(|| async { "test" }))
.route("/unmatchable/", web::get().to(|| async { "unmatchable" }));

use actix_web::http::StatusCode;
use actix_web::test::{call_service, init_service, TestRequest};

let app = init_service(app).await;

let req = TestRequest::with_uri("/test").to_request();
let res = call_service(&app, req).await;
assert_eq!(res.status(), StatusCode::OK);

let req = TestRequest::with_uri("/test/").to_request();
let res = call_service(&app, req).await;
assert_eq!(res.status(), StatusCode::OK);

let req = TestRequest::with_uri("/unmatchable").to_request();
let res = call_service(&app, req).await;
assert_eq!(res.status(), StatusCode::NOT_FOUND);

let req = TestRequest::with_uri("/unmatchable/").to_request();
let res = call_service(&app, req).await;
assert_eq!(res.status(), StatusCode::NOT_FOUND);
# })
```"""

    @staticmethod
    def default() -> "NormalizePath": ...

    @staticmethod
    def new(trailing_slash_style: TrailingSlash) -> "NormalizePath": ...

    @staticmethod
    def trim() -> "NormalizePath": ...

    def new_transform(self, service: S) -> Future: ...

class NormalizePathNormalization:

    def call(self, req: ServiceRequest) -> Future: ...

class Condition:
    """Middleware for conditionally enabling other middleware.

# Examples
```
use actix_web::middleware::{Condition, NormalizePath};
use actix_web::App;

let enable_normalize = std::env::var("NORMALIZE_PATH").is_ok();
let app = App::new()
.wrap(Condition::new(enable_normalize, NormalizePath::default()));
```"""

    @staticmethod
    def new(enable: bool, transformer: T) -> "Condition": ...

    def new_transform(self, service: S) -> Future: ...

class DefaultHeaders:
    """Middleware for setting default response headers.

Headers with the same key that are already set in a response will *not* be overwritten.

# Examples
```
use actix_web::{web, http, middleware, App, HttpResponse};

let app = App::new()
.wrap(middleware::DefaultHeaders::new().add(("X-Version", "0.2")))
.service(
web::resource("/test")
.route(web::get().to(|| HttpResponse::Ok()))
.route(web::method(http::Method::HEAD).to(|| HttpResponse::MethodNotAllowed()))
);
```"""

    @staticmethod
    def new() -> "DefaultHeaders": ...

    def add(self, header: object) -> Self: ...

    def header(self, key: K, value: V) -> Self: ...

    def add_content_type(self) -> Self: ...

    def new_transform(self, service: S) -> Future: ...

class DefaultHeadersMiddleware:

    def call(self, req: ServiceRequest) -> Future: ...

class Compress:
    """Middleware for compressing response payloads.

# Encoding Negotiation
`Compress` will read the `Accept-Encoding` header to negotiate which compression codec to use.
Payloads are not compressed if the header is not sent. The `compress-*` [feature flags] are also
considered in this selection process.

# Pre-compressed Payload
If you are serving some data that is already using a compressed representation (e.g., a gzip
compressed HTML file from disk) you can signal this to `Compress` by setting an appropriate
`Content-Encoding` header. In addition to preventing double compressing the payload, this header
is required by the spec when using compressed representations and will inform the client that
the content should be uncompressed.

However, it is not advised to unconditionally serve encoded representations of content because
the client may not support it. The [`AcceptEncoding`] typed header has some utilities to help
perform manual encoding negotiation, if required. When negotiating content encoding, it is also
required by the spec to send a `Vary: Accept-Encoding` header.

A (naïve) example serving an pre-compressed Gzip file is included below.

# Examples
To enable automatic payload compression just include `Compress` as a top-level middleware:
```
use actix_web::{middleware, web, App, HttpResponse};

let app = App::new()
.wrap(middleware::Compress::default())
.default_service(web::to(|| async { HttpResponse::Ok().body("hello world") }));
```

Pre-compressed Gzip file being served from disk with correct headers added to bypass middleware:
```no_run
use actix_web::{middleware, http::header, web, App, HttpResponse, Responder};

async fn index_handler() -> actix_web::Result<impl Responder> {
Ok(actix_files::NamedFile::open_async("./assets/index.html.gz").await?
.customize()
.insert_header(header::ContentEncoding::Gzip))
}

let app = App::new()
.wrap(middleware::Compress::default())
.default_service(web::to(index_handler));
```

[feature flags]: ../index.html#crate-features"""

    def new_transform(self, service: S) -> Future: ...

class CompressMiddleware:

    def call(self, req: ServiceRequest) -> Future: ...

class MiddlewareFn:
    """Middleware transform for [`from_fn`]."""

    def new_transform(self, service: S) -> Future: ...

class MiddlewareFnService:
    """Middleware service for [`from_fn`]."""

    def call(self, req: ServiceRequest) -> Future: ...

class Next:
    """Wraps the "next" service in the middleware chain."""

    def call(self, req: ServiceRequest) -> Future: ...

    def call(self, req: ServiceRequest) -> Future: ...

class CustomizeResponder:
    """Allows overriding status code and headers (including cookies) for a [`Responder`].

Created by calling the [`customize`](Responder::customize) method on a [`Responder`] type."""

    def with_status(self, status: StatusCode) -> Self: ...

    def insert_header(self, header: object) -> Self: ...

    def append_header(self, header: object) -> Self: ...

    def with_header(self, header: object) -> Self: ...

    def add_cookie(self, cookie: Cookie) -> Self: ...

    def respond_to(self, req: HttpRequest) -> object: ...

class HttpResponseBuilder:
    """An HTTP response builder.

This type can be used to construct an instance of `Response` through a builder-like pattern."""

    @staticmethod
    def new(status: StatusCode) -> "HttpResponseBuilder": ...

    def status(self, status: StatusCode) -> Self: ...

    def insert_header(self, header: object) -> Self: ...

    def append_header(self, header: object) -> Self: ...

    def set_header(self, key: K, value: V) -> Self: ...

    def header(self, key: K, value: V) -> Self: ...

    def reason(self, reason: object) -> Self: ...

    def keep_alive(self) -> Self: ...

    def upgrade(self, value: V) -> Self: ...

    def force_close(self) -> Self: ...

    def no_chunking(self, len: int) -> Self: ...

    def content_type(self, value: V) -> Self: ...

    def cookie(self, cookie: Cookie) -> Self: ...

    def extensions(self) -> object: ...

    def extensions_mut(self) -> object: ...

    def body(self, body: B) -> object: ...

    def message_body(self, body: B) -> object: ...

    def streaming(self, stream: S) -> HttpResponse: ...

    def json(self, value: object) -> HttpResponse: ...

    def finish(self) -> HttpResponse: ...

    def take(self) -> Self: ...

    def poll(self, _: Context) -> object: ...

    def respond_to(self, _: HttpRequest) -> object: ...

class HttpResponse:
    """An outgoing response."""

    @staticmethod
    def from_(builder: HttpResponseBuilder) -> "HttpResponse": ...

    @staticmethod
    def new(status: StatusCode) -> "HttpResponse": ...

    @staticmethod
    def build(status: StatusCode) -> HttpResponseBuilder: ...

    @staticmethod
    def from_error(error: object) -> "HttpResponse": ...

    @staticmethod
    def with_body(status: StatusCode, body: B) -> "HttpResponse": ...

    def head(self) -> ResponseHead: ...

    def head_mut(self) -> ResponseHead: ...

    def error(self) -> object: ...

    def status(self) -> StatusCode: ...

    def status_mut(self) -> StatusCode: ...

    def headers(self) -> HeaderMap: ...

    def headers_mut(self) -> HeaderMap: ...

    def cookies(self) -> CookieIter: ...

    def add_cookie(self, cookie: Cookie) -> None: ...

    def add_removal_cookie(self, cookie: Cookie) -> None: ...

    def del_cookie(self, name: str) -> int: ...

    def upgrade(self) -> bool: ...

    def keep_alive(self) -> bool: ...

    def extensions(self) -> object: ...

    def extensions_mut(self) -> object: ...

    def body(self) -> B: ...

    def set_body(self, body: B2) -> object: ...

    def into_parts(self) -> object: ...

    def drop_body(self) -> object: ...

    def map_body(self, f: F) -> object: ...

    def map_into_left_body(self) -> object: ...

    def map_into_right_body(self) -> object: ...

    def map_into_boxed_body(self) -> object: ...

    def into_body(self) -> B: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(res: object) -> "HttpResponse": ...

    @staticmethod
    def from_(err: Exception) -> "HttpResponse": ...

    def poll(self, _: Context) -> object: ...

    def respond_to(self, _: HttpRequest) -> object: ...

    @staticmethod
    def from_(res: object) -> object: ...

class CookieIter:

    def next(self) -> Cookie | None: ...

class ServiceRequest:
    """A service level request wrapper.

Allows mutable access to request's internal structures."""

    def into_parts(self) -> object: ...

    def parts_mut(self) -> object: ...

    def parts(self) -> object: ...

    def request(self) -> HttpRequest: ...

    def extract(self) -> Future: ...

    @staticmethod
    def from_parts(req: HttpRequest, payload: Payload) -> "ServiceRequest": ...

    @staticmethod
    def from_request(req: HttpRequest) -> "ServiceRequest": ...

    def into_response(self, res: R) -> object: ...

    def error_response(self, err: E) -> ServiceResponse: ...

    def head(self) -> RequestHead: ...

    def head_mut(self) -> RequestHead: ...

    def uri(self) -> Uri: ...

    def method(self) -> Method: ...

    def version(self) -> Version: ...

    def headers(self) -> HeaderMap: ...

    def headers_mut(self) -> HeaderMap: ...

    def path(self) -> str: ...

    def query_string(self) -> str: ...

    def peer_addr(self) -> SocketAddr | None: ...

    def connection_info(self) -> object: ...

    def match_info(self) -> object: ...

    def match_info_mut(self) -> object: ...

    def match_name(self) -> object: ...

    def match_pattern(self) -> str | None: ...

    def resource_map(self) -> ResourceMap: ...

    def app_config(self) -> AppConfig: ...

    def app_data(self) -> object: ...

    def conn_data(self) -> object: ...

    def cookies(self) -> object: ...

    def cookie(self, name: str) -> Cookie | None: ...

    def set_payload(self, payload: Payload) -> None: ...

    def add_data_container(self, extensions: object) -> None: ...

    def guard_ctx(self) -> GuardContext: ...

    def resource_path(self) -> object: ...

    def headers(self) -> HeaderMap: ...

    def extensions(self) -> object: ...

    def extensions_mut(self) -> object: ...

    def take_payload(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class ServiceResponse:
    """A service level response wrapper."""

    def map_body(self) -> object: ...

    @staticmethod
    def from_err(err: E, request: HttpRequest) -> "ServiceResponse": ...

    @staticmethod
    def new(request: HttpRequest, response: object) -> "ServiceResponse": ...

    def error_response(self, err: E) -> ServiceResponse: ...

    def into_response(self, response: object) -> object: ...

    def request(self) -> HttpRequest: ...

    def response(self) -> object: ...

    def response_mut(self) -> object: ...

    def status(self) -> StatusCode: ...

    def headers(self) -> HeaderMap: ...

    def headers_mut(self) -> HeaderMap: ...

    def into_parts(self) -> object: ...

    def map_body(self, f: F) -> object: ...

    def map_into_left_body(self) -> object: ...

    def map_into_right_body(self) -> object: ...

    def map_into_boxed_body(self) -> object: ...

    def into_body(self) -> B: ...

    def fmt(self, f: Formatter) -> Result: ...

class WebService:

    @staticmethod
    def new(path: T) -> "WebService": ...

    def name(self, name: str) -> Self: ...

    def guard(self, guard: G) -> Self: ...

    def finish(self, service: F) -> object: ...

class Json:
    """JSON extractor and responder.

`Json` has two uses: JSON responses, and extracting typed data from JSON request payloads.

# Extractor
To extract typed data from a request body, the inner type `T` must implement the
[`serde::Deserialize`] trait.

Use [`JsonConfig`] to configure extraction options.

```
use actix_web::{post, web, App};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
username: String,
}

/// deserialize `Info` from request's body
#[post("/")]
async fn index(info: web::Json<Info>) -> String {
format!("Welcome {}!", info.username)
}
```

# Responder
The `Json` type  JSON formatted responses. A handler may return a value of type
`Json<T>` where `T` is the type of a structure to serialize into JSON. The type `T` must
implement [`serde::Serialize`].

```
use actix_web::{post, web, HttpRequest};
use serde::Serialize;

#[derive(Serialize)]
struct Info {
name: String,
}

#[post("/{name}")]
async fn index(req: HttpRequest) -> web::Json<Info> {
web::Json(Info {
name: req.match_info().get("name").unwrap().to_owned(),
})
}
```"""

    def into_inner(self) -> T: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    def serialize(self, serializer: S) -> Ok: ...

    def respond_to(self, _: HttpRequest) -> object: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

class JsonExtractFut:

    def poll(self, cx: Context) -> object: ...

class JsonConfig:
    """`Json` extractor configuration.

# Examples
```
use actix_web::{error, post, web, App, FromRequest, HttpResponse};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
name: String,
}

// `Json` extraction is bound by custom `JsonConfig` applied to App.
#[post("/")]
async fn index(info: web::Json<Info>) -> String {
format!("Welcome {}!", info.name)
}

// custom `Json` extractor configuration
let json_cfg = web::JsonConfig::default()
// limit request payload size
.limit(4096)
// only accept text/plain content type
.content_type(|mime| mime == mime::TEXT_PLAIN)
// use custom error handler
.error_handler(|err, req| {
error::InternalError::from_response(err, HttpResponse::Conflict().into()).into()
});

App::new()
.app_data(json_cfg)
.service(index);
```"""

    def limit(self, limit: int) -> Self: ...

    def error_handler(self, f: F) -> Self: ...

    def content_type(self, predicate: F) -> Self: ...

    def content_type_required(self, content_type_required: bool) -> Self: ...

    @staticmethod
    def default() -> "JsonConfig": ...

class Path:
    """Extract typed data from request path segments.

Use [`PathConfig`] to configure extraction option.

Unlike, [`HttpRequest::match_info`], this extractor will fully percent-decode dynamic segments,
including `/`, `%`, and `+`.

# Examples
```
use actix_web::{get, web};

// extract path info from "/{name}/{count}/index.html" into tuple
// {name}  - deserialize a String
// {count} - deserialize a u32
#[get("/{name}/{count}/index.html")]
async fn index(path: web::Path<(String, u32)>) -> String {
let (name, count) = path.into_inner();
format!("Welcome {}! {}", name, count)
}
```

Path segments also can be deserialized into any type that implements [`serde::Deserialize`].
Path segment labels will be matched with struct field names.

```
use actix_web::{get, web};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
name: String,
}

// extract `Info` from a path using serde
#[get("/{name}")]
async fn index(info: web::Path<Info>) -> String {
format!("Welcome {}!", info.name)
}
```"""

    def into_inner(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class PathConfig:
    """Path extractor configuration

```
use actix_web::web::PathConfig;
use actix_web::{error, web, App, FromRequest, HttpResponse};
use serde::Deserialize;

#[derive(Deserialize, Debug)]
enum Folder {
#[serde(rename = "inbox")]
Inbox,

#[serde(rename = "outbox")]
Outbox,
}

// deserialize `Info` from request's path
async fn index(folder: web::Path<Folder>) -> String {
format!("Selected folder: {:?}!", folder)
}

let app = App::new().service(
web::resource("/messages/{folder}")
.app_data(PathConfig::default().error_handler(|err, req| {
error::InternalError::from_response(
err,
HttpResponse::Conflict().into(),
)
.into()
}))
.route(web::post().to(index)),
);
```"""

    def error_handler(self, f: F) -> Self: ...

class Html:
    """Semantic HTML responder.

When used as a responder, creates a 200 OK response, sets the correct HTML content type, and
uses the string passed to [`Html::new()`] as the body.

```
# use actix_web::web::Html;
Html::new("<p>Hello, World!</p>")
# ;
```"""

    @staticmethod
    def new(html: object) -> "Html": ...

    def respond_to(self, _req: HttpRequest) -> object: ...

class Form:
    """URL encoded payload extractor and responder.

`Form` has two uses: URL encoded responses, and extracting typed data from URL request payloads.

# Extractor
To extract typed data from a request body, the inner type `T` must implement the
[`DeserializeOwned`] trait.

Use [`FormConfig`] to configure extraction options.

## Examples
```
use actix_web::{post, web};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
name: String,
}

// This handler is only called if:
// - request headers declare the content type as `application/x-www-form-urlencoded`
// - request payload deserializes into an `Info` struct from the URL encoded format
#[post("/")]
async fn index(web::Form(form): web::Form<Info>) -> String {
format!("Welcome {}!", form.name)
}
```

# Responder
The `Form` type also allows you to create URL encoded responses by returning a value of type
`Form<T>` where `T` is the type to be URL encoded, as long as `T` implements [`Serialize`].

## Examples
```
use actix_web::{get, web};
use serde::Serialize;

#[derive(Serialize)]
struct SomeForm {
name: String,
age: u8
}

// Response will have:
// - status: 200 OK
// - header: `Content-Type: application/x-www-form-urlencoded`
// - body: `name=actix&age=123`
#[get("/")]
async fn index() -> web::Form<SomeForm> {
web::Form(SomeForm {
name: "actix".to_owned(),
age: 123
})
}
```

# Panics
URL encoded forms consist of unordered `key=value` pairs, therefore they cannot be decoded into
any type which depends upon data ordering (eg. tuples). Trying to do so will result in a panic."""

    def into_inner(self) -> T: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def serialize(self, serializer: S) -> Ok: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

    def fmt(self, f: Formatter) -> Result: ...

    def respond_to(self, _: HttpRequest) -> object: ...

class FormExtractFut:

    def poll(self, cx: Context) -> object: ...

class FormConfig:
    """[`Form`] extractor configuration.

```
use actix_web::{post, web, App, FromRequest, Result};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
username: String,
}

// Custom `FormConfig` is applied to App.
// Max payload size for URL encoded forms is set to 4kB.
#[post("/")]
async fn index(form: web::Form<Info>) -> Result<String> {
Ok(format!("Welcome {}!", form.username))
}

App::new()
.app_data(web::FormConfig::default().limit(4096))
.service(index);
```"""

    def limit(self, limit: int) -> Self: ...

    def error_handler(self, f: F) -> Self: ...

    @staticmethod
    def default() -> "FormConfig": ...

class UrlEncoded:
    """Future that resolves to some `T` when parsed from a URL encoded payload.

Form can be deserialized from any type `T` that implements [`serde::Deserialize`].

Returns error if:
- content type is not `application/x-www-form-urlencoded`
- content length is greater than [limit](UrlEncoded::limit())"""

    @staticmethod
    def new(req: HttpRequest, payload: Payload) -> "UrlEncoded": ...

    def limit(self, limit: int) -> Self: ...

    def poll(self, cx: Context) -> object: ...

class Payload:
    """Extract a request's raw payload stream.

See [`PayloadConfig`] for important notes when using this advanced extractor.

# Examples
```
use std::future::Future;
use futures_util::StreamExt as _;
use actix_web::{post, web};

// `body: web::Payload` parameter extracts raw payload stream from request
#[post("/")]
async fn index(mut body: web::Payload) -> actix_web::Result<String> {
// for demonstration only; in a normal case use the `Bytes` extractor
// collect payload stream into a bytes object
let mut bytes = web::BytesMut::new();
while let Some(item) = body.next().await {
bytes.extend_from_slice(&item?);
}

Ok(format!("Request Body Bytes:\\n{:?}", bytes))
}
```"""

    def into_inner(self) -> Payload: ...

    def to_bytes_limited(self, limit: int) -> Bytes: ...

    def to_bytes(self) -> Bytes: ...

    def poll_next(self, cx: Context) -> object: ...

    @staticmethod
    def from_request(_: HttpRequest, payload: Payload) -> Future: ...

class BytesExtractFut:
    """Future for `Bytes` extractor."""

    def poll(self, cx: Context) -> object: ...

class StringExtractFut:
    """Future for `String` extractor."""

    def poll(self, cx: Context) -> object: ...

class PayloadConfig:
    """Configuration for request payloads.

Applies to the built-in [`Bytes`] and [`String`] extractors.
Note that the [`Payload`] extractor does not automatically check
conformance with this configuration to allow more flexibility when
building extractors on top of [`Payload`].

By default, the payload size limit is 256kB and there is no mime type condition.

To use this, add an instance of it to your [`app`](crate::App), [`scope`](crate::Scope)
or [`resource`](crate::Resource) through the associated `.app_data()` method."""

    @staticmethod
    def new(limit: int) -> "PayloadConfig": ...

    def limit(self, limit: int) -> Self: ...

    def mimetype(self, mt: Mime) -> Self: ...

    @staticmethod
    def default() -> "PayloadConfig": ...

class HttpMessageBody:
    """Future that resolves to a complete HTTP body payload.

By default only 256kB payload is accepted before `PayloadError::Overflow` is returned.
Use `MessageBody::limit()` method to change upper limit."""

    @staticmethod
    def new(req: HttpRequest, payload: Payload) -> "HttpMessageBody": ...

    def limit(self, limit: int) -> Self: ...

    def poll(self, cx: Context) -> object: ...

class Header:
    """Extract typed headers from the request.

To extract a header, the inner type `T` must implement the
[`Header`](crate::http::header::Header) trait.

# Examples
```
use actix_web::{get, web, http::header};

#[get("/")]
async fn index(date: web::Header<header::Date>) -> String {
format!("Request was sent at {}", date.to_string())
}
```"""

    def into_inner(self) -> T: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class Readlines:
    """Stream that reads request line by line."""

    @staticmethod
    def new(req: T) -> "Readlines": ...

    def limit(self, limit: int) -> Self: ...

    def poll_next(self, cx: Context) -> object: ...

class Query:
    """Extract typed information from the request's query.

To extract typed data from the URL query string, the inner type `T` must implement the
[`DeserializeOwned`] trait.

Use [`QueryConfig`] to configure extraction process.

# Panics
A query string consists of unordered `key=value` pairs, therefore it cannot be decoded into any
type which depends upon data ordering (eg. tuples). Trying to do so will result in a panic.

# Examples
```
use actix_web::{get, web};
use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub enum ResponseType {
Token,
Code
}

#[derive(Debug, Deserialize)]
pub struct AuthRequest {
id: u64,
response_type: ResponseType,
}

// Deserialize `AuthRequest` struct from query string.
// This handler gets called only if the request's query parameters contain both fields.
// A valid request path for this handler would be `/?id=64&response_type=Code"`.
#[get("/")]
async fn index(info: web::Query<AuthRequest>) -> String {
format!("Authorization request for id={} and type={:?}!", info.id, info.response_type)
}

// To access the entire underlying query struct, use `.into_inner()`.
#[get("/debug1")]
async fn debug1(info: web::Query<AuthRequest>) -> String {
dbg!("Authorization object = {:?}", info.into_inner());
"OK".to_string()
}

// Or use destructuring, which is equivalent to `.into_inner()`.
#[get("/debug2")]
async fn debug2(web::Query(info): web::Query<AuthRequest>) -> String {
dbg!("Authorization object = {:?}", info);
"OK".to_string()
}
```"""

    def into_inner(self) -> T: ...

    @staticmethod
    def from_query(query_str: str) -> object: ...

    def deref(self) -> T: ...

    def deref_mut(self) -> T: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class QueryConfig:
    """Query extractor configuration.

# Examples
```
use actix_web::{error, get, web, App, FromRequest, HttpResponse};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
username: String,
}

/// deserialize `Info` from request's querystring
#[get("/")]
async fn index(info: web::Query<Info>) -> String {
format!("Welcome {}!", info.username)
}

// custom `Query` extractor configuration
let query_cfg = web::QueryConfig::default()
// use custom error handler
.error_handler(|err, req| {
error::InternalError::from_response(err, HttpResponse::Conflict().finish()).into()
});

App::new()
.app_data(query_cfg)
.service(index);
```"""

    def error_handler(self, f: F) -> Self: ...

class ContentRangeSpec:
    """Content-Range header, defined
in [RFC 7233 §4.2](https://datatracker.ietf.org/doc/html/rfc7233#section-4.2)

# ABNF
```plain
Content-Range       = byte-content-range
/ other-content-range

byte-content-range  = bytes-unit SP
( byte-range-resp / unsatisfied-range )

byte-range-resp     = byte-range "/" ( complete-length / "*" )
byte-range          = first-byte-pos "-" last-byte-pos
unsatisfied-range   = "*/" complete-length

complete-length     = 1*DIGIT

other-content-range = other-range-unit SP other-range-resp
other-range-resp    = *CHAR
```"""
    Bytes: "ContentRangeSpec"
    Unregistered: "ContentRangeSpec"

    @staticmethod
    def from_str(s: str) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def try_into_value(self) -> HeaderValue: ...

class Range:
    """`Range` header, defined
in [RFC 7233 §3.1](https://datatracker.ietf.org/doc/html/rfc7233#section-3.1)

The "Range" header field on a GET request modifies the method semantics to request transfer of
only one or more sub-ranges of the selected representation data, rather than the entire selected
representation data.

# ABNF
```plain
Range = byte-ranges-specifier / other-ranges-specifier
other-ranges-specifier = other-range-unit "=" other-range-set
other-range-set = 1*VCHAR

bytes-unit = "bytes"

byte-ranges-specifier = bytes-unit "=" byte-range-set
byte-range-set = 1#(byte-range-spec / suffix-byte-range-spec)
byte-range-spec = first-byte-pos "-" [last-byte-pos]
suffix-byte-range-spec = "-" suffix-length
suffix-length = 1*DIGIT
first-byte-pos = 1*DIGIT
last-byte-pos = 1*DIGIT
```

# Example Values
* `bytes=1000-`
* `bytes=-50`
* `bytes=0-1,30-40`
* `bytes=0-10,20-90,-100`
* `custom_unit=0-123`
* `custom_unit=xxx-yyy`

# Examples
```
use actix_web::http::header::{Range, ByteRangeSpec};
use actix_web::HttpResponse;

let mut builder = HttpResponse::Ok();
builder.insert_header(Range::Bytes(
vec![ByteRangeSpec::FromTo(1, 100), ByteRangeSpec::From(200)]
));
builder.insert_header(Range::Unregistered("letters".to_owned(), "a-f".to_owned()));
builder.insert_header(Range::bytes(1, 100));
builder.insert_header(Range::bytes_multi(vec![(1, 100), (200, 300)]));
```"""
    Bytes: "Range"
    Unregistered: "Range"

    @staticmethod
    def bytes(from_: int, to: int) -> "Range": ...

    @staticmethod
    def bytes_multi(ranges: list[object]) -> "Range": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> "Range": ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: T) -> object: ...

    def try_into_value(self) -> HeaderValue: ...

class ByteRangeSpec:
    """A range of bytes to fetch.

Each [`Range::Bytes`] header can contain one or more `ByteRangeSpec`s."""
    FromTo: "ByteRangeSpec"
    From: "ByteRangeSpec"
    Last: "ByteRangeSpec"

    def to_satisfiable_range(self, full_length: int) -> object | None: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> "ByteRangeSpec": ...

class AnyOrSome:
    """A wrapper for types used in header values where wildcard (`*`) items are allowed but the
underlying type does not support them.

For example, we use the `language-tags` crate for the [`AcceptLanguage`](super::AcceptLanguage)
typed header but it does parse `*` successfully. On the other hand, the `mime` crate, used for
[`Accept`](super::Accept), has first-party support for wildcard items so this wrapper is not
used in those header types."""
    Any: "AnyOrSome"
    Item: "AnyOrSome"

    def is_any(self) -> bool: ...

    def is_item(self) -> bool: ...

    def item(self) -> object: ...

    def into_item(self) -> T | None: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

class Preference:
    """A wrapper for types used in header values where wildcard (`*`) items are allowed but the
underlying type does not support them.

For example, we use the `language-tags` crate for the [`AcceptLanguage`](super::AcceptLanguage)
typed header but it does not parse `*` successfully. On the other hand, the `mime` crate, used
for [`Accept`](super::Accept), has first-party support for wildcard items so this wrapper is not
used in those header types."""
    Any: "Preference"
    Specific: "Preference"

    def is_any(self) -> bool: ...

    def is_specific(self) -> bool: ...

    def item(self) -> object: ...

    def into_item(self) -> T | None: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

class Encoding:
    """A value to represent an encoding used in the `Accept-Encoding` and `Content-Encoding` header."""
    Known: "Encoding"
    Unknown: "Encoding"

    @staticmethod
    def identity() -> "Encoding": ...

    @staticmethod
    def brotli() -> "Encoding": ...

    @staticmethod
    def deflate() -> "Encoding": ...

    @staticmethod
    def gzip() -> "Encoding": ...

    @staticmethod
    def zstd() -> "Encoding": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(enc: str) -> object: ...

class IfRange:
    """`If-Range` header, defined
in [RFC 7233 §3.2](https://datatracker.ietf.org/doc/html/rfc7233#section-3.2)

If a client has a partial copy of a representation and wishes to have
an up-to-date copy of the entire representation, it could use the
Range header field with a conditional GET (using either or both of
If-Unmodified-Since and If-Match.)  However, if the precondition
fails because the representation has been modified, the client would
then have to make a second request to obtain the entire current
representation.

The `If-Range` header field allows a client to \\"short-circuit\\" the
second request.  Informally, its meaning is as follows: if the
representation is unchanged, send me the part(s) that I am requesting
in Range; otherwise, send me the entire representation.

# ABNF
```plain
If-Range = entity-tag / HTTP-date
```

# Example Values

* `Sat, 29 Oct 1994 19:43:31 GMT`
* `\\"xyzzy\\"`

# Examples
```
use actix_web::HttpResponse;
use actix_web::http::header::{EntityTag, IfRange};

let mut builder = HttpResponse::Ok();
builder.insert_header(
IfRange::EntityTag(
EntityTag::new(false, "abc".to_owned())
)
);
```

```
use std::time::{Duration, SystemTime};
use actix_web::{http::header::IfRange, HttpResponse};

let mut builder = HttpResponse::Ok();
let fetched = SystemTime::now() - Duration::from_secs(60 * 60 * 24);
builder.insert_header(
IfRange::Date(fetched.into())
);
```"""
    EntityTag: "IfRange"
    Date: "IfRange"

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: T) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def try_into_value(self) -> HeaderValue: ...

class CacheDirective:
    """`CacheControl` contains a list of these directives."""
    NoCache: "CacheDirective"
    NoStore: "CacheDirective"
    NoTransform: "CacheDirective"
    OnlyIfCached: "CacheDirective"
    MaxAge: "CacheDirective"
    MaxStale: "CacheDirective"
    MinFresh: "CacheDirective"
    MustRevalidate: "CacheDirective"
    Public: "CacheDirective"
    Private: "CacheDirective"
    ProxyRevalidate: "CacheDirective"
    SMaxAge: "CacheDirective"
    Extension: "CacheDirective"

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(s: str) -> object: ...

class DispositionType:
    """The implied disposition of the content of the HTTP body."""
    Inline: "DispositionType"
    Attachment: "DispositionType"
    FormData: "DispositionType"
    Ext: "DispositionType"

    @staticmethod
    def from_(origin: object) -> "DispositionType": ...

    def fmt(self, f: Formatter) -> Result: ...

class DispositionParam:
    """Parameter in [`ContentDisposition`].

# Examples
```
use actix_web::http::header::DispositionParam;

let param = DispositionParam::Filename(String::from("sample.txt"));
assert!(param.is_filename());
assert_eq!(param.as_filename().unwrap(), "sample.txt");
```"""
    Name: "DispositionParam"
    Filename: "DispositionParam"
    FilenameExt: "DispositionParam"
    Unknown: "DispositionParam"
    UnknownExt: "DispositionParam"

    def is_name(self) -> bool: ...

    def is_filename(self) -> bool: ...

    def is_filename_ext(self) -> bool: ...

    def is_unknown(self, name: T) -> bool: ...

    def is_unknown_ext(self, name: T) -> bool: ...

    def as_name(self) -> object: ...

    def as_filename(self) -> object: ...

    def as_filename_ext(self) -> object: ...

    def as_unknown(self, name: T) -> object: ...

    def as_unknown_ext(self, name: T) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class UrlGenerationError:
    """Errors which can occur when attempting to generate resource uri."""
    ResourceNotFound: "UrlGenerationError"
    NotEnoughElements: "UrlGenerationError"
    ParseError: "UrlGenerationError"

class UrlencodedError:
    """A set of errors that can occur during parsing urlencoded payloads"""
    Chunked: "UrlencodedError"
    Overflow: "UrlencodedError"
    UnknownLength: "UrlencodedError"
    ContentType: "UrlencodedError"
    Parse: "UrlencodedError"
    Encoding: "UrlencodedError"
    Serialize: "UrlencodedError"
    Payload: "UrlencodedError"

    def status_code(self) -> StatusCode: ...

class JsonPayloadError:
    """A set of errors that can occur during parsing json payloads"""
    OverflowKnownLength: "JsonPayloadError"
    Overflow: "JsonPayloadError"
    ContentType: "JsonPayloadError"
    Deserialize: "JsonPayloadError"
    Serialize: "JsonPayloadError"
    Payload: "JsonPayloadError"

    @staticmethod
    def from_(err: PayloadError) -> "JsonPayloadError": ...

    def status_code(self) -> StatusCode: ...

class PathError:
    """A set of errors that can occur during parsing request paths"""
    Deserialize: "PathError"

    def status_code(self) -> StatusCode: ...

class QueryPayloadError:
    """A set of errors that can occur during parsing query strings."""
    Deserialize: "QueryPayloadError"

    def status_code(self) -> StatusCode: ...

class ReadlinesError:
    """Error type returned when reading body as lines."""
    EncodingError: "ReadlinesError"
    Payload: "ReadlinesError"
    LimitOverflow: "ReadlinesError"
    ContentTypeError: "ReadlinesError"

    def status_code(self) -> StatusCode: ...

class ErrorHandlerResponse:
    """Return type for [`ErrorHandlers`] custom handlers."""
    Response: "ErrorHandlerResponse"
    Future: "ErrorHandlerResponse"

class TrailingSlash:
    """Determines the behavior of the [`NormalizePath`] middleware.

The default is `TrailingSlash::Trim`."""
    Trim: "TrailingSlash"
    MergeOnly: "TrailingSlash"
    Always: "TrailingSlash"

class ConditionMiddleware:
    Enable: "ConditionMiddleware"
    Disable: "ConditionMiddleware"

    def poll_ready(self, cx: Context) -> object: ...

    def call(self, req: Req) -> Future: ...

class JsonBody:
    """Future that resolves to some `T` when parsed from a JSON payload.

Can deserialize any type `T` that implements [`Deserialize`][serde::Deserialize].

Returns error if:
- `Content-Type` is not `application/json` when `ctype_required` (passed to [`new`][Self::new])
is `true`.
- `Content-Length` is greater than [limit](JsonBody::limit()).
- The payload, when consumed, is not valid JSON."""
    Error: "JsonBody"
    Body: "JsonBody"

    @staticmethod
    def new(req: HttpRequest, payload: Payload, ctype_fn: object, ctype_required: bool) -> "JsonBody": ...

    def limit(self, limit: int) -> Self: ...

    def poll(self, cx: Context) -> object: ...

class Either:
    """Combines two extractor or responder types into a single type.

# Extractor
Provides a mechanism for trying two extractors, a primary and a fallback. Useful for
"polymorphic payloads" where, for example, a form might be JSON or URL encoded.

It is important to note that this extractor, by necessity, buffers the entire request payload
as part of its implementation. Though, it does respect any `PayloadConfig` maximum size limits.

```
use actix_web::{post, web, Either};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
name: String,
}

// handler that accepts form as JSON or form-urlencoded.
#[post("/")]
async fn index(form: Either<web::Json<Info>, web::Form<Info>>) -> String {
let name: String = match form {
Either::Left(json) => json.name.to_owned(),
Either::Right(form) => form.name.to_owned(),
};

format!("Welcome {}!", name)
}
```

# Responder
It may be desirable to use a concrete type for a response with multiple branches. As long as
both types implement `Responder`, so will the `Either` type, enabling it to be used as a
handler's return type.

All properties of a response are determined by the Responder branch returned.

```
use actix_web::{get, Either, Error, HttpResponse};

#[get("/")]
async fn index() -> Either<&'static str, Result<HttpResponse, Error>> {
if 1 == 2 {
// respond with Left variant
Either::Left("Bad data")
} else {
// respond with Right variant
Either::Right(
Ok(HttpResponse::Ok()
.content_type(mime::TEXT_HTML)
.body("<p>Hello!</p>"))
)
}
}
```"""
    Left: "Either"
    Right: "Either"

    def into_inner(self) -> T: ...

    def into_inner(self) -> T: ...

    def respond_to(self, req: HttpRequest) -> object: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

class EitherExtractError:
    """A composite error resulting from failure to extract an `Either<L, R>`.

The implementation of `Into<actix_web::Error>` will return the payload buffering error or the
error from the primary extractor. To access the fallback error, use a match clause."""
    Bytes: "EitherExtractError"
    Extract: "EitherExtractError"

"""Initialize service from application builder instance.

# Examples
```
use actix_service::Service;
use actix_web::{test, web, App, HttpResponse, http::StatusCode};

#[actix_web::test]
async fn test_init_service() {
let app = test::init_service(
App::new()
.service(web::resource("/test").to(|| async { "OK" }))
).await;

// Create request object
let req = test::TestRequest::with_uri("/test").to_request();

// Execute application
let res = app.call(req).await.unwrap();
assert_eq!(res.status(), StatusCode::OK);
}
```

# Panics
Panics if service initialization returns an error."""
async def init_service(app: R) -> object: ...

"""Calls service and waits for response future completion.

# Examples
```
use actix_web::{test, web, App, HttpResponse, http::StatusCode};

#[actix_web::test]
async fn test_response() {
let app = test::init_service(
App::new()
.service(web::resource("/test").to(|| async {
HttpResponse::Ok()
}))
).await;

// Create request object
let req = test::TestRequest::with_uri("/test").to_request();

// Call application
let res = test::call_service(&app, req).await;
assert_eq!(res.status(), StatusCode::OK);
}
```

# Panics
Panics if service call returns error. To handle errors use `app.call(req)`."""
async def call_service(app: S, req: R) -> Response: ...

"""Fallible version of [`call_service`] that allows testing response completion errors."""
async def try_call_service(app: S, req: R) -> Response: ...

"""Helper function that returns a response body of a TestRequest

# Examples
```
use actix_web::{test, web, App, HttpResponse, http::header};
use bytes::Bytes;

#[actix_web::test]
async fn test_index() {
let app = test::init_service(
App::new().service(
web::resource("/index.html")
.route(web::post().to(|| async {
HttpResponse::Ok().body("welcome!")
})))
).await;

let req = test::TestRequest::post()
.uri("/index.html")
.header(header::CONTENT_TYPE, "application/json")
.to_request();

let result = test::call_and_read_body(&app, req).await;
assert_eq!(result, Bytes::from_static(b"welcome!"));
}
```

# Panics
Panics if:
- service call returns error;
- body yields an error while it is being read."""
async def call_and_read_body(app: S, req: Request) -> Bytes: ...

async def read_response(app: S, req: Request) -> Bytes: ...

"""Helper function that returns a response body of a ServiceResponse.

# Examples
```
use actix_web::{test, web, App, HttpResponse, http::header};
use bytes::Bytes;

#[actix_web::test]
async fn test_index() {
let app = test::init_service(
App::new().service(
web::resource("/index.html")
.route(web::post().to(|| async {
HttpResponse::Ok().body("welcome!")
})))
).await;

let req = test::TestRequest::post()
.uri("/index.html")
.header(header::CONTENT_TYPE, "application/json")
.to_request();

let res = test::call_service(&app, req).await;
let result = test::read_body(res).await;
assert_eq!(result, Bytes::from_static(b"welcome!"));
}
```

# Panics
Panics if body yields an error while it is being read."""
async def read_body(res: object) -> Bytes: ...

"""Fallible version of [`read_body`] that allows testing MessageBody reading errors."""
async def try_read_body(res: object) -> Bytes: ...

"""Helper function that returns a deserialized response body of a ServiceResponse.

# Examples
```
use actix_web::{App, test, web, HttpResponse, http::header};
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct Person {
id: String,
name: String,
}

#[actix_web::test]
async fn test_post_person() {
let app = test::init_service(
App::new().service(
web::resource("/people")
.route(web::post().to(|person: web::Json<Person>| async {
HttpResponse::Ok()
.json(person)})
))
).await;

let payload = r#"{"id":"12345","name":"User name"}"#.as_bytes();

let res = test::TestRequest::post()
.uri("/people")
.header(header::CONTENT_TYPE, "application/json")
.set_payload(payload)
.send_request(&mut app)
.await;

assert!(res.status().is_success());

let result: Person = test::read_body_json(res).await;
}
```

# Panics
Panics if:
- body yields an error while it is being read;
- received body is not a valid JSON representation of `T`."""
async def read_body_json(res: object) -> T: ...

"""Fallible version of [`read_body_json`] that allows testing response deserialization errors."""
async def try_read_body_json(res: object) -> T: ...

"""Helper function that returns a deserialized response body of a TestRequest

# Examples
```
use actix_web::{App, test, web, HttpResponse, http::header};
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct Person {
id: String,
name: String
}

#[actix_web::test]
async fn test_add_person() {
let app = test::init_service(
App::new().service(
web::resource("/people")
.route(web::post().to(|person: web::Json<Person>| async {
HttpResponse::Ok()
.json(person)})
))
).await;

let payload = r#"{"id":"12345","name":"User name"}"#.as_bytes();

let req = test::TestRequest::post()
.uri("/people")
.header(header::CONTENT_TYPE, "application/json")
.set_payload(payload)
.to_request();

let result: Person = test::call_and_read_body_json(&mut app, req).await;
}
```

# Panics
Panics if:
- service call returns an error body yields an error while it is being read;
- body yields an error while it is being read;
- received body is not a valid JSON representation of `T`."""
async def call_and_read_body_json(app: S, req: Request) -> T: ...

"""Fallible version of [`call_and_read_body_json`] that allows testing service call errors."""
async def try_call_and_read_body_json(app: S, req: Request) -> T: ...

async def read_response_json(app: S, req: Request) -> T: ...

"""Creates service that always responds with `200 OK` and no body."""
def ok_service() -> object: ...

"""Creates service that always responds with given status code and no body."""
def status_service(status_code: StatusCode) -> object: ...

def simple_service(status_code: StatusCode) -> object: ...

def default_service(status_code: StatusCode) -> object: ...

"""Creates a guard that matches requests targeting a specific host.

# Matching Host
This guard will:
- match against the `Host` header, if present;
- fall-back to matching against the request target's host, if present;
- return false if host cannot be determined;

# Matching Scheme
Optionally, this guard can match against the host's scheme. Set the scheme for matching using
`Host(host).scheme(protocol)`. If the request's scheme cannot be determined, it will not prevent
the guard from matching successfully.

# Examples
The `Host` guard can be used to set up a form of [virtual hosting] within a single app.
Overlapping scope prefixes are usually discouraged, but when combined with non-overlapping guard
definitions they become safe to use in this way. Without these host guards, only routes under
the first-to-be-defined scope would be accessible. You can test this locally using `127.0.0.1`
and `localhost` as the `Host` guards.
```
use actix_web::{web, http::Method, guard, App, HttpResponse};

App::new()
.service(
web::scope("")
.guard(guard::Host("www.rust-lang.org"))
.default_service(web::to(|| async {
HttpResponse::Ok().body("marketing site")
})),
)
.service(
web::scope("")
.guard(guard::Host("play.rust-lang.org"))
.default_service(web::to(|| async {
HttpResponse::Ok().body("playground frontend")
})),
);
```

The example below additionally guards on the host URI's scheme. This could allow routing to
different handlers for `http:` vs `https:` visitors; to redirect, for example.
```
use actix_web::{web, guard::Host, HttpResponse};

web::scope("/admin")
.guard(Host("admin.rust-lang.org").scheme("https"))
.default_service(web::to(|| async {
HttpResponse::Ok().body("admin connection is secure")
}));
```

[virtual hosting]: https://en.wikipedia.org/wiki/Virtual_hosting"""
def Host(host: object) -> HostGuard: ...

"""Creates a guard using the given function.

# Examples
```
use actix_web::{guard, web, HttpResponse};

web::route()
.guard(guard::fn_guard(|ctx| {
ctx.head().headers().contains_key("content-type")
}))
.to(|| HttpResponse::Ok());
```"""
def fn_guard(f: F) -> object: ...

"""Creates a guard that matches if any added guards match.

# Examples
The handler below will be called for either request method `GET` or `POST`.
```
use actix_web::{web, guard, HttpResponse};

web::route()
.guard(
guard::Any(guard::Get())
.or(guard::Post()))
.to(|| HttpResponse::Ok());
```"""
def Any(guard: F) -> AnyGuard: ...

"""Creates a guard that matches if all added guards match.

# Examples
The handler below will only be called if the request method is `GET` **and** the specified
header name and value match exactly.
```
use actix_web::{guard, web, HttpResponse};

web::route()
.guard(
guard::All(guard::Get())
.and(guard::Header("accept", "text/plain"))
)
.to(|| HttpResponse::Ok());
```"""
def All(guard: F) -> AllGuard: ...

"""Creates a guard that matches a specified HTTP method."""
def Method(method: HttpMethod) -> object: ...

"""Creates a guard that matches if request contains given header name and value.

# Examples
The handler below will be called when the request contains an `x-guarded` header with value
equal to `secret`.
```
use actix_web::{guard, web, HttpResponse};

web::route()
.guard(guard::Header("x-guarded", "secret"))
.to(|| HttpResponse::Ok());
```"""
def Header(name: object, value: object) -> object: ...

"""compile-only test for returning app type from function"""
def my_app() -> object: ...

def gzip_decode(bytes: object) -> list[int]: ...

"""Wraps an async function to be used as a middleware.

# Examples

The wrapped function should have the following form:

```
# use actix_web::{
#     App, Error,
#     body::MessageBody,
#     dev::{ServiceRequest, ServiceResponse, Service as _},
# };
use actix_web::middleware::{self, Next};

async fn my_mw(
req: ServiceRequest,
next: Next<impl MessageBody>,
) -> Result<ServiceResponse<impl MessageBody>, Error> {
// pre-processing
next.call(req).await
// post-processing
}
# App::new().wrap(middleware::from_fn(my_mw));
```

Then use in an app builder like this:

```
use actix_web::{
App, Error,
dev::{ServiceRequest, ServiceResponse, Service as _},
};
use actix_web::middleware::from_fn;
# use actix_web::middleware::Next;
# async fn my_mw<B>(req: ServiceRequest, next: Next<B>) -> Result<ServiceResponse<B>, Error> {
#     next.call(req).await
# }

App::new()
.wrap(from_fn(my_mw))
# ;
```

It is also possible to write a middleware that automatically uses extractors, similar to request
handlers, by declaring them as the first parameters. As usual, **take care with extractors that
consume the body stream**, since handlers will no longer be able to read it again without
putting the body "back" into the request object within your middleware.

```
# use std::collections::HashMap;
# use actix_web::{
#     App, Error,
#     body::MessageBody,
#     dev::{ServiceRequest, ServiceResponse},
#     http::header::{Accept, Date},
#     web::{Header, Query},
# };
use actix_web::middleware::Next;

async fn my_extracting_mw(
accept: Header<Accept>,
query: Query<HashMap<String, String>>,
req: ServiceRequest,
next: Next<impl MessageBody>,
) -> Result<ServiceResponse<impl MessageBody>, Error> {
// pre-processing
next.call(req).await
// post-processing
}
# App::new().wrap(actix_web::middleware::from_fn(my_extracting_mw));"""
def from_fn(mw_fn: F) -> object: ...

"""Creates a new resource for a specific path.

Resources may have dynamic path segments. For example, a resource with the path `/a/{name}/c`
would match all incoming requests with paths such as `/a/b/c`, `/a/1/c`, or `/a/etc/c`.

A dynamic segment is specified in the form `{identifier}`, where the identifier can be used
later in a request handler to access the matched value for that segment. This is done by looking
up the identifier in the `Path` object returned by [`HttpRequest::match_info()`](crate::HttpRequest::match_info) method.

By default, each segment matches the regular expression `[^{}/]+`.

You can also specify a custom regex in the form `{identifier:regex}`:

For instance, to route `GET`-requests on any route matching `/users/{userid}/{friend}` and store
`userid` and `friend` in the exposed `Path` object:

# Examples
```
use actix_web::{web, App, HttpResponse};

let app = App::new().service(
web::resource("/users/{userid}/{friend}")
.route(web::get().to(|| HttpResponse::Ok()))
.route(web::head().to(|| HttpResponse::MethodNotAllowed()))
);
```"""
def resource(path: T) -> Resource: ...

"""Creates scope for common path prefix.

Scopes collect multiple paths under a common path prefix. The scope's path can contain dynamic
path segments.

# Avoid Trailing Slashes
Avoid using trailing slashes in the scope prefix (e.g., `web::scope("/scope/")`). It will almost
certainly not have the expected behavior. See the [documentation on resource definitions][pat]
to understand why this is the case and how to correctly construct scope/prefix definitions.

# Examples
In this example, three routes are set up (and will handle any method):
- `/{project_id}/path1`
- `/{project_id}/path2`
- `/{project_id}/path3`

# Examples
```
use actix_web::{web, App, HttpResponse};

let app = App::new().service(
web::scope("/{project_id}")
.service(web::resource("/path1").to(|| HttpResponse::Ok()))
.service(web::resource("/path2").to(|| HttpResponse::Ok()))
.service(web::resource("/path3").to(|| HttpResponse::MethodNotAllowed()))
);
```

[pat]: crate::dev::ResourceDef#prefix-resources"""
def scope(path: str) -> Scope: ...

"""Creates a new un-configured route."""
def route() -> Route: ...

"""Creates a new route with specified method guard.

# Examples
In this example, one `GET /{project_id}` route is set up:

```
use actix_web::{web, http, App, HttpResponse};

let app = App::new().service(
web::resource("/{project_id}")
.route(web::method(http::Method::GET).to(|| HttpResponse::Ok()))
);
```"""
def method(method: Method) -> Route: ...

"""Creates a new any-method route with handler.

```
use actix_web::{web, App, HttpResponse, Responder};

async fn index() -> impl Responder {
HttpResponse::Ok()
}

App::new().service(
web::resource("/").route(
web::to(index))
);
```"""
def to(handler: F) -> Route: ...

"""Creates a raw service for a specific path.

```
use actix_web::{dev, web, guard, App, Error, HttpResponse};

async fn my_service(req: dev::ServiceRequest) -> Result<dev::ServiceResponse, Error> {
Ok(req.into_response(HttpResponse::Ok().finish()))
}

let app = App::new().service(
web::service("/users/*")
.guard(guard::Header("content-type", "text/plain"))
.finish(my_service)
);
```"""
def service(path: T) -> WebService: ...

"""Create a relative or absolute redirect.

See [`Redirect`] docs for usage details.

# Examples
```
use actix_web::{web, App};

let app = App::new()
// the client will resolve this redirect to /api/to-path
.service(web::redirect("/api/from-path", "to-path"));
```"""
def redirect(from_: object, to: object) -> Redirect: ...

"""Executes blocking function on a thread pool, returns future that resolves to result of the
function execution."""
def block(f: F) -> object: ...

__all__: list[str] = ["init_service", "call_service", "try_call_service", "call_and_read_body", "read_response", "read_body", "try_read_body", "read_body_json", "try_read_body_json", "call_and_read_body_json", "try_call_and_read_body_json", "read_response_json", "ok_service", "status_service", "simple_service", "default_service", "Host", "fn_guard", "Any", "All", "Method", "Header", "my_app", "gzip_decode", "from_fn", "resource", "scope", "route", "method", "to", "service", "redirect", "block", "ErrorBadRequest", "ErrorUnauthorized", "ErrorForbidden", "ErrorNotFound", "ErrorInternalServerError", "get", "post", "put", "delete", "patch", "HttpResponse", "App", "HttpServer", "Data", "Query", "Json", "Form", "Path", "HttpRequest", "Route", "Result", "Person", "TestRequest", "ThinData", "ReqData", "Resource", "ResourceFactory", "ResourceService", "ResourceEndpoint", "HttpServer", "Data", "AppService", "AppConfig", "ServiceConfig", "HostGuard", "Acceptable", "GuardContext", "AnyGuard", "AllGuard", "Not", "AppInit", "AppInitService", "AppRoutingFactory", "AppRouting", "AppEntry", "ConnectionInfo", "PeerAddr", "MissingPeerAddr", "Route", "RouteService", "Redirect", "ResourceMap", "HttpRequest", "Scope", "ScopeFactory", "ScopeService", "ScopeEndpoint", "App", "ContentDisposition", "ContentLength", "EntityTag", "InternalError", "BlockingError", "Error", "Identity", "IdentityMiddleware", "ErrorHandlers", "ErrorHandlersMiddleware", "Compat", "CompatMiddleware", "Logger", "LoggerMiddleware", "NormalizePath", "NormalizePathNormalization", "Condition", "DefaultHeaders", "DefaultHeadersMiddleware", "Compress", "CompressMiddleware", "MiddlewareFn", "MiddlewareFnService", "Next", "CustomizeResponder", "HttpResponseBuilder", "HttpResponse", "CookieIter", "ServiceRequest", "ServiceResponse", "WebService", "Json", "JsonExtractFut", "JsonConfig", "Path", "PathConfig", "Html", "Form", "FormExtractFut", "FormConfig", "UrlEncoded", "Payload", "BytesExtractFut", "StringExtractFut", "PayloadConfig", "HttpMessageBody", "Header", "Readlines", "Query", "QueryConfig", "ContentRangeSpec", "Range", "ByteRangeSpec", "AnyOrSome", "Preference", "Encoding", "IfRange", "CacheDirective", "DispositionType", "DispositionParam", "UrlGenerationError", "UrlencodedError", "JsonPayloadError", "PathError", "QueryPayloadError", "ReadlinesError", "ErrorHandlerResponse", "TrailingSlash", "ConditionMiddleware", "JsonBody", "Either", "EitherExtractError"]
