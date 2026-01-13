"""Python stubs for the actix-web-lab Rust crate.

Install with: cookcrab install actix-web-lab
"""

from __future__ import annotations

from typing import Self

class Host:
    """Host information.

See [`ConnectionInfo::host()`](actix_web::dev::ConnectionInfo::host) for more."""

    def into_inner(self) -> str: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class Bytes:
    """Bytes extractor with const-generic payload size limit.

# Extractor
Extracts raw bytes from a request body, even if it.

Use the `LIMIT` const generic parameter to control the payload size limit. The default limit
that is exported (`DEFAULT_LIMIT`) is 4MiB.

# Differences from `actix_web::web::Bytes`
- Does not read `PayloadConfig` from app data.
- Supports const-generic size limits.
- Will not automatically decompress request bodies.

# Examples
```
use actix_web::{App, post};
use actix_web_lab::extract::{Bytes, DEFAULT_BYTES_LIMIT};

/// Deserialize `Info` from request's body.
#[post("/")]
async fn index(info: Bytes) -> String {
format!("Payload up to 4MiB: {info:?}!")
}

const LIMIT_32_MB: usize = 33_554_432;

/// Deserialize payload with a higher 32MiB limit.
#[post("/big-payload")]
async fn big_payload(info: Bytes<LIMIT_32_MB>) -> String {
format!("Payload up to 32MiB: {info:?}!")
}
```"""

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def as_ref(self) -> Bytes: ...

    def as_mut(self) -> Bytes: ...

    def into_inner(self) -> Bytes: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

class BytesExtractFut:

    def poll(self, cx: Context) -> object: ...

class ClearSiteData:
    """The `Clear-Site-Data` header, defined in the [W3C Clear-Site-Data spec].

Contains a list of [directives](ClearSiteDataDirective) for clearing out various types of data
from the user agent.

[Read more on MDN.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)

# ABNF

```text
Clear-Site-Data = 1#( quoted-string )
```

# Sample Values

- `"cache"`
- `"cache", "cookies"`
- `"*"`

# Examples

```
use actix_web::HttpResponse;
use actix_web_lab::header::{ClearSiteData, ClearSiteDataDirective};

let mut res = HttpResponse::Ok();
res.insert_header(ClearSiteData(vec![ClearSiteDataDirective::All]));

// shortcut for the all ("*", wildcard) directive
let mut res = HttpResponse::Ok();
res.insert_header(ClearSiteData::all());
```

[W3C Clear-Site-Data spec]: https://www.w3.org/TR/clear-site-data"""

    @staticmethod
    def all() -> "ClearSiteData": ...

    def fmt(self, f: Formatter) -> Result: ...

    def try_into_value(self) -> HeaderValue: ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: M) -> object: ...

class Json:
    """JSON extractor with const-generic payload size limit.

`Json` is used to extract typed data from JSON request payloads.

# Extractor
To extract typed data from a request body, the inner type `T` must implement the
[`serde::Deserialize`] trait.

Use the `LIMIT` const generic parameter to control the payload size limit. The default limit
that is exported (`DEFAULT_LIMIT`) is 2MiB.

```
use actix_web::{error, post, App, HttpRequest, HttpResponse, Responder};
use actix_web_lab::extract::{Json, JsonPayloadError, DEFAULT_JSON_LIMIT};
use serde::{Deserialize, Serialize};
use serde_json::json;

#[derive(Deserialize, Serialize)]
struct Info {
username: String,
}

/// Deserialize `Info` from request's body.
#[post("/")]
async fn index(info: Json<Info>) -> String {
format!("Welcome {}!", info.username)
}

const LIMIT_32_MB: usize = 33_554_432;

/// Deserialize payload with a higher 32MiB limit.
#[post("/big-payload")]
async fn big_payload(info: Json<Info, LIMIT_32_MB>) -> String {
format!("Welcome {}!", info.username)
}

/// Capture the error that may have occurred when deserializing the body.
#[post("/normal-payload")]
async fn normal_payload(
res: Result<Json<Info>, JsonPayloadError>,
req: HttpRequest,
) -> actix_web::Result<impl Responder> {
let item = res.map_err(|err| {
eprintln!("failed to deserialize JSON: {err}");
let res = HttpResponse::BadGateway().json(json!({
"error": "invalid_json",
"detail": err.to_string(),
}));
error::InternalError::from_response(err, res)
})?;

Ok(HttpResponse::Ok().json(item.0))
}
```"""

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def into_inner(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

class JsonExtractFut:

    def poll(self, cx: Context) -> object: ...

class JsonDeserializeError:
    """Deserialization errors that can occur during parsing query strings."""

    def path(self) -> object: ...

    def source(self) -> Exception: ...

    def fmt(self, f: Formatter) -> Result: ...

class LoadShed:
    """A middleware that sheds load when the inner service isn't ready."""

    @staticmethod
    def new() -> "LoadShed": ...

    def new_transform(self, service: S) -> Future: ...

class LoadShedService:
    """A service wrapper that sheds load when the inner service isn't ready."""

    def poll_ready(self, cx: Context) -> object: ...

    def call(self, req: Req) -> Future: ...

class Spa:
    """Single Page App (SPA) service builder.

# Examples

```no_run
# use actix_web::App;
# use actix_web_lab::web::spa;
App::new()
// ...api routes...
.service(
spa()
.index_file("./examples/assets/spa.html")
.static_resources_mount("/static")
.static_resources_location("./examples/assets")
.finish(),
)
# ;
```"""

    def index_file(self, index_file: object) -> Self: ...

    def static_resources_mount(self, static_resources_mount: object) -> Self: ...

    def static_resources_location(self, static_resources_location: object) -> Self: ...

    def finish(self) -> object: ...

    @staticmethod
    def default() -> "Spa": ...

class Data:
    """Server-sent events data message containing a `data` field and optional `id` and `event` fields.

# Examples
```
# #[actix_web::main] async fn test() {
use std::convert::Infallible;

use actix_web::body;
use actix_web_lab::sse;
use futures_util::stream;
use serde::Serialize;

#[derive(serde::Serialize)]
struct Foo {
bar: u32,
}

let sse = sse::Sse::from_stream(stream::iter([
Ok::<_, Infallible>(sse::Event::Data(sse::Data::new("foo"))),
Ok::<_, Infallible>(sse::Event::Data(
sse::Data::new_json(Foo { bar: 42 }).unwrap(),
)),
]));

assert_eq!(
body::to_bytes(sse).await.unwrap(),
"data: foo\\n\\ndata: {\\"bar\\":42}\\n\\n",
);
# }; test();
```"""

    @staticmethod
    def new(data: object) -> "Data": ...

    @staticmethod
    def new_json(data: object) -> object: ...

    def set_data(self, data: object) -> None: ...

    def id(self, id: object) -> Self: ...

    def set_id(self, id: object) -> None: ...

    def event(self, event: object) -> Self: ...

    def set_event(self, event: object) -> None: ...

class Cbor:
    """[CBOR] responder.

[CBOR]: https://cbor.io/"""

    def respond_to(self, _req: HttpRequest) -> object: ...

class SwapData:
    """A wrapper around `ArcSwap` that can be used as an extractor.

Can serve as a replacement for `Data<RwLock<T>>` in certain situations.

Currently exposes some internals of `arc-swap` and may change in the future."""

    @staticmethod
    def new(item: T) -> "SwapData": ...

    def load(self) -> object: ...

    def store(self, item: T) -> None: ...

    def clone(self) -> Self: ...

    @staticmethod
    def from_request(req: HttpRequest, _pl: Payload) -> Future: ...

class MapResBodyMiddleware:
    """Middleware transform for [`map_response_body`]."""

    def new_transform(self, service: S) -> Future: ...

class MapResBodyService:
    """Middleware service for [`from_fn`]."""

    def call(self, req: ServiceRequest) -> Future: ...

class Sender:
    """A channel-like sender for body chunks."""

    def send(self, chunk: Bytes) -> None: ...

    def close(self, error: E | None) -> None: ...

class Writer:
    """An `AsyncWrite` response body writer."""

    def poll_write(self, _cx: Context, buf: object) -> object: ...

    def poll_flush(self, _cx: Context) -> object: ...

    def poll_shutdown(self, _cx: Context) -> object: ...

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
use actix_web::{App, middleware, web};

# actix_web::rt::System::new().block_on(async {
let app = App::new()
.wrap(middleware::NormalizePath::trim())
.route("/test", web::get().to(|| async { "test" }))
.route("/unmatchable/", web::get().to(|| async { "unmatchable" }));

use actix_web::{
http::StatusCode,
test::{TestRequest, call_service, init_service},
};

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
    def new(behavior: TrailingSlash) -> "NormalizePath": ...

    @staticmethod
    def trim() -> "NormalizePath": ...

    def use_redirects(self) -> Self: ...

    def use_redirects_with(self, status_code: StatusCode) -> Self: ...

    def new_transform(self, service: S) -> Future: ...

class NormalizePathService:
    """Middleware service implementation for [`NormalizePath`]."""

    def call(self, req: ServiceRequest) -> Future: ...

class CacheControl:
    """The `Cache-Control` header, defined in [RFC 7234 §5.2].

Includes built-in support for directives introduced in subsequent specifications. [Read more
about the full list of supported directives on MDN][mdn].

The `Cache-Control` header field is used to specify [directives](CacheDirective) for caches
along the request/response chain. Such cache directives are unidirectional in that the presence
of a directive in a request does not imply that the same directive is to be given in the
response.

# ABNF
```text
Cache-Control   = 1#cache-directive
cache-directive = token [ \\"=\\" ( token / quoted-string ) ]
```

# Example Values
- `max-age=30`
- `no-cache, no-store`
- `public, max-age=604800, immutable`
- `private, community=\\"UCI\\"`

# Examples
```
use actix_web::{
HttpResponse,
http::header::{CacheControl, CacheDirective},
};

let mut builder = HttpResponse::Ok();
builder.insert_header(CacheControl(vec![CacheDirective::MaxAge(86400u32)]));
```

```
use actix_web::{
HttpResponse,
http::header::{CacheControl, CacheDirective},
};

let mut builder = HttpResponse::Ok();
builder.insert_header(CacheControl(vec![
CacheDirective::NoCache,
CacheDirective::Private,
CacheDirective::MaxAge(360u32),
CacheDirective::Extension("foo".to_owned(), Some("bar".to_owned())),
]));
```

[RFC 7234 §5.2]: https://datatracker.ietf.org/doc/html/rfc7234#section-5.2
[mdn]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control"""

    def fmt(self, f: Formatter) -> Result: ...

    def try_into_value(self) -> HeaderValue: ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: M) -> object: ...

class XForwardedPrefix:
    """The conventional `X-Forwarded-Prefix` header.

The `X-Forwarded-Prefix` header field is used to signal that a prefix was stripped from the path
while being proxied.

# Example Values

- `/`
- `/foo`

# Examples

```
use actix_web::HttpResponse;
use actix_web_lab::header::XForwardedPrefix;

let mut builder = HttpResponse::Ok();
builder.insert_header(XForwardedPrefix("/bar".parse().unwrap()));
```"""

    def try_into_value(self) -> HeaderValue: ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: M) -> object: ...

class ReconstructedPath:
    """Reconstructed path using X-Forwarded-Prefix header.

```
# use actix_web::{FromRequest as _, test::TestRequest};
# actix_web::rt::System::new().block_on(async {
use actix_web_lab::extract::ReconstructedPath;

let req = TestRequest::with_uri("/bar")
.insert_header(("x-forwarded-prefix", "/foo"))
.to_http_request();

let path = ReconstructedPath::extract(&req).await.unwrap();
assert_eq!(path.to_string(), "/foo/bar");
# })
```"""

    @staticmethod
    def from_request(req: HttpRequest, _payload: Payload) -> Future: ...

class Path:
    """Extract typed data from request path segments.

Alternative to `web::Path` extractor from Actix Web that allows deconstruction, but omits the
implementation of `Deref`.

Unlike, [`HttpRequest::match_info`], this extractor will fully percent-decode dynamic segments,
including `/`, `%`, and `+`.

# Examples
```
use actix_web::get;
use actix_web_lab::extract::Path;

// extract path info from "/{name}/{count}/index.html" into tuple
// {name}  - deserialize a String
// {count} - deserialize a u32
#[get("/{name}/{count}/index.html")]
async fn index(Path((name, count)): Path<(String, u32)>) -> String {
format!("Welcome {}! {}", name, count)
}
```

Path segments also can be deserialized into any type that implements [`serde::Deserialize`].
Path segment labels will be matched with struct field names.

```
use actix_web::get;
use actix_web_lab::extract::Path;
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
name: String,
}

// extract `Info` from a path using serde
#[get("/{name}")]
async fn index(info: Path<Info>) -> String {
let info = info.into_inner();
format!("Welcome {}!", info.name)
}
```"""

    def into_inner(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class LazyData:
    """A lazy extractor for thread-local data.

Using `LazyData` as an extractor will not initialize the data; [`get`](Self::get) must be used."""

    def clone(self) -> Self: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(init: F) -> object: ...

    def get(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class BodyLimit:
    """Extractor wrapper that limits size of payload used.

# Examples
```no_run
use actix_web::{Responder, get, web::Bytes};
use actix_web_lab::extract::BodyLimit;

const BODY_LIMIT: usize = 1_048_576; // 1MB

#[get("/")]
async fn handler(body: BodyLimit<Bytes, BODY_LIMIT>) -> impl Responder {
let body = body.into_inner();
assert!(body.len() < BODY_LIMIT);
body
}
```"""

    def fmt(self, f: Formatter) -> Result: ...

    def as_ref(self) -> T: ...

    @staticmethod
    def from_(inner: T) -> "BodyLimit": ...

    def into_inner(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

class BodyLimitFut:

    def poll(self, cx: Context) -> object: ...

class ConditionOption:
    """Middleware for conditionally enabling other middleware in an [`Option`].

# Example
```
use actix_web::{App, middleware::Logger};
use actix_web_lab::middleware::ConditionOption;

let normalize: ConditionOption<_> = Some(Logger::default()).into();
let app = App::new().wrap(normalize);
```"""

    @staticmethod
    def from_(value: T | None) -> "ConditionOption": ...

    def new_transform(self, service: S) -> Future: ...

class Forwarded:
    """The `Forwarded` header, defined in [RFC 7239].

Also see the [Forwarded header's MDN docs][mdn] for field semantics.

[RFC 7239]: https://datatracker.ietf.org/doc/html/rfc7239
[mdn]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded"""

    @staticmethod
    def new(by: object, r#for: object, host: object, proto: object) -> "Forwarded": ...

    @staticmethod
    def new_for(r#for: object) -> "Forwarded": ...

    def for_client(self) -> object: ...

    def for_chain(self) -> object: ...

    def by(self) -> object: ...

    def host(self) -> object: ...

    def proto(self) -> object: ...

    def push_for(self, identifier: object) -> None: ...

    @staticmethod
    def from_str(val: str) -> object: ...

    def try_into_value(self) -> HeaderValue: ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: M) -> object: ...

class MapResMiddleware:
    """Middleware transform for [`map_response`]."""

    def new_transform(self, service: S) -> Future: ...

class MapResService:
    """Middleware service for [`from_fn`]."""

    def call(self, req: ServiceRequest) -> Future: ...

class LazyDataShared:
    """A lazy extractor for globally shared data.

Unlike, [`LazyData`], this type implements [`Send`] and [`Sync`].

Using `SharedLazyData` as an extractor will not initialize the data; [`get`](Self::get) must be
used.

[`LazyData`]: crate::extract::LazyData"""

    def clone(self) -> Self: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(init: F) -> object: ...

    def get(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class ContentLength:
    """The `Content-Length` header, defined in [RFC 9110 §8.6].

The "Content-Length" header field indicates the associated representation's data length as a
decimal non-negative integer number of octets.

# ABNF
```plain
Content-Length = 1*DIGIT
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

class CatchPanic:
    """A middleware to catch panics in wrapped handlers and middleware, returning empty 500 responses.

**This middleware should never be used as replacement for proper error handling.** See [this
thread](https://github.com/actix/actix-web/issues/1501#issuecomment-627517783) for historical
discussion on why Actix Web does not do this by default.

It is recommended that this middleware be registered last. That is, `wrap`ed after everything
else except `Logger`.

# Examples

```
# use actix_web::App;
use actix_web_lab::middleware::CatchPanic;

App::new().wrap(CatchPanic::default())
# ;
```

```no_run
# use actix_web::App;
use actix_web::middleware::{Logger, NormalizePath};
use actix_web_lab::middleware::CatchPanic;

// recommended wrap order
App::new()
.wrap(NormalizePath::default())
.wrap(CatchPanic::default()) // <- after everything except logger
.wrap(Logger::default())
# ;
```"""

    def new_transform(self, service: S) -> Future: ...

class CatchPanicMiddleware:
    """A middleware to catch panics in wrapped handlers and middleware, returning empty 500 responses.

See [`CatchPanic`]."""

    def call(self, req: ServiceRequest) -> Future: ...

class RequestSignature:
    """Wraps an extractor and calculates a request signature hash alongside.

Warning: Currently, this will always take the body meaning that if a body extractor is used,
this needs to wrap it or else it will not work."""

    def into_parts(self) -> object: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

class RedirectHttps:
    """Middleware to redirect traffic to HTTPS if connection is insecure.

# HSTS

[HTTP Strict Transport Security (HSTS)] is configurable. Care should be taken when setting up
HSTS for your site; misconfiguration can potentially leave parts of your site in an unusable
state. By default it is disabled.

See [`StrictTransportSecurity`] docs for more info.

# Examples

```
# use std::time::Duration;
# use actix_web::App;
use actix_web_lab::{header::StrictTransportSecurity, middleware::RedirectHttps};

let mw = RedirectHttps::default();
let mw = RedirectHttps::default().to_port(8443);
let mw = RedirectHttps::with_hsts(StrictTransportSecurity::default());
let mw = RedirectHttps::with_hsts(StrictTransportSecurity::new(Duration::from_secs(60 * 60)));
let mw = RedirectHttps::with_hsts(StrictTransportSecurity::recommended());

App::new().wrap(mw)
# ;
```

[HTTP Strict Transport Security (HSTS)]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security"""

    @staticmethod
    def with_hsts(hsts: StrictTransportSecurity) -> "RedirectHttps": ...

    def to_port(self, port: int) -> Self: ...

    def new_transform(self, service: S) -> Future: ...

class RedirectHttpsMiddleware:
    """Middleware service implementation for [`RedirectHttps`]."""

    def call(self, req: ServiceRequest) -> Future: ...

class ErrorHandlers:
    """Middleware for registering custom status code based error handlers.

Register handlers with the `ErrorHandlers::handler()` method to register a custom error handler
for a given status code. Handlers can modify existing responses or create completely new ones.

# Examples
```
use actix_web::{
App, HttpResponse, Result,
body::EitherBody,
dev::ServiceResponse,
http::{StatusCode, header},
web,
};
use actix_web_lab::middleware::ErrorHandlers;

async fn add_error_header<B>(
mut res: ServiceResponse<B>,
) -> Result<ServiceResponse<EitherBody<B>>> {
res.response_mut().headers_mut().insert(
header::CONTENT_TYPE,
header::HeaderValue::from_static("Error"),
);
Ok(res.map_into_left_body())
}

let app = App::new()
.wrap(ErrorHandlers::new().handler(StatusCode::INTERNAL_SERVER_ERROR, add_error_header))
.service(web::resource("/").route(web::get().to(HttpResponse::InternalServerError)));
```"""

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def default() -> "ErrorHandlers": ...

    @staticmethod
    def new() -> "ErrorHandlers": ...

    def handler(self, status: StatusCode, handler: F) -> Self: ...

    def new_transform(self, service: S) -> Future: ...

class ErrorHandlersMiddleware:
    """Middleware for registering custom status code based error handlers.

See [`ErrorHandlers`]."""

    def call(self, req: ServiceRequest) -> Future: ...

class UrlEncodedForm:
    """URL-encoded form extractor with const-generic payload size limit.

`UrlEncodedForm` is used to extract typed data from URL-encoded request payloads.

# Extractor
To extract typed data from a request body, the inner type `T` must implement the
[`serde::Deserialize`] trait.

Use the `LIMIT` const generic parameter to control the payload size limit. The default limit
that is exported (`DEFAULT_LIMIT`) is 2MiB.

```
use actix_web::{App, post};
use actix_web_lab::extract::{DEFAULT_URL_ENCODED_FORM_LIMIT, UrlEncodedForm};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
username: String,
}

/// Deserialize `Info` from request's body.
#[post("/")]
async fn index(info: UrlEncodedForm<Info>) -> String {
format!("Welcome {}!", info.username)
}

const LIMIT_32_MB: usize = 33_554_432;

/// Deserialize payload with a higher 32MiB limit.
#[post("/big-payload")]
async fn big_payload(info: UrlEncodedForm<Info, LIMIT_32_MB>) -> String {
format!("Welcome {}!", info.username)
}
```"""

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def into_inner(self) -> T: ...

    @staticmethod
    def from_request(req: HttpRequest, payload: Payload) -> Future: ...

class UrlEncodedFormExtractFut:

    def poll(self, cx: Context) -> object: ...

class UrlEncodedFormDeserializeError:
    """Errors that can occur while deserializing URL-encoded forms query strings."""

    def path(self) -> object: ...

    def source(self) -> Exception: ...

    def fmt(self, f: Formatter) -> Result: ...

class Query:
    """Extract typed information from the request's query.

To extract typed data from the URL query string, the inner type `T` must implement the
[`DeserializeOwned`] trait.

# Differences From `actix_web::web::Query`
This extractor uses `serde_html_form` under-the-hood which supports multi-value items. These are
sent by HTML select inputs when multiple options are chosen and can be collected into a `Vec`.

This version also removes the custom error handler config; users should instead prefer to handle
errors using the explicit `Result<Query<T>, E>` extractor in their handlers.

# Panics
A query string consists of unordered `key=value` pairs, therefore it cannot be decoded into any
type which depends upon data ordering (eg. tuples). Trying to do so will result in a panic.

# Examples
```
use actix_web::{Responder, get};
use actix_web_lab::extract::Query;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
#[serde(rename_all = "lowercase")]
enum LogType {
Reports,
Actions,
}

#[derive(Debug, Deserialize)]
pub struct LogsParams {
#[serde(rename = "type")]
log_type: u64,

#[serde(rename = "user")]
users: Vec<String>,
}

// Deserialize `LogsParams` struct from query string.
// This handler gets called only if the request's query parameters contain both fields.
// A valid request path for this handler would be `/logs?type=reports&user=foo&user=bar"`.
#[get("/logs")]
async fn index(info: Query<LogsParams>) -> impl Responder {
let LogsParams { log_type, users } = info.into_inner();
format!("Logs request for type={log_type} and user list={users:?}!")
}

// Or use destructuring, which is equivalent to `.into_inner()`.
#[get("/debug2")]
async fn debug2(Query(info): Query<LogsParams>) -> impl Responder {
dbg!("Authorization object = {info:?}");
"OK"
}
```"""

    def into_inner(self) -> T: ...

    @staticmethod
    def from_query(query_str: str) -> object: ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class QueryDeserializeError:
    """Deserialization errors that can occur during parsing query strings."""

    def path(self) -> object: ...

    def source(self) -> Exception: ...

    def fmt(self, f: Formatter) -> Result: ...

    def status_code(self) -> StatusCode: ...

class MessagePack:
    """[MessagePack] responder.

If you require the fields to be named, use [`MessagePackNamed`].

[MessagePack]: https://msgpack.org/"""

    def respond_to(self, _req: HttpRequest) -> object: ...

class MessagePackNamed:
    """MessagePack responder with named fields."""

    def respond_to(self, _req: HttpRequest) -> object: ...

class LocalData:
    """A thread-local equivalent to [`SharedData`](crate::extract::SharedData)."""

    @staticmethod
    def new(item: T) -> object: ...

    def deref(self) -> T: ...

    def clone(self) -> object: ...

    @staticmethod
    def from_(rc: object) -> "LocalData": ...

    @staticmethod
    def from_request(req: HttpRequest, _: Payload) -> Future: ...

class PanicReporter:
    """A middleware that triggers a callback when the worker is panicking.

Mostly useful for logging or metrics publishing. The callback received the object with which
panic was originally invoked to allow down-casting.

# Examples

```no_run
# use actix_web::App;
use actix_web_lab::middleware::PanicReporter;
# mod metrics {
#   macro_rules! increment_counter {
#       ($tt:tt) => {{}};
#   }
#   pub(crate) use increment_counter;
# }

App::new().wrap(PanicReporter::new(|_| metrics::increment_counter!("panic")))
# ;
```"""

    @staticmethod
    def new(callback: object) -> "PanicReporter": ...

    def fmt(self, f: Formatter) -> Result: ...

    def new_transform(self, service: S) -> Future: ...

class PanicReporterMiddleware:
    """Middleware service implementation for [`PanicReporter`]."""

    def call(self, req: Req) -> Future: ...

class StrictTransportSecurity:
    """HTTP Strict Transport Security (HSTS) configuration.

Care should be taken when setting up HSTS for your site; misconfiguration can potentially leave
parts of your site in an unusable state.

# `Default`

The `Default` implementation uses a 5 minute `max-age` and does not include subdomains or
preloading. This default is intentionally conservative to prevent accidental misconfiguration
causing irrecoverable problems for users.

Once you have configured and tested the default HSTS config, [`recommended`](Self::recommended)
can be used as a secure default for production.

# References

See the [HSTS page on MDN] for more information.

[HSTS page on MDN]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security"""

    @staticmethod
    def new(duration: Duration) -> "StrictTransportSecurity": ...

    @staticmethod
    def recommended() -> "StrictTransportSecurity": ...

    def include_subdomains(self) -> Self: ...

    def preload(self) -> Self: ...

    @staticmethod
    def default() -> "StrictTransportSecurity": ...

    @staticmethod
    def from_str(val: str) -> object: ...

    def try_into_value(self) -> HeaderValue: ...

    @staticmethod
    def name() -> HeaderName: ...

    @staticmethod
    def parse(msg: M) -> object: ...

class BytesBody:
    """Future that resolves to `Bytes` when the payload is been completely read.

Returns error if:
- `Content-Length` is greater than `LIMIT`."""
    Error: "BytesBody"
    Body: "BytesBody"

    @staticmethod
    def new(req: HttpRequest, payload: Payload) -> "BytesBody": ...

    def poll(self, cx: Context) -> object: ...

class BytesPayloadError:
    """A set of errors that can occur during parsing json payloads"""
    OverflowKnownLength: "BytesPayloadError"
    Overflow: "BytesPayloadError"
    Payload: "BytesPayloadError"

    @staticmethod
    def from_(err: PayloadError) -> "BytesPayloadError": ...

    def status_code(self) -> StatusCode: ...

    def eq(self, other: Self) -> bool: ...

class ClearSiteDataDirective:
    """Directives contained in a [`ClearSiteData`] header.

[Read more on MDN.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data#directives)"""
    All: "ClearSiteDataDirective"
    Cache: "ClearSiteDataDirective"
    ClientHints: "ClearSiteDataDirective"
    Cookies: "ClearSiteDataDirective"
    Storage: "ClearSiteDataDirective"
    ExecutionContexts: "ClearSiteDataDirective"

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(dir: str) -> object: ...

class JsonBody:
    """Future that resolves to some `T` when parsed from a JSON payload.

Can deserialize any type `T` that implements [`Deserialize`][serde::Deserialize].

Returns error if:
- `Content-Type` is not `application/json`.
- `Content-Length` is greater than `LIMIT`.
- The payload, when consumed, is not valid JSON."""
    Error: "JsonBody"
    Body: "JsonBody"

    @staticmethod
    def new(req: HttpRequest, payload: Payload) -> "JsonBody": ...

    def poll(self, cx: Context) -> object: ...

class JsonPayloadError:
    """A set of errors that can occur during parsing json payloads"""
    Overflow: "JsonPayloadError"
    ContentType: "JsonPayloadError"
    Deserialize: "JsonPayloadError"
    Payload: "JsonPayloadError"

    def status_code(self) -> StatusCode: ...

class Overloaded:
    """An error returned by [`LoadShed`] service when the inner service is not ready to handle any
requests at the time of being called."""
    Service: "Overloaded"
    Overloaded: "Overloaded"

    def fmt(self, f: Formatter) -> Result: ...

    def source(self) -> object: ...

    def status_code(self) -> StatusCode: ...

class Event:
    """Server-sent events message containing one or more fields."""
    Data: "Event"
    Comment: "Event"

    @staticmethod
    def from_(data: Data) -> "Event": ...

class CacheDirective:
    """Directives contained in a [`CacheControl`] header.

[Read more on MDN.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#cache_directives)"""
    MaxAge: "CacheDirective"
    MaxStale: "CacheDirective"
    MinFresh: "CacheDirective"
    SMaxAge: "CacheDirective"
    NoCache: "CacheDirective"
    NoStore: "CacheDirective"
    NoTransform: "CacheDirective"
    OnlyIfCached: "CacheDirective"
    MustRevalidate: "CacheDirective"
    ProxyRevalidate: "CacheDirective"
    MustUnderstand: "CacheDirective"
    Private: "CacheDirective"
    Public: "CacheDirective"
    Immutable: "CacheDirective"
    StaleWhileRevalidate: "CacheDirective"
    StaleIfError: "CacheDirective"
    Extension: "CacheDirective"

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_str(dir: str) -> object: ...

class BodyLimitError:
    Extractor: "BodyLimitError"
    Overflow: "BodyLimitError"

    def fmt(self, f: Formatter) -> Result: ...

class ConditionMiddleware:
    """TODO"""
    Enable: "ConditionMiddleware"
    Disable: "ConditionMiddleware"

    def poll_ready(self, cx: Context) -> object: ...

    def call(self, req: Req) -> Future: ...

class RequestSignatureError:
    """Errors that can occur when extracting and processing request signatures."""
    Extractor: "RequestSignatureError"
    Signature: "RequestSignatureError"

    def fmt(self, f: Formatter) -> Result: ...

class UrlEncodedFormBody:
    """Future that resolves to some `T` when parsed from a URL-encoded payload.

Can deserialize any type `T` that implements [`Deserialize`][serde::Deserialize].

Returns error if:
- `Content-Type` is not `application/x-www-form-urlencoded`.
- `Content-Length` is greater than `LIMIT`.
- The payload, when consumed, is not URL-encoded."""
    Error: "UrlEncodedFormBody"
    Body: "UrlEncodedFormBody"

    @staticmethod
    def new(req: HttpRequest, payload: Payload) -> "UrlEncodedFormBody": ...

    def poll(self, cx: Context) -> object: ...

class UrlEncodedFormError:
    """Errors that can occur while extracting URL-encoded forms."""
    Overflow: "UrlEncodedFormError"
    ContentType: "UrlEncodedFormError"
    Deserialize: "UrlEncodedFormError"
    Payload: "UrlEncodedFormError"

    def status_code(self) -> StatusCode: ...

"""Returns an effectively cloned payload that supports streaming efficiently.

The cloned payload:
- yields identical chunks;
- does not poll ahead of the original;
- does not poll significantly slower than the original;
- receives an error signal if the original errors, but details are opaque to the copy.

If the payload is forked in one of the extractors used in a handler, then the original _must_ be
read in another extractor or else the request will hang."""
def fork_request_payload(orig_payload: Payload) -> Payload: ...

"""Creates a middleware from an async function that is used as a mapping function for an
[`impl MessageBody`][MessageBody].

# Examples
Completely replaces the body:
```
# use actix_web_lab::middleware::map_response_body;
use actix_web::{HttpRequest, body::MessageBody};

async fn replace_body(
_req: HttpRequest,
_: impl MessageBody,
) -> actix_web::Result<impl MessageBody> {
Ok("foo".to_owned())
}
# actix_web::App::new().wrap(map_response_body(replace_body));
```

Appends some bytes to the body:
```
# use actix_web_lab::middleware::map_response_body;
use actix_web::{
HttpRequest,
body::{self, MessageBody},
web::{BufMut as _, BytesMut},
};

async fn append_bytes(
_req: HttpRequest,
body: impl MessageBody,
) -> actix_web::Result<impl MessageBody> {
let buf = body::to_bytes(body).await.ok().unwrap();

let mut body = BytesMut::from(&buf[..]);
body.put_slice(b" - hope you like things ruining your payload format");

Ok(body)
}
# actix_web::App::new().wrap(map_response_body(append_bytes));
```"""
def map_response_body(mapper_fn: F) -> object: ...

"""Creates service that always responds with given status code and echoes request path as response
body."""
def echo_path_service(status_code: StatusCode) -> object: ...

"""Returns a sender half and a receiver half that can be used as a body type.

# Examples
```
# use actix_web::{HttpResponse, web};
use std::convert::Infallible;

use actix_web_lab::body;

# async fn index() {
let (mut body_tx, body) = body::channel::<Infallible>();

let _ = web::block(move || {
body_tx
.send(web::Bytes::from_static(b"body from another thread"))
.unwrap();
});

HttpResponse::Ok().body(body)
# ;}
```"""
def channel() -> object: ...

"""Returns an `AsyncWrite` response body writer and its associated body type.

# Examples
```
# use actix_web::{HttpResponse, web};
use actix_web_lab::body;
use tokio::io::AsyncWriteExt as _;

# async fn index() {
let (mut wrt, body) = body::writer();

let _ = tokio::spawn(async move { wrt.write_all(b"body from another thread").await });

HttpResponse::Ok().body(body)
# ;}
```"""
def writer() -> object: ...

"""Constructs a new [`BodyStream`] from an infallible byte chunk stream.

This could be stabilized into Actix Web as `BodyStream::from_infallible()`."""
def new_infallible_body_stream(stream: S) -> object: ...

"""Constructs a new [`SizedStream`] from an infallible byte chunk stream.

This could be stabilized into Actix Web as `SizedStream::from_infallible()`."""
def new_infallible_sized_stream(size: int, stream: S) -> object: ...

"""Creates a middleware from an async function that is used as a mapping function for a
[`ServiceResponse`].

# Examples
Adds header:
```
# use actix_web_lab::middleware::map_response;
use actix_web::{body::MessageBody, dev::ServiceResponse, http::header};

async fn add_header(
mut res: ServiceResponse<impl MessageBody>,
) -> actix_web::Result<ServiceResponse<impl MessageBody>> {
res.headers_mut()
.insert(header::WARNING, header::HeaderValue::from_static("42"));

Ok(res)
}
# actix_web::App::new().wrap(map_response(add_header));
```

Maps body:
```
# use actix_web_lab::middleware::map_response;
use actix_web::{body::MessageBody, dev::ServiceResponse};

async fn mutate_body_type(
res: ServiceResponse<impl MessageBody + 'static>,
) -> actix_web::Result<ServiceResponse<impl MessageBody>> {
Ok(res.map_into_left_body::<()>())
}
# actix_web::App::new().wrap(map_response(mutate_body_type));
```"""
def map_response(mapper_fn: F) -> object: ...

"""A function middleware to redirect traffic to `www.` if not already there.

# Examples

```
# use actix_web::App;
use actix_web::middleware::from_fn;
use actix_web_lab::middleware::redirect_to_www;

App::new().wrap(from_fn(redirect_to_www))
# ;
```"""
async def redirect_to_www(req: ServiceRequest, next: object) -> object: ...

"""A function middleware to redirect traffic away from `www.` if it's present.

# Examples

```
# use actix_web::App;
use actix_web::middleware::from_fn;
use actix_web_lab::middleware::redirect_to_non_www;

App::new().wrap(from_fn(redirect_to_non_www))
# ;
```"""
async def redirect_to_non_www(req: ServiceRequest, next: object) -> object: ...

"""Constructs a new Single-page Application (SPA) builder.

See [`Spa`] docs for more details.

# Examples
```
# use actix_web::App;
# use actix_web_lab::web::spa;
let app = App::new()
// ...api routes...
.service(
spa()
.index_file("./examples/assets/spa.html")
.static_resources_mount("/static")
.static_resources_location("./examples/assets")
.finish(),
);
```"""
def spa() -> Spa: ...

__all__: list[str] = ["fork_request_payload", "map_response_body", "echo_path_service", "channel", "writer", "new_infallible_body_stream", "new_infallible_sized_stream", "map_response", "redirect_to_www", "redirect_to_non_www", "spa", "Host", "Bytes", "BytesExtractFut", "ClearSiteData", "Json", "JsonExtractFut", "JsonDeserializeError", "LoadShed", "LoadShedService", "Spa", "Data", "Cbor", "SwapData", "MapResBodyMiddleware", "MapResBodyService", "Sender", "Writer", "NormalizePath", "NormalizePathService", "CacheControl", "XForwardedPrefix", "ReconstructedPath", "Path", "LazyData", "BodyLimit", "BodyLimitFut", "ConditionOption", "Forwarded", "MapResMiddleware", "MapResService", "LazyDataShared", "ContentLength", "CatchPanic", "CatchPanicMiddleware", "RequestSignature", "RedirectHttps", "RedirectHttpsMiddleware", "ErrorHandlers", "ErrorHandlersMiddleware", "UrlEncodedForm", "UrlEncodedFormExtractFut", "UrlEncodedFormDeserializeError", "Query", "QueryDeserializeError", "MessagePack", "MessagePackNamed", "LocalData", "PanicReporter", "PanicReporterMiddleware", "StrictTransportSecurity", "BytesBody", "BytesPayloadError", "ClearSiteDataDirective", "JsonBody", "JsonPayloadError", "Overloaded", "Event", "CacheDirective", "BodyLimitError", "ConditionMiddleware", "RequestSignatureError", "UrlEncodedFormBody", "UrlEncodedFormError"]
