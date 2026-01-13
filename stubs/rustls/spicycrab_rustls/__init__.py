"""Python stubs for the rustls Rust crate.

Install with: cookcrab install rustls
"""

from __future__ import annotations

from typing import Self

class RootCertStore:
    """A container for root certificates able to provide a root-of-trust
for connection authentication."""

    @staticmethod
    def empty() -> "RootCertStore": ...

    def add_parsable_certificates(self, der_certs: object) -> object: ...

    def add(self, der: CertificateDer) -> None: ...

    def subjects(self) -> list[DistinguishedName]: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    @staticmethod
    def from_iter(iter: T) -> "RootCertStore": ...

    def extend(self, iter: T) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

class ClientCertVerifierBuilder:
    """A builder for configuring a `webpki` client certificate verifier.

For more information, see the [`WebPkiClientVerifier`] documentation."""

    def clear_root_hint_subjects(self) -> Self: ...

    def add_root_hint_subjects(self, subjects: object) -> Self: ...

    def with_crls(self, crls: object) -> Self: ...

    def only_check_end_entity_revocation(self) -> Self: ...

    def allow_unauthenticated(self) -> Self: ...

    def allow_unknown_revocation_status(self) -> Self: ...

    def enforce_revocation_expiration(self) -> Self: ...

    def build(self) -> object: ...

class WebPkiClientVerifier:
    """A client certificate verifier that uses the `webpki` crate[^1] to perform client certificate
validation.

It must be created via the [`WebPkiClientVerifier::builder()`] or
[`WebPkiClientVerifier::builder_with_provider()`] functions.

Once built, the provided `Arc<dyn ClientCertVerifier>` can be used with a Rustls [`ServerConfig`]
to configure client certificate validation using [`with_client_cert_verifier`][ConfigBuilder<ClientConfig, WantsVerifier>::with_client_cert_verifier].

Example:

To require all clients present a client certificate issued by a trusted CA:
```no_run
# #[cfg(any(feature = "ring", feature = "aws_lc_rs"))] {
# use rustls::RootCertStore;
# use rustls::server::WebPkiClientVerifier;
# let roots = RootCertStore::empty();
let client_verifier = WebPkiClientVerifier::builder(roots.into())
.build()
.unwrap();
# }
```

Or, to allow clients presenting a client certificate authenticated by a trusted CA, or
anonymous clients that present no client certificate:
```no_run
# #[cfg(any(feature = "ring", feature = "aws_lc_rs"))] {
# use rustls::RootCertStore;
# use rustls::server::WebPkiClientVerifier;
# let roots = RootCertStore::empty();
let client_verifier = WebPkiClientVerifier::builder(roots.into())
.allow_unauthenticated()
.build()
.unwrap();
# }
```

If you wish to disable advertising client authentication:
```no_run
# use rustls::RootCertStore;
# use rustls::server::WebPkiClientVerifier;
# let roots = RootCertStore::empty();
let client_verifier = WebPkiClientVerifier::no_client_auth();
```

You can also configure the client verifier to check for certificate revocation with
client certificate revocation lists (CRLs):
```no_run
# #[cfg(any(feature = "ring", feature = "aws_lc_rs"))] {
# use rustls::RootCertStore;
# use rustls::server::{WebPkiClientVerifier};
# let roots = RootCertStore::empty();
# let crls = Vec::new();
let client_verifier = WebPkiClientVerifier::builder(roots.into())
.with_crls(crls)
.build()
.unwrap();
# }
```

[^1]: <https://github.com/rustls/webpki>"""

    @staticmethod
    def builder(roots: object) -> ClientCertVerifierBuilder: ...

    @staticmethod
    def builder_with_provider(roots: object, provider: object) -> ClientCertVerifierBuilder: ...

    @staticmethod
    def no_client_auth() -> object: ...

    def offer_client_auth(self) -> bool: ...

    def client_auth_mandatory(self) -> bool: ...

    def root_hint_subjects(self) -> object: ...

    def verify_client_cert(self, end_entity: CertificateDer, intermediates: object, now: UnixTime) -> ClientCertVerified: ...

    def verify_tls12_signature(self, message: object, cert: CertificateDer, dss: DigitallySignedStruct) -> HandshakeSignatureValid: ...

    def verify_tls13_signature(self, message: object, cert: CertificateDer, dss: DigitallySignedStruct) -> HandshakeSignatureValid: ...

    def supported_verify_schemes(self) -> list[SignatureScheme]: ...

class WebPkiSupportedAlgorithms:
    """Describes which `webpki` signature verification algorithms are supported and
how they map to TLS [`SignatureScheme`]s."""

    def supported_schemes(self) -> list[SignatureScheme]: ...

    def fips(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class ParsedCertificate:
    """Wrapper around internal representation of a parsed certificate.

This is used in order to avoid parsing twice when specifying custom verification"""

    def subject_public_key_info(self) -> SubjectPublicKeyInfoDer: ...

    @staticmethod
    def try_from(value: object) -> object: ...

class ServerCertVerifierBuilder:
    """A builder for configuring a `webpki` server certificate verifier.

For more information, see the [`WebPkiServerVerifier`] documentation."""

    def with_crls(self, crls: object) -> Self: ...

    def only_check_end_entity_revocation(self) -> Self: ...

    def allow_unknown_revocation_status(self) -> Self: ...

    def enforce_revocation_expiration(self) -> Self: ...

    def build(self) -> object: ...

class WebPkiServerVerifier:
    """Default `ServerCertVerifier`, see the trait impl for more information."""

    @staticmethod
    def builder(roots: object) -> ServerCertVerifierBuilder: ...

    @staticmethod
    def builder_with_provider(roots: object, provider: object) -> ServerCertVerifierBuilder: ...

    def verify_server_cert(self, end_entity: CertificateDer, intermediates: object, server_name: ServerName, ocsp_response: object, now: UnixTime) -> ServerCertVerified: ...

    def verify_tls12_signature(self, message: object, cert: CertificateDer, dss: DigitallySignedStruct) -> HandshakeSignatureValid: ...

    def verify_tls13_signature(self, message: object, cert: CertificateDer, dss: DigitallySignedStruct) -> HandshakeSignatureValid: ...

    def supported_verify_schemes(self) -> list[SignatureScheme]: ...

class KeyLogFile:
    """[`KeyLog`] implementation that opens a file whose name is
given by the `SSLKEYLOGFILE` environment variable, and writes
keys into it.

If `SSLKEYLOGFILE` is not set, this does nothing.

If such a file cannot be opened, or cannot be written then
this does nothing but logs errors at warning-level."""

    @staticmethod
    def new() -> "KeyLogFile": ...

    def log(self, label: str, client_random: object, secret: object) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

class Mutex:
    """A wrapper around [`std::sync::Mutex`]."""

    @staticmethod
    def new(data: T) -> "Mutex": ...

    def lock(self) -> object: ...

    @staticmethod
    def new(val: T) -> "Mutex": ...

    def lock(self) -> object: ...

class Mutex:
    """A no-std compatible wrapper around [`Lock`]."""

    @staticmethod
    def new(data: T) -> "Mutex": ...

    def lock(self) -> object: ...

    @staticmethod
    def new(val: T) -> "Mutex": ...

    def lock(self) -> object: ...

class Poisoned:
    """A marker type used to indicate `Lock::lock` failed due to a poisoned lock."""
    pass

class Tls13CipherSuite:
    """A TLS 1.3 cipher suite supported by rustls."""

    def can_resume_from(self, prev: object) -> object: ...

    def fips(self) -> bool: ...

    def quic_suite(self) -> Suite | None: ...

    def eq(self, other: Self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class Reader:
    """A structure that implements [`std::io::Read`] for reading plaintext."""

    def into_first_chunk(self) -> object: ...

    def read(self, buf: object) -> int: ...

    def read_buf(self, cursor: BorrowedCursor) -> object: ...

    def fill_buf(self) -> object: ...

    def consume(self, amt: int) -> None: ...

    @staticmethod
    def init(bytes: object) -> "Reader": ...

    def sub(self, length: int) -> object: ...

    def rest(self) -> object: ...

    def take(self, length: int) -> object: ...

    def any_left(self) -> bool: ...

    def expect_empty(self, name: object) -> None: ...

    def used(self) -> int: ...

    def left(self) -> int: ...

class Writer:
    """A structure that implements [`std::io::Write`] for writing plaintext."""

    def write(self, buf: object) -> int: ...

    def write_vectored(self, bufs: object) -> int: ...

    def flush(self) -> object: ...

class ConnectionCommon:
    """Interface shared by client and server connections."""

    def write(self, buf: object) -> int: ...

    def write_vectored(self, bufs: object) -> int: ...

    def flush(self) -> object: ...

    def process_new_packets(self) -> IoState: ...

    def export_keying_material(self, output: T, label: object, context: object) -> T: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def set_buffer_limit(self, limit: int | None) -> None: ...

    def refresh_traffic_keys(self) -> None: ...

    def reader(self) -> Reader: ...

    def writer(self) -> Writer: ...

    def complete_io(self, io: T) -> object: ...

    def read_tls(self, rd: Read) -> int: ...

    def write_tls(self, wr: Write) -> int: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    @staticmethod
    def from_(core: object) -> "ConnectionCommon": ...

    def quic_transport_parameters(self) -> object: ...

    def zero_rtt_keys(self) -> DirectionalKeys | None: ...

    def read_hs(self, plaintext: object) -> None: ...

    def write_hs(self, buf: list[int]) -> KeyChange | None: ...

    def alert(self) -> AlertDescription | None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    @staticmethod
    def from_(core: object) -> "ConnectionCommon": ...

class UnbufferedConnectionCommon:
    """Interface shared by unbuffered client and server connections."""

    @staticmethod
    def from_(core: object) -> "UnbufferedConnectionCommon": ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def deref(self) -> Target: ...

    def process_tls_records(self, incoming_tls: object) -> object: ...

    def process_tls_records(self, incoming_tls: object) -> object: ...

class KernelConnection:
    """A kernel connection.

This does not directly wrap a kernel connection, rather it gives you the
minimal interfaces you need to implement a well-behaved TLS connection on
top of kTLS.

See the [`crate::kernel`] module docs for more details."""

    def negotiated_cipher_suite(self) -> SupportedCipherSuite: ...

    def protocol_version(self) -> ProtocolVersion: ...

    def update_tx_secret(self) -> object: ...

    def update_rx_secret(self) -> object: ...

    def handle_new_session_ticket(self, payload: object) -> None: ...

class UnbufferedStatus:
    """The current status of the `UnbufferedConnection*`"""
    pass

class ReadTraffic:
    """Application data is available"""

    def next_record(self) -> AppDataRecord | None: ...

    def peek_len(self) -> NonZeroUsize | None: ...

class ReadEarlyData:
    """Early application-data is available."""

    def next_record(self) -> AppDataRecord | None: ...

    def peek_len(self) -> NonZeroUsize | None: ...

    def read(self, buf: object) -> int: ...

    def read_buf(self, cursor: BorrowedCursor) -> object: ...

class AppDataRecord:
    """A decrypted application-data record"""
    pass

class WriteTraffic:
    """Allows encrypting app-data"""

    def encrypt(self, application_data: object, outgoing_tls: object) -> int: ...

    def queue_close_notify(self, outgoing_tls: object) -> int: ...

    def refresh_traffic_keys(self) -> None: ...

class EncodeTlsData:
    """A handshake record must be encoded"""

    def encode(self, outgoing_tls: object) -> int: ...

class TransmitTlsData:
    """Previously encoded TLS data must be transmitted"""

    def done(self) -> None: ...

    def may_encrypt_app_data(self) -> object: ...

    def may_encrypt_early_data(self) -> MayEncryptEarlyData | None: ...

class InsufficientSizeError:
    """Provided buffer was too small"""
    pass

class NoKeyLog:
    """KeyLog that does exactly nothing."""

    def log(self, _: str, _1: object, _2: object) -> None: ...

    def will_log(self, _label: str) -> bool: ...

class DefaultTimeProvider:
    """Default `TimeProvider` implementation that uses `std`"""

    def current_time(self) -> UnixTime | None: ...

class ClientConnection:
    """A QUIC client connection."""

    @staticmethod
    def new(config: object, quic_version: Version, name: ServerName, params: list[int]) -> object: ...

    @staticmethod
    def new_with_alpn(config: object, quic_version: Version, name: ServerName, params: list[int], alpn_protocols: list[list[int]]) -> object: ...

    def is_early_data_accepted(self) -> bool: ...

    def tls13_tickets_received(self) -> int: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(config: object, name: ServerName) -> object: ...

    @staticmethod
    def new_with_alpn(config: object, name: ServerName, alpn_protocols: list[list[int]]) -> object: ...

    def early_data(self) -> WriteEarlyData | None: ...

    def is_early_data_accepted(self) -> bool: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def ech_status(self) -> EchStatus: ...

    def tls13_tickets_received(self) -> int: ...

    def fips(self) -> bool: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

class ServerConnection:
    """A QUIC server connection."""

    @staticmethod
    def new(config: object, quic_version: Version, params: list[int]) -> object: ...

    def reject_early_data(self) -> None: ...

    def server_name(self) -> object: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(config: object) -> object: ...

    def server_name(self) -> object: ...

    def received_resumption_data(self) -> object: ...

    def set_resumption_data(self, data: object) -> None: ...

    def reject_early_data(self) -> None: ...

    def early_data(self) -> ReadEarlyData | None: ...

    def fips(self) -> bool: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def fmt(self, f: Formatter) -> Result: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

class ConnectionCommon:
    """A shared interface for QUIC connections."""

    def write(self, buf: object) -> int: ...

    def write_vectored(self, bufs: object) -> int: ...

    def flush(self) -> object: ...

    def process_new_packets(self) -> IoState: ...

    def export_keying_material(self, output: T, label: object, context: object) -> T: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def set_buffer_limit(self, limit: int | None) -> None: ...

    def refresh_traffic_keys(self) -> None: ...

    def reader(self) -> Reader: ...

    def writer(self) -> Writer: ...

    def complete_io(self, io: T) -> object: ...

    def read_tls(self, rd: Read) -> int: ...

    def write_tls(self, wr: Write) -> int: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    @staticmethod
    def from_(core: object) -> "ConnectionCommon": ...

    def quic_transport_parameters(self) -> object: ...

    def zero_rtt_keys(self) -> DirectionalKeys | None: ...

    def read_hs(self, plaintext: object) -> None: ...

    def write_hs(self, buf: list[int]) -> KeyChange | None: ...

    def alert(self) -> AlertDescription | None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    @staticmethod
    def from_(core: object) -> "ConnectionCommon": ...

class Secrets:
    """Secrets used to encrypt/decrypt traffic"""

    def next_packet_keys(self) -> PacketKeySet: ...

class DirectionalKeys:
    """Keys used to communicate in a single direction"""
    pass

class Tag:
    """Authentication tag from an AEAD seal operation."""

    @staticmethod
    def from_(value: object) -> "Tag": ...

    def as_ref(self) -> object: ...

    @staticmethod
    def new(bytes: object) -> "Tag": ...

    def drop(self) -> None: ...

    def as_ref(self) -> object: ...

class PacketKeySet:
    """Packet protection keys for bidirectional 1-RTT communication"""
    pass

class Suite:
    """Produces QUIC initial keys from a TLS 1.3 ciphersuite and a QUIC key generation algorithm."""

    def keys(self, client_dst_connection_id: object, side: Side, version: Version) -> Keys: ...

class Keys:
    """Complete set of keys used to communicate with the peer"""

    @staticmethod
    def initial(version: Version, suite: object, quic: object, client_dst_connection_id: object, side: Side) -> "Keys": ...

class ClientHello:
    """A struct representing the received Client Hello"""

    def server_name(self) -> object: ...

    def signature_schemes(self) -> object: ...

    def alpn(self) -> object: ...

    def cipher_suites(self) -> object: ...

    def server_cert_types(self) -> object: ...

    def client_cert_types(self) -> object: ...

    def certificate_authorities(self) -> object: ...

    def named_groups(self) -> object: ...

class ServerConfig:
    """Common configuration for a set of server sessions.

Making one of these is cheap, though one of the inputs may be expensive: gathering trust roots
from the operating system to add to the [`RootCertStore`] passed to a `ClientCertVerifier`
builder may take on the order of a few hundred milliseconds.

These must be created via the [`ServerConfig::builder()`] or [`ServerConfig::builder_with_provider()`]
function.

# Defaults

* [`ServerConfig::max_fragment_size`]: the default is `None` (meaning 16kB).
* [`ServerConfig::session_storage`]: if the `std` feature is enabled, the default stores 256
sessions in memory. If the `std` feature is not enabled, the default is to not store any
sessions. In a no-std context, by enabling the `hashbrown` feature you may provide your
own `session_storage` using [`ServerSessionMemoryCache`] and a `crate::lock::MakeMutex`
implementation.
* [`ServerConfig::alpn_protocols`]: the default is empty -- no ALPN protocol is negotiated.
* [`ServerConfig::key_log`]: key material is not logged.
* [`ServerConfig::send_tls13_tickets`]: 2 tickets are sent.
* [`ServerConfig::cert_compressors`]: depends on the crate features, see [`compress::default_cert_compressors()`].
* [`ServerConfig::cert_compression_cache`]: caches the most recently used 4 compressions
* [`ServerConfig::cert_decompressors`]: depends on the crate features, see [`compress::default_cert_decompressors()`].

# Sharing resumption storage between `ServerConfig`s

In a program using many `ServerConfig`s it may improve resumption rates
(which has a significant impact on connection performance) if those
configs share [`ServerConfig::session_storage`] or [`ServerConfig::ticketer`].

However, caution is needed: other fields influence the security of a session
and resumption between them can be surprising.  If sharing
[`ServerConfig::session_storage`] or [`ServerConfig::ticketer`] between two
`ServerConfig`s, you should also evaluate the following fields and ensure
they are equivalent:

* `ServerConfig::verifier` -- client authentication requirements,
* [`ServerConfig::cert_resolver`] -- server identities.

To illustrate, imagine two `ServerConfig`s `A` and `B`.  `A` requires
client authentication, `B` does not.  If `A` and `B` shared a resumption store,
it would be possible for a session originated by `B` (that is, an unauthenticated client)
to be inserted into the store, and then resumed by `A`.  This would give a false
impression to the user of `A` that the client was authenticated.  This is possible
whether the resumption is performed statefully (via [`ServerConfig::session_storage`])
or statelessly (via [`ServerConfig::ticketer`]).

_Unlike_ `ClientConfig`, rustls does not enforce any policy here.

[`RootCertStore`]: crate::RootCertStore
[`ServerSessionMemoryCache`]: crate::server::handy::ServerSessionMemoryCache"""

    @staticmethod
    def builder() -> object: ...

    @staticmethod
    def builder_with_protocol_versions(versions: object) -> object: ...

    @staticmethod
    def builder_with_provider(provider: object) -> object: ...

    @staticmethod
    def builder_with_details(provider: object, time_provider: object) -> object: ...

    def fips(self) -> bool: ...

    def crypto_provider(self) -> object: ...

class ReadEarlyData:
    """Allows reading of early data in resumed TLS1.3 connections.

"Early data" is also known as "0-RTT data".

This structure implements [`std::io::Read`]."""

    def next_record(self) -> AppDataRecord | None: ...

    def peek_len(self) -> NonZeroUsize | None: ...

    def read(self, buf: object) -> int: ...

    def read_buf(self, cursor: BorrowedCursor) -> object: ...

class ServerConnection:
    """This represents a single TLS server connection.

Send TLS-protected data to the peer using the `io::Write` trait implementation.
Read data from the peer using the `io::Read` trait implementation."""

    @staticmethod
    def new(config: object, quic_version: Version, params: list[int]) -> object: ...

    def reject_early_data(self) -> None: ...

    def server_name(self) -> object: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(config: object) -> object: ...

    def server_name(self) -> object: ...

    def received_resumption_data(self) -> object: ...

    def set_resumption_data(self, data: object) -> None: ...

    def reject_early_data(self) -> None: ...

    def early_data(self) -> ReadEarlyData | None: ...

    def fips(self) -> bool: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def fmt(self, f: Formatter) -> Result: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

class Acceptor:
    """Handle a server-side connection before configuration is available.

`Acceptor` allows the caller to choose a [`ServerConfig`] after reading
the [`super::ClientHello`] of an incoming connection. This is useful for servers
that choose different certificates or cipher suites based on the
characteristics of the `ClientHello`. In particular it is useful for
servers that need to do some I/O to load a certificate and its private key
and don't want to use the blocking interface provided by
[`super::ResolvesServerCert`].

Create an Acceptor with [`Acceptor::default()`].

# Example

```no_run
# #[cfg(feature = "aws_lc_rs")] {
# fn choose_server_config(
#     _: rustls::server::ClientHello,
# ) -> std::sync::Arc<rustls::ServerConfig> {
#     unimplemented!();
# }
# #[allow(unused_variables)]
# fn main() {
use rustls::server::{Acceptor, ServerConfig};
let listener = std::net::TcpListener::bind("127.0.0.1:0").unwrap();
for stream in listener.incoming() {
let mut stream = stream.unwrap();
let mut acceptor = Acceptor::default();
let accepted = loop {
acceptor.read_tls(&mut stream).unwrap();
if let Some(accepted) = acceptor.accept().unwrap() {
break accepted;
}
};

// For some user-defined choose_server_config:
let config = choose_server_config(accepted.client_hello());
let conn = accepted
.into_connection(config)
.unwrap();

// Proceed with handling the ServerConnection.
}
# }
# }
```"""

    @staticmethod
    def default() -> "Acceptor": ...

    def read_tls(self, rd: Read) -> int: ...

    def accept(self) -> Accepted | None: ...

class AcceptedAlert:
    """Represents a TLS alert resulting from handling the client's `ClientHello` message.

When [`Acceptor::accept()`] returns an error, it yields an `AcceptedAlert` such that the
application can communicate failure to the client via [`AcceptedAlert::write()`]."""

    def write(self, wr: Write) -> int: ...

    def write_all(self, wr: Write) -> None: ...

    @staticmethod
    def from_(conn: object) -> "AcceptedAlert": ...

    def fmt(self, f: Formatter) -> Result: ...

class UnbufferedServerConnection:
    """Unbuffered version of `ServerConnection`

See the [`crate::unbuffered`] module docs for more details"""

    @staticmethod
    def new(config: object) -> object: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def dangerous_into_kernel_connection(self) -> object: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

class Accepted:
    """Represents a `ClientHello` message received through the [`Acceptor`].

Contains the state required to resume the connection through [`Accepted::into_connection()`]."""

    def client_hello(self) -> ClientHello: ...

    def into_connection(self, config: object) -> ServerConnection: ...

    def fmt(self, f: Formatter) -> Result: ...

class ServerConnectionData:
    """State associated with a server connection."""
    pass

class NoServerSessionStorage:
    """Something which never stores sessions."""

    def put(self, _id: list[int], _sec: list[int]) -> bool: ...

    def get(self, _id: object) -> list[int] | None: ...

    def take(self, _id: object) -> list[int] | None: ...

    def can_cache(self) -> bool: ...

class ServerSessionMemoryCache:
    """An implementer of `StoresServerSessions` that stores everything
in memory.  If enforces a limit on the number of stored sessions
to bound memory usage."""

    @staticmethod
    def new(size: int) -> object: ...

    @staticmethod
    def new(size: int) -> object: ...

    def put(self, key: list[int], value: list[int]) -> bool: ...

    def get(self, key: object) -> list[int] | None: ...

    def take(self, key: object) -> list[int] | None: ...

    def can_cache(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class AlwaysResolvesServerRawPublicKeys:
    """An exemplar `ResolvesServerCert` implementation that always resolves to a single
[RFC 7250] raw public key.

[RFC 7250]: https://tools.ietf.org/html/rfc7250"""

    @staticmethod
    def new(certified_key: object) -> "AlwaysResolvesServerRawPublicKeys": ...

    def resolve(self, _client_hello: ClientHello) -> object | None: ...

    def only_raw_public_keys(self) -> bool: ...

class ResolvesServerCertUsingSni:
    """Something that resolves do different cert chains/keys based
on client-supplied server name (via SNI)."""

    @staticmethod
    def new() -> "ResolvesServerCertUsingSni": ...

    def add(self, name: str, ck: CertifiedKey) -> None: ...

    def resolve(self, client_hello: ClientHello) -> object | None: ...

class WantsServerCert:
    """A config builder state where the caller must supply how to provide a server certificate to
the connecting peer.

For more information, see the [`ConfigBuilder`] documentation."""
    pass

class CipherSuiteCommon:
    """Common state for cipher suites (both for TLS 1.2 and TLS 1.3)"""

    def fips(self) -> bool: ...

class ExtractedSecrets:
    """Secrets for transmitting/receiving data over a TLS session.

After performing a handshake with rustls, these secrets can be extracted
to configure kTLS for a socket, and have the kernel take over encryption
and/or decryption."""
    pass

class SupportedProtocolVersion:
    """A TLS protocol version supported by rustls.

All possible instances of this class are provided by the library in
the [`ALL_VERSIONS`] array, as well as individually as [`TLS12`]
and [`TLS13`]."""

    def fmt(self, f: Formatter) -> Result: ...

class Tls12CipherSuite:
    """A TLS 1.2 cipher suite supported by rustls."""

    def resolve_sig_schemes(self, offered: object) -> list[SignatureScheme]: ...

    def fips(self) -> bool: ...

    def eq(self, other: Self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class ConfigBuilder:
    """A [builder] for [`ServerConfig`] or [`ClientConfig`] values.

To get one of these, call [`ServerConfig::builder()`] or [`ClientConfig::builder()`].

To build a config, you must make at least two decisions (in order):

- How should this client or server verify certificates provided by its peer?
- What certificates should this client or server present to its peer?

For settings besides these, see the fields of [`ServerConfig`] and [`ClientConfig`].

The usual choice for protocol primitives is to call
[`ClientConfig::builder`]/[`ServerConfig::builder`]
which will use rustls' default cryptographic provider and safe defaults for ciphersuites and
supported protocol versions.

```
# #[cfg(feature = "aws_lc_rs")] {
# rustls::crypto::aws_lc_rs::default_provider().install_default();
use rustls::{ClientConfig, ServerConfig};
ClientConfig::builder()
//  ...
# ;

ServerConfig::builder()
//  ...
# ;
# }
```

You may also override the choice of protocol versions:

```no_run
# #[cfg(feature = "aws_lc_rs")] {
# rustls::crypto::aws_lc_rs::default_provider().install_default();
# use rustls::ServerConfig;
ServerConfig::builder_with_protocol_versions(&[&rustls::version::TLS13])
//  ...
# ;
# }
```

Overriding the default cryptographic provider introduces a `Result` that must be unwrapped,
because the config builder checks for consistency of the choices made. For instance, it's an error to
configure only TLS 1.2 cipher suites while specifying that TLS 1.3 should be the only supported protocol
version.

If you configure a smaller set of protocol primitives than the default, you may get a smaller binary,
since the code for the unused ones can be optimized away at link time.

After choosing protocol primitives, you must choose (a) how to verify certificates and (b) what certificates
(if any) to send to the peer. The methods to do this are specific to whether you're building a ClientConfig
or a ServerConfig, as tracked by the [`ConfigSide`] type parameter on the various impls of ConfigBuilder.

# ClientConfig certificate configuration

For a client, _certificate verification_ must be configured either by calling one of:
- [`ConfigBuilder::with_root_certificates`] or
- [`ConfigBuilder::dangerous()`] and [`DangerousClientConfigBuilder::with_custom_certificate_verifier`]

Next, _certificate sending_ (also known as "client authentication", "mutual TLS", or "mTLS") must be configured
or disabled using one of:
- [`ConfigBuilder::with_no_client_auth`] - to not send client authentication (most common)
- [`ConfigBuilder::with_client_auth_cert`] - to always send a specific certificate
- [`ConfigBuilder::with_client_cert_resolver`] - to send a certificate chosen dynamically

For example:

```
# #[cfg(feature = "aws_lc_rs")] {
# rustls::crypto::aws_lc_rs::default_provider().install_default();
# use rustls::ClientConfig;
# let root_certs = rustls::RootCertStore::empty();
ClientConfig::builder()
.with_root_certificates(root_certs)
.with_no_client_auth();
# }
```

# ServerConfig certificate configuration

For a server, _certificate verification_ must be configured by calling one of:
- [`ConfigBuilder::with_no_client_auth`] - to not require client authentication (most common)
- [`ConfigBuilder::with_client_cert_verifier`] - to use a custom verifier

Next, _certificate sending_ must be configured by calling one of:
- [`ConfigBuilder::with_single_cert`] - to send a specific certificate
- [`ConfigBuilder::with_single_cert_with_ocsp`] - to send a specific certificate, plus stapled OCSP
- [`ConfigBuilder::with_cert_resolver`] - to send a certificate chosen dynamically

For example:

```no_run
# #[cfg(feature = "aws_lc_rs")] {
# rustls::crypto::aws_lc_rs::default_provider().install_default();
# use rustls::ServerConfig;
# let certs = vec![];
# let private_key = pki_types::PrivateKeyDer::from(
#    pki_types::PrivatePkcs8KeyDer::from(vec![])
# );
ServerConfig::builder()
.with_no_client_auth()
.with_single_cert(certs, private_key)
.expect("bad certificate/key");
# }
```

# Types

ConfigBuilder uses the [typestate] pattern to ensure at compile time that each required
configuration item is provided exactly once. This is tracked in the `State` type parameter,
which can have these values:

- [`WantsVersions`]
- [`WantsVerifier`]
- [`WantsClientCert`]
- [`WantsServerCert`]

The other type parameter is `Side`, which is either `ServerConfig` or `ClientConfig`
depending on whether the ConfigBuilder was built with [`ServerConfig::builder()`] or
[`ClientConfig::builder()`].

You won't need to write out either of these type parameters explicitly. If you write a
correct chain of configuration calls they will be used automatically. If you write an
incorrect chain of configuration calls you will get an error message from the compiler
mentioning some of these types.

Additionally, ServerConfig and ClientConfig carry a private field containing a
[`CryptoProvider`], from [`ClientConfig::builder_with_provider()`] or
[`ServerConfig::builder_with_provider()`]. This determines which cryptographic backend
is used. The default is [the process-default provider](`CryptoProvider::get_default`).

[builder]: https://rust-unofficial.github.io/patterns/patterns/creational/builder.html
[typestate]: http://cliffle.com/blog/rust-typestate/
[`ServerConfig`]: crate::ServerConfig
[`ServerConfig::builder`]: crate::ServerConfig::builder
[`ClientConfig`]: crate::ClientConfig
[`ClientConfig::builder()`]: crate::ClientConfig::builder()
[`ServerConfig::builder()`]: crate::ServerConfig::builder()
[`ClientConfig::builder_with_provider()`]: crate::ClientConfig::builder_with_provider()
[`ServerConfig::builder_with_provider()`]: crate::ServerConfig::builder_with_provider()
[`ConfigBuilder<ClientConfig, WantsVerifier>`]: struct.ConfigBuilder.html#impl-3
[`ConfigBuilder<ServerConfig, WantsVerifier>`]: struct.ConfigBuilder.html#impl-6
[`WantsClientCert`]: crate::client::WantsClientCert
[`WantsServerCert`]: crate::server::WantsServerCert
[`CryptoProvider::get_default`]: crate::crypto::CryptoProvider::get_default
[`DangerousClientConfigBuilder::with_custom_certificate_verifier`]: crate::client::danger::DangerousClientConfigBuilder::with_custom_certificate_verifier"""

    def with_client_cert_verifier(self, client_cert_verifier: object) -> object: ...

    def with_no_client_auth(self) -> object: ...

    def with_single_cert(self, cert_chain: list[CertificateDer], key_der: PrivateKeyDer) -> ServerConfig: ...

    def with_single_cert_with_ocsp(self, cert_chain: list[CertificateDer], key_der: PrivateKeyDer, ocsp: list[int]) -> ServerConfig: ...

    def with_cert_resolver(self, cert_resolver: object) -> ServerConfig: ...

    def crypto_provider(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    def with_safe_default_protocol_versions(self) -> object: ...

    def with_protocol_versions(self, versions: object) -> object: ...

    def with_ech(self, mode: EchMode) -> object: ...

    def with_root_certificates(self, root_store: object) -> object: ...

    def with_webpki_verifier(self, verifier: object) -> object: ...

    def dangerous(self) -> DangerousClientConfigBuilder: ...

    def with_client_auth_cert(self, cert_chain: list[CertificateDer], key_der: PrivateKeyDer) -> ClientConfig: ...

    def with_no_client_auth(self) -> ClientConfig: ...

    def with_client_cert_resolver(self, client_auth_cert_resolver: object) -> ClientConfig: ...

class WantsVersions:
    """Config builder state where the caller must supply TLS protocol versions.

For more information, see the [`ConfigBuilder`] documentation."""
    pass

class WantsVerifier:
    """Config builder state where the caller must supply a verifier.

For more information, see the [`ConfigBuilder`] documentation."""
    pass

class MessageFragmenter:

    @staticmethod
    def default() -> "MessageFragmenter": ...

    def fragment_message(self, msg: object) -> object: ...

    def set_max_fragment_size(self, max_fragment_size: int | None) -> None: ...

class InboundOpaqueMessage:
    """A TLS frame, named TLSPlaintext in the standard.

This inbound type borrows its encrypted payload from a buffer elsewhere.
It is used for joining and is consumed by decryption."""

    @staticmethod
    def new(typ: ContentType, version: ProtocolVersion, payload: object) -> "InboundOpaqueMessage": ...

    def into_plain_message(self) -> InboundPlainMessage: ...

    def into_plain_message_range(self, range: object) -> InboundPlainMessage: ...

    def into_tls13_unpadded_message(self) -> InboundPlainMessage: ...

class BorrowedPayload:

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def truncate(self, len: int) -> None: ...

class InboundPlainMessage:
    """A TLS frame, named `TLSPlaintext` in the standard.

This inbound type borrows its decrypted payload from the original buffer.
It results from decryption."""
    pass

class OutboundPlainMessage:
    """A TLS frame, named `TLSPlaintext` in the standard.

This outbound type borrows its "to be encrypted" payload from the "user".
It is used for fragmenting and is consumed by encryption."""
    pass

class OutboundOpaqueMessage:
    """A TLS frame, named `TLSPlaintext` in the standard.

This outbound type owns all memory for its interior parts.
It results from encryption and is used for io write."""

    @staticmethod
    def new(typ: ContentType, version: ProtocolVersion, payload: PrefixedPayload) -> "OutboundOpaqueMessage": ...

    @staticmethod
    def read(r: Reader) -> object: ...

    def encode(self) -> list[int]: ...

    def into_plain_message(self) -> PlainMessage: ...

class PrefixedPayload:

    @staticmethod
    def with_capacity(capacity: int) -> "PrefixedPayload": ...

    def extend_from_slice(self, slice: object) -> None: ...

    def extend_from_chunks(self, chunks: OutboundChunks) -> None: ...

    def truncate(self, len: int) -> None: ...

    def as_ref(self) -> object: ...

    def as_mut(self) -> object: ...

    def extend(self, iter: T) -> None: ...

    @staticmethod
    def from_(content: object) -> "PrefixedPayload": ...

    @staticmethod
    def from_(content: object) -> "PrefixedPayload": ...

class PlainMessage:
    """A decrypted TLS frame

This type owns all memory for its interior parts. It can be decrypted from an OpaqueMessage
or encrypted into an OpaqueMessage, and it is also used for joining and fragmenting."""

    @staticmethod
    def from_(msg: Message) -> "PlainMessage": ...

    def into_unencrypted_opaque(self) -> OutboundOpaqueMessage: ...

    def borrow_inbound(self) -> InboundPlainMessage: ...

    def borrow_outbound(self) -> OutboundPlainMessage: ...

class Message:
    """A message with decoded payload"""

    def is_handshake_type(self, hstyp: HandshakeType) -> bool: ...

    @staticmethod
    def build_alert(level: AlertLevel, desc: AlertDescription) -> "Message": ...

    @staticmethod
    def build_key_update_notify() -> "Message": ...

    @staticmethod
    def build_key_update_request() -> "Message": ...

    @staticmethod
    def try_from(plain: PlainMessage) -> object: ...

    @staticmethod
    def try_from(plain: InboundPlainMessage) -> object: ...

class Tls13ClientSessionValue:

    def max_early_data_size(self) -> int: ...

    def suite(self) -> object: ...

    def rewind_epoch(self, delta: int) -> None: ...

    def _private_set_max_early_data_size(self, new: int) -> None: ...

    def set_quic_params(self, quic_params: object) -> None: ...

    def quic_params(self) -> list[int]: ...

    def deref(self) -> Target: ...

class Tls12ClientSessionValue:

    def rewind_epoch(self, delta: int) -> None: ...

    def deref(self) -> Target: ...

class ClientSessionCommon:
    pass

class ServerSessionValue:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class PayloadU16:
    """An arbitrary, unknown-content, u16-length-prefixed payload

The `C` type parameter controls whether decoded values may
be empty."""

    @staticmethod
    def new(bytes: list[int]) -> "PayloadU16": ...

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class MaybeEmpty:
    pass

class NonEmpty:
    pass

class ChangeCipherSpecPayload:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class Reader:
    """Wrapper over a slice of bytes that allows reading chunks from
with the current position state held using a cursor.

A new reader for a sub section of the buffer can be created
using the `sub` function or a section of a certain length can
be obtained using the `take` function"""

    def into_first_chunk(self) -> object: ...

    def read(self, buf: object) -> int: ...

    def read_buf(self, cursor: BorrowedCursor) -> object: ...

    def fill_buf(self) -> object: ...

    def consume(self, amt: int) -> None: ...

    @staticmethod
    def init(bytes: object) -> "Reader": ...

    def sub(self, length: int) -> object: ...

    def rest(self) -> object: ...

    def take(self, length: int) -> object: ...

    def any_left(self) -> bool: ...

    def expect_empty(self, name: object) -> None: ...

    def used(self) -> int: ...

    def left(self) -> int: ...

class u24:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class FfdheGroup:
    """Parameters of an FFDHE group, with Big-endian byte order"""

    @staticmethod
    def from_named_group(named_group: NamedGroup) -> object: ...

    def named_group(self) -> NamedGroup | None: ...

    @staticmethod
    def from_params_trimming_leading_zeros(p: object, g: object) -> "FfdheGroup": ...

class UnknownExtension:
    pass

class HandshakeMessagePayload:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class HpkeSymmetricCipherSuite:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class HpkeKeyConfig:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class EchConfigContents:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class AlertMessagePayload:

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class GetRandomFailed:
    """Random material generation failed."""
    pass

class PrfUsingHmac:
    """Implements [`Prf`] using a [`hmac::Hmac`]."""

    def for_key_exchange(self, output: object, kx: dynActiveKeyExchange, peer_pub_key: object, label: object, seed: object) -> None: ...

    def for_secret(self, output: object, secret: object, label: object, seed: object) -> None: ...

class SingleCertAndKey:
    """Server certificate resolver which always resolves to the same certificate and key.

For use with [`ConfigBuilder::with_cert_resolver()`].

[`ConfigBuilder::with_cert_resolver()`]: crate::ConfigBuilder::with_cert_resolver"""

    @staticmethod
    def from_(certified_key: CertifiedKey) -> "SingleCertAndKey": ...

    @staticmethod
    def from_(certified_key: object) -> "SingleCertAndKey": ...

    def resolve(self, _root_hint_subjects: object, _sigschemes: object) -> object | None: ...

    def has_certs(self) -> bool: ...

    def resolve(self, _client_hello: ClientHello) -> object | None: ...

class CertifiedKey:
    """A packaged-together certificate chain, matching `SigningKey` and
optional stapled OCSP response.

Note: this struct is also used to represent an [RFC 7250] raw public key,
when the client/server is configured to use raw public keys instead of
certificates.

[RFC 7250]: https://tools.ietf.org/html/rfc7250"""

    @staticmethod
    def from_der(cert_chain: list[CertificateDer], key: PrivateKeyDer, provider: CryptoProvider) -> object: ...

    @staticmethod
    def new(cert: list[CertificateDer], key: object) -> "CertifiedKey": ...

    def keys_match(self) -> None: ...

    def end_entity_cert(self) -> object: ...

class RsaSigningKey:
    """A `SigningKey` for RSA-PKCS1 or RSA-PSS.

This is used by the test suite, so it must be `pub`, but it isn't part of
the public, stable, API."""

    @staticmethod
    def new(der: PrivateKeyDer) -> object: ...

    def choose_scheme(self, offered: object) -> dynSigner | None: ...

    def public_key(self) -> SubjectPublicKeyInfoDer | None: ...

    def algorithm(self) -> SignatureAlgorithm: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(der: PrivateKeyDer) -> object: ...

    def choose_scheme(self, offered: object) -> dynSigner | None: ...

    def public_key(self) -> SubjectPublicKeyInfoDer | None: ...

    def algorithm(self) -> SignatureAlgorithm: ...

    def fmt(self, f: Formatter) -> Result: ...

class Ticketer:
    """A concrete, safe ticket creation mechanism."""

    @staticmethod
    def new() -> object: ...

    @staticmethod
    def new() -> object: ...

class HpkeAwsLcRs:
    """`HpkeAwsLcRs` holds the concrete instantiations of the algorithms specified by the [HpkeSuite]."""

    def seal(self, info: object, aad: object, plaintext: object, pub_key: HpkePublicKey) -> object: ...

    def setup_sealer(self, info: object, pub_key: HpkePublicKey) -> object: ...

    def open(self, enc: EncapsulatedSecret, info: object, aad: object, ciphertext: object, secret_key: HpkePrivateKey) -> list[int]: ...

    def setup_opener(self, enc: EncapsulatedSecret, info: object, secret_key: HpkePrivateKey) -> object: ...

    def fips(self) -> bool: ...

    def generate_key_pair(self) -> object: ...

    def suite(self) -> HpkeSuite: ...

    def fmt(self, f: Formatter) -> Result: ...

    def setup_test_sealer(self, info: object, pub_key: HpkePublicKey, sk_em: object) -> object: ...

class Output:
    """A hash output, stored as a value."""

    @staticmethod
    def new(bytes: object) -> "Output": ...

    def as_ref(self) -> object: ...

class RsaSigningKey:
    """A `SigningKey` for RSA-PKCS1 or RSA-PSS.

This is used by the test suite, so it must be `pub`, but it isn't part of
the public, stable, API."""

    @staticmethod
    def new(der: PrivateKeyDer) -> object: ...

    def choose_scheme(self, offered: object) -> dynSigner | None: ...

    def public_key(self) -> SubjectPublicKeyInfoDer | None: ...

    def algorithm(self) -> SignatureAlgorithm: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(der: PrivateKeyDer) -> object: ...

    def choose_scheme(self, offered: object) -> dynSigner | None: ...

    def public_key(self) -> SubjectPublicKeyInfoDer | None: ...

    def algorithm(self) -> SignatureAlgorithm: ...

    def fmt(self, f: Formatter) -> Result: ...

class Ticketer:
    """A concrete, safe ticket creation mechanism."""

    @staticmethod
    def new() -> object: ...

    @staticmethod
    def new() -> object: ...

class CryptoProvider:
    """Controls core cryptography used by rustls.

This crate comes with two built-in options, provided as
`CryptoProvider` structures:

- [`crypto::aws_lc_rs::default_provider`]: (behind the `aws_lc_rs` crate feature,
which is enabled by default).  This provider uses the [aws-lc-rs](https://github.com/aws/aws-lc-rs)
crate.  The `fips` crate feature makes this option use FIPS140-3-approved cryptography.
- [`crypto::ring::default_provider`]: (behind the `ring` crate feature, which
is optional).  This provider uses the [*ring*](https://github.com/briansmith/ring)
crate.

This structure provides defaults. Everything in it can be overridden at
runtime by replacing field values as needed.

# Using the per-process default `CryptoProvider`

There is the concept of an implicit default provider, configured at run-time once in
a given process.

It is used for functions like [`ClientConfig::builder()`] and [`ServerConfig::builder()`].

The intention is that an application can specify the [`CryptoProvider`] they wish to use
once, and have that apply to the variety of places where their application does TLS
(which may be wrapped inside other libraries).
They should do this by calling [`CryptoProvider::install_default()`] early on.

To achieve this goal:

- _libraries_ should use [`ClientConfig::builder()`]/[`ServerConfig::builder()`]
or otherwise rely on the [`CryptoProvider::get_default()`] provider.
- _applications_ should call [`CryptoProvider::install_default()`] early
in their `fn main()`. If _applications_ uses a custom provider based on the one built-in,
they can activate the `custom-provider` feature to ensure its usage.

# Using a specific `CryptoProvider`

Supply the provider when constructing your [`ClientConfig`] or [`ServerConfig`]:

- [`ClientConfig::builder_with_provider()`]
- [`ServerConfig::builder_with_provider()`]

When creating and configuring a webpki-backed client or server certificate verifier, a choice of
provider is also needed to start the configuration process:

- [`client::WebPkiServerVerifier::builder_with_provider()`]
- [`server::WebPkiClientVerifier::builder_with_provider()`]

If you install a custom provider and want to avoid any accidental use of a built-in provider, the feature
`custom-provider` can be activated to ensure your custom provider is used everywhere
and not a built-in one. This will disable any implicit use of a built-in provider.

# Making a custom `CryptoProvider`

Your goal will be to populate an instance of this `CryptoProvider` struct.

## Which elements are required?

There is no requirement that the individual elements ([`SupportedCipherSuite`], [`SupportedKxGroup`],
[`SigningKey`], etc.) come from the same crate.  It is allowed and expected that uninteresting
elements would be delegated back to one of the default providers (statically) or a parent
provider (dynamically).

For example, if we want to make a provider that just overrides key loading in the config builder
API (with [`ConfigBuilder::with_single_cert`], etc.), it might look like this:

```
# #[cfg(feature = "aws_lc_rs")] {
# use std::sync::Arc;
# mod fictious_hsm_api { pub fn load_private_key(key_der: pki_types::PrivateKeyDer<'static>) -> ! { unreachable!(); } }
use rustls::crypto::aws_lc_rs;

pub fn provider() -> rustls::crypto::CryptoProvider {
rustls::crypto::CryptoProvider{
key_provider: &HsmKeyLoader,
..aws_lc_rs::default_provider()
}
}

#[derive(Debug)]
struct HsmKeyLoader;

impl rustls::crypto::KeyProvider for HsmKeyLoader {
fn load_private_key(&self, key_der: pki_types::PrivateKeyDer<'static>) -> Result<Arc<dyn rustls::sign::SigningKey>, rustls::Error> {
fictious_hsm_api::load_private_key(key_der)
}
}
# }
```

## References to the individual elements

The elements are documented separately:

- **Random** - see [`crypto::SecureRandom::fill()`].
- **Cipher suites** - see [`SupportedCipherSuite`], [`Tls12CipherSuite`], and
[`Tls13CipherSuite`].
- **Key exchange groups** - see [`crypto::SupportedKxGroup`].
- **Signature verification algorithms** - see [`crypto::WebPkiSupportedAlgorithms`].
- **Authentication key loading** - see [`crypto::KeyProvider::load_private_key()`] and
[`sign::SigningKey`].

# Example code

See custom [`provider-example/`] for a full client and server example that uses
cryptography from the [`RustCrypto`] and [`dalek-cryptography`] projects.

```shell
$ cargo run --example client | head -3
Current ciphersuite: TLS13_CHACHA20_POLY1305_SHA256
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 19899
```

[`provider-example/`]: https://github.com/rustls/rustls/tree/main/provider-example/
[`RustCrypto`]: https://github.com/RustCrypto
[`dalek-cryptography`]: https://github.com/dalek-cryptography

# FIPS-approved cryptography
The `fips` crate feature enables use of the `aws-lc-rs` crate in FIPS mode.

You can verify the configuration at runtime by checking
[`ServerConfig::fips()`]/[`ClientConfig::fips()`] return `true`."""

    def install_default(self) -> object: ...

    @staticmethod
    def get_default() -> object: ...

    def fips(self) -> bool: ...

class CompletedKeyExchange:
    """The result from [`SupportedKxGroup::start_and_complete()`]."""
    pass

class SharedSecret:
    """The result from [`ActiveKeyExchange::complete`] or [`ActiveKeyExchange::complete_hybrid_component`]."""

    def secret_bytes(self) -> object: ...

    def drop(self) -> None: ...

    @staticmethod
    def from_(source: object) -> "SharedSecret": ...

    @staticmethod
    def from_(buf: list[int]) -> "SharedSecret": ...

class HkdfExpanderUsingHmac:
    """Implementation of `HkdfExpander` via `hmac::Key`."""

    def expand_slice(self, info: object, output: object) -> None: ...

    def expand_block(self, info: object) -> OkmBlock: ...

    def hash_len(self) -> int: ...

class HkdfUsingHmac:
    """Implementation of `Hkdf` (and thence `HkdfExpander`) via `hmac::Hmac`."""

    def extract_from_zero_ikm(self, salt: object) -> dynHkdfExpander: ...

    def extract_from_secret(self, salt: object, secret: object) -> dynHkdfExpander: ...

    def expander_for_okm(self, okm: OkmBlock) -> dynHkdfExpander: ...

    def hmac_sign(self, key: OkmBlock, message: object) -> Tag: ...

    def extract_prk_from_secret(self, salt: object, secret: object) -> list[int]: ...

class OkmBlock:
    """Output key material from HKDF, as a value type."""

    @staticmethod
    def new(bytes: object) -> "OkmBlock": ...

    def drop(self) -> None: ...

    def as_ref(self) -> object: ...

class OutputLengthError:
    """An error type used for `HkdfExpander::expand_slice` when
the slice exceeds the maximum HKDF output length."""
    pass

class UnsupportedOperationError:
    """An error indicating that the AEAD algorithm does not support the requested operation."""

    def fmt(self, f: Formatter) -> Result: ...

class KeyBlockShape:
    """How a TLS1.2 `key_block` is partitioned.

Note: ciphersuites with non-zero `mac_key_length` are  not currently supported."""
    pass

class Iv:
    """A write or read IV."""

    @staticmethod
    def new(value: object) -> "Iv": ...

    @staticmethod
    def copy(value: object) -> "Iv": ...

    @staticmethod
    def from_(bytes: object) -> "Iv": ...

    def as_ref(self) -> object: ...

class Nonce:
    """A nonce.  This is unique for all messages on a connection."""

    @staticmethod
    def new(iv: Iv, seq: int) -> "Nonce": ...

    @staticmethod
    def for_path(path_id: int, iv: Iv, pn: int) -> "Nonce": ...

class AeadKey:
    """A key for an AEAD algorithm.

This is a value type for a byte string up to `AeadKey::MAX_LEN` bytes in length."""

    def drop(self) -> None: ...

    def drop(self) -> None: ...

    def as_ref(self) -> object: ...

    @staticmethod
    def from_(bytes: object) -> "AeadKey": ...

class Tag:
    """A HMAC tag, stored as a value."""

    @staticmethod
    def from_(value: object) -> "Tag": ...

    def as_ref(self) -> object: ...

    @staticmethod
    def new(bytes: object) -> "Tag": ...

    def drop(self) -> None: ...

    def as_ref(self) -> object: ...

class HpkeSuite:
    """An HPKE suite, specifying a key encapsulation mechanism and a symmetric cipher suite."""
    pass

class HpkePublicKey:
    """An HPKE public key."""
    pass

class HpkePrivateKey:
    """An HPKE private key."""

    def secret_bytes(self) -> object: ...

    @staticmethod
    def from_(bytes: list[int]) -> "HpkePrivateKey": ...

    def drop(self) -> None: ...

class HpkeKeyPair:
    """An HPKE key pair, made of a matching public and private key."""
    pass

class EncapsulatedSecret:
    """An encapsulated secret returned from setting up a sender or receiver context."""
    pass

class TicketSwitcher:
    """A ticketer that has a 'current' sub-ticketer and a single
'previous' ticketer.  It creates a new ticketer every so
often, demoting the current ticketer."""

    @staticmethod
    def new(lifetime: int, generator: object) -> object: ...

    @staticmethod
    def new(lifetime: int, generator: object, time_provider: object) -> object: ...

    def lifetime(self) -> int: ...

    def enabled(self) -> bool: ...

    def encrypt(self, message: object) -> list[int] | None: ...

    def decrypt(self, ciphertext: object) -> list[int] | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class TicketRotator:
    """A ticketer that has a 'current' sub-ticketer and a single
'previous' ticketer.  It creates a new ticketer every so
often, demoting the current ticketer."""

    @staticmethod
    def new(lifetime: int, generator: object) -> object: ...

    def lifetime(self) -> int: ...

    def enabled(self) -> bool: ...

    def encrypt(self, message: object) -> list[int] | None: ...

    def decrypt(self, ciphertext: object) -> list[int] | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class EchConfig:
    """Configuration for performing encrypted client hello.

Note: differs from the protocol-encoded EchConfig (`EchConfigMsg`)."""

    @staticmethod
    def new(ech_config_list: EchConfigListBytes, hpke_suites: object) -> object: ...

class EchGreaseConfig:
    """Configuration for GREASE Encrypted Client Hello."""

    @staticmethod
    def new(suite: object, placeholder_key: HpkePublicKey) -> "EchGreaseConfig": ...

class ClientConfig:
    """Common configuration for (typically) all connections made by a program.

Making one of these is cheap, though one of the inputs may be expensive: gathering trust roots
from the operating system to add to the [`RootCertStore`] passed to `with_root_certificates()`
(the rustls-native-certs crate is often used for this) may take on the order of a few hundred
milliseconds.

These must be created via the [`ClientConfig::builder()`] or [`ClientConfig::builder_with_provider()`]
function.

Note that using [`ConfigBuilder<ClientConfig, WantsVersions>::with_ech()`] will produce a common
configuration specific to the provided [`crate::client::EchConfig`] that may not be appropriate
for all connections made by the program. In this case the configuration should only be shared
by connections intended for domains that offer the provided [`crate::client::EchConfig`] in
their DNS zone.

# Defaults

* [`ClientConfig::max_fragment_size`]: the default is `None` (meaning 16kB).
* [`ClientConfig::resumption`]: supports resumption with up to 256 server names, using session
ids or tickets, with a max of eight tickets per server.
* [`ClientConfig::alpn_protocols`]: the default is empty -- no ALPN protocol is negotiated.
* [`ClientConfig::key_log`]: key material is not logged.
* [`ClientConfig::cert_decompressors`]: depends on the crate features, see [`compress::default_cert_decompressors()`].
* [`ClientConfig::cert_compressors`]: depends on the crate features, see [`compress::default_cert_compressors()`].
* [`ClientConfig::cert_compression_cache`]: caches the most recently used 4 compressions

[`RootCertStore`]: crate::RootCertStore"""

    @staticmethod
    def builder() -> object: ...

    @staticmethod
    def builder_with_protocol_versions(versions: object) -> object: ...

    @staticmethod
    def builder_with_provider(provider: object) -> object: ...

    @staticmethod
    def builder_with_details(provider: object, time_provider: object) -> object: ...

    def fips(self) -> bool: ...

    def crypto_provider(self) -> object: ...

    def dangerous(self) -> DangerousClientConfig: ...

class Resumption:
    """Configuration for how/when a client is allowed to resume a previous session."""

    @staticmethod
    def in_memory_sessions(num: int) -> "Resumption": ...

    @staticmethod
    def store(store: object) -> "Resumption": ...

    @staticmethod
    def disabled() -> "Resumption": ...

    def tls12_resumption(self, tls12: Tls12Resumption) -> Self: ...

    @staticmethod
    def default() -> "Resumption": ...

class DangerousClientConfig:
    """Accessor for dangerous configuration options."""

    def set_certificate_verifier(self, verifier: object) -> None: ...

class WriteEarlyData:
    """Stub that implements io::Write and dispatches to `write_early_data`."""

    def bytes_left(self) -> int: ...

    def write(self, buf: object) -> int: ...

    def flush(self) -> object: ...

class ClientConnection:
    """This represents a single TLS client connection."""

    @staticmethod
    def new(config: object, quic_version: Version, name: ServerName, params: list[int]) -> object: ...

    @staticmethod
    def new_with_alpn(config: object, quic_version: Version, name: ServerName, params: list[int], alpn_protocols: list[list[int]]) -> object: ...

    def is_early_data_accepted(self) -> bool: ...

    def tls13_tickets_received(self) -> int: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(config: object, name: ServerName) -> object: ...

    @staticmethod
    def new_with_alpn(config: object, name: ServerName, alpn_protocols: list[list[int]]) -> object: ...

    def early_data(self) -> WriteEarlyData | None: ...

    def is_early_data_accepted(self) -> bool: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def ech_status(self) -> EchStatus: ...

    def tls13_tickets_received(self) -> int: ...

    def fips(self) -> bool: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

class UnbufferedClientConnection:
    """Unbuffered version of `ClientConnection`

See the [`crate::unbuffered`] module docs for more details"""

    @staticmethod
    def new(config: object, name: ServerName) -> object: ...

    @staticmethod
    def new_with_alpn(config: object, name: ServerName, alpn_protocols: list[list[int]]) -> object: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def dangerous_into_kernel_connection(self) -> object: ...

    def tls13_tickets_received(self) -> int: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

class MayEncryptEarlyData:
    """Allows encrypting early (RTT-0) data"""

    def encrypt(self, early_data: object, outgoing_tls: object) -> int: ...

class ClientConnectionData:
    """State associated with a client connection."""
    pass

class ClientSessionMemoryCache:
    """An implementer of `ClientSessionStore` that stores everything
in memory.

It enforces a limit on the number of entries to bound memory usage."""

    @staticmethod
    def new(size: int) -> "ClientSessionMemoryCache": ...

    @staticmethod
    def new(size: int) -> "ClientSessionMemoryCache": ...

    def set_kx_hint(self, server_name: ServerName, group: NamedGroup) -> None: ...

    def kx_hint(self, server_name: ServerName) -> NamedGroup | None: ...

    def set_tls12_session(self, _server_name: ServerName, _value: Tls12ClientSessionValue) -> None: ...

    def tls12_session(self, _server_name: ServerName) -> Tls12ClientSessionValue | None: ...

    def remove_tls12_session(self, _server_name: ServerName) -> None: ...

    def insert_tls13_ticket(self, server_name: ServerName, value: Tls13ClientSessionValue) -> None: ...

    def take_tls13_ticket(self, server_name: ServerName) -> Tls13ClientSessionValue | None: ...

    def fmt(self, f: Formatter) -> Result: ...

class AlwaysResolvesClientRawPublicKeys:
    """An exemplar `ResolvesClientCert` implementation that always resolves to a single
[RFC 7250] raw public key.

[RFC 7250]: https://tools.ietf.org/html/rfc7250"""

    @staticmethod
    def new(certified_key: object) -> "AlwaysResolvesClientRawPublicKeys": ...

    def resolve(self, _root_hint_subjects: object, _sigschemes: object) -> object | None: ...

    def only_raw_public_keys(self) -> bool: ...

    def has_certs(self) -> bool: ...

class DangerousClientConfigBuilder:
    """Accessor for dangerous configuration options."""

    def with_custom_certificate_verifier(self, verifier: object) -> object: ...

class WantsClientCert:
    """A config builder state where the caller needs to supply whether and how to provide a client
certificate.

For more information, see the [`ConfigBuilder`] documentation."""
    pass

class CommonState:
    """Connection state common to both client and server connections."""

    def wants_write(self) -> bool: ...

    def is_handshaking(self) -> bool: ...

    def peer_certificates(self) -> object: ...

    def alpn_protocol(self) -> object: ...

    def negotiated_cipher_suite(self) -> SupportedCipherSuite | None: ...

    def negotiated_key_exchange_group(self) -> object: ...

    def protocol_version(self) -> ProtocolVersion | None: ...

    def handshake_kind(self) -> HandshakeKind | None: ...

    def send_close_notify(self) -> None: ...

    def wants_read(self) -> bool: ...

class IoState:
    """Values of this structure are returned from [`Connection::process_new_packets`]
and tell the caller the current I/O state of the TLS connection.

[`Connection::process_new_packets`]: crate::Connection::process_new_packets"""

    def tls_bytes_to_write(self) -> int: ...

    def plaintext_bytes_to_read(self) -> int: ...

    def peer_has_closed(self) -> bool: ...

class DecompressionFailed:
    """A content-less error for when `CertDecompressor::decompress` fails."""
    pass

class CompressionFailed:
    """A content-less error for when `CertCompressor::compress` fails."""
    pass

class CompressionCacheInner:
    """Innards of an enabled CompressionCache.

You cannot make one of these directly. Use [`CompressionCache::new`]."""
    pass

class Stream:
    """This type implements `io::Read` and `io::Write`, encapsulating
a Connection `C` and an underlying transport `T`, such as a socket.

Relies on [`ConnectionCommon::complete_io()`] to perform the necessary I/O.

This allows you to use a rustls Connection like a normal stream."""

    @staticmethod
    def new(conn: object, sock: object) -> "Stream": ...

    def read(self, buf: object) -> int: ...

    def read_buf(self, cursor: BorrowedCursor) -> None: ...

    def fill_buf(self) -> object: ...

    def consume(self, amt: int) -> None: ...

    def write(self, buf: object) -> int: ...

    def write_vectored(self, bufs: object) -> int: ...

    def flush(self) -> None: ...

class StreamOwned:
    """This type implements `io::Read` and `io::Write`, encapsulating
and owning a Connection `C` and an underlying transport `T`, such as a socket.

Relies on [`ConnectionCommon::complete_io()`] to perform the necessary I/O.

This allows you to use a rustls Connection like a normal stream."""

    @staticmethod
    def new(conn: C, sock: T) -> "StreamOwned": ...

    def get_ref(self) -> T: ...

    def get_mut(self) -> T: ...

    def into_parts(self) -> object: ...

    def read(self, buf: object) -> int: ...

    def read_buf(self, cursor: BorrowedCursor) -> None: ...

    def fill_buf(self) -> object: ...

    def consume(self, amt: int) -> None: ...

    def write(self, buf: object) -> int: ...

    def flush(self) -> None: ...

class OtherError:
    """Any other error that cannot be expressed by a more specific [`Error`] variant.

For example, an `OtherError` could be produced by a custom crypto provider
exposing a provider specific error.

Enums holding this type will never compare equal to each other."""

    def eq(self, _other: Self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

    def source(self) -> object: ...

class HandshakeSignatureValid:
    """Zero-sized marker type representing verification of a signature."""

    @staticmethod
    def assertion() -> "HandshakeSignatureValid": ...

class ServerCertVerified:
    """Zero-sized marker type representing verification of a server cert chain."""

    @staticmethod
    def assertion() -> "ServerCertVerified": ...

class ClientCertVerified:
    """Zero-sized marker type representing verification of a client cert chain."""

    @staticmethod
    def assertion() -> "ClientCertVerified": ...

class NoClientAuth:
    """Turns off client authentication.

In contrast to using
`WebPkiClientVerifier::builder(roots).allow_unauthenticated().build()`, the `NoClientAuth`
`ClientCertVerifier` will not offer client authentication at all, vs offering but not
requiring it."""

    def offer_client_auth(self) -> bool: ...

    def root_hint_subjects(self) -> object: ...

    def verify_client_cert(self, _end_entity: CertificateDer, _intermediates: object, _now: UnixTime) -> ClientCertVerified: ...

    def verify_tls12_signature(self, _message: object, _cert: CertificateDer, _dss: DigitallySignedStruct) -> HandshakeSignatureValid: ...

    def verify_tls13_signature(self, _message: object, _cert: CertificateDer, _dss: DigitallySignedStruct) -> HandshakeSignatureValid: ...

    def supported_verify_schemes(self) -> list[SignatureScheme]: ...

class DigitallySignedStruct:
    """This type combines a [`SignatureScheme`] and a signature payload produced with that scheme."""

    def signature(self) -> object: ...

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class VerifierBuilderError:
    """An error that can occur when building a certificate verifier."""
    NoRootAnchors: "VerifierBuilderError"
    InvalidCrl: "VerifierBuilderError"

    @staticmethod
    def from_(value: CertRevocationListError) -> "VerifierBuilderError": ...

    def fmt(self, f: Formatter) -> Result: ...

class Connection:
    """A client or server connection."""
    Client: "Connection"
    Server: "Connection"

    def read_tls(self, rd: mutdynRead) -> int: ...

    def write_tls(self, wr: Write) -> int: ...

    def reader(self) -> Reader: ...

    def writer(self) -> Writer: ...

    def process_new_packets(self) -> IoState: ...

    def export_keying_material(self, output: T, label: object, context: object) -> T: ...

    def complete_io(self, io: T) -> object: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def set_buffer_limit(self, limit: int | None) -> None: ...

    def refresh_traffic_keys(self) -> None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def quic_transport_parameters(self) -> object: ...

    def zero_rtt_keys(self) -> DirectionalKeys | None: ...

    def read_hs(self, plaintext: object) -> None: ...

    def write_hs(self, buf: list[int]) -> KeyChange | None: ...

    def alert(self) -> AlertDescription | None: ...

    def export_keying_material(self, output: T, label: object, context: object) -> T: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    @staticmethod
    def from_(c: ClientConnection) -> "Connection": ...

    @staticmethod
    def from_(c: ServerConnection) -> "Connection": ...

    @staticmethod
    def from_(conn: ServerConnection) -> "Connection": ...

    @staticmethod
    def from_(conn: ClientConnection) -> "Connection": ...

class ConnectionState:
    """The state of the [`UnbufferedConnectionCommon`] object"""
    ReadTraffic: "ConnectionState"
    PeerClosed: "ConnectionState"
    Closed: "ConnectionState"
    ReadEarlyData: "ConnectionState"
    EncodeTlsData: "ConnectionState"
    TransmitTlsData: "ConnectionState"
    BlockedHandshake: "ConnectionState"
    WriteTraffic: "ConnectionState"

    @staticmethod
    def from_(v: object) -> "ConnectionState": ...

    @staticmethod
    def from_(v: object) -> "ConnectionState": ...

    @staticmethod
    def from_(v: object) -> "ConnectionState": ...

    @staticmethod
    def from_(v: object) -> "ConnectionState": ...

    def fmt(self, f: Formatter) -> Result: ...

class EncodeError:
    """Errors that may arise when encoding a handshake record"""
    InsufficientSize: "EncodeError"
    AlreadyEncoded: "EncodeError"

    @staticmethod
    def from_(v: InsufficientSizeError) -> "EncodeError": ...

    def fmt(self, f: Formatter) -> Result: ...

class EncryptError:
    """Errors that may arise when encrypting application data"""
    InsufficientSize: "EncryptError"
    EncryptExhausted: "EncryptError"

    @staticmethod
    def from_(v: InsufficientSizeError) -> "EncryptError": ...

    def fmt(self, f: Formatter) -> Result: ...

class Connection:
    """A QUIC client or server connection."""
    Client: "Connection"
    Server: "Connection"

    def read_tls(self, rd: mutdynRead) -> int: ...

    def write_tls(self, wr: Write) -> int: ...

    def reader(self) -> Reader: ...

    def writer(self) -> Writer: ...

    def process_new_packets(self) -> IoState: ...

    def export_keying_material(self, output: T, label: object, context: object) -> T: ...

    def complete_io(self, io: T) -> object: ...

    def dangerous_extract_secrets(self) -> ExtractedSecrets: ...

    def set_buffer_limit(self, limit: int | None) -> None: ...

    def refresh_traffic_keys(self) -> None: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    def quic_transport_parameters(self) -> object: ...

    def zero_rtt_keys(self) -> DirectionalKeys | None: ...

    def read_hs(self, plaintext: object) -> None: ...

    def write_hs(self, buf: list[int]) -> KeyChange | None: ...

    def alert(self) -> AlertDescription | None: ...

    def export_keying_material(self, output: T, label: object, context: object) -> T: ...

    def deref(self) -> Target: ...

    def deref_mut(self) -> Target: ...

    @staticmethod
    def from_(c: ClientConnection) -> "Connection": ...

    @staticmethod
    def from_(c: ServerConnection) -> "Connection": ...

    @staticmethod
    def from_(conn: ServerConnection) -> "Connection": ...

    @staticmethod
    def from_(conn: ClientConnection) -> "Connection": ...

class KeyChange:
    """Key material for use in QUIC packet spaces

QUIC uses 4 different sets of keys (and progressive key updates for long-running connections):

* Initial: these can be created from [`Keys::initial()`]
* 0-RTT keys: can be retrieved from [`ConnectionCommon::zero_rtt_keys()`]
* Handshake: these are returned from [`ConnectionCommon::write_hs()`] after `ClientHello` and
`ServerHello` messages have been exchanged
* 1-RTT keys: these are returned from [`ConnectionCommon::write_hs()`] after the handshake is done

Once the 1-RTT keys have been exchanged, either side may initiate a key update. Progressive
update keys can be obtained from the [`Secrets`] returned in [`KeyChange::OneRtt`]. Note that
only packet keys are updated by key updates; header protection keys remain the same."""
    Handshake: "KeyChange"
    OneRtt: "KeyChange"

class Version:
    """QUIC protocol version

Governs version-specific behavior in the TLS layer"""
    V1Draft: "Version"
    V1: "Version"
    V2: "Version"

class SupportedCipherSuite:
    """A cipher suite supported by rustls.

This type carries both configuration and implementation. Compare with
[`CipherSuite`], which carries solely a cipher suite identifier."""
    Tls12: "SupportedCipherSuite"
    Tls13: "SupportedCipherSuite"

    @staticmethod
    def from_(s: object) -> "SupportedCipherSuite": ...

    def suite(self) -> CipherSuite: ...

    def tls13(self) -> object: ...

    def version(self) -> object: ...

    def usable_for_signature_algorithm(self, _sig_alg: SignatureAlgorithm) -> bool: ...

    def fips(self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(s: object) -> "SupportedCipherSuite": ...

class ConnectionTrafficSecrets:
    """Secrets used to encrypt/decrypt data in a TLS session.

These can be used to configure kTLS for a socket in one direction.
The only other piece of information needed is the sequence number,
which is in [ExtractedSecrets]."""
    Aes128Gcm: "ConnectionTrafficSecrets"
    Aes256Gcm: "ConnectionTrafficSecrets"
    Chacha20Poly1305: "ConnectionTrafficSecrets"

class OutboundChunks:
    """A collection of borrowed plaintext slices.

Warning: OutboundChunks does not guarantee that the simplest variant is used.
Multiple can hold non fragmented or empty payloads."""
    Single: "OutboundChunks"
    Multiple: "OutboundChunks"

    @staticmethod
    def new(chunks: object) -> "OutboundChunks": ...

    @staticmethod
    def new_empty() -> "OutboundChunks": ...

    def to_vec(self) -> list[int]: ...

    def copy_to_vec(self, vec: list[int]) -> None: ...

    def split_at(self, mid: int) -> object: ...

    def is_empty(self) -> bool: ...

    def len(self) -> int: ...

    @staticmethod
    def from_(payload: object) -> "OutboundChunks": ...

class MessagePayload:
    Alert: "MessagePayload"
    Handshake: "MessagePayload"
    HandshakeFlight: "MessagePayload"
    ChangeCipherSpec: "MessagePayload"
    ApplicationData: "MessagePayload"

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def handshake(parsed: HandshakeMessagePayload) -> "MessagePayload": ...

    @staticmethod
    def new(typ: ContentType, vers: ProtocolVersion, payload: object) -> object: ...

    def content_type(self) -> ContentType: ...

class MessageError:
    TooShortForHeader: "MessageError"
    TooShortForLength: "MessageError"
    InvalidEmptyPayload: "MessageError"
    MessageTooLarge: "MessageError"
    InvalidContentType: "MessageError"
    UnknownProtocolVersion: "MessageError"

class Payload:
    """An externally length'd payload"""
    Borrowed: "Payload"
    Owned: "Payload"

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

    def bytes(self) -> object: ...

    def into_owned(self) -> Payload: ...

    def into_vec(self) -> list[int]: ...

    @staticmethod
    def read(r: Reader) -> "Payload": ...

    @staticmethod
    def new(bytes: object) -> "Payload": ...

    @staticmethod
    def empty() -> "Payload": ...

    def fmt(self, f: Formatter) -> Result: ...

class KeyExchangeAlgorithm:
    """Describes supported key exchange mechanisms."""
    DHE: "KeyExchangeAlgorithm"
    ECDHE: "KeyExchangeAlgorithm"

class EchConfigPayload:
    """An encrypted client hello (ECH) config."""
    V18: "EchConfigPayload"
    Unknown: "EchConfigPayload"

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class EchConfigExtension:
    Unknown: "EchConfigExtension"

    def encode(self, bytes: list[int]) -> None: ...

    @staticmethod
    def read(r: Reader) -> object: ...

class EchMode:
    """Controls how Encrypted Client Hello (ECH) is used in a client handshake."""
    Enable: "EchMode"
    Grease: "EchMode"

    def fips(self) -> bool: ...

    @staticmethod
    def from_(config: EchConfig) -> "EchMode": ...

    @staticmethod
    def from_(config: EchGreaseConfig) -> "EchMode": ...

class EchStatus:
    """An enum representing ECH offer status."""
    NotOffered: "EchStatus"
    Grease: "EchStatus"
    Offered: "EchStatus"
    Accepted: "EchStatus"
    Rejected: "EchStatus"

class Tls12Resumption:
    """What mechanisms to support for resuming a TLS 1.2 session."""
    Disabled: "Tls12Resumption"
    SessionIdOnly: "Tls12Resumption"
    SessionIdOrTickets: "Tls12Resumption"

class EarlyDataError:
    """Errors that may arise when encrypting early (RTT-0) data"""
    ExceededAllowedEarlyData: "EarlyDataError"
    Encrypt: "EarlyDataError"

    @staticmethod
    def from_(v: EncryptError) -> "EarlyDataError": ...

    def fmt(self, f: Formatter) -> Result: ...

class HandshakeKind:
    """Describes which sort of handshake happened."""
    Full: "HandshakeKind"
    FullWithHelloRetryRequest: "HandshakeKind"
    Resumed: "HandshakeKind"

class Side:
    """Side of the connection."""
    Client: "Side"
    Server: "Side"

class CompressionLevel:
    """A hint for how many resources to dedicate to a compression."""
    Interactive: "CompressionLevel"
    Amortized: "CompressionLevel"

class CompressionCache:
    """An LRU cache for compressions.

The prospect of being able to reuse a given compression for many connections
means we can afford to spend more time on that compression (by passing
`CompressionLevel::Amortized` to the compressor)."""
    Disabled: "CompressionCache"
    Enabled: "CompressionCache"

    @staticmethod
    def new(size: int) -> "CompressionCache": ...

    @staticmethod
    def default() -> "CompressionCache": ...

class Error:
    """rustls reports protocol errors using this type."""
    InappropriateMessage: "Error"
    InappropriateHandshakeMessage: "Error"
    InvalidEncryptedClientHello: "Error"
    InvalidMessage: "Error"
    NoCertificatesPresented: "Error"
    UnsupportedNameType: "Error"
    DecryptError: "Error"
    EncryptError: "Error"
    PeerIncompatible: "Error"
    PeerMisbehaved: "Error"
    AlertReceived: "Error"
    InvalidCertificate: "Error"
    InvalidCertRevocationList: "Error"
    General: "Error"
    FailedToGetCurrentTime: "Error"
    FailedToGetRandomBytes: "Error"
    HandshakeNotComplete: "Error"
    PeerSentOversizedRecord: "Error"
    NoApplicationProtocol: "Error"
    BadMaxFragmentSize: "Error"
    InconsistentKeys: "Error"
    Other: "Error"

    @staticmethod
    def from_(value: UnsupportedOperationError) -> "Error": ...

    @staticmethod
    def from_(e: InconsistentKeys) -> "Error": ...

    @staticmethod
    def from_(e: InvalidMessage) -> "Error": ...

    @staticmethod
    def from_(e: PeerMisbehaved) -> "Error": ...

    @staticmethod
    def from_(e: PeerIncompatible) -> "Error": ...

    @staticmethod
    def from_(e: CertificateError) -> "Error": ...

    @staticmethod
    def from_(e: CertRevocationListError) -> "Error": ...

    @staticmethod
    def from_(e: EncryptedClientHelloError) -> "Error": ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(_: SystemTimeError) -> "Error": ...

    @staticmethod
    def from_(_: GetRandomFailed) -> "Error": ...

    @staticmethod
    def from_(value: OtherError) -> "Error": ...

class InconsistentKeys:
    """Specific failure cases from [`keys_match`] or a [`crate::crypto::signer::SigningKey`] that cannot produce a corresponding public key.

[`keys_match`]: crate::crypto::signer::CertifiedKey::keys_match"""
    KeyMismatch: "InconsistentKeys"
    Unknown: "InconsistentKeys"

class InvalidMessage:
    """A corrupt TLS message payload that resulted in an error."""
    CertificatePayloadTooLarge: "InvalidMessage"
    HandshakePayloadTooLarge: "InvalidMessage"
    InvalidCcs: "InvalidMessage"
    InvalidContentType: "InvalidMessage"
    InvalidCertificateStatusType: "InvalidMessage"
    InvalidCertRequest: "InvalidMessage"
    InvalidDhParams: "InvalidMessage"
    InvalidEmptyPayload: "InvalidMessage"
    InvalidKeyUpdate: "InvalidMessage"
    InvalidServerName: "InvalidMessage"
    MessageTooLarge: "InvalidMessage"
    MessageTooShort: "InvalidMessage"
    MissingData: "InvalidMessage"
    MissingKeyExchange: "InvalidMessage"
    NoSignatureSchemes: "InvalidMessage"
    TrailingData: "InvalidMessage"
    UnexpectedMessage: "InvalidMessage"
    UnknownProtocolVersion: "InvalidMessage"
    UnsupportedCompression: "InvalidMessage"
    UnsupportedCurveType: "InvalidMessage"
    UnsupportedKeyExchangeAlgorithm: "InvalidMessage"
    EmptyTicketValue: "InvalidMessage"
    IllegalEmptyList: "InvalidMessage"
    IllegalEmptyValue: "InvalidMessage"
    DuplicateExtension: "InvalidMessage"
    PreSharedKeyIsNotFinalExtension: "InvalidMessage"
    UnknownHelloRetryRequestExtension: "InvalidMessage"
    UnknownCertificateExtension: "InvalidMessage"

class PeerMisbehaved:
    """The set of cases where we failed to make a connection because we thought
the peer was misbehaving.

This is `non_exhaustive`: we might add or stop using items here in minor
versions.  We also don't document what they mean.  Generally a user of
rustls shouldn't vary its behaviour on these error codes, and there is
nothing it can do to improve matters.

Please file a bug against rustls if you see `Error::PeerMisbehaved` in
the wild."""
    AttemptedDowngradeToTls12WhenTls13IsSupported: "PeerMisbehaved"
    BadCertChainExtensions: "PeerMisbehaved"
    DisallowedEncryptedExtension: "PeerMisbehaved"
    DuplicateClientHelloExtensions: "PeerMisbehaved"
    DuplicateEncryptedExtensions: "PeerMisbehaved"
    DuplicateHelloRetryRequestExtensions: "PeerMisbehaved"
    DuplicateNewSessionTicketExtensions: "PeerMisbehaved"
    DuplicateServerHelloExtensions: "PeerMisbehaved"
    DuplicateServerNameTypes: "PeerMisbehaved"
    EarlyDataAttemptedInSecondClientHello: "PeerMisbehaved"
    EarlyDataExtensionWithoutResumption: "PeerMisbehaved"
    EarlyDataOfferedWithVariedCipherSuite: "PeerMisbehaved"
    HandshakeHashVariedAfterRetry: "PeerMisbehaved"
    IllegalHelloRetryRequestWithEmptyCookie: "PeerMisbehaved"
    IllegalHelloRetryRequestWithNoChanges: "PeerMisbehaved"
    IllegalHelloRetryRequestWithOfferedGroup: "PeerMisbehaved"
    IllegalHelloRetryRequestWithUnofferedCipherSuite: "PeerMisbehaved"
    IllegalHelloRetryRequestWithUnofferedNamedGroup: "PeerMisbehaved"
    IllegalHelloRetryRequestWithUnsupportedVersion: "PeerMisbehaved"
    IllegalHelloRetryRequestWithWrongSessionId: "PeerMisbehaved"
    IllegalHelloRetryRequestWithInvalidEch: "PeerMisbehaved"
    IllegalMiddleboxChangeCipherSpec: "PeerMisbehaved"
    IllegalTlsInnerPlaintext: "PeerMisbehaved"
    IncorrectBinder: "PeerMisbehaved"
    InvalidCertCompression: "PeerMisbehaved"
    InvalidMaxEarlyDataSize: "PeerMisbehaved"
    InvalidKeyShare: "PeerMisbehaved"
    KeyEpochWithPendingFragment: "PeerMisbehaved"
    KeyUpdateReceivedInQuicConnection: "PeerMisbehaved"
    MessageInterleavedWithHandshakeMessage: "PeerMisbehaved"
    MissingBinderInPskExtension: "PeerMisbehaved"
    MissingKeyShare: "PeerMisbehaved"
    MissingPskModesExtension: "PeerMisbehaved"
    MissingQuicTransportParameters: "PeerMisbehaved"
    OfferedDuplicateCertificateCompressions: "PeerMisbehaved"
    OfferedDuplicateKeyShares: "PeerMisbehaved"
    OfferedEarlyDataWithOldProtocolVersion: "PeerMisbehaved"
    OfferedEmptyApplicationProtocol: "PeerMisbehaved"
    OfferedIncorrectCompressions: "PeerMisbehaved"
    PskExtensionMustBeLast: "PeerMisbehaved"
    PskExtensionWithMismatchedIdsAndBinders: "PeerMisbehaved"
    RefusedToFollowHelloRetryRequest: "PeerMisbehaved"
    RejectedEarlyDataInterleavedWithHandshakeMessage: "PeerMisbehaved"
    ResumptionAttemptedWithVariedEms: "PeerMisbehaved"
    ResumptionOfferedWithVariedCipherSuite: "PeerMisbehaved"
    ResumptionOfferedWithVariedEms: "PeerMisbehaved"
    ResumptionOfferedWithIncompatibleCipherSuite: "PeerMisbehaved"
    SelectedDifferentCipherSuiteAfterRetry: "PeerMisbehaved"
    SelectedInvalidPsk: "PeerMisbehaved"
    SelectedTls12UsingTls13VersionExtension: "PeerMisbehaved"
    SelectedUnofferedApplicationProtocol: "PeerMisbehaved"
    SelectedUnofferedCertCompression: "PeerMisbehaved"
    SelectedUnofferedCipherSuite: "PeerMisbehaved"
    SelectedUnofferedCompression: "PeerMisbehaved"
    SelectedUnofferedKxGroup: "PeerMisbehaved"
    SelectedUnofferedPsk: "PeerMisbehaved"
    SelectedUnusableCipherSuiteForVersion: "PeerMisbehaved"
    ServerEchoedCompatibilitySessionId: "PeerMisbehaved"
    ServerHelloMustOfferUncompressedEcPoints: "PeerMisbehaved"
    ServerNameDifferedOnRetry: "PeerMisbehaved"
    ServerNameMustContainOneHostName: "PeerMisbehaved"
    SignedKxWithWrongAlgorithm: "PeerMisbehaved"
    SignedHandshakeWithUnadvertisedSigScheme: "PeerMisbehaved"
    TooManyEmptyFragments: "PeerMisbehaved"
    TooManyKeyUpdateRequests: "PeerMisbehaved"
    TooManyRenegotiationRequests: "PeerMisbehaved"
    TooManyWarningAlertsReceived: "PeerMisbehaved"
    TooMuchEarlyDataReceived: "PeerMisbehaved"
    UnexpectedCleartextExtension: "PeerMisbehaved"
    UnsolicitedCertExtension: "PeerMisbehaved"
    UnsolicitedEncryptedExtension: "PeerMisbehaved"
    UnsolicitedSctList: "PeerMisbehaved"
    UnsolicitedServerHelloExtension: "PeerMisbehaved"
    WrongGroupForKeyShare: "PeerMisbehaved"
    UnsolicitedEchExtension: "PeerMisbehaved"

class PeerIncompatible:
    """The set of cases where we failed to make a connection because a peer
doesn't support a TLS version/feature we require.

This is `non_exhaustive`: we might add or stop using items here in minor
versions."""
    EcPointsExtensionRequired: "PeerIncompatible"
    ExtendedMasterSecretExtensionRequired: "PeerIncompatible"
    IncorrectCertificateTypeExtension: "PeerIncompatible"
    KeyShareExtensionRequired: "PeerIncompatible"
    NamedGroupsExtensionRequired: "PeerIncompatible"
    NoCertificateRequestSignatureSchemesInCommon: "PeerIncompatible"
    NoCipherSuitesInCommon: "PeerIncompatible"
    NoEcPointFormatsInCommon: "PeerIncompatible"
    NoKxGroupsInCommon: "PeerIncompatible"
    NoSignatureSchemesInCommon: "PeerIncompatible"
    NullCompressionRequired: "PeerIncompatible"
    ServerDoesNotSupportTls12Or13: "PeerIncompatible"
    ServerSentHelloRetryRequestWithUnknownExtension: "PeerIncompatible"
    ServerTlsVersionIsDisabledByOurConfig: "PeerIncompatible"
    SignatureAlgorithmsExtensionRequired: "PeerIncompatible"
    SupportedVersionsExtensionRequired: "PeerIncompatible"
    Tls12NotOffered: "PeerIncompatible"
    Tls12NotOfferedOrEnabled: "PeerIncompatible"
    Tls13RequiredForQuic: "PeerIncompatible"
    UncompressedEcPointsRequired: "PeerIncompatible"
    UnsolicitedCertificateTypeExtension: "PeerIncompatible"
    ServerRejectedEncryptedClientHello: "PeerIncompatible"

class CertificateError:
    """The ways in which certificate validators can express errors.

Note that the rustls TLS protocol code interprets specifically these
error codes to send specific TLS alerts.  Therefore, if a
custom certificate validator uses incorrect errors the library as
a whole will send alerts that do not match the standard (this is usually
a minor issue, but could be misleading)."""
    BadEncoding: "CertificateError"
    Expired: "CertificateError"
    ExpiredContext: "CertificateError"
    NotValidYet: "CertificateError"
    NotValidYetContext: "CertificateError"
    Revoked: "CertificateError"
    UnhandledCriticalExtension: "CertificateError"
    UnknownIssuer: "CertificateError"
    UnknownRevocationStatus: "CertificateError"
    ExpiredRevocationList: "CertificateError"
    ExpiredRevocationListContext: "CertificateError"
    BadSignature: "CertificateError"
    UnsupportedSignatureAlgorithm: "CertificateError"
    UnsupportedSignatureAlgorithmContext: "CertificateError"
    UnsupportedSignatureAlgorithmForPublicKeyContext: "CertificateError"
    NotValidForName: "CertificateError"
    NotValidForNameContext: "CertificateError"
    InvalidPurpose: "CertificateError"
    InvalidPurposeContext: "CertificateError"
    InvalidOcspResponse: "CertificateError"
    ApplicationVerificationFailure: "CertificateError"
    Other: "CertificateError"

    def eq(self, other: Self) -> bool: ...

    def fmt(self, f: Formatter) -> Result: ...

class ExtendedKeyPurpose:
    """Extended Key Usage (EKU) purpose values.

These are usually represented as OID values in the certificate's extension (if present), but
we represent the values that are most relevant to rustls as named enum variants."""
    ClientAuth: "ExtendedKeyPurpose"
    ServerAuth: "ExtendedKeyPurpose"
    Other: "ExtendedKeyPurpose"

    def fmt(self, f: Formatter) -> Result: ...

class CertRevocationListError:
    """The ways in which a certificate revocation list (CRL) can be invalid."""
    BadSignature: "CertRevocationListError"
    UnsupportedSignatureAlgorithm: "CertRevocationListError"
    UnsupportedSignatureAlgorithmContext: "CertRevocationListError"
    UnsupportedSignatureAlgorithmForPublicKeyContext: "CertRevocationListError"
    InvalidCrlNumber: "CertRevocationListError"
    InvalidRevokedCertSerialNumber: "CertRevocationListError"
    IssuerInvalidForCrl: "CertRevocationListError"
    Other: "CertRevocationListError"
    ParseError: "CertRevocationListError"
    UnsupportedCrlVersion: "CertRevocationListError"
    UnsupportedCriticalExtension: "CertRevocationListError"
    UnsupportedDeltaCrl: "CertRevocationListError"
    UnsupportedIndirectCrl: "CertRevocationListError"
    UnsupportedRevocationReason: "CertRevocationListError"

    def eq(self, other: Self) -> bool: ...

class EncryptedClientHelloError:
    """An error that occurred while handling Encrypted Client Hello (ECH)."""
    InvalidConfigList: "EncryptedClientHelloError"
    NoCompatibleConfig: "EncryptedClientHelloError"
    SniRequired: "EncryptedClientHelloError"

"""Verify that the end-entity certificate `end_entity` is a valid server cert
and chains to at least one of the trust anchors in the `roots` [RootCertStore].

This function is primarily useful when building a custom certificate verifier. It
performs **no revocation checking**. Implementers must handle this themselves,
along with checking that the server certificate is valid for the subject name
being used (see [`verify_server_name`]).

`intermediates` contains all certificates other than `end_entity` that
were sent as part of the server's `Certificate` message. It is in the
same order that the server sent them and may be empty."""
def verify_server_cert_signed_by_trust_anchor(cert: ParsedCertificate, roots: RootCertStore, intermediates: object, now: UnixTime, supported_algs: object) -> None: ...

"""Verify that the `end_entity` has an alternative name matching the `server_name`.

Note: this only verifies the name and should be used in conjunction with more verification
like [verify_server_cert_signed_by_trust_anchor]"""
def verify_server_name(cert: ParsedCertificate, server_name: ServerName) -> None: ...

"""Verify a message signature using the `cert` public key and any supported scheme.

This function verifies the `dss` signature over `message` using the subject public key from
`cert`. Since TLS 1.2 doesn't provide enough information to map the `dss.scheme` into a single
[`SignatureVerificationAlgorithm`], this function will map to several candidates and try each in
succession until one succeeds or we exhaust all candidates.

See [WebPkiSupportedAlgorithms::mapping] for more information."""
def verify_tls12_signature(message: object, cert: CertificateDer, dss: DigitallySignedStruct, supported_schemes: WebPkiSupportedAlgorithms) -> HandshakeSignatureValid: ...

"""Verify a message signature using the `cert` public key and the first TLS 1.3 compatible
supported scheme.

This function verifies the `dss` signature over `message` using the subject public key from
`cert`. Unlike [verify_tls12_signature], this function only tries the first matching scheme. See
[WebPkiSupportedAlgorithms::mapping] for more information."""
def verify_tls13_signature(msg: object, cert: CertificateDer, dss: DigitallySignedStruct, supported_schemes: WebPkiSupportedAlgorithms) -> HandshakeSignatureValid: ...

"""Verify a message signature using a raw public key and the first TLS 1.3 compatible
supported scheme."""
def verify_tls13_signature_with_raw_key(msg: object, spki: SubjectPublicKeyInfoDer, dss: DigitallySignedStruct, supported_schemes: WebPkiSupportedAlgorithms) -> HandshakeSignatureValid: ...

"""[HKDF-Expand-Label] where the output is an AEAD key.

[HKDF-Expand-Label]: <https://www.rfc-editor.org/rfc/rfc8446#section-7.1>"""
def derive_traffic_key(expander: dynHkdfExpander, aead_alg: dynTls13AeadAlgorithm) -> AeadKey: ...

"""[HKDF-Expand-Label] where the output is an IV.

[HKDF-Expand-Label]: <https://www.rfc-editor.org/rfc/rfc8446#section-7.1>"""
def derive_traffic_iv(expander: dynHkdfExpander) -> Iv: ...

def fuzz_deframer(data: object) -> None: ...

"""Convert a public key and algorithm identifier into [`SubjectPublicKeyInfoDer`]."""
def public_key_to_spki(alg_id: AlgorithmIdentifier, public_key: object) -> SubjectPublicKeyInfoDer: ...

"""Parse `der` as any supported key encoding/type, returning
the first which works."""
def any_supported_type(der: PrivateKeyDer) -> object: ...

"""Parse `der` as any ECDSA key type, returning the first which works.

Both SEC1 (PEM section starting with 'BEGIN EC PRIVATE KEY') and PKCS8
(PEM section starting with 'BEGIN PRIVATE KEY') encodings are supported."""
def any_ecdsa_type(der: PrivateKeyDer) -> object: ...

"""Parse `der` as any EdDSA key type, returning the first which works.

Note that, at the time of writing, Ed25519 does not have wide support
in browsers.  It is also not supported by the WebPKI, because the
CA/Browser Forum Baseline Requirements do not support it for publicly
trusted certificates."""
def any_eddsa_type(der: PrivatePkcs8KeyDer) -> object: ...

"""A `CryptoProvider` backed by aws-lc-rs."""
def default_provider() -> CryptoProvider: ...

"""Parse `der` as any supported key encoding/type, returning
the first which works."""
def any_supported_type(der: PrivateKeyDer) -> object: ...

"""Parse `der` as any ECDSA key type, returning the first which works.

Both SEC1 (PEM section starting with 'BEGIN EC PRIVATE KEY') and PKCS8
(PEM section starting with 'BEGIN PRIVATE KEY') encodings are supported."""
def any_ecdsa_type(der: PrivateKeyDer) -> object: ...

"""Parse `der` as any EdDSA key type, returning the first which works.

Note that, at the time of writing, Ed25519 does not have wide support
in browsers.  It is also not supported by the WebPKI, because the
CA/Browser Forum Baseline Requirements do not support it for publicly
trusted certificates."""
def any_eddsa_type(der: PrivatePkcs8KeyDer) -> object: ...

"""A `CryptoProvider` backed by the [*ring*] crate.

[*ring*]: https://github.com/briansmith/ring"""
def default_provider() -> CryptoProvider: ...

"""This function returns a [`CryptoProvider`] that uses
FIPS140-3-approved cryptography.

Using this function expresses in your code that you require
FIPS-approved cryptography, and will not compile if you make
a mistake with cargo features.

See our [FIPS documentation](crate::manual::_06_fips) for
more detail.

Install this as the process-default provider, like:

```rust
# #[cfg(feature = "fips")] {
rustls::crypto::default_fips_provider().install_default()
.expect("default provider already set elsewhere");
# }
```

You can also use this explicitly, like:

```rust
# #[cfg(feature = "fips")] {
# let root_store = rustls::RootCertStore::empty();
let config = rustls::ClientConfig::builder_with_provider(
rustls::crypto::default_fips_provider().into()
)
.with_safe_default_protocol_versions()
.unwrap()
.with_root_certificates(root_store)
.with_no_client_auth();
# }
```"""
def default_fips_provider() -> CryptoProvider: ...

"""`HKDF-Expand(PRK, info, L)` to construct any type from a byte array.

- `PRK` is the implicit key material represented by this instance.
- `L := N`; N is the size of the byte array.
- `info` is a slice of byte slices, which should be processed sequentially
(or concatenated if that is not possible).

This is infallible, because the set of types (and therefore their length) is known
at compile time."""
def expand(expander: dynHkdfExpander, info: object) -> T: ...

"""Returns a TLS1.3 `additional_data` encoding.

See RFC8446 s5.2 for the `additional_data` definition."""
def make_tls13_aad(payload_len: int) -> object: ...

"""Returns a TLS1.2 `additional_data` encoding.

See RFC5246 s6.2.3.3 for the `additional_data` definition."""
def make_tls12_aad(seq: int, typ: ContentType, vers: ProtocolVersion, len: int) -> object: ...

"""Returns the supported `CertDecompressor` implementations enabled
by crate features."""
def default_cert_decompressors() -> object: ...

"""Returns the supported `CertCompressor` implementations enabled
by crate features."""
def default_cert_compressors() -> object: ...

__all__: list[str] = ["verify_server_cert_signed_by_trust_anchor", "verify_server_name", "verify_tls12_signature", "verify_tls13_signature", "verify_tls13_signature_with_raw_key", "derive_traffic_key", "derive_traffic_iv", "fuzz_deframer", "public_key_to_spki", "any_supported_type", "any_ecdsa_type", "any_eddsa_type", "default_provider", "any_supported_type", "any_ecdsa_type", "any_eddsa_type", "default_provider", "default_fips_provider", "expand", "make_tls13_aad", "make_tls12_aad", "default_cert_decompressors", "default_cert_compressors", "RootCertStore", "ClientCertVerifierBuilder", "WebPkiClientVerifier", "WebPkiSupportedAlgorithms", "ParsedCertificate", "ServerCertVerifierBuilder", "WebPkiServerVerifier", "KeyLogFile", "Mutex", "Mutex", "Poisoned", "Tls13CipherSuite", "Reader", "Writer", "ConnectionCommon", "UnbufferedConnectionCommon", "KernelConnection", "UnbufferedStatus", "ReadTraffic", "ReadEarlyData", "AppDataRecord", "WriteTraffic", "EncodeTlsData", "TransmitTlsData", "InsufficientSizeError", "NoKeyLog", "DefaultTimeProvider", "ClientConnection", "ServerConnection", "ConnectionCommon", "Secrets", "DirectionalKeys", "Tag", "PacketKeySet", "Suite", "Keys", "ClientHello", "ServerConfig", "ReadEarlyData", "ServerConnection", "Acceptor", "AcceptedAlert", "UnbufferedServerConnection", "Accepted", "ServerConnectionData", "NoServerSessionStorage", "ServerSessionMemoryCache", "AlwaysResolvesServerRawPublicKeys", "ResolvesServerCertUsingSni", "WantsServerCert", "CipherSuiteCommon", "ExtractedSecrets", "SupportedProtocolVersion", "Tls12CipherSuite", "ConfigBuilder", "WantsVersions", "WantsVerifier", "MessageFragmenter", "InboundOpaqueMessage", "BorrowedPayload", "InboundPlainMessage", "OutboundPlainMessage", "OutboundOpaqueMessage", "PrefixedPayload", "PlainMessage", "Message", "Tls13ClientSessionValue", "Tls12ClientSessionValue", "ClientSessionCommon", "ServerSessionValue", "PayloadU16", "MaybeEmpty", "NonEmpty", "ChangeCipherSpecPayload", "Reader", "u24", "FfdheGroup", "UnknownExtension", "HandshakeMessagePayload", "HpkeSymmetricCipherSuite", "HpkeKeyConfig", "EchConfigContents", "AlertMessagePayload", "GetRandomFailed", "PrfUsingHmac", "SingleCertAndKey", "CertifiedKey", "RsaSigningKey", "Ticketer", "HpkeAwsLcRs", "Output", "RsaSigningKey", "Ticketer", "CryptoProvider", "CompletedKeyExchange", "SharedSecret", "HkdfExpanderUsingHmac", "HkdfUsingHmac", "OkmBlock", "OutputLengthError", "UnsupportedOperationError", "KeyBlockShape", "Iv", "Nonce", "AeadKey", "Tag", "HpkeSuite", "HpkePublicKey", "HpkePrivateKey", "HpkeKeyPair", "EncapsulatedSecret", "TicketSwitcher", "TicketRotator", "EchConfig", "EchGreaseConfig", "ClientConfig", "Resumption", "DangerousClientConfig", "WriteEarlyData", "ClientConnection", "UnbufferedClientConnection", "MayEncryptEarlyData", "ClientConnectionData", "ClientSessionMemoryCache", "AlwaysResolvesClientRawPublicKeys", "DangerousClientConfigBuilder", "WantsClientCert", "CommonState", "IoState", "DecompressionFailed", "CompressionFailed", "CompressionCacheInner", "Stream", "StreamOwned", "OtherError", "HandshakeSignatureValid", "ServerCertVerified", "ClientCertVerified", "NoClientAuth", "DigitallySignedStruct", "VerifierBuilderError", "Connection", "ConnectionState", "EncodeError", "EncryptError", "Connection", "KeyChange", "Version", "SupportedCipherSuite", "ConnectionTrafficSecrets", "OutboundChunks", "MessagePayload", "MessageError", "Payload", "KeyExchangeAlgorithm", "EchConfigPayload", "EchConfigExtension", "EchMode", "EchStatus", "Tls12Resumption", "EarlyDataError", "HandshakeKind", "Side", "CompressionLevel", "CompressionCache", "Error", "InconsistentKeys", "InvalidMessage", "PeerMisbehaved", "PeerIncompatible", "CertificateError", "ExtendedKeyPurpose", "CertRevocationListError", "EncryptedClientHelloError"]
