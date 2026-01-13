"""Python stubs for the ureq Rust crate.

Install with: cookcrab install ureq
"""

from __future__ import annotations

from typing import Self

class ConnectProxyConnector:
    """Connector for CONNECT proxy settings.

This operates on the previous chained transport typically a TcpConnector optionally
wrapped in TLS."""

    def connect(self, details: ConnectionDetails, chained: In | None) -> Out | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class LazyBuffers:
    """Default buffer implementation.

The buffers are lazy such that no allocations are made until needed. That means
a [`Transport`](crate::transport::Transport) implementation can freely instantiate
the `LazyBuffers`."""

    @staticmethod
    def new(input_size: int, output_size: int) -> "LazyBuffers": ...

    def output(self) -> object: ...

    def input(self) -> object: ...

    def input_append_buf(self) -> object: ...

    def tmp_and_output(self) -> object: ...

    def input_appended(self, amount: int) -> None: ...

    def input_consume(self, amount: int) -> None: ...

    def can_use_input(self) -> bool: ...

class ChainedConnector:
    """Two chained connectors called one after another.

Created by calling [`Connector::chain`] on the first connector."""

    def connect(self, details: ConnectionDetails, chained: In | None) -> Out | None: ...

    def fmt(self, f: Formatter) -> Result: ...

    def clone(self) -> Self: ...

class ConnectionDetails:
    """The parameters needed to create a [`Transport`]."""

    def needs_tls(self) -> bool: ...

class DefaultConnector:
    """Default connector providing TCP sockets, TLS and SOCKS proxy.

This connector is the following chain:

1. [`SocksConnector`] to handle proxy settings if set.
2. [`TcpConnector`] to open a socket directly if a proxy is not used.
3. [`RustlsConnector`] which wraps the
connection from 1 or 2 in TLS if the scheme is `https` and the
[`TlsConfig`](crate::tls::TlsConfig) indicate we are using **rustls**.
This is the default TLS provider.
4. [`NativeTlsConnector`] which wraps
the connection from 1 or 2 in TLS if the scheme is `https` and
[`TlsConfig`](crate::tls::TlsConfig) indicate we are using **native-tls**.
"""

    @staticmethod
    def new() -> "DefaultConnector": ...

    @staticmethod
    def default() -> "DefaultConnector": ...

    def connect(self, details: ConnectionDetails, chained: object) -> Out | None: ...

class TransportAdapter:
    """Helper to turn a [`Transport`] into a std::io [`Read`](io::Read) and [`Write`](io::Write).

This is useful when integrating with components that expect a regular `Read`/`Write`. In
ureq this is used both for the [`RustlsConnector`](crate::unversioned::transport::RustlsConnector) and the
[`NativeTlsConnector`](crate::unversioned::transport::NativeTlsConnector)."""

    @staticmethod
    def new(transport: T) -> "TransportAdapter": ...

    def set_timeout(self, timeout: NextTimeout) -> None: ...

    def get_ref(self) -> dynTransport: ...

    def get_mut(self) -> mutdynTransport: ...

    def inner(self) -> dynTransport: ...

    def into_inner(self) -> T: ...

    def read(self, buf: object) -> int: ...

    def write(self, buf: object) -> int: ...

    def flush(self) -> object: ...

class SocksConnector:
    """Connector for SOCKS proxies.

Requires the **socks-proxy** feature.

The connector looks at the proxy settings in [`proxy`](crate::config::ConfigBuilder::proxy) to
determine whether to attempt a proxy connection or not."""

    def connect(self, details: ConnectionDetails, chained: In | None) -> Out | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class TcpConnector:
    """Connector for regular TCP sockets."""

    def connect(self, details: ConnectionDetails, chained: In | None) -> Out | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class TcpTransport:

    @staticmethod
    def new(stream: TcpStream, buffers: LazyBuffers) -> "TcpTransport": ...

    def buffers(self) -> mutdynBuffers: ...

    def transmit_output(self, amount: int, timeout: NextTimeout) -> None: ...

    def await_input(self, timeout: NextTimeout) -> bool: ...

    def is_open(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class DefaultResolver:
    """Default resolver implementation.

Uses std::net [`ToSocketAddrs`](https://doc.rust-lang.org/std/net/trait.ToSocketAddrs.html) to
do the lookup. Can optionally spawn a thread to abort lookup if the relevant timeout is set."""

    @staticmethod
    def host_and_port(scheme: Scheme, authority: Authority) -> str | None: ...

    def resolve(self, uri: Uri, config: Config, timeout: NextTimeout) -> ResolvedSocketAddrs: ...

    def fmt(self, f: Formatter) -> Result: ...

class Body:
    """A response body returned as [`http::Response<Body>`].

# Default size limit

Methods like `read_to_string()`, `read_to_vec()`, and `read_json()` have a **default 10MB limit**
to prevent memory exhaustion. To download larger files, use `with_config().limit(new_size)`:

```
// Download a 20MB file
let bytes = ureq::get("http://httpbin.org/bytes/200000000")
.call()?
.body_mut()
.with_config()
.limit(20 * 1024 * 1024) // 20MB
.read_to_vec()?;
# Ok::<_, ureq::Error>(())
```

# Body lengths

HTTP/1.1 has two major modes of transfering body data. Either a `Content-Length`
header defines exactly how many bytes to transfer, or `Transfer-Encoding: chunked`
facilitates a streaming style when the size is not known up front.

To protect against a problem called [request smuggling], ureq has heuristics for
how to interpret a server sending both `Transfer-Encoding` and `Content-Length` headers.

1. `chunked` takes precedence if there both headers are present (not for HTTP/1.0)
2. `content-length` is used if there is no chunked
3. If there are no headers, fall back on "close delimited" meaning the socket
must close to end the body

When a `Content-Length` header is used, ureq will ensure the received body is _EXACTLY_
as many bytes as declared (it cannot be less). This mechanic is in `ureq-proto`
and is different to the [`BodyWithConfig::limit()`] below.

# Pool reuse

To return a connection (aka [`Transport`][crate::unversioned::transport::Transport])
to the Agent's pool, the body must be read to end. If [`BodyWithConfig::limit()`] is set
shorter size than the actual response body, the connection will not be reused.

# Example

```
use std::io::Read;
let mut res = ureq::get("http://httpbin.org/bytes/100")
.call()?;

assert!(res.headers().contains_key("Content-Length"));
let len: usize = res.headers().get("Content-Length")
.unwrap().to_str().unwrap().parse().unwrap();

let mut bytes: Vec<u8> = Vec::with_capacity(len);
res.body_mut().as_reader()
.read_to_end(&mut bytes)?;

assert_eq!(bytes.len(), len);
# Ok::<_, ureq::Error>(())
```

[request smuggling]: https://en.wikipedia.org/wiki/HTTP_request_smuggling"""

    @staticmethod
    def builder() -> BodyBuilder: ...

    def mime_type(self) -> object: ...

    def charset(self) -> object: ...

    def content_length(self) -> int | None: ...

    def as_reader(self) -> BodyReader: ...

    def into_reader(self) -> BodyReader: ...

    def read_to_string(self) -> str: ...

    def read_to_vec(self) -> list[int]: ...

    def read_json(self) -> T: ...

    def with_config(self) -> BodyWithConfig: ...

    def into_with_config(self) -> BodyWithConfig: ...

    def fmt(self, f: Formatter) -> Result: ...

    def as_body(self) -> SendBody: ...

class BodyWithConfig:
    """Configuration of how to read the body.

Obtained via one of:

* [Body::with_config()]
* [Body::into_with_config()]

# Handling large responses

The `BodyWithConfig` is the primary way to increase the default 10MB size limit
when downloading large files to memory:

```
// Download a 50MB file
let large_data = ureq::get("http://httpbin.org/bytes/200000000")
.call()?
.body_mut()
.with_config()
.limit(50 * 1024 * 1024) // 50MB
.read_to_vec()?;
# Ok::<_, ureq::Error>(())
```"""

    def limit(self, value: int) -> Self: ...

    def lossy_utf8(self, value: bool) -> Self: ...

    def reader(self) -> BodyReader: ...

    def read_to_string(self) -> str: ...

    def read_to_vec(self) -> list[int]: ...

    def read_json(self) -> T: ...

class BodyReader:
    """A reader of the response data.

1. If `Transfer-Encoding: chunked`, the returned reader will unchunk it
and any `Content-Length` header is ignored.
2. If `Content-Encoding: gzip` (or `br`) and the corresponding feature
flag is enabled (**gzip** and **brotli**), decompresses the body data.
3. Given a header like `Content-Type: text/plain; charset=ISO-8859-1`
and the **charset** feature enabled, will translate the body to utf-8.
This mechanic need two components a mime-type starting `text/` and
a non-utf8 charset indication.
4. If `Content-Length` is set, the returned reader is limited to this byte
length regardless of how many bytes the server sends.
5. If no length header, the reader is until server stream end.
6. The limit in the body method used to obtain the reader.

Note: The reader is also limited by the [`Body::as_reader`] and
[`Body::into_reader`] calls. If that limit is set very high, a malicious
server might return enough bytes to exhaust available memory. If you're
making requests to untrusted servers, you should use set that
limit accordingly.

# Example

```
use std::io::Read;
let mut res = ureq::get("http://httpbin.org/bytes/100")
.call()?;

assert!(res.headers().contains_key("Content-Length"));
let len: usize = res.headers().get("Content-Length")
.unwrap().to_str().unwrap().parse().unwrap();

let mut bytes: Vec<u8> = Vec::with_capacity(len);
res.body_mut().as_reader()
.read_to_end(&mut bytes)?;

assert_eq!(bytes.len(), len);
# Ok::<_, ureq::Error>(())
```"""

    def read(self, buf: object) -> int: ...

class LossyUtf8Reader:

    def read(self, buf: object) -> int: ...

class BodyBuilder:
    """Builder for creating a response body.

This is useful for testing, or for [`Middleware`][crate::middleware::Middleware] that
returns another body than the requested one.

# Example

```
use ureq::Body;
use ureq::http::Response;

let body = Body::builder()
.mime_type("text/plain")
.charset("utf-8")
.data("Hello world!");

let mut response = Response::builder()
.status(200)
.header("content-type", "text/plain; charset=utf-8")
.body(body)?;

let text = response
.body_mut()
.read_to_string()?;

assert_eq!(text, "Hello world!");
# Ok::<_, ureq::Error>(())
```"""

    def mime_type(self, mime_type: object) -> Self: ...

    def charset(self, charset: object) -> Self: ...

    def limit(self, l: int) -> Self: ...

    def data(self, data: object) -> Body: ...

    def reader(self, data: object) -> Body: ...

class NativeTlsConnector:
    """Wrapper for TLS using native-tls.

Requires feature flag **native-tls**."""

    def connect(self, details: ConnectionDetails, chained: In | None) -> Out | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class NativeTlsTransport:

    def buffers(self) -> mutdynBuffers: ...

    def transmit_output(self, amount: int, timeout: NextTimeout) -> None: ...

    def await_input(self, timeout: NextTimeout) -> bool: ...

    def is_open(self) -> bool: ...

    def is_tls(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class Certificate:
    """An X509 certificate for a server or a client.

These are either used as trust roots, or client authentication.

The internal representation is DER form. The provided helpers for PEM
translates to DER."""

    @staticmethod
    def from_der(der: object) -> "Certificate": ...

    @staticmethod
    def from_pem(pem: object) -> "Certificate": ...

    def der(self) -> object: ...

    def to_owned(self) -> Certificate: ...

    def fmt(self, f: Formatter) -> Result: ...

class PrivateKey:
    """A private key used in client certificate auth.

The internal representation is DER form. The provided helpers for PEM
translates to DER.

Deliberately not `Clone` to avoid accidental copies in memory."""

    def as_ref(self) -> object: ...

    @staticmethod
    def from_der(kind: KeyKind, der: object) -> "PrivateKey": ...

    @staticmethod
    def from_pem(pem: object) -> "PrivateKey": ...

    def kind(self) -> KeyKind: ...

    def der(self) -> object: ...

    def to_owned(self) -> PrivateKey: ...

    def fmt(self, f: Formatter) -> Result: ...

class RustlsConnector:
    """Wrapper for TLS using rustls.

Requires feature flag **rustls**."""

    def connect(self, details: ConnectionDetails, chained: In | None) -> Out | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class RustlsTransport:

    def buffers(self) -> mutdynBuffers: ...

    def transmit_output(self, amount: int, timeout: NextTimeout) -> None: ...

    def await_input(self, timeout: NextTimeout) -> bool: ...

    def is_open(self) -> bool: ...

    def is_tls(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class TlsConfig:
    """Configuration of TLS.

This configuration is in common for both the different TLS mechanisms (available through
feature flags **rustls** and **native-tls**)."""

    @staticmethod
    def builder() -> TlsConfigBuilder: ...

    def provider(self) -> TlsProvider: ...

    def client_cert(self) -> object: ...

    def root_certs(self) -> RootCerts: ...

    def use_sni(self) -> bool: ...

    def disable_verification(self) -> bool: ...

    def unversioned_rustls_crypto_provider(self) -> object | None: ...

    @staticmethod
    def default() -> "TlsConfig": ...

    def fmt(self, f: Formatter) -> Result: ...

    def hash(self, state: H) -> None: ...

class TlsConfigBuilder:
    """Builder of [`TlsConfig`]"""

    def provider(self, v: TlsProvider) -> Self: ...

    def client_cert(self, v: ClientCert | None) -> Self: ...

    def root_certs(self, v: RootCerts) -> Self: ...

    def use_sni(self, v: bool) -> Self: ...

    def disable_verification(self, v: bool) -> Self: ...

    def unversioned_rustls_crypto_provider(self, v: object) -> Self: ...

    def build(self) -> TlsConfig: ...

class ClientCert:
    """A client certificate."""

    @staticmethod
    def new_with_certs(chain: object, key: PrivateKey) -> "ClientCert": ...

    def certs(self) -> object: ...

    def private_key(self) -> PrivateKey: ...

class CookieJar:
    """Collection of cookies.

The jar is accessed using [`Agent::cookie_jar_lock`][crate::Agent::cookie_jar_lock].
It can be saved and loaded."""

    def get(self, domain: str, path: str, name: str) -> Cookie | None: ...

    def remove(self, domain: str, path: str, name: str) -> Cookie | None: ...

    def insert(self, cookie: Cookie, uri: Uri) -> None: ...

    def clear(self) -> None: ...

    def iter(self) -> object: ...

    def save_json(self, writer: W) -> None: ...

    def load_json(self, reader: R) -> None: ...

    def release(self) -> None: ...

class Cookie:
    """Representation of an HTTP cookie.

Conforms to [IETF RFC6265](https://datatracker.ietf.org/doc/html/rfc6265)

## Constructing a `Cookie`

To construct a cookie it must be parsed and bound to a uri:

```
use ureq::Cookie;
use ureq::http::Uri;

let uri = Uri::from_static("https://my.server.com");
let cookie = Cookie::parse("name=value", &uri)?;
assert_eq!(cookie.to_string(), "name=value");
# Ok::<_, ureq::Error>(())
```"""

    @staticmethod
    def parse(cookie_str: S, uri: Uri) -> "Cookie": ...

    def name(self) -> str: ...

    def value(self) -> str: ...

    def fmt(self, f: Formatter) -> Result: ...

class Proxy:
    """Proxy server settings

This struct represents a proxy server configuration that can be used to route HTTP/HTTPS
requests through a proxy server. It supports various proxy protocols including HTTP CONNECT,
HTTPS CONNECT, SOCKS4, SOCKS4A, and SOCKS5.

# Protocol Support

* `HTTP`: HTTP CONNECT proxy
* `HTTPS`: HTTPS CONNECT proxy (requires a TLS provider)
* `SOCKS4`: SOCKS4 proxy (requires **socks-proxy** feature)
* `SOCKS4A`: SOCKS4A proxy (requires **socks-proxy** feature)
* `SOCKS5`: SOCKS5 proxy (requires **socks-proxy** feature)

# DNS Resolution

The `resolve_target` setting controls where DNS resolution happens:

* When `true`: DNS resolution happens locally before connecting to the proxy.
The resolved IP address is sent to the proxy.
* When `false`: The hostname is sent to the proxy, which performs DNS resolution.

Default behavior:
* For SOCKS4: `true` (local resolution required)
* For all other protocols: `false` (proxy performs resolution)

# Examples

```rust
use ureq::{Proxy, ProxyProtocol};

// Create a proxy from a URI string
let proxy = Proxy::new("http://localhost:8080").unwrap();

// Create a proxy using the builder pattern
let proxy = Proxy::builder(ProxyProtocol::Socks5)
.host("proxy.example.com")
.port(1080)
.username("user")
.password("pass")
.resolve_target(true)  // Force local DNS resolution
.build()
.unwrap();

// Read proxy settings from environment variables
if let Some(proxy) = Proxy::try_from_env() {
// Use proxy from environment
}
```"""

    @staticmethod
    def new(proxy: str) -> object: ...

    @staticmethod
    def builder(p: ProxyProtocol) -> ProxyBuilder: ...

    @staticmethod
    def try_from_env() -> object: ...

    def protocol(self) -> ProxyProtocol: ...

    def uri(self) -> Uri: ...

    def host(self) -> str: ...

    def port(self) -> int: ...

    def username(self) -> object: ...

    def password(self) -> object: ...

    def is_from_env(self) -> bool: ...

    def resolve_target(self) -> bool: ...

    def is_no_proxy(self, uri: Uri) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class ProxyBuilder:
    """Builder for configuring a proxy.

Obtained via [`Proxy::builder()`]."""

    def host(self, host: str) -> Self: ...

    def port(self, port: int) -> Self: ...

    def username(self, v: str) -> Self: ...

    def password(self, v: str) -> Self: ...

    def resolve_target(self, do_resolve: bool) -> Self: ...

    def no_proxy(self, expr: str) -> Self: ...

    def build(self) -> Proxy: ...

class AgentScope:
    """Typestate for [`Config`] when configured for an [`Agent`]."""

    def config(self) -> Config: ...

class RequestScope:
    """Typestate for [`Config`] when configured on the [`RequestBuilder`] level."""

    def config(self) -> Config: ...

class HttpCrateScope:
    """Typestate for for [`Config`] when configured via [`Agent::configure_request`]."""

    def config(self) -> Config: ...

class RequestExtScope:
    """Typestate for for [`Config`] when configured via [`crate::RequestExt::with_agent`]."""

    def config(self) -> Config: ...

class Config:
    """Config primarily for the [`Agent`], but also per-request.

Config objects are cheap to clone and should not incur any heap allocations.

# Agent level config

## Example

```
use ureq::Agent;
use std::time::Duration;

let config = Agent::config_builder()
.timeout_global(Some(Duration::from_secs(10)))
.https_only(true)
.build();

let agent = Agent::new_with_config(config);
```


# Request level config

The config can also be change per-request. Since every request ultimately executes
using an [`Agent`] (also the root-level `ureq::get(...)` have an implicit agent),
a request level config clones the agent level config.

There are two ways of getting a request level config.

## Request builder example

The first way is via [`RequestBuilder::config()`][crate::RequestBuilder::config].

```
use ureq::Agent;

let agent: Agent = Agent::config_builder()
.https_only(false)
.build()
.into();

let response = agent.get("http://httpbin.org/get")
.config()
// override agent level setting for this request
.https_only(true)
.build()
.call();
```

## HTTP request example

The second way is via [`Agent::configure_request()`][crate::Agent::configure_request].
This is used when working with the http crate [`http::Request`] type directly.

```
use ureq::{http, Agent};

let agent: Agent = Agent::config_builder()
.https_only(false)
.build()
.into();

let request = http::Request::get("http://httpbin.org/get")
.body(()).unwrap();

let request = agent.configure_request(request)
// override agent level setting for this request
.https_only(true)
.build();

let response = agent.run(request);
```
"""

    @staticmethod
    def builder() -> object: ...

    def new_agent(self) -> Agent: ...

    def http_status_as_error(self) -> bool: ...

    def https_only(self) -> bool: ...

    def ip_family(self) -> IpFamily: ...

    def tls_config(self) -> TlsConfig: ...

    def proxy(self) -> object: ...

    def no_delay(self) -> bool: ...

    def max_redirects(self) -> int: ...

    def max_redirects_will_error(self) -> bool: ...

    def redirect_auth_headers(self) -> RedirectAuthHeaders: ...

    def save_redirect_history(self) -> bool: ...

    def user_agent(self) -> AutoHeaderValue: ...

    def accept(self) -> AutoHeaderValue: ...

    def accept_encoding(self) -> AutoHeaderValue: ...

    def timeouts(self) -> Timeouts: ...

    def max_response_header_size(self) -> int: ...

    def input_buffer_size(self) -> int: ...

    def output_buffer_size(self) -> int: ...

    def max_idle_connections(self) -> int: ...

    def max_idle_connections_per_host(self) -> int: ...

    def max_idle_age(self) -> Duration: ...

    def allow_non_standard_methods(self) -> bool: ...

    @staticmethod
    def default() -> "Config": ...

    def fmt(self, f: Formatter) -> Result: ...

class ConfigBuilder:
    """Builder of [`Config`]"""

    def http_status_as_error(self, v: bool) -> Self: ...

    def https_only(self, v: bool) -> Self: ...

    def ip_family(self, v: IpFamily) -> Self: ...

    def tls_config(self, v: TlsConfig) -> Self: ...

    def proxy(self, v: Proxy | None) -> Self: ...

    def no_delay(self, v: bool) -> Self: ...

    def max_redirects(self, v: int) -> Self: ...

    def max_redirects_will_error(self, v: bool) -> Self: ...

    def redirect_auth_headers(self, v: RedirectAuthHeaders) -> Self: ...

    def save_redirect_history(self, v: bool) -> Self: ...

    def user_agent(self, v: object) -> Self: ...

    def accept(self, v: object) -> Self: ...

    def accept_encoding(self, v: object) -> Self: ...

    def max_response_header_size(self, v: int) -> Self: ...

    def input_buffer_size(self, v: int) -> Self: ...

    def output_buffer_size(self, v: int) -> Self: ...

    def max_idle_connections(self, v: int) -> Self: ...

    def max_idle_connections_per_host(self, v: int) -> Self: ...

    def max_idle_age(self, v: Duration) -> Self: ...

    def allow_non_standard_methods(self, v: bool) -> Self: ...

    def middleware(self, v: object) -> Self: ...

    def timeout_global(self, v: Duration | None) -> Self: ...

    def timeout_per_call(self, v: Duration | None) -> Self: ...

    def timeout_resolve(self, v: Duration | None) -> Self: ...

    def timeout_connect(self, v: Duration | None) -> Self: ...

    def timeout_send_request(self, v: Duration | None) -> Self: ...

    def timeout_await_100(self, v: Duration | None) -> Self: ...

    def timeout_send_body(self, v: Duration | None) -> Self: ...

    def timeout_recv_response(self, v: Duration | None) -> Self: ...

    def timeout_recv_body(self, v: Duration | None) -> Self: ...

    def build(self) -> Config: ...

    def build(self) -> object: ...

    def build(self) -> object: ...

    def build(self) -> object: ...

    def run(self) -> object: ...

class Timeouts:
    """Request timeout configuration.

This can be configured both on Agent level as well as per request."""

    @staticmethod
    def default() -> "Timeouts": ...

    def fmt(self, f: Formatter) -> Result: ...

class WithAgent:
    """Wrapper struct that holds a [`Request`] associated with an [`Agent`]."""

    def configure(self) -> object: ...

    def run(self) -> object: ...

class SendBody:
    """Request body for sending data via POST, PUT and PATCH.

Typically not interacted with directly since the trait [`AsSendBody`] is implemented
for the majority of the types of data a user might want to send to a remote server.
That means if you want to send things like `String`, `&str` or `[u8]`, they can be
used directly. See documentation for [`AsSendBody`].

The exception is when using [`Read`] trait bodies, in which case we wrap the request
body directly. See below [`SendBody::from_reader`].
"""

    @staticmethod
    def none() -> "SendBody": ...

    @staticmethod
    def from_reader(reader: object) -> "SendBody": ...

    @staticmethod
    def from_owned_reader(reader: object) -> "SendBody": ...

    @staticmethod
    def from_json(value: object) -> "SendBody": ...

    def into_reader(self) -> object: ...

    def as_body(self) -> SendBody: ...

    @staticmethod
    def from_(_: object) -> "SendBody": ...

class MiddlewareNext:
    """Continuation of a [`Middleware`] chain."""

    def handle(self, request: object) -> object: ...

class RequestBuilder:
    """Transparent wrapper around [`http::request::Builder`].

The purpose is to provide the [`.call()`][RequestBuilder::call] and [`.send()`][RequestBuilder::send]
and additional helpers for query parameters like [`.query()`][RequestBuilder::query] functions to
make an API for sending requests."""

    def method_ref(self) -> object: ...

    def header(self, key: K, value: V) -> Self: ...

    def headers_ref(self) -> object: ...

    def headers_mut(self) -> object: ...

    def query(self, key: K, value: V) -> Self: ...

    def query_raw(self, key: K, value: V) -> Self: ...

    def query_pairs(self, iter: I) -> Self: ...

    def query_pairs_raw(self, iter: I) -> Self: ...

    def uri(self, uri: T) -> Self: ...

    def uri_ref(self) -> object: ...

    def version(self, version: Version) -> Self: ...

    def version_ref(self) -> object: ...

    def config(self) -> object: ...

    def extension(self, extension: T) -> Self: ...

    def extensions_ref(self) -> object: ...

    def extensions_mut(self) -> object: ...

    def call(self) -> object: ...

    def force_send_body(self) -> object: ...

    def content_type(self, content_type: V) -> Self: ...

    def send(self, data: object) -> object: ...

    def send_empty(self) -> object: ...

    def send_form(self, iter: I) -> object: ...

    def send_json(self, data: object) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

class WithoutBody:
    """Typestate when [`RequestBuilder`] has no send body.

`RequestBuilder<WithoutBody>`

Methods: GET, DELETE, HEAD, OPTIONS, CONNECT, TRACE"""
    pass

class WithBody:
    """Typestate when [`RequestBuilder`] needs to a send body.

`RequestBuilder<WithBody>`

Methods: POST, PUT, PATCH"""
    pass

class Agent:
    """Agents keep state between requests.

By default, no state, such as cookies, is kept between requests.
But by creating an agent as entry point for the request, we
can keep a state.

# Example

```no_run
let mut agent = ureq::agent();

agent
.post("http://example.com/post/login")
.send(b"my password")?;

let secret = agent
.get("http://example.com/get/my-protected-page")
.call()?
.body_mut()
.read_to_string()?;

println!("Secret is: {}", secret);
# Ok::<_, ureq::Error>(())
```

# About threads and cloning

Agent uses inner [`Arc`]. Cloning an Agent results in an instance
that shares the same underlying connection pool and other state.

The connection pool contains an inner [`Mutex`][std::sync::Mutex] which is (briefly)
held when borrowing a pooled connection, or returning a connection to the pool.

All request functions in ureq have a signature similar to this:

```
# use ureq::{http, Body, AsSendBody, Error};
fn run(request: http::Request<impl AsSendBody>) -> Result<http::Response<Body>, Error> {
// <something>
# todo!()
}
```

It follows that:

* An Agent is borrowed for the duration of:
1. Sending the request header ([`http::Request`])
2. Sending the request body ([`SendBody`])
3. Receiving the response header ([`http::Response`])
* The [`Body`] of the response is not bound to the lifetime of the Agent.

A response [`Body`] can be streamed (for instance via [`Body::into_reader()`]). The [`Body`]
implements [`Send`], which means it's possible to read the response body on another thread than
the one that run the request. Behind the scenes, the [`Body`] retains the connection to the remote
server and it is returned to the agent's pool, once the Body instance (or reader) is dropped.

There is an asymmetry in that sending a request body will borrow the Agent instance, while receiving
the response body does not. This inconvenience is somewhat mitigated by that [`Agent::run()`] (or
going via the methods such as [`Agent::get()`]), borrows `&self`, i.e. not exclusive `mut` borrows.

That cloning the agent shares the connection pool is considered a feature. It is often useful to
retain a single pool for the entire process, while dispatching requests from different threads.
And if we want separate pools, we can create multiple agents via one of the constructors
(such as [`Agent::new_with_config()`]).

Note that both [`Config::clone()`] and [`Agent::clone()`] are  "cheap" meaning they should not
incur any heap allocation."""

    @staticmethod
    def new_with_defaults() -> "Agent": ...

    @staticmethod
    def new_with_config(config: Config) -> "Agent": ...

    @staticmethod
    def config_builder() -> object: ...

    @staticmethod
    def with_parts(config: Config, connector: object, resolver: object) -> "Agent": ...

    def cookie_jar_lock(self) -> CookieJar: ...

    def run(self, request: object) -> object: ...

    def config(self) -> Config: ...

    def configure_request(self, request: object) -> object: ...

    def get(self, uri: T) -> object: ...

    def post(self, uri: T) -> object: ...

    def put(self, uri: T) -> object: ...

    def delete(self, uri: T) -> object: ...

    def head(self, uri: T) -> object: ...

    def options(self, uri: T) -> object: ...

    def connect(self, uri: T) -> object: ...

    def patch(self, uri: T) -> object: ...

    def trace(self, uri: T) -> object: ...

    @staticmethod
    def from_(value: Config) -> "Agent": ...

    def fmt(self, f: Formatter) -> Result: ...

    def pool_count(self) -> int: ...

class NextTimeout:
    """A pair of [`Duration`] and [`Timeout`]."""

    def not_zero(self) -> Duration | None: ...

class Form:
    """A multipart/form-data request.

Use this to send multipart form data, which is commonly used for file uploads
and forms with mixed content types.

When using [`RequestBuilder::send()`](crate::RequestBuilder::send) with a `Form`,
the `Content-Type: multipart/form-data; boundary=...` header is automatically set.

# Examples

Basic usage with file upload:

```
# fn no_run() -> Result<(), ureq::Error> {
use ureq::unversioned::multipart::Form;

let form = Form::new()
.text("description", "My uploaded file")
.file("upload", "path/to/file.txt")?;

// Send the form as part of a POST request
let response = ureq::post("http://httpbin.org/post")
.send(form)?;
# Ok(())}
```

Uploading a file with custom filename and MIME type:

```
# fn no_run() -> Result<(), ureq::Error> {
use ureq::unversioned::multipart::{Form, Part};

let form = Form::new()
.text("description", "My uploaded file")
.part(
"upload",
// File path gives us no clue what it is
Part::file("path/to/file").unwrap()
// Override the file name
.file_name("avatar.jpg")
// Override the mime type
.mime_str("image/jpeg")?,
);

let response = ureq::post("http://httpbin.org/post")
.send(form)?;
# Ok(())}
```"""

    @staticmethod
    def default() -> "Form": ...

    @staticmethod
    def new() -> "Form": ...

    def boundary(self) -> str: ...

    def text(self, name: object, value: object) -> Self: ...

    def file(self, name: object, path: P) -> object: ...

    def part(self, name: object, part: Part) -> Self: ...

    def as_body(self) -> SendBody: ...

    def read(self, buf: object) -> int: ...

class Part:
    """A field in a multipart form.

This gives you more control over the part, such as setting the file name and/or mime type.

# Example

Uploading a file with custom filename and MIME type:

```
# fn no_run() -> Result<(), ureq::Error> {
use ureq::unversioned::multipart::{Form, Part};

let form = Form::new()
.text("description", "My uploaded file")
.part(
"upload",
// File path gives us no clue what it is
Part::file("path/to/file").unwrap()
// Override the file name
.file_name("avatar.jpg")
// Override the mime type
.mime_str("image/jpeg")?,
);

let response = ureq::post("http://httpbin.org/post")
.send(form)?;
# Ok(())}
```"""

    @staticmethod
    def text(text: object) -> "Part": ...

    @staticmethod
    def bytes(bytes: object) -> "Part": ...

    @staticmethod
    def reader(reader: object) -> "Part": ...

    @staticmethod
    def owned_reader(reader: object) -> "Part": ...

    @staticmethod
    def file(path: P) -> "Part": ...

    def file_name(self, name: str) -> Self: ...

    def mime_str(self, mime: str) -> object: ...

    def headers(self) -> HeaderMap: ...

class Instant:
    """Wrapper for [`std::time::Instant`] that provides additional time points in the past or future"""
    AlreadyHappened: "Instant"
    Exact: "Instant"
    NotHappening: "Instant"

    @staticmethod
    def now() -> "Instant": ...

    def add(self, rhs: Duration) -> Output: ...

    def partial_cmp(self, other: Self) -> Ordering | None: ...

    def cmp(self, other: Self) -> Ordering: ...

class Duration:
    """Wrapper for [`std::time::Duration`] that provides a duration to a distant future"""
    Exact: "Duration"
    NotHappening: "Duration"

    @staticmethod
    def from_secs(secs: int) -> "Duration": ...

    def is_not_happening(self) -> bool: ...

    def deref(self) -> Target: ...

    def partial_cmp(self, other: Self) -> Ordering | None: ...

    def cmp(self, other: Self) -> Ordering: ...

    @staticmethod
    def from_(value: Duration) -> "Duration": ...

class Either:
    """A selection between two transports."""
    A: "Either"
    B: "Either"

    def buffers(self) -> Buffers: ...

    def transmit_output(self, amount: int, timeout: NextTimeout) -> None: ...

    def await_input(self, timeout: NextTimeout) -> bool: ...

    def is_open(self) -> bool: ...

    def is_tls(self) -> bool: ...

class KeyKind:
    """The kind of private key.

* For **rustls** any kind is valid.
* For **native-tls** the only valid option is [`Pkcs8`](KeyKind::Pkcs8)."""
    Pkcs1: "KeyKind"
    Pkcs8: "KeyKind"
    Sec1: "KeyKind"

class PemItem:
    """Kinds of PEM data found by [`parse_pem`]"""
    Certificate: "PemItem"
    PrivateKey: "PemItem"

    @staticmethod
    def from_(value: Certificate) -> "PemItem": ...

    @staticmethod
    def from_(value: PrivateKey) -> "PemItem": ...

class TlsProvider:
    """Setting for which TLS provider to use.

Defaults to [`Rustls`][Self::Rustls] because this has the highest chance
to compile and "just work" straight out of the box without installing additional
development dependencies."""
    Rustls: "TlsProvider"
    NativeTls: "TlsProvider"

class RootCerts:
    """Configuration setting for root certs."""
    Specific: "RootCerts"
    PlatformVerifier: "RootCerts"
    WebPki: "RootCerts"

    @staticmethod
    def new_with_certs(certs: object) -> "RootCerts": ...

    @staticmethod
    def from_(value: I) -> "RootCerts": ...

class ProxyProtocol:
    """Proxy protocol"""
    Http: "ProxyProtocol"
    Https: "ProxyProtocol"
    Socks4: "ProxyProtocol"
    Socks4A: "ProxyProtocol"
    Socks5: "ProxyProtocol"

    @staticmethod
    def try_from(scheme: str) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class AutoHeaderValue:
    """Possible config values for headers.

* `None` no automatic header
* `Default` default behavior. I.e. for user-agent something like `ureq/3.1.2`
* `Provided` is a user provided header"""
    None_: "AutoHeaderValue"
    Default: "AutoHeaderValue"
    Provided: "AutoHeaderValue"

    @staticmethod
    def from_(value: S) -> "AutoHeaderValue": ...

class IpFamily:
    """Configuration of IP family to use.

Used to limit the IP to either IPv4, IPv6 or any."""
    Any: "IpFamily"
    Ipv4Only: "IpFamily"
    Ipv6Only: "IpFamily"

    def keep_wanted(self, iter: object) -> object: ...

class AgentRef:
    """Reference type to hold an owned or borrowed [`Agent`]."""
    Owned: "AgentRef"
    Borrowed: "AgentRef"

    @staticmethod
    def from_(value: Agent) -> "AgentRef": ...

    @staticmethod
    def from_(value: object) -> "AgentRef": ...

    def deref(self) -> Target: ...

class Timeout:
    """The various timeouts.

Each enum corresponds to a value in
[`ConfigBuilder::timeout_xxx`][crate::config::ConfigBuilder::timeout_global]."""
    Global: "Timeout"
    PerCall: "Timeout"
    Resolve: "Timeout"
    Connect: "Timeout"
    SendRequest: "Timeout"
    Await100: "Timeout"
    SendBody: "Timeout"
    RecvResponse: "Timeout"
    RecvBody: "Timeout"

    def fmt(self, f: Formatter) -> Result: ...

class Error:
    """Errors from ureq."""
    StatusCode: "Error"
    Http: "Error"
    BadUri: "Error"
    Protocol: "Error"
    Io: "Error"
    Timeout: "Error"
    HostNotFound: "Error"
    RedirectFailed: "Error"
    InvalidProxyUrl: "Error"
    ConnectionFailed: "Error"
    BodyExceedsLimit: "Error"
    TooManyRedirects: "Error"
    Tls: "Error"
    Pem: "Error"
    Rustls: "Error"
    NativeTls: "Error"
    Der: "Error"
    Cookie: "Error"
    CookieValue: "Error"
    CookieJar: "Error"
    UnknownCharset: "Error"
    RequireHttpsOnly: "Error"
    LargeResponseHeader: "Error"
    Decompress: "Error"
    Json: "Error"
    InvalidMimeType: "Error"
    ConnectProxyFailed: "Error"
    TlsRequired: "Error"
    Other: "Error"
    BodyStalled: "Error"

    def into_io(self) -> Exception: ...

    @staticmethod
    def from_(e: Exception) -> "Error": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(value: Exception) -> "Error": ...

    @staticmethod
    def from_(value: Exception) -> "Error": ...

    @staticmethod
    def from_(value: Exception) -> "Error": ...

    @staticmethod
    def from_(value: Exception) -> "Error": ...

    @staticmethod
    def from_(value: Exception) -> "Error": ...

    @staticmethod
    def from_(value: CookieError) -> "Error": ...

    @staticmethod
    def from_(value: Exception) -> "Error": ...

    @staticmethod
    def from_(value: Exception) -> "Error": ...

"""Helper for **_test** feature tests."""
def set_handler(pattern: object, status: int, headers: object, body: object) -> None: ...

"""Parser of PEM data.

The data may contain one or many PEM items. The iterator produces the recognized PEM
items and skip others."""
def parse_pem(pem: object) -> object: ...

"""Run a [`http::Request<impl AsSendBody>`]."""
def run(request: object) -> object: ...

"""A new [Agent] with default configuration

Agents are used to hold configuration and keep state between requests."""
def agent() -> Agent: ...

"""Make a GET request.

Run on a use-once [`Agent`]."""
def get(uri: T) -> object: ...

"""Make a POST request.

Run on a use-once [`Agent`]."""
def post(uri: T) -> object: ...

"""Make a PUT request.

Run on a use-once [`Agent`]."""
def put(uri: T) -> object: ...

"""Make a DELETE request.

Run on a use-once [`Agent`]."""
def delete(uri: T) -> object: ...

"""Make a HEAD request.

Run on a use-once [`Agent`]."""
def head(uri: T) -> object: ...

"""Make an OPTIONS request.

Run on a use-once [`Agent`]."""
def options(uri: T) -> object: ...

"""Make a CONNECT request.

Run on a use-once [`Agent`]."""
def connect(uri: T) -> object: ...

"""Make a PATCH request.

Run on a use-once [`Agent`]."""
def patch(uri: T) -> object: ...

"""Make a TRACE request.

Run on a use-once [`Agent`]."""
def trace(uri: T) -> object: ...

def init_test_log() -> None: ...

"""Percent-encode a string using the ENCODED_IN_QUERY set."""
def url_enc(i: str) -> object: ...

"""Percent-encode a string using the ENCODED_IN_QUERY set, but replace encoded `%20` with `+`."""
def form_url_enc(i: str) -> object: ...

__all__: list[str] = ["set_handler", "parse_pem", "run", "agent", "get", "post", "put", "delete", "head", "options", "connect", "patch", "trace", "init_test_log", "url_enc", "form_url_enc", "ConnectProxyConnector", "LazyBuffers", "ChainedConnector", "ConnectionDetails", "DefaultConnector", "TransportAdapter", "SocksConnector", "TcpConnector", "TcpTransport", "DefaultResolver", "Body", "BodyWithConfig", "BodyReader", "LossyUtf8Reader", "BodyBuilder", "NativeTlsConnector", "NativeTlsTransport", "Certificate", "PrivateKey", "RustlsConnector", "RustlsTransport", "TlsConfig", "TlsConfigBuilder", "ClientCert", "CookieJar", "Cookie", "Proxy", "ProxyBuilder", "AgentScope", "RequestScope", "HttpCrateScope", "RequestExtScope", "Config", "ConfigBuilder", "Timeouts", "WithAgent", "SendBody", "MiddlewareNext", "RequestBuilder", "WithoutBody", "WithBody", "Agent", "NextTimeout", "Form", "Part", "Instant", "Duration", "Either", "KeyKind", "PemItem", "TlsProvider", "RootCerts", "ProxyProtocol", "AutoHeaderValue", "IpFamily", "AgentRef", "Timeout", "Error"]
