"""Python stubs for the redis Rust crate.

Install with: cookcrab install redis
"""

from __future__ import annotations

from typing import Self

class SendError:
    """An error showing that the receiver"""
    pass

class Monitor:
    """Represents a `Monitor` connection."""

    def on_message(self) -> object: ...

    def into_on_message(self) -> object: ...

class PubSubSink:
    """The sink part of a split async Pubsub.

The sink is used to subscribe and unsubscribe from
channels.
The stream part is independent from the sink,
and dropping the sink doesn't cause the stream part to
stop working.
The sink isn't independent from the stream - dropping
the stream will cause the sink to return errors on requests."""

    def subscribe(self, channel_name: object) -> object: ...

    def unsubscribe(self, channel_name: object) -> object: ...

    def psubscribe(self, channel_pattern: object) -> object: ...

    def punsubscribe(self, channel_pattern: object) -> object: ...

    def ping_message(self, message: object) -> object: ...

    def ping(self) -> object: ...

class PubSub:
    """A connection dedicated to RESP2 pubsub messages.

If you're using a DB that supports RESP3, consider using a regular connection and setting a [crate::aio::AsyncPushSender] on it using [crate::client::AsyncConnectionConfig::set_push_sender]."""

    @staticmethod
    def new(connection_info: RedisConnectionInfo, stream: C) -> object: ...

    def subscribe(self, channel_name: object) -> object: ...

    def unsubscribe(self, channel_name: object) -> object: ...

    def psubscribe(self, channel_pattern: object) -> object: ...

    def punsubscribe(self, channel_pattern: object) -> object: ...

    def ping(self) -> object: ...

    def ping_message(self, message: object) -> object: ...

    def on_message(self) -> object: ...

    def into_on_message(self) -> PubSubStream: ...

    def split(self) -> object: ...

    def subscribe(self, channel: T) -> object: ...

    def psubscribe(self, pchannel: T) -> object: ...

    def unsubscribe(self, channel: T) -> object: ...

    def punsubscribe(self, pchannel: T) -> object: ...

    def ping_message(self, message: object) -> object: ...

    def ping(self) -> object: ...

    def get_message(self) -> object: ...

    def set_read_timeout(self, dur: Duration | None) -> object: ...

    def drop(self) -> None: ...

class ConnectionManagerConfig:
    """The configuration for reconnect mechanism and request timing for the [ConnectionManager]"""

    def fmt(self, f: Formatter) -> None: ...

    @staticmethod
    def new() -> "ConnectionManagerConfig": ...

    def min_delay(self) -> Duration: ...

    def max_delay(self) -> Duration | None: ...

    def exponent_base(self) -> float: ...

    def number_of_retries(self) -> int: ...

    def response_timeout(self) -> Duration | None: ...

    def connection_timeout(self) -> Duration | None: ...

    def automatic_resubscription(self) -> bool: ...

    def cache_config(self) -> object: ...

    def set_min_delay(self, min_delay: Duration) -> ConnectionManagerConfig: ...

    def set_max_delay(self, time: Duration) -> ConnectionManagerConfig: ...

    def set_exponent_base(self, base: float) -> ConnectionManagerConfig: ...

    def set_number_of_retries(self, amount: int) -> ConnectionManagerConfig: ...

    def set_response_timeout(self, duration: Duration | None) -> ConnectionManagerConfig: ...

    def set_connection_timeout(self, duration: Duration | None) -> ConnectionManagerConfig: ...

    def set_push_sender(self, sender: object) -> Self: ...

    def set_automatic_resubscription(self) -> Self: ...

    def set_cache_config(self, cache_config: CacheConfig) -> Self: ...

    def set_pipeline_buffer_size(self, size: int) -> Self: ...

    def set_concurrency_limit(self, limit: int) -> Self: ...

    def set_credentials_provider(self, provider: P) -> Self: ...

    @staticmethod
    def default() -> "ConnectionManagerConfig": ...

class ConnectionManager:
    """A `ConnectionManager` is a proxy that wraps a [multiplexed
connection][multiplexed-connection] and automatically reconnects to the
server when necessary.

Like the [`MultiplexedConnection`][multiplexed-connection], this
manager can be cloned, allowing requests to be sent concurrently on
the same underlying connection (tcp/unix socket).

## Behavior

- When creating an instance of the `ConnectionManager`, an initial
connection will be established and awaited. Connection errors will be
returned directly.
- When a command sent to the server fails with an error that represents
a "connection dropped" condition, that error will be passed on to the
user, but it will trigger a reconnection in the background.
- The reconnect code will atomically swap the current (dead) connection
with a future that will eventually resolve to a `MultiplexedConnection`
or to a `RedisError`
- All commands that are issued after the reconnect process has been
initiated, will have to await the connection future.
- If reconnecting fails, all pending commands will be failed as well. A
new reconnection attempt will be triggered if the error is an I/O error.
- If the connection manager uses RESP3 connection,it actively listens to updates from the
server, and so it will cause the manager to reconnect after a disconnection, even if the manager was unused at
the time of the disconnect.

[multiplexed-connection]: struct.MultiplexedConnection.html"""

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(client: Client) -> object: ...

    @staticmethod
    def new_with_config(client: Client, config: ConnectionManagerConfig) -> object: ...

    @staticmethod
    def new_lazy_with_config(client: Client, config: ConnectionManagerConfig) -> object: ...

    def send_packed_command(self, cmd: Cmd) -> object: ...

    def send_packed_commands(self, cmd: Pipeline, offset: int, count: int) -> object: ...

    def subscribe(self, channel_name: object) -> object: ...

    def unsubscribe(self, channel_name: object) -> object: ...

    def psubscribe(self, channel_pattern: object) -> object: ...

    def punsubscribe(self, channel_pattern: object) -> object: ...

    def get_cache_statistics(self) -> CacheStatistics | None: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, cmd: Pipeline, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

class MultiplexedConnection:
    """A connection object which can be cloned, allowing requests to be be sent concurrently
on the same underlying connection (tcp/unix socket).

This connection object is cancellation-safe, and the user can drop request future without polling them to completion,
but this doesn't mean that the actual request sent to the server is cancelled.
A side-effect of this is that the underlying connection won't be closed until all sent requests have been answered,
which means that in case of blocking commands, the underlying connection resource might not be released,
even when all clones of the multiplexed connection have been dropped (see <https://github.com/redis-rs/redis-rs/issues/1236>).
This isn't an issue in a connection that was created in a canonical way, which ensures that `_task_handle` is set, so that
once all of the connection's clones are dropped, the task will also be dropped. If the user creates the connection in
another way and `_task_handle` isn't set, they should manually spawn the returned driver function, keep the spawned task's
handle and abort the task whenever they want, at the risk of effectively closing the clones of the multiplexed connection."""

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new(connection_info: RedisConnectionInfo, stream: C) -> object: ...

    @staticmethod
    def new_with_config(connection_info: RedisConnectionInfo, stream: C, config: AsyncConnectionConfig) -> object: ...

    def set_response_timeout(self, timeout: Duration) -> None: ...

    def send_packed_command(self, cmd: Cmd) -> object: ...

    def send_packed_commands(self, cmd: Pipeline, offset: int, count: int) -> object: ...

    def get_cache_statistics(self) -> CacheStatistics | None: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, cmd: Pipeline, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

    def subscribe(self, channel_name: object) -> object: ...

    def unsubscribe(self, channel_name: object) -> object: ...

    def psubscribe(self, channel_pattern: object) -> object: ...

    def punsubscribe(self, channel_pattern: object) -> object: ...

    @staticmethod
    def connect_with_config(info: T, config: AsyncConnectionConfig) -> object: ...

class ValueCodec:

    def encode(self, item: list[int], dst: BytesMut) -> None: ...

    def decode(self, bytes: BytesMut) -> Item | None: ...

    def decode_eof(self, bytes: BytesMut) -> Item | None: ...

class Parser:
    """The internal redis response parser."""

    @staticmethod
    def default() -> "Parser": ...

    @staticmethod
    def new() -> "Parser": ...

    def parse_value(self, reader: T) -> object: ...

class ServerError:
    """An error that was returned from the server"""

    def kind(self) -> ServerErrorKind | None: ...

    def code(self) -> str: ...

    def details(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def try_from(err: RedisError) -> "ServerError": ...

class RedisError:
    """Represents a redis error.

For the most part you should be using the Error trait to interact with this
rather than the actual struct."""

    @staticmethod
    def from_(_: Elapsed) -> "RedisError": ...

    @staticmethod
    def from_(serde_err: Exception) -> "RedisError": ...

    def eq(self, other: RedisError) -> bool: ...

    @staticmethod
    def from_(err: Exception) -> "RedisError": ...

    @staticmethod
    def from_(err: InvalidDnsNameError) -> "RedisError": ...

    @staticmethod
    def from_(err: Exception) -> "RedisError": ...

    @staticmethod
    def from_(_: object) -> "RedisError": ...

    @staticmethod
    def from_(_: object) -> "RedisError": ...

    def source(self) -> object: ...

    def fmt(self, f: Formatter) -> None: ...

    def fmt(self, f: Formatter) -> None: ...

    def kind(self) -> ErrorKind: ...

    def detail(self) -> object: ...

    def code(self) -> object: ...

    def category(self) -> str: ...

    def is_io_error(self) -> bool: ...

    def is_cluster_error(self) -> bool: ...

    def is_connection_refusal(self) -> bool: ...

    def is_timeout(self) -> bool: ...

    def is_connection_dropped(self) -> bool: ...

    def is_unrecoverable_error(self) -> bool: ...

    def redirect_node(self) -> object | None: ...

    def retry_method(self) -> RetryMethod: ...

    def into_server_errors(self) -> object: ...

    @staticmethod
    def from_(err: Exception) -> "RedisError": ...

    @staticmethod
    def from_(err: Exception) -> "RedisError": ...

    @staticmethod
    def from_(err: ServerError) -> "RedisError": ...

    @staticmethod
    def from_(err: ParsingError) -> "RedisError": ...

class ParsingError:
    """Describes a type conversion or parsing failure."""

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def from_(err: NulError) -> "ParsingError": ...

    @staticmethod
    def from_(_: Utf8Error) -> "ParsingError": ...

    @staticmethod
    def from_(err: Exception) -> "ParsingError": ...

    @staticmethod
    def from_(err: FromUtf8Error) -> "ParsingError": ...

    @staticmethod
    def from_(err: str) -> "ParsingError": ...

    @staticmethod
    def from_(err: object) -> "ParsingError": ...

    @staticmethod
    def from_(err: ArcStr) -> "ParsingError": ...

class ClientCertificate:
    """A client certificate in PKCS12 (PFX) that can be used for client certificate authentication.

The certificate data should be base64-encoded PKCS12 content.
If the PKCS12 archive is password-protected, provide the password via `password`."""
    pass

class EntraIdCredentialsProvider:
    """Entra ID credentials provider that uses Azure Identity for authentication"""

    @staticmethod
    def new_developer_tools() -> object: ...

    @staticmethod
    def new_developer_tools_with_scopes(scopes: list[str], options: DeveloperToolsCredentialOptions | None) -> object: ...

    @staticmethod
    def new_client_secret(tenant_id: str, client_id: str, client_secret: str) -> object: ...

    @staticmethod
    def new_client_secret_with_scopes(tenant_id: str, client_id: str, client_secret: str, scopes: list[str], options: ClientSecretCredentialOptions | None) -> object: ...

    @staticmethod
    def new_client_certificate(tenant_id: str, client_id: str, client_certificate: ClientCertificate) -> object: ...

    @staticmethod
    def new_client_certificate_with_scopes(tenant_id: str, client_id: str, client_certificate: ClientCertificate, scopes: list[str], options: ClientCertificateCredentialOptions | None) -> object: ...

    @staticmethod
    def new_system_assigned_managed_identity() -> object: ...

    @staticmethod
    def new_system_assigned_managed_identity_with_scopes(scopes: list[str], options: ManagedIdentityCredentialOptions | None) -> object: ...

    @staticmethod
    def new_user_assigned_managed_identity() -> object: ...

    @staticmethod
    def new_user_assigned_managed_identity_with_scopes(scopes: list[str], options: ManagedIdentityCredentialOptions | None) -> object: ...

    @staticmethod
    def new_with_credential(credential_provider: object, scopes: list[str]) -> object: ...

    def start(self, retry_config: RetryConfig) -> None: ...

    def subscribe(self) -> object: ...

    def fmt(self, f: Formatter) -> Result: ...

class Sentinel:
    """The Sentinel type, serves as a special purpose client which builds other clients on
demand."""

    @staticmethod
    def build(params: list[T]) -> object: ...

    @staticmethod
    def build(params: list[T]) -> object: ...

    def master_for(self, service_name: str, node_connection_info: object) -> object: ...

    def get_replica_clients(self, service_name: str, node_connection_info: object) -> object: ...

    def replica_for(self, service_name: str, node_connection_info: object) -> object: ...

    def replica_rotate_for(self, service_name: str, node_connection_info: object) -> object: ...

    def async_master_for(self, service_name: str, node_connection_info: object) -> object: ...

    def async_get_replica_clients(self, service_name: str, node_connection_info: object) -> object: ...

    def async_replica_for(self, service_name: str, node_connection_info: object) -> object: ...

    def async_replica_rotate_for(self, service_name: str, node_connection_info: object) -> object: ...

class SentinelNodeConnectionInfo:
    """Holds the connection information that a sentinel should use when connecting to the
servers (masters and replicas) belonging to it."""

    def set_tls_mode(self, tls_mode: TlsMode) -> Self: ...

    def set_redis_connection_info(self, redis_connection_info: RedisConnectionInfo) -> Self: ...

    def set_tcp_settings(self, tcp_settings: TcpSettings) -> Self: ...

class LockedSentinelClient:
    """LockedSentinelClient is a wrapper around SentinelClient usable in r2d2."""

    @staticmethod
    def new(client: SentinelClient) -> "LockedSentinelClient": ...

    def get_connection(self) -> object: ...

class AsyncLockedSentinelClient:
    """AsyncLockedSentinelClient is a wrapper around SentinelClient usable in bb8."""

    @staticmethod
    def new(client: SentinelClient) -> "AsyncLockedSentinelClient": ...

    def get_async_connection(self) -> object: ...

class SentinelClient:
    """A utility wrapping `Sentinel` with an interface similar to [Client].

Uses the Sentinel type internally. This is a utility to help make it easier
to use sentinels but with an interface similar to the client (`get_connection` and
`get_async_connection`). The type of server (master or replica) and name of the
desired master are specified when constructing an instance, so it will always
return connections to the same target (for example, always to the master with name
"mymaster123", or always to replicas of the master "another-master-abc")."""

    @staticmethod
    def build(params: list[T], service_name: str, node_connection_info: SentinelNodeConnectionInfo | None, server_type: SentinelServerType) -> object: ...

    @staticmethod
    def build(params: list[T], service_name: object, node_connection_info: SentinelNodeConnectionInfo | None, server_type: SentinelServerType) -> object: ...

    def get_client(self) -> object: ...

    def get_sentinel_client(self) -> object: ...

    def get_connection(self) -> object: ...

    def async_get_client(self) -> object: ...

    def async_get_sentinel_client(self) -> object: ...

    def get_async_connection(self) -> object: ...

    def get_async_connection_with_config(self, config: AsyncConnectionConfig) -> object: ...

class SentinelClientBuilder:
    """Used to configure and build a [`SentinelClient`].
There are two connections that can be configured independently
1. The connection towards the redis nodes (configured via `set_client_to_redis_..` functions)
2. The connection towards the sentinel nodes (configure via `set_client_to_sentinel_..` functions)"""

    @staticmethod
    def new(sentinels: T, service_name: object, server_type: SentinelServerType) -> object: ...

    def build(self) -> object: ...

    def set_client_to_redis_tls_mode(self, tls_mode: TlsMode) -> SentinelClientBuilder: ...

    def set_client_to_redis_db(self, db: int) -> SentinelClientBuilder: ...

    def set_client_to_redis_username(self, username: object) -> SentinelClientBuilder: ...

    def set_client_to_redis_password(self, password: object) -> SentinelClientBuilder: ...

    def set_client_to_redis_protocol(self, protocol: ProtocolVersion) -> SentinelClientBuilder: ...

    def set_client_to_redis_certificates(self, certificates: TlsCertificates) -> SentinelClientBuilder: ...

    def set_client_to_redis_tcp_settings(self, tcp_settings: TcpSettings) -> SentinelClientBuilder: ...

    def set_client_to_sentinel_tls_mode(self, tls_mode: TlsMode) -> SentinelClientBuilder: ...

    def set_client_to_sentinel_username(self, username: object) -> SentinelClientBuilder: ...

    def set_client_to_sentinel_password(self, password: object) -> SentinelClientBuilder: ...

    def set_client_to_sentinel_tcp_settings(self, tcp_settings: TcpSettings) -> SentinelClientBuilder: ...

    def set_client_to_sentinel_protocol(self, protocol: ProtocolVersion) -> SentinelClientBuilder: ...

    def set_client_to_sentinel_certificates(self, certificates: TlsCertificates) -> SentinelClientBuilder: ...

class InfoDict:
    """An info dictionary type for `INFO`s response.

This type provides convenient access to key/value data returned by
the `INFO` command.  It acts like a regular mapping but also has
a convenience method `get` which can return data in the appropriate
type.

For instance this can be used to query the server for the role it's
in (master, slave) etc:

# Caveats

As this struct internally uses a [`HashMap`], it only collects the last value for each key, if
they occur multiple times. So if a key occurs multiple times (e.g.: `module`), this struct holds
only its last value.

# Examples

```rust,no_run
# fn do_something() -> redis::RedisResult<()> {
# let client = redis::Client::open("redis://127.0.0.1/").unwrap();
# let mut con = client.get_connection().unwrap();
let info : redis::InfoDict = redis::cmd("INFO").query(&mut con)?;
let role : Option<String> = info.get("role");
# Ok(()) }
```"""

    @staticmethod
    def new(kvpairs: str) -> "InfoDict": ...

    def get(self, key: str) -> T | None: ...

    def find(self, key: str) -> object: ...

    def contains_key(self, key: str) -> bool: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def deref(self) -> Target: ...

    @staticmethod
    def from_redis_value_ref(v: Value) -> "InfoDict": ...

    @staticmethod
    def from_redis_value(v: Value) -> "InfoDict": ...

class ReplicaInfo:
    """Replication information for a replica, as returned by the [`ROLE`][1] command.

[1]: https://redis.io/docs/latest/commands/role/"""

    @staticmethod
    def from_redis_value_ref(v: Value) -> object: ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class PushInfo:
    """A push message from the server."""
    pass

class Client:
    """The client type."""

    @staticmethod
    def open(params: T) -> object: ...

    def get_connection(self) -> object: ...

    def get_connection_with_timeout(self, timeout: Duration) -> object: ...

    def get_connection_info(self) -> ConnectionInfo: ...

    @staticmethod
    def build_with_tls(conn_info: C, tls_certs: TlsCertificates) -> object: ...

    def get_multiplexed_async_connection(self) -> object: ...

    def get_multiplexed_async_connection_with_config(self, config: AsyncConnectionConfig) -> object: ...

    def get_connection_manager(self) -> object: ...

    def get_connection_manager_lazy(self, config: ConnectionManagerConfig) -> object: ...

    def get_connection_manager_with_config(self, config: ConnectionManagerConfig) -> object: ...

    def get_async_pubsub(self) -> object: ...

    def get_async_monitor(self) -> object: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, cmd: object, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

    def check_connection(self) -> bool: ...

    def is_open(self) -> bool: ...

class AsyncConnectionConfig:
    """Options for creation of async connection"""

    @staticmethod
    def default() -> "AsyncConnectionConfig": ...

    @staticmethod
    def new() -> "AsyncConnectionConfig": ...

    def set_connection_timeout(self, connection_timeout: Duration | None) -> Self: ...

    def set_response_timeout(self, response_timeout: Duration | None) -> Self: ...

    def set_push_sender(self, sender: object) -> Self: ...

    def set_cache_config(self, cache_config: CacheConfig) -> Self: ...

    def set_dns_resolver(self, dns_resolver: object) -> Self: ...

    def set_pipeline_buffer_size(self, size: int) -> Self: ...

    def set_concurrency_limit(self, limit: int) -> Self: ...

    def set_credentials_provider(self, provider: P) -> Self: ...

class NodeAddress:
    """The address of a node in a Redis Cluster.

Stores the host and port components separately, providing structured access
without repeated string parsing. The host may be an IPv4 address
(e.g. `127.0.0.1`), an IPv6 address (e.g. `dead::cafe:beef`), or a hostname
(e.g. `redis-node-1.example.com`)."""

    @staticmethod
    def new(host: object, port: int) -> "NodeAddress": ...

    @staticmethod
    def from_parts(host: ArcStr, port: int) -> "NodeAddress": ...

    def host(self) -> str: ...

    def port(self) -> int: ...

    def fmt(self, f: Formatter) -> Result: ...

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def try_from(s: str) -> object: ...

    @staticmethod
    def try_from(addr: ConnectionAddr) -> object: ...

    def eq(self, other: str) -> bool: ...

    def eq(self, other: str) -> bool: ...

class ClusterConfig:
    """Options for creation of connection"""

    @staticmethod
    def new() -> "ClusterConfig": ...

    def set_connection_timeout(self, connection_timeout: Duration) -> Self: ...

    def set_response_timeout(self, response_timeout: Duration) -> Self: ...

    def set_push_sender(self, sender: object) -> Self: ...

    def set_dns_resolver(self, resolver: object) -> Self: ...

class ClusterConnection:
    """This represents a Redis Cluster connection.

It stores the underlying connections maintained for each node in the cluster,
as well as common parameters for connecting to nodes and executing commands."""

    def set_auto_reconnect(self, value: bool) -> None: ...

    def set_write_timeout(self, dur: Duration | None) -> object: ...

    def set_read_timeout(self, dur: Duration | None) -> object: ...

    def check_connection(self) -> bool: ...

    def route_command(self, cmd: Cmd, routing: RoutingInfo) -> object: ...

    def supports_pipelining(self) -> bool: ...

    def req_command(self, cmd: Cmd) -> object: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, cmd: object, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

    def is_open(self) -> bool: ...

    def check_connection(self) -> bool: ...

    def route_command(self, cmd: Cmd, routing: RoutingInfo) -> object: ...

    def route_pipeline(self, pipeline: Pipeline, offset: int, count: int, route: SingleNodeRoutingInfo) -> object: ...

    def subscribe(self, channel_name: object) -> object: ...

    def unsubscribe(self, channel_name: object) -> object: ...

    def psubscribe(self, channel_pattern: object) -> object: ...

    def punsubscribe(self, channel_pattern: object) -> object: ...

    def ssubscribe(self, channel_name: object) -> object: ...

    def sunsubscribe(self, channel_name: object) -> object: ...

    def get_cache_statistics(self) -> CacheStatistics | None: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, pipeline: Pipeline, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

class ClusterPipeline:
    """Represents a Redis Cluster command pipeline."""

    @staticmethod
    def new() -> "ClusterPipeline": ...

    @staticmethod
    def with_capacity(capacity: int) -> "ClusterPipeline": ...

    def query(self, con: ClusterConnection) -> object: ...

    def exec(self, con: ClusterConnection) -> object: ...

class ClusterClientBuilder:
    """Used to configure and build a [`ClusterClient`]."""

    @staticmethod
    def new(initial_nodes: object) -> "ClusterClientBuilder": ...

    def build(self) -> object: ...

    def password(self, password: object) -> ClusterClientBuilder: ...

    def username(self, username: object) -> ClusterClientBuilder: ...

    def retries(self, retries: int) -> ClusterClientBuilder: ...

    def max_retry_wait(self, max_wait: int) -> ClusterClientBuilder: ...

    def min_retry_wait(self, min_wait: int) -> ClusterClientBuilder: ...

    def retry_wait_formula(self, factor: int, exponent_base: int) -> ClusterClientBuilder: ...

    def tls(self, tls: TlsMode) -> ClusterClientBuilder: ...

    def danger_accept_invalid_hostnames(self, insecure: bool) -> ClusterClientBuilder: ...

    def certs(self, certificates: TlsCertificates) -> ClusterClientBuilder: ...

    def read_from_replicas(self) -> ClusterClientBuilder: ...

    def read_routing_strategy(self, strategy: object) -> ClusterClientBuilder: ...

    def connection_timeout(self, connection_timeout: Duration) -> ClusterClientBuilder: ...

    def response_timeout(self, response_timeout: Duration) -> ClusterClientBuilder: ...

    def overall_response_timeout(self, timeout: Duration | None) -> ClusterClientBuilder: ...

    def use_protocol(self, protocol: ProtocolVersion) -> ClusterClientBuilder: ...

    def database_id(self, database_id: int) -> ClusterClientBuilder: ...

    def push_sender(self, push_sender: object) -> ClusterClientBuilder: ...

    def tcp_settings(self, tcp_settings: TcpSettings) -> ClusterClientBuilder: ...

    def async_dns_resolver(self, resolver: object) -> ClusterClientBuilder: ...

    def cache_config(self, cache_config: CacheConfig) -> Self: ...

    def connection_concurrency_limit(self, limit: int) -> ClusterClientBuilder: ...

    def set_credentials_provider(self, provider: P) -> ClusterClientBuilder: ...

class ClusterClient:
    """A Redis Cluster client, used to create connections."""

    @staticmethod
    def new(initial_nodes: object) -> object: ...

    @staticmethod
    def builder(initial_nodes: object) -> ClusterClientBuilder: ...

    def get_connection(self) -> object: ...

    def get_connection_with_config(self, config: ClusterConfig) -> object: ...

    def get_async_connection(self) -> object: ...

    def get_async_connection_with_config(self, config: ClusterConfig) -> object: ...

    def get_pending_async_connection_with_config(self, config: ClusterConfig) -> ClusterConnection: ...

    def get_generic_connection(self) -> object: ...

    def get_async_generic_connection(self) -> object: ...

class ClusterConnection:
    """This represents an async Redis Cluster connection.

It stores the underlying connections maintained for each node in the cluster,
as well as common parameters for connecting to nodes and executing commands."""

    def set_auto_reconnect(self, value: bool) -> None: ...

    def set_write_timeout(self, dur: Duration | None) -> object: ...

    def set_read_timeout(self, dur: Duration | None) -> object: ...

    def check_connection(self) -> bool: ...

    def route_command(self, cmd: Cmd, routing: RoutingInfo) -> object: ...

    def supports_pipelining(self) -> bool: ...

    def req_command(self, cmd: Cmd) -> object: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, cmd: object, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

    def is_open(self) -> bool: ...

    def check_connection(self) -> bool: ...

    def route_command(self, cmd: Cmd, routing: RoutingInfo) -> object: ...

    def route_pipeline(self, pipeline: Pipeline, offset: int, count: int, route: SingleNodeRoutingInfo) -> object: ...

    def subscribe(self, channel_name: object) -> object: ...

    def unsubscribe(self, channel_name: object) -> object: ...

    def psubscribe(self, channel_pattern: object) -> object: ...

    def punsubscribe(self, channel_pattern: object) -> object: ...

    def ssubscribe(self, channel_name: object) -> object: ...

    def sunsubscribe(self, channel_name: object) -> object: ...

    def get_cache_statistics(self) -> CacheStatistics | None: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, pipeline: Pipeline, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

class Route:
    """Defines the slot and the [`SlotAddr`] to which
a command should be sent"""

    @staticmethod
    def new(slot: int, slot_addr: SlotAddr) -> "Route": ...

    @staticmethod
    def with_slot(slot: Slot, slot_addr: SlotAddr) -> "Route": ...

    @staticmethod
    def with_key(key: object, slot_addr: SlotAddr) -> "Route": ...

class Slot:
    """Defines the valid redis key slot."""

    @staticmethod
    def new(slot: int) -> object: ...

    @staticmethod
    def for_key(key: object) -> "Slot": ...

class RandomReplicaStrategy:
    """Routes reads to a random replica node."""

    def route_read(self, candidates: ReadCandidates) -> object: ...

class Shard:
    """A snapshot of the topology for a single shard in the cluster.

A shard is a group of slot ranges served by the same set of nodes."""

    @staticmethod
    def new(slot_ranges: object, primary: NodeAddress, replicas: object) -> "Shard": ...

    def slot_ranges(self) -> object: ...

    def primary(self) -> NodeAddress: ...

    def replicas(self) -> object: ...

class ClusterTopology:
    """A pre-built view of the cluster topology, organized by shard.

Provides iteration over all shards and O(log n) slot-to-shard lookup."""

    @staticmethod
    def from_shards(shards: list[Shard]) -> "ClusterTopology": ...

    def shard_for_slot(self, slot: int) -> object: ...

    def shards(self) -> object: ...

class Replicas:
    """A non-empty slice of replica [`NodeAddress`]es.

This wrapper guarantees that the underlying slice contains at least one
element, so callers never need to handle the empty case."""

    @staticmethod
    def new(slice: object) -> object: ...

    def len(self) -> NonZeroUsize: ...

    def first(self) -> object: ...

    def get(self, idx: int) -> object: ...

    def choose_random(self) -> object: ...

    def iter(self) -> object: ...

class AnyNodeCandidates:
    """Candidates when any node (primary or replica) is acceptable for a read."""

    def slot(self) -> int: ...

    def primary(self) -> object: ...

    def replicas(self) -> Replicas: ...

class ReplicasOnlyCandidates:
    """Candidates when only replicas are acceptable for a read."""

    def slot(self) -> int: ...

    def replicas(self) -> Replicas: ...

class RoundRobinReplicaStrategy:
    """Routes reads to replica nodes in round-robin order.

Each instance maintains an independent counter **per shard** that increments
on every call to [`route_read`](ReadRoutingStrategy::route_read). This
ensures that reads to different shards rotate independently — a hot shard
won't skew the rotation for other shards."""

    @staticmethod
    def new() -> "RoundRobinReplicaStrategy": ...

    @staticmethod
    def default() -> "RoundRobinReplicaStrategy": ...

    def on_topology_changed(self, topology: ClusterTopology) -> None: ...

    def route_read(self, candidates: ReadCandidates) -> object: ...

class CommandCacheConfig:
    """CommandCacheConfig is used to define caching behaviour of individual commands.
# Example
```rust
use std::time::Duration;
use redis::{CommandCacheConfig, Cmd};

let ttl = Duration::from_secs(120); // 2 minutes TTL
let config = CommandCacheConfig::new()
.set_enable_cache(true)
.set_client_side_ttl(ttl);
let command = Cmd::new().arg("GET").arg("key").set_cache_config(config);
```"""

    @staticmethod
    def new() -> "CommandCacheConfig": ...

    def set_enable_cache(self, enable_cache: bool) -> Self: ...

    def set_client_side_ttl(self, client_side_ttl: Duration) -> Self: ...

    @staticmethod
    def default() -> "CommandCacheConfig": ...

class Cmd:
    """Represents redis commands."""

    def arg_idx(self, idx: int) -> object: ...

    def position(self, candidate: object) -> int | None: ...

    def fmt(self, f: Formatter) -> Result: ...

    def write_arg(self, arg: object) -> None: ...

    def write_arg_fmt(self, arg: object) -> None: ...

    def writer_for_next_arg(self) -> object: ...

    def reserve_space_for_args(self, additional: object) -> None: ...

    def bufmut_for_next_arg(self, capacity: int) -> object: ...

    @staticmethod
    def default() -> "Cmd": ...

    @staticmethod
    def new() -> "Cmd": ...

    @staticmethod
    def with_capacity(arg_count: int, size_of_data: int) -> "Cmd": ...

    def clear(self) -> None: ...

    def arg(self, arg: T) -> Cmd: ...

    def take(self) -> Self: ...

    def cursor_arg(self, cursor: int) -> Cmd: ...

    def get_packed_command(self) -> list[int]: ...

    def write_packed_command(self, dst: list[int]) -> None: ...

    def in_scan_mode(self) -> bool: ...

    def query(self, con: mutdynConnectionLike) -> object: ...

    def query_async(self, con: object) -> object: ...

    def iter(self, con: mutdynConnectionLike) -> object: ...

    def iter_async(self, con: object) -> object: ...

    def exec(self, con: mutdynConnectionLike) -> object: ...

    def exec_async(self, con: object) -> object: ...

    def args_iter(self) -> object: ...

    def set_no_response(self, nr: bool) -> Cmd: ...

    def is_no_response(self) -> bool: ...

    def set_cache_config(self, command_cache_config: CommandCacheConfig) -> Cmd: ...

class Iter:
    """Represents a redis iterator."""

    def next(self) -> object | None: ...

class AsyncIter:
    """Represents a redis iterator that can be used with async connections."""

    def next_item(self) -> object | None: ...

    def poll_next(self, cx: Context) -> object: ...

class TcpSettings:
    """Settings for a TCP stream."""

    def nodelay(self) -> bool: ...

    def keepalive(self) -> object: ...

    def user_timeout(self) -> Duration | None: ...

    def set_nodelay(self, nodelay: bool) -> Self: ...

    def set_keepalive(self, keepalive: TcpKeepalive) -> Self: ...

    def set_linger_time(self, linger: Duration) -> Self: ...

    def set_user_timeout(self, user_timeout: Duration) -> Self: ...

    @staticmethod
    def default() -> "TcpSettings": ...

class TokenRefreshConfig:
    """Configuration for token refresh behavior"""

    def set_expiration_refresh_ratio(self, ratio: float) -> Self: ...

    def set_retry_config(self, retry_config: RetryConfig) -> Self: ...

    @staticmethod
    def default() -> "TokenRefreshConfig": ...

class RetryConfig:
    """Configuration for handling failed token refresh attempts"""

    @staticmethod
    def default() -> "RetryConfig": ...

    def set_number_of_retries(self, number_of_retries: int) -> Self: ...

    def set_min_delay(self, min_delay: Duration) -> Self: ...

    def set_max_delay(self, max_delay: Duration) -> Self: ...

    def set_exponent_base(self, exponent_base: float) -> Self: ...

class Pipeline:
    """Represents a redis command pipeline."""

    def fmt(self, f: Formatter) -> Result: ...

    @staticmethod
    def new() -> "Pipeline": ...

    @staticmethod
    def with_capacity(capacity: int) -> "Pipeline": ...

    def atomic(self) -> Pipeline: ...

    def ignore_errors(self) -> Pipeline: ...

    def is_transaction(self) -> bool: ...

    def get_packed_pipeline(self) -> list[int]: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

    def query(self, con: mutdynConnectionLike) -> object: ...

    def query_async(self, con: object) -> object: ...

    def exec(self, con: mutdynConnectionLike) -> object: ...

    def exec_async(self, con: object) -> object: ...

    def set_cache_config(self, command_cache_config: CommandCacheConfig) -> Self: ...

class BloomFilterInfoTypeResponse:
    """Response of a Bloom filter info type query

`RESP2` and `RESP3` respond with different structures, so we need to abstract that difference
away to make the info type query usage simple. Note that it derefs to `f64` for ease of use."""

    def deref(self) -> Target: ...

    def eq(self, other: float) -> bool: ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class BloomFilterInsertOptions:
    """Options for inserting items to a Bloom filter"""

    def nocreate(self) -> Self: ...

    def expansion(self, scale_option: BloomFilterScalingOptions) -> Self: ...

    def error_rate(self, error_rate: float) -> Self: ...

    def capacity(self, capacity: int) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class BloomFilterDumpChunk:
    """Single chunk of a Bloom filter scan dump"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class BloomFilterDumpIterator:
    """An iterator performing a Bloom filter scan dump

# Examples

```rust,no_run
# fn dump() -> redis::RedisResult<()> {
let client = redis::Client::open("redis://127.0.0.1/")?;
let mut con = client.get_connection()?;

// Fully dump the bloom filter at key `foo`
let full_dump = redis::bloom::BloomFilterDumpIterator::new(&mut con, "foo")
.map(|r| r.expect("dump should succeed"))
.collect::<Vec<_>>();
# Ok(())
# }
```"""

    @staticmethod
    def new(con: object, key: object) -> "BloomFilterDumpIterator": ...

    def next(self) -> Item | None: ...

class TlsConnParams:
    pass

class ConnectionInfo:
    """Holds the connection information that redis should use for connecting."""

    def addr(self) -> ConnectionAddr: ...

    def tcp_settings(self) -> TcpSettings: ...

    def redis_settings(self) -> RedisConnectionInfo: ...

    def set_addr(self, addr: ConnectionAddr) -> Self: ...

    def set_tcp_settings(self, tcp_settings: TcpSettings) -> Self: ...

    def set_redis_settings(self, redis: RedisConnectionInfo) -> Self: ...

    @staticmethod
    def from_str(s: str) -> object: ...

    def into_connection_info(self) -> object: ...

class RedisConnectionInfo:
    """Redis specific/connection independent information used to establish a connection to redis."""

    def username(self) -> object: ...

    def password(self) -> object: ...

    def protocol(self) -> ProtocolVersion: ...

    def skip_set_lib_name(self) -> bool: ...

    def lib_name(self) -> object: ...

    def lib_ver(self) -> object: ...

    def db(self) -> int: ...

    def set_username(self, username: object) -> Self: ...

    def set_password(self, password: object) -> Self: ...

    def set_protocol(self, protocol: ProtocolVersion) -> Self: ...

    def set_skip_set_lib_name(self) -> Self: ...

    def set_lib_name(self, lib_name: object, lib_ver: object) -> Self: ...

    def set_db(self, db: int) -> Self: ...

    def fmt(self, f: Formatter) -> Result: ...

class Connection:
    """Represents a stateful redis TCP connection."""

    @staticmethod
    def connect(info: T, timeout: Duration | None) -> object: ...

    def send_packed_command(self, cmd: object) -> object: ...

    def set_write_timeout(self, dur: Duration | None) -> object: ...

    def set_read_timeout(self, dur: Duration | None) -> object: ...

    def recv_response(self) -> object: ...

    def send_packed_command(self, cmd: object) -> object: ...

    def recv_response(self) -> object: ...

    def set_write_timeout(self, dur: Duration | None) -> object: ...

    def set_read_timeout(self, dur: Duration | None) -> object: ...

    def as_pubsub(self) -> PubSub: ...

    def set_push_sender(self, sender: SyncPushSender) -> None: ...

    def subscribe_resp3(self, channel: T) -> object: ...

    def psubscribe_resp3(self, pchannel: T) -> object: ...

    def unsubscribe_resp3(self, channel: T) -> object: ...

    def punsubscribe_resp3(self, pchannel: T) -> object: ...

    def req_command(self, cmd: Cmd) -> object: ...

    def req_packed_command(self, cmd: object) -> object: ...

    def req_packed_commands(self, cmd: object, offset: int, count: int) -> object: ...

    def get_db(self) -> int: ...

    def check_connection(self) -> bool: ...

    def is_open(self) -> bool: ...

    def subscribe(self, channels: C, func: F) -> object: ...

    def psubscribe(self, patterns: P, func: F) -> object: ...

class PubSub:
    """Represents a RESP2 pubsub connection.

If you're using a DB that supports RESP3, consider using a regular connection and setting a push sender it using [Connection::set_push_sender]."""

    @staticmethod
    def new(connection_info: RedisConnectionInfo, stream: C) -> object: ...

    def subscribe(self, channel_name: object) -> object: ...

    def unsubscribe(self, channel_name: object) -> object: ...

    def psubscribe(self, channel_pattern: object) -> object: ...

    def punsubscribe(self, channel_pattern: object) -> object: ...

    def ping(self) -> object: ...

    def ping_message(self, message: object) -> object: ...

    def on_message(self) -> object: ...

    def into_on_message(self) -> PubSubStream: ...

    def split(self) -> object: ...

    def subscribe(self, channel: T) -> object: ...

    def psubscribe(self, pchannel: T) -> object: ...

    def unsubscribe(self, channel: T) -> object: ...

    def punsubscribe(self, pchannel: T) -> object: ...

    def ping_message(self, message: object) -> object: ...

    def ping(self) -> object: ...

    def get_message(self) -> object: ...

    def set_read_timeout(self, dur: Duration | None) -> object: ...

    def drop(self) -> None: ...

class Msg:
    """Represents a pubsub message."""

    @staticmethod
    def from_value(value: Value) -> object: ...

    @staticmethod
    def from_owned_value(value: Value) -> object: ...

    @staticmethod
    def from_push_info(push_info: PushInfo) -> object: ...

    def get_channel(self) -> object: ...

    def get_channel_name(self) -> str: ...

    def get_payload(self) -> object: ...

    def get_payload_bytes(self) -> object: ...

    def from_pattern(self) -> bool: ...

    def get_pattern(self) -> object: ...

class CacheConfig:
    """Configuration for client side caching."""

    @staticmethod
    def new() -> "CacheConfig": ...

    def set_mode(self, mode: CacheMode) -> Self: ...

    def set_size(self, size: NonZeroUsize) -> Self: ...

    def set_default_client_ttl(self, ttl: Duration) -> Self: ...

    @staticmethod
    def default() -> "CacheConfig": ...

class CacheStatistics:
    """CacheStatistics holds statistics generated by Client Side Caching."""

    @staticmethod
    def from_(value: object) -> "CacheStatistics": ...

class Script:
    """Represents a lua script."""

    @staticmethod
    def new(code: str) -> "Script": ...

    def get_hash(self) -> str: ...

    def load(self, con: mutdynConnectionLike) -> object: ...

    def load_async(self, con: C) -> object: ...

    def key(self, key: T) -> ScriptInvocation: ...

    def arg(self, arg: T) -> ScriptInvocation: ...

    def prepare_invoke(self) -> ScriptInvocation: ...

    def invoke(self, con: mutdynConnectionLike) -> object: ...

    def invoke_async(self, con: C) -> object: ...

class ScriptInvocation:
    """Represents a prepared script call."""

    def arg(self, arg: T) -> object: ...

    def key(self, key: T) -> object: ...

    def invoke(self, con: mutdynConnectionLike) -> object: ...

    def invoke_async(self, con: object) -> object: ...

    def load(self, con: mutdynConnectionLike) -> object: ...

    def load_async(self, con: C) -> object: ...

class BasicAuth:
    """Basic authentication credentials for a Redis connection"""

    @staticmethod
    def new(username: str, password: str) -> "BasicAuth": ...

    def username(self) -> str: ...

    def password(self) -> str: ...

    def set_username(self, username: str) -> None: ...

    def set_password(self, password: str) -> None: ...

class ClientTlsConfig:
    """Structure to hold mTLS client _certificate_ and _key_ binaries in PEM format
"""
    pass

class TlsCertificates:
    """Structure to hold TLS certificates
- `client_tls`: binaries of clientkey and certificate within a `ClientTlsConfig` structure if mTLS is used
- `root_cert`: binary CA certificate in PEM format if CA is not in local truststore
"""
    pass

class ClientTlsParams:

    def clone(self) -> Self: ...

class StreamTrimOptions:
    """Builder options for [`xtrim_options`] command

[`xtrim_options`]: ../trait.Commands.html#method.xtrim_options
"""

    @staticmethod
    def maxlen(mode: StreamTrimmingMode, max_entries: int) -> "StreamTrimOptions": ...

    @staticmethod
    def minid(mode: StreamTrimmingMode, stream_id: object) -> "StreamTrimOptions": ...

    def limit(self, limit: int) -> Self: ...

    def set_deletion_policy(self, deletion_policy: StreamDeletionPolicy) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class StreamConfigOptions:
    """Configuration options for [`xcfgset`] command

Configures idempotency parameters for a stream.
Use the constructor methods to create an instance with at least one parameter set,
or use the setter methods to add parameters to an existing instance.

[`xcfgset`]: ../trait.Commands.html#method.xcfgset

# Example
```no_run
use redis::{Commands, streams::StreamConfigOptions};
# let client = redis::Client::open("redis://127.0.0.1/").unwrap();
# let mut con = client.get_connection().unwrap();

// Create with idempotency duration in seconds, optionally add maxsize
let opts1 = StreamConfigOptions::with_idempotency_seconds(300)
.unwrap()
.idempotency_maxsize(1000)
.unwrap();
let _: String = con.xcfgset("key", &opts1).unwrap();

// Or create with maxsize only and optionally add idempotency duration in seconds
let opts2 = StreamConfigOptions::with_idempotency_maxsize(500)
.unwrap()
.idempotency_seconds(300)
.unwrap();
let _: String = con.xcfgset("key", &opts2).unwrap();
```"""

    @staticmethod
    def with_idempotency_seconds(seconds: int) -> object: ...

    @staticmethod
    def with_idempotency_maxsize(size: int) -> object: ...

    def idempotency_seconds(self, seconds: int) -> object: ...

    def idempotency_maxsize(self, size: int) -> object: ...

    def write_redis_args(self, out: W) -> None: ...

class StreamAddOptions:
    """Builder options for [`xadd_options`] command

[`xadd_options`]: ../trait.Commands.html#method.xadd_options
"""

    def nomkstream(self) -> Self: ...

    def trim(self, trim: StreamTrimStrategy) -> Self: ...

    def set_deletion_policy(self, deletion_policy: StreamDeletionPolicy) -> Self: ...

    def idmp(self, producer_id: object, idempotent_id: object) -> Self: ...

    def idmpauto(self, producer_id: object) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class StreamAutoClaimOptions:
    """Builder options for [`xautoclaim_options`] command.

[`xautoclaim_options`]: ../trait.Commands.html#method.xautoclaim_options
"""

    def count(self, n: int) -> Self: ...

    def with_justid(self) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class StreamClaimOptions:
    """Builder options for [`xclaim_options`] command.

[`xclaim_options`]: ../trait.Commands.html#method.xclaim_options
"""

    def idle(self, ms: int) -> Self: ...

    def time(self, ms_time: int) -> Self: ...

    def retry(self, count: int) -> Self: ...

    def with_force(self) -> Self: ...

    def with_justid(self) -> Self: ...

    def with_lastid(self, lastid: object) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class StreamReadOptions:
    """Builder options for [`xread_options`] command.

[`xread_options`]: ../trait.Commands.html#method.xread_options
"""

    def read_only(self) -> bool: ...

    def noack(self) -> Self: ...

    def block(self, ms: int) -> Self: ...

    def count(self, n: int) -> Self: ...

    def group(self, group_name: GN, consumer_name: CN) -> Self: ...

    def claim(self, min_idle_time: int) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class StreamAutoClaimReply:
    """Reply type used with the [`xautoclaim_options`] command.

[`xautoclaim_options`]: ../trait.Commands.html#method.xautoclaim_options
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamReadReply:
    """Reply type used with [`xread`] or [`xread_options`] commands.

[`xread`]: ../trait.Commands.html#method.xread
[`xread_options`]: ../trait.Commands.html#method.xread_options
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamRangeReply:
    """Reply type used with [`xrange`], [`xrange_count`], [`xrange_all`], [`xrevrange`], [`xrevrange_count`], [`xrevrange_all`] commands.

Represents stream entries matching a given range of `id`'s.

[`xrange`]: ../trait.Commands.html#method.xrange
[`xrange_count`]: ../trait.Commands.html#method.xrange_count
[`xrange_all`]: ../trait.Commands.html#method.xrange_all
[`xrevrange`]: ../trait.Commands.html#method.xrevrange
[`xrevrange_count`]: ../trait.Commands.html#method.xrevrange_count
[`xrevrange_all`]: ../trait.Commands.html#method.xrevrange_all
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamClaimReply:
    """Reply type used with [`xclaim`] command.

Represents that ownership of the specified messages was changed.

[`xclaim`]: ../trait.Commands.html#method.xclaim
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamPendingData:
    """Inner reply type when an [`xpending`] command has data.

[`xpending`]: ../trait.Commands.html#method.xpending"""
    pass

class StreamPendingCountReply:
    """Reply type used with [`xpending_count`] and
[`xpending_consumer_count`] commands.

Data returned here have been fetched from the stream without
any acknowledgement.

[`xpending_count`]: ../trait.Commands.html#method.xpending_count
[`xpending_consumer_count`]: ../trait.Commands.html#method.xpending_consumer_count
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamInfoStreamReply:
    """Reply type used with [`xinfo_stream`] command, containing
general information about the stream stored at the specified key.

The very first and last IDs in the stream are shown,
in order to give some sense about what is the stream content.

**Note:** For Redis 8.6+ idempotency tracking fields, use [`StreamInfoStreamReplyWithIdempotency`]
via the [`xinfo_stream_with_idempotency`] command instead.

[`xinfo_stream`]: ../trait.Commands.html#method.xinfo_stream
[`xinfo_stream_with_idempotency`]: ../trait.Commands.html#method.xinfo_stream_with_idempotency
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamInfoStreamReplyWithIdempotency:
    """Reply type used with [`xinfo_stream_with_idempotency`] command (Redis 8.6+).

This type composes [`StreamInfoStreamReply`] with additional idempotency tracking fields
introduced in Redis 8.6.

The base stream information is accessible via the `base` field, while idempotency
fields are directly available as top-level fields.

[`xinfo_stream_with_idempotency`]: ../trait.Commands.html#method.xinfo_stream_with_idempotency

# Example
```no_run
use redis::{Commands, streams::StreamInfoStreamReplyWithIdempotency};
# let client = redis::Client::open("redis://127.0.0.1/").unwrap();
# let mut con = client.get_connection().unwrap();

let info: StreamInfoStreamReplyWithIdempotency = con.xinfo_stream_with_idempotency("stream").unwrap();

// Access base stream info
println!("Stream length: {}", info.base.length);
println!("Last ID: {}", info.base.last_generated_id);

// Access idempotency tracking (Redis 8.6+)
println!("Producers tracked: {}", info.pids_tracked);
println!("Idempotent IDs tracked: {}", info.iids_tracked);
println!("Duplicates prevented: {}", info.iids_duplicates);
```"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamInfoConsumersReply:
    """Reply type used with [`xinfo_consumer`] command, an array of every
consumer in a specific consumer group.

[`xinfo_consumer`]: ../trait.Commands.html#method.xinfo_consumer
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamInfoGroupsReply:
    """Reply type used with [`xinfo_groups`] command.

This output represents all the consumer groups associated with
the stream.

[`xinfo_groups`]: ../trait.Commands.html#method.xinfo_groups
"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamInfoConsumer:
    """A consumer parsed from [`xinfo_consumers`] command.

[`xinfo_consumers`]: ../trait.Commands.html#method.xinfo_consumers
"""
    pass

class StreamInfoGroup:
    """A group parsed from [`xinfo_groups`] command.

[`xinfo_groups`]: ../trait.Commands.html#method.xinfo_groups
"""
    pass

class StreamPendingId:
    """Represents a pending message parsed from [`xpending`] methods.

[`xpending`]: ../trait.Commands.html#method.xpending"""
    pass

class StreamKey:
    """Represents a stream `key` and its `id`'s parsed from `xread` methods."""
    pass

class StreamId:
    """Represents a stream `id` and its field/values as a `HashMap`
Also contains optional PEL information if the message was fetched with XREADGROUP with a `claim` option"""

    def get(self, key: str) -> T | None: ...

    def contains_key(self, key: str) -> bool: ...

    def len(self) -> int: ...

    def is_empty(self) -> bool: ...

class ScanOptions:
    """Options for the [SCAN](https://redis.io/commands/scan) command

# Example

```rust
use redis::{Commands, RedisResult, ScanOptions, Iter};
fn force_fetching_every_matching_key<'a, T: redis::FromRedisValue>(
con: &'a mut redis::Connection,
pattern: &'a str,
count: usize,
) -> RedisResult<Iter<'a, T>> {
let opts = ScanOptions::default()
.with_pattern(pattern)
.with_count(count);
con.scan_options(opts)
}
```"""

    def with_count(self, n: int) -> Self: ...

    def with_pattern(self, p: object) -> Self: ...

    def with_type(self, t: object) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

    def num_of_args(self) -> int: ...

class LposOptions:
    """Options for the [LPOS](https://redis.io/commands/lpos) command

# Example

```rust,no_run
use redis::{Commands, RedisResult, LposOptions};
fn fetch_list_position(
con: &mut redis::Connection,
key: &str,
value: &str,
count: usize,
rank: isize,
maxlen: usize,
) -> RedisResult<Vec<usize>> {
let opts = LposOptions::default()
.count(count)
.rank(rank)
.maxlen(maxlen);
con.lpos(key, value, opts)
}
```"""

    def count(self, n: int) -> Self: ...

    def rank(self, n: int) -> Self: ...

    def maxlen(self, n: int) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

    def num_of_args(self) -> int: ...

class CopyOptions:
    """Options for the [COPY](https://redis.io/commands/copy) command

# Example
```rust,no_run
use redis::{Commands, RedisResult, CopyOptions, SetExpiry, ExistenceCheck};
fn copy_value(
con: &mut redis::Connection,
old: &str,
new: &str,
) -> RedisResult<Vec<usize>> {
let opts = CopyOptions::default()
.db("my_other_db")
.replace(true);
con.copy(old, new, opts)
}
```"""

    @staticmethod
    def default() -> "CopyOptions": ...

    def db(self, db: Db2) -> object: ...

    def replace(self, replace: bool) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class SetOptions:
    """Options for the [SET](https://redis.io/commands/set) command

# Example
```rust,no_run
use redis::{Commands, RedisResult, SetOptions, SetExpiry, ExistenceCheck, ValueComparison};
fn set_key_value(
con: &mut redis::Connection,
key: &str,
value: &str,
) -> RedisResult<Vec<usize>> {
let opts = SetOptions::default()
.conditional_set(ExistenceCheck::NX)
.value_comparison(ValueComparison::ifeq("old_value"))
.get(true)
.with_expiration(SetExpiry::EX(60));
con.set_options(key, value, opts)
}
```"""

    def conditional_set(self, existence_check: ExistenceCheck) -> Self: ...

    def value_comparison(self, value_comparison: ValueComparison) -> Self: ...

    def get(self, get: bool) -> Self: ...

    def with_expiration(self, expiration: SetExpiry) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class MSetOptions:
    """Options for the [MSETEX](https://redis.io/commands/msetex) command

# Example
```rust,no_run
use redis::{Commands, RedisResult, MSetOptions, SetExpiry, ExistenceCheck};
fn set_multiple_key_values(
con: &mut redis::Connection,
) -> RedisResult<bool> {
let opts = MSetOptions::default()
.conditional_set(ExistenceCheck::NX)
.with_expiration(SetExpiry::EX(60));
con.mset_ex(&[("key1", "value1"), ("key2", "value2")], opts)
}
```"""

    def conditional_set(self, existence_check: ExistenceCheck) -> Self: ...

    def with_expiration(self, expiration: SetExpiry) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class FlushAllOptions:
    """Options for the [FLUSHALL](https://redis.io/commands/flushall) command

# Example
```rust,no_run
use redis::{Commands, RedisResult, FlushAllOptions};
fn flushall_sync(
con: &mut redis::Connection,
) -> RedisResult<()> {
let opts = FlushAllOptions{blocking: true};
con.flushall_options(&opts)
}
```"""

    def blocking(self, blocking: bool) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class HashFieldExpirationOptions:
    """Options for the HSETEX command"""

    def set_existence_check(self, field_existence_check: FieldExistenceCheck) -> Self: ...

    def set_expiration(self, expiration: SetExpiry) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class SortedSetAddOptions:
    """Options for the [ZADD](https://redis.io/commands/zadd) command"""

    @staticmethod
    def add_only() -> "SortedSetAddOptions": ...

    @staticmethod
    def update_only(conditional_update: UpdateCheck | None) -> "SortedSetAddOptions": ...

    @staticmethod
    def add_or_update(conditional_update: UpdateCheck | None) -> "SortedSetAddOptions": ...

    def include_changed_count(self) -> Self: ...

    def increment_score(self) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class AclInfo:
    """An info dictionary type storing Redis ACL information as multiple `Rule`.
This type collects key/value data returned by the [`ACL GETUSER`][1] command.

[1]: https://redis.io/commands/acl-getuser"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class Coord:
    """A coordinate (longitude, latitude).

Can be used with [`geo_pos`][1] to parse response from Redis.

[1]: ../trait.Commands.html#method.geo_pos

`T` is the type of the every value.

* You may want to use either `f64` or `f32` if you want to perform mathematical operations.
* To keep the raw value from Redis, use `String`."""

    @staticmethod
    def lon_lat(longitude: T, latitude: T) -> object: ...

    @staticmethod
    def from_redis_value_ref(v: Value) -> object: ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

    def write_redis_args(self, out: W) -> None: ...

    def num_of_args(self) -> int: ...

class RadiusOptions:
    """Options for the [GEORADIUS][1] and [GEORADIUSBYMEMBER][2] commands

[1]: https://redis.io/commands/georadius
[2]: https://redis.io/commands/georadiusbymember

# Example

```rust,no_run
use redis::{Commands, RedisResult};
use redis::geo::{RadiusSearchResult, RadiusOptions, RadiusOrder, Unit};
fn nearest_in_radius(
con: &mut redis::Connection,
key: &str,
longitude: f64,
latitude: f64,
meters: f64,
limit: usize,
) -> RedisResult<Vec<RadiusSearchResult>> {
let opts = RadiusOptions::default()
.order(RadiusOrder::Asc)
.limit(limit);
con.geo_radius(key, longitude, latitude, meters, Unit::Meters, opts)
}
```"""

    def limit(self, n: int) -> Self: ...

    def with_dist(self) -> Self: ...

    def with_coord(self) -> Self: ...

    def order(self, o: RadiusOrder) -> Self: ...

    def store(self, key: K) -> Self: ...

    def store_dist(self, key: K) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

    def num_of_args(self) -> int: ...

class RadiusSearchResult:
    """Contain an item returned by [`geo_radius`][1] and [`geo_radius_by_member`][2].

[1]: ../trait.Commands.html#method.geo_radius
[2]: ../trait.Commands.html#method.geo_radius_by_member"""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class VSimOptions:
    """Options for the VSIM command

# Example
```rust,no_run
use redis::{Commands, RedisResult, vector_sets::*};
fn search_similar_vectors(
con: &mut redis::Connection,
key: &str,
element: &str,
) -> RedisResult<redis::Value> {
let opts = VSimOptions::default()
.set_with_scores(true)
.set_count(10)
.set_search_exploration_factor(100)
.set_filter_expression(".size == \\"large\\"")
.set_max_filtering_effort(10)
.set_truth(true)
.set_no_thread(true);
con.vsim_options(key, VectorSimilaritySearchInput::Element(element), &opts)
}
```"""

    def set_with_scores(self, enabled: bool) -> Self: ...

    def set_count(self, count: int) -> Self: ...

    def set_search_exploration_factor(self, factor: int) -> Self: ...

    def set_filter_expression(self, expression: S) -> Self: ...

    def set_max_filtering_effort(self, effort: int) -> Self: ...

    def set_truth(self, enabled: bool) -> Self: ...

    def set_no_thread(self, enabled: bool) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class VAddOptions:
    """Options for the VADD command

# Example
```rust,no_run
use redis::{Commands, RedisResult, vector_sets::*};
fn add_vector(
con: &mut redis::Connection,
key: &str,
vector: &[f64],
element: &str,
) -> RedisResult<bool> {
let opts = VAddOptions::default()
.set_reduction_dimension(5)
.set_check_and_set_style(true)
.set_quantization(VectorQuantization::Q8)
.set_build_exploration_factor(300)
.set_attributes(serde_json::json!({"name": "Vector attribute name", "description": "Vector attribute description"}))
.set_max_number_of_links(16);
con.vadd_options(key, VectorAddInput::Values(EmbeddingInput::Float64(vector)), element, &opts)
}
```"""

    def set_reduction_dimension(self, dimension: int) -> Self: ...

    def set_check_and_set_style(self, cas_enabled: bool) -> Self: ...

    def set_quantization(self, vector_quantization: VectorQuantization) -> Self: ...

    def set_build_exploration_factor(self, build_exploration_factor: int) -> Self: ...

    def set_attributes(self, attributes: Value) -> Self: ...

    def set_max_number_of_links(self, max_number_of_links: int) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class VEmbOptions:
    """Options for the VEMB command

# Example
```rust,no_run
use redis::{Commands, RedisResult, vector_sets::VEmbOptions};
fn get_vector_embedding(
con: &mut redis::Connection,
key: &str,
element: &str,
) -> RedisResult<redis::Value> {
let opts = VEmbOptions::default().set_raw_representation(true);
con.vemb_options(key, element, &opts)
}
```"""

    def set_raw_representation(self, enabled: bool) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class HotkeysOptions:
    """Options for the HOTKEYS START command.

At least one of `cpu` or `net` must be enabled to specify which metrics to collect.
The `METRICS count` is automatically derived from how many metric types are enabled.

Use [`HotkeysOptions::new_with_cpu()`] or [`HotkeysOptions::new_with_net()`] constructors to create
valid options with at least one metric enabled.

# Example

```rust,no_run
use redis::{HotkeysOptions, HotkeysCommands};

# fn example() -> redis::RedisResult<()> {
let client = redis::Client::open("redis://127.0.0.1/")?;
let mut con = client.get_connection()?;

// Track hotkeys by both CPU and network usage for 60 seconds
let opts = HotkeysOptions::new_with_cpu()
.and_net()
.with_duration_secs(60);

con.hotkeys_start(opts)?;
# Ok(())
# }
```"""

    @staticmethod
    def new_with_cpu() -> "HotkeysOptions": ...

    @staticmethod
    def new_with_net() -> "HotkeysOptions": ...

    def and_cpu(self) -> Self: ...

    def and_net(self) -> Self: ...

    def with_count(self, k: int) -> object: ...

    def with_duration_secs(self, seconds: int) -> Self: ...

    def with_sample_ratio(self, ratio: int) -> Self: ...

    def with_slots(self, slots: list[int]) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

    def num_of_args(self) -> int: ...

class HotKeyEntry:
    """A single hotkey entry with its metric value."""
    pass

class SlotRange:
    """Represents a range of slots."""

    @staticmethod
    def new(s: int, e: int, m: NodeAddress, r: list[NodeAddress]) -> "SlotRange": ...

class HotkeysResponse:
    """Response from the HOTKEYS GET command.

Contains information about the hotkeys tracking session,
including tracking metadata, performance statistics, and lists of top K
hot keys sorted by the metrics specified in HOTKEYS START."""

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class ServerErrorKind:
    """Kinds of errors returned from the server"""
    ResponseError: "ServerErrorKind"
    ExecAbort: "ServerErrorKind"
    BusyLoading: "ServerErrorKind"
    NoScript: "ServerErrorKind"
    Moved: "ServerErrorKind"
    Ask: "ServerErrorKind"
    TryAgain: "ServerErrorKind"
    ClusterDown: "ServerErrorKind"
    CrossSlot: "ServerErrorKind"
    MasterDown: "ServerErrorKind"
    ReadOnly: "ServerErrorKind"
    NotBusy: "ServerErrorKind"
    NoSub: "ServerErrorKind"
    NoPerm: "ServerErrorKind"

class ErrorKind:
    """An enum of all error kinds."""
    Parse: "ErrorKind"
    AuthenticationFailed: "ErrorKind"
    UnexpectedReturnType: "ErrorKind"
    InvalidClientConfig: "ErrorKind"
    Io: "ErrorKind"
    Client: "ErrorKind"
    Extension: "ErrorKind"
    MasterNameNotFoundBySentinel: "ErrorKind"
    NoValidReplicasFoundBySentinel: "ErrorKind"
    EmptySentinelList: "ErrorKind"
    ClusterConnectionNotFound: "ErrorKind"
    Server: "ErrorKind"
    Serialize: "ErrorKind"
    RESP3NotSupported: "ErrorKind"

    @staticmethod
    def from_(kind: ServerErrorKind) -> "ErrorKind": ...

class RetryMethod:
    """What method should be used if retrying this request."""
    Reconnect: "RetryMethod"
    NoRetry: "RetryMethod"
    RetryImmediately: "RetryMethod"
    WaitAndRetry: "RetryMethod"
    AskRedirect: "RetryMethod"
    MovedRedirect: "RetryMethod"
    ReconnectFromInitialConnections: "RetryMethod"
    RefreshSlotsAndRetry: "RetryMethod"

class SentinelServerType:
    """Enum defining the server types from a sentinel's point of view."""
    Master: "SentinelServerType"
    Replica: "SentinelServerType"

class Expiry:
    """Helper enum that is used to define expiry time"""
    EX: "Expiry"
    PX: "Expiry"
    EXAT: "Expiry"
    PXAT: "Expiry"
    PERSIST: "Expiry"

    def write_redis_args(self, out: W) -> None: ...

class SetExpiry:
    """Helper enum that is used to define expiry time for SET command"""
    EX: "SetExpiry"
    PX: "SetExpiry"
    EXAT: "SetExpiry"
    PXAT: "SetExpiry"
    KEEPTTL: "SetExpiry"

    def write_redis_args(self, out: W) -> None: ...

class ExistenceCheck:
    """Helper enum that is used to define existence checks"""
    NX: "ExistenceCheck"
    XX: "ExistenceCheck"

    def write_redis_args(self, out: W) -> None: ...

class FieldExistenceCheck:
    """Helper enum that is used to define field existence checks"""
    FNX: "FieldExistenceCheck"
    FXX: "FieldExistenceCheck"

    def write_redis_args(self, out: W) -> None: ...

class NumericBehavior:
    """Helper enum that is used in some situations to describe
the behavior of arguments in a numeric context."""
    NonNumeric: "NumericBehavior"
    NumberIsInteger: "NumericBehavior"
    NumberIsFloat: "NumericBehavior"

class Value:
    """Internal low-level redis value enum."""
    Nil: "Value"
    Int: "Value"
    BulkString: "Value"
    Array: "Value"
    SimpleString: "Value"
    Okay: "Value"
    Map: "Value"
    Attribute: "Value"
    Set: "Value"
    Double: "Value"
    Boolean: "Value"
    VerbatimString: "Value"
    BigNumber: "Value"
    BigNumber: "Value"
    Push: "Value"
    ServerError: "Value"

    def looks_like_cursor(self) -> bool: ...

    def as_sequence(self) -> object: ...

    def into_sequence(self) -> list[Value]: ...

    def as_map_iter(self) -> MapIter | None: ...

    def into_map_iter(self) -> OwnedMapIter: ...

    def extract_error(self) -> object: ...

    def fmt(self, fmt: Formatter) -> Result: ...

    @staticmethod
    def from_redis_value_ref(v: Value) -> "Value": ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

    @staticmethod
    def from_(value: Output) -> "Value": ...

    def arg_idx(self, idx: int) -> object: ...

    def position(self, candidate: object) -> int | None: ...

class ValueComparison:
    """Helper enum that is used to define comparisons between values and their digests

# Example
```rust
use redis::ValueComparison;

// Create comparisons using constructor methods
let eq_comparison = ValueComparison::ifeq("my_value");
let ne_comparison = ValueComparison::ifne("other_value");
let deq_comparison = ValueComparison::ifdeq("digest_hash");
let dne_comparison = ValueComparison::ifdne("other_digest");
```"""
    IFEQ: "ValueComparison"
    IFNE: "ValueComparison"
    IFDEQ: "ValueComparison"
    IFDNE: "ValueComparison"

    @staticmethod
    def ifeq(value: object) -> "ValueComparison": ...

    @staticmethod
    def ifne(value: object) -> "ValueComparison": ...

    @staticmethod
    def ifdeq(digest: object) -> "ValueComparison": ...

    @staticmethod
    def ifdne(digest: object) -> "ValueComparison": ...

    def write_redis_args(self, out: W) -> None: ...

class VerbatimFormat:
    """`VerbatimString`'s format types defined by spec"""
    Unknown: "VerbatimFormat"
    Markdown: "VerbatimFormat"
    Text: "VerbatimFormat"

    def fmt(self, f: Formatter) -> Result: ...

class PushKind:
    """`Push` type's currently known kinds."""
    Disconnection: "PushKind"
    Other: "PushKind"
    Invalidate: "PushKind"
    Message: "PushKind"
    PMessage: "PushKind"
    SMessage: "PushKind"
    Unsubscribe: "PushKind"
    PUnsubscribe: "PushKind"
    SUnsubscribe: "PushKind"
    Subscribe: "PushKind"
    PSubscribe: "PushKind"
    SSubscribe: "PushKind"

    def fmt(self, f: Formatter) -> Result: ...

class MapIter:
    Array: "MapIter"
    Map: "MapIter"

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

class OwnedMapIter:
    Array: "OwnedMapIter"
    Map: "OwnedMapIter"

    def next(self) -> Item | None: ...

    def size_hint(self) -> object: ...

class Role:
    """High level representation of response to the [`ROLE`][1] command.

[1]: https://redis.io/docs/latest/commands/role/"""
    Primary: "Role"
    Replica: "Role"
    Sentinel: "Role"

    @staticmethod
    def from_redis_value_ref(v: Value) -> object: ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class ProtocolVersion:
    """Enum representing the communication protocol with the server.

This enum represents the types of data that the server can send to the client,
and the capabilities that the client can use."""
    RESP2: "ProtocolVersion"
    RESP3: "ProtocolVersion"

    def supports_resp3(self) -> bool: ...

class ExpireOption:
    """Helper enum that is used to define option for the hash expire commands"""
    NONE: "ExpireOption"
    NX: "ExpireOption"
    XX: "ExpireOption"
    GT: "ExpireOption"
    LT: "ExpireOption"

    def write_redis_args(self, out: W) -> None: ...

class ValueType:
    """Possible types of value held in Redis: [Redis Docs](https://redis.io/docs/latest/commands/type/)"""
    None_: "ValueType"
    String: "ValueType"
    List: "ValueType"
    Set: "ValueType"
    ZSet: "ValueType"
    Hash: "ValueType"
    Stream: "ValueType"
    VectorSet: "ValueType"
    JSON: "ValueType"
    BloomFilterRedis: "ValueType"
    CuckooFilter: "ValueType"
    CountMin: "ValueType"
    TDigest: "ValueType"
    TopK: "ValueType"
    TimeSeries: "ValueType"
    Trie: "ValueType"
    BloomFilterValKey: "ValueType"
    Unknown: "ValueType"

    @staticmethod
    def from_(s: T) -> "ValueType": ...

    @staticmethod
    def from_redis_value_ref(v: Value) -> object: ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class IntegerReplyOrNoOp:
    """Returned by typed commands which either return a positive integer or some negative integer indicating some kind of no-op."""
    IntegerReply: "IntegerReplyOrNoOp"
    NotExists: "IntegerReplyOrNoOp"
    ExistsButNotRelevant: "IntegerReplyOrNoOp"

    def raw(self) -> int: ...

    @staticmethod
    def from_redis_value_ref(v: Value) -> object: ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

    def eq(self, other: int) -> bool: ...

    def eq(self, other: int) -> bool: ...

    def eq(self, other: int) -> bool: ...

    def eq(self, other: int) -> bool: ...

class LogicalAggregateOp:
    """Logical bitwise aggregating operators."""
    And: "LogicalAggregateOp"

class AggregateOp:
    """Numerical aggregating operators."""
    Min: "AggregateOp"
    Sum: "AggregateOp"

class ResponsePolicy:
    """Policy defining how to combine multiple responses into one."""
    OneSucceeded: "ResponsePolicy"
    FirstSucceededNonEmptyOrAllEmpty: "ResponsePolicy"
    AllSucceeded: "ResponsePolicy"
    AggregateLogical: "ResponsePolicy"
    Aggregate: "ResponsePolicy"
    CombineArrays: "ResponsePolicy"
    Special: "ResponsePolicy"
    CombineMaps: "ResponsePolicy"

class RoutingInfo:
    """Defines whether a request should be routed to a single node, or multiple ones."""
    SingleNode: "RoutingInfo"
    MultiNode: "RoutingInfo"

class SingleNodeRoutingInfo:
    """Defines which single node should receive a request."""
    Random: "SingleNodeRoutingInfo"
    RandomPrimary: "SingleNodeRoutingInfo"
    SpecificNode: "SingleNodeRoutingInfo"
    ByAddress: "SingleNodeRoutingInfo"

    @staticmethod
    def from_(value: Route | None) -> "SingleNodeRoutingInfo": ...

class MultipleNodeRoutingInfo:
    """Defines which collection of nodes should receive a request"""
    AllNodes: "MultipleNodeRoutingInfo"
    AllMasters: "MultipleNodeRoutingInfo"
    MultiSlot: "MultipleNodeRoutingInfo"

class MultiSlotArgPattern:
    """Represents the pattern of argument structures in multi-slot commands,
defining how the arguments are organized in the command."""
    KeysOnly: "MultiSlotArgPattern"
    KeyValuePairs: "MultiSlotArgPattern"
    KeysAndLastArg: "MultiSlotArgPattern"
    KeyWithTwoArgTriples: "MultiSlotArgPattern"

class SlotAddr:
    """What type of node should a request be routed to, assuming read from replica is enabled."""
    Master: "SlotAddr"
    ReplicaOptional: "SlotAddr"
    ReplicaRequired: "SlotAddr"

class ReadCandidates:
    """The candidate nodes passed to [`ReadRoutingStrategy::route_read`].

The strategy is only called when there are replicas available for the
target slot. If a slot has no replicas, the caller falls back to the
primary without consulting the strategy."""
    AnyNode: "ReadCandidates"
    ReplicasOnly: "ReadCandidates"

    def slot(self) -> int: ...

class Arg:
    """An argument to a redis command"""
    Simple: "Arg"
    Cursor: "Arg"

class BloomFilterInfoType:
    """Specific type of information to query for Bloom filters"""
    Capacity: "BloomFilterInfoType"
    Size: "BloomFilterInfoType"
    Filters: "BloomFilterInfoType"
    Items: "BloomFilterInfoType"
    Expansion: "BloomFilterInfoType"

    def write_redis_args(self, out: W) -> None: ...

class BloomFilterScalingOptions:
    """Strategies for how a Bloom filter can scale to hold more items"""
    ExpansionRate: "BloomFilterScalingOptions"
    NonScaling: "BloomFilterScalingOptions"

    def write_redis_args(self, out: W) -> None: ...

class TlsMode:
    """TlsMode indicates use or do not use verification of certification.

Check [ConnectionAddr](ConnectionAddr::TcpTls::insecure) for more."""
    Secure: "TlsMode"
    Insecure: "TlsMode"

class ConnectionAddr:
    """Defines the connection address.

Not all connection addresses are supported on all platforms.  For instance
to connect to a unix socket you need to run this on an operating system
that supports them."""
    Tcp: "ConnectionAddr"
    TcpTls: "ConnectionAddr"
    Unix: "ConnectionAddr"

    def eq(self, other: Self) -> bool: ...

    def is_supported(self) -> bool: ...

    def set_danger_accept_invalid_hostnames(self, insecure: bool) -> None: ...

    def fmt(self, f: Formatter) -> Result: ...

    def into_connection_info(self) -> object: ...

class CacheMode:
    """Defines the behavior of the cache regarding which commands should be cached."""
    All: "CacheMode"
    OptIn: "CacheMode"

class StreamMaxlen:
    """Utility enum for passing `MAXLEN [= or ~] [COUNT]`
arguments into `StreamCommands`.
The enum value represents the count."""
    Equals: "StreamMaxlen"
    Approx: "StreamMaxlen"

    def write_redis_args(self, out: W) -> None: ...

class StreamTrimmingMode:
    """Utility enum for passing the trim mode`[=|~]`
arguments into `StreamCommands`."""
    Exact: "StreamTrimmingMode"
    Approx: "StreamTrimmingMode"

    def write_redis_args(self, out: W) -> None: ...

class StreamTrimStrategy:
    """Utility enum for passing `<MAXLEN|MINID> [=|~] threshold [LIMIT count]`
arguments into `StreamCommands`.
The enum values the trimming mode (=|~), the threshold, and the optional limit"""
    MaxLen: "StreamTrimStrategy"
    MinId: "StreamTrimStrategy"

    @staticmethod
    def maxlen(trim: StreamTrimmingMode, max_entries: int) -> "StreamTrimStrategy": ...

    @staticmethod
    def minid(trim: StreamTrimmingMode, stream_id: object) -> "StreamTrimStrategy": ...

    def limit(self, limit: int) -> Self: ...

    def write_redis_args(self, out: W) -> None: ...

class StreamIdempotencyMode:
    """Idempotency mode for stream message production

Supports idempotent message processing to prevent duplicate entries.
See [Redis Streams Idempotency](https://redis.io/docs/latest/develop/data-types/streams/idempotency/)"""
    Manual: "StreamIdempotencyMode"
    Automatic: "StreamIdempotencyMode"

    def write_redis_args(self, out: W) -> None: ...

class StreamPendingReply:
    """Reply type used with [`xpending`] command.

Data returned here were fetched from the stream without
having been acknowledged.

[`xpending`]: ../trait.Commands.html#method.xpending
"""
    Empty: "StreamPendingReply"
    Data: "StreamPendingReply"

    def count(self) -> int: ...

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class StreamDeletionPolicy:
    """Deletion policy for stream entries."""
    KeepRef: "StreamDeletionPolicy"
    DelRef: "StreamDeletionPolicy"
    Acked: "StreamDeletionPolicy"

    def write_redis_args(self, out: W) -> None: ...

class XDelExStatusCode:
    """Status codes returned by the `XDELEX` command"""
    IdNotFound: "XDelExStatusCode"
    Deleted: "XDelExStatusCode"
    NotDeletedUnacknowledgedOrStillReferenced: "XDelExStatusCode"

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class XAckDelStatusCode:
    """Status codes returned by the `XACKDEL` command"""
    IdNotFound: "XAckDelStatusCode"
    AcknowledgedAndDeleted: "XAckDelStatusCode"
    AcknowledgedNotDeletedStillReferenced: "XAckDelStatusCode"

    @staticmethod
    def from_redis_value(v: Value) -> object: ...

class ControlFlow:
    """Allows pubsub callbacks to stop receiving messages.

Arbitrary data may be returned from `Break`."""
    Continue: "ControlFlow"
    Break: "ControlFlow"

class Direction:
    """Enum for the LEFT | RIGHT args used by some commands"""
    Left: "Direction"
    Right: "Direction"

    def write_redis_args(self, out: W) -> None: ...

class UpdateCheck:
    """Helper enum that is used to define update checks"""
    LT: "UpdateCheck"
    GT: "UpdateCheck"

    def write_redis_args(self, out: W) -> None: ...

class Rule:
    """ACL rules are used in order to activate or remove a flag, or to perform a
given change to the user ACL, which under the hood are just single words."""
    On: "Rule"
    Off: "Rule"
    AddCommand: "Rule"
    RemoveCommand: "Rule"
    AddCategory: "Rule"
    RemoveCategory: "Rule"
    AllCommands: "Rule"
    NoCommands: "Rule"
    AddPass: "Rule"
    RemovePass: "Rule"
    AddHashedPass: "Rule"
    RemoveHashedPass: "Rule"
    NoPass: "Rule"
    ResetPass: "Rule"
    Pattern: "Rule"
    AllKeys: "Rule"
    ResetKeys: "Rule"
    Channel: "Rule"
    ResetChannels: "Rule"
    Selector: "Rule"
    Reset: "Rule"
    Other: "Rule"

    def write_redis_args(self, out: W) -> None: ...

class Unit:
    """Units used by [`geo_dist`][1] and [`geo_radius`][2].

[1]: ../trait.Commands.html#method.geo_dist
[2]: ../trait.Commands.html#method.geo_radius"""
    Meters: "Unit"
    Kilometers: "Unit"
    Miles: "Unit"
    Feet: "Unit"

    def write_redis_args(self, out: W) -> None: ...

class RadiusOrder:
    """Options to sort results from [GEORADIUS][1] and [GEORADIUSBYMEMBER][2] commands

[1]: https://redis.io/commands/georadius
[2]: https://redis.io/commands/georadiusbymember"""
    Unsorted: "RadiusOrder"
    Asc: "RadiusOrder"
    Desc: "RadiusOrder"

class EmbeddingInput:
    """Input data formats that can be used to generate vector embeddings:

- 32-bit floats
- 64-bit floats
- Strings (e.g., numbers as strings)"""
    Float32: "EmbeddingInput"
    Float64: "EmbeddingInput"
    String: "EmbeddingInput"

    def write_redis_args(self, out: W) -> None: ...

class VectorAddInput:
    """Represents different ways to input data for vector add commands"""
    Fp32: "VectorAddInput"
    Values: "VectorAddInput"

    def write_redis_args(self, out: W) -> None: ...

class VectorQuantization:
    """Quantization options for vector storage"""
    NoQuant: "VectorQuantization"
    Q8: "VectorQuantization"
    Bin: "VectorQuantization"

class VectorSimilaritySearchInput:
    """Represents different ways to input query data for vector similarity search commands"""
    Fp32: "VectorSimilaritySearchInput"
    Values: "VectorSimilaritySearchInput"
    Element: "VectorSimilaritySearchInput"

    def write_redis_args(self, out: W) -> None: ...

"""Mark Smol as the preferred runtime.

If the function returns `Err`, another runtime preference was already set, and won't be changed.
Call this function if the application doesn't use multiple runtimes,
but the crate is compiled with multiple runtimes enabled, which is a bad pattern that should be avoided."""
def prefer_smol() -> None: ...

"""Mark Tokio as the preferred runtime.

If the function returns `Err`, another runtime preference was already set, and won't be changed.
Call this function if the application doesn't use multiple runtimes,
but the crate is compiled with multiple runtimes enabled, which is a bad pattern that should be avoided."""
def prefer_tokio() -> None: ...

"""Executes a Redis transaction asynchronously by automatically watching keys and running
a transaction loop until it succeeds. Similar to the synchronous [`transaction`](crate::transaction)
function but for async execution.

The provided closure may be executed multiple times if the transaction fails due to
watched keys being modified between WATCH and EXEC. Any side effects in the closure
should account for possible multiple executions. The closure should return `Ok(None)` to indicate a transaction failure and to
retry (this will happen automatically if the last call in the closure is to run the transaction), or `Err(err)` to abort the
transaction with an error. A successful transaction should return `Ok(Some(value))` with the desired result from the EXEC command.

# Examples

```rust,no_run
use redis::{AsyncCommands, RedisResult, pipe};

async fn increment(con: redis::aio::MultiplexedConnection) -> RedisResult<isize> {
let key = "my_counter";
redis::aio::transaction_async(con, &[key], |mut con, mut pipe| async move {
// Read the current value first
let val: isize = con.get(key).await?;
// Build the pipeline and execute it atomically (MULTI/EXEC are added automatically)
pipe.set(key, val + 1)
.ignore()
.get(key)
.query_async(&mut con)
.await
})
.await
}
```

# Notes

- The closure may be executed multiple times if watched keys are modified by other
clients between `WATCH` and `EXEC`; its side effects must be idempotent.
- A successful `EXEC` automatically discards all `WATCH`es, so no explicit `UNWATCH`
is needed on the success path.
- The transaction is automatically abandoned if the closure returns an error; an
explicit `UNWATCH` is sent in that case to leave the connection in a clean state.

## Warning: Concurrent Transactions on Multiplexed Connections

When using a multiplexed connection (e.g. async connection types in this crate),
cloning shares the underlying channel. Running concurrent transactions on clones of
the same multiplexed connection could lead to unexpected behavior: the
`WATCH`/`MULTI`/`EXEC` sequence from one transaction may interleave with commands from
another. Ensure at most one transaction is active on a given multiplexed
connection at a time.

## Warning: Transactions on cluster connections

A cluster connection is a collection of multiple underlying connections to different
cluster nodes. Running a transaction on a cluster connection is only safe if all the
keys being watched and modified in the transaction are guaranteed to be on the same
cluster node, since Redis transactions cannot span multiple nodes. It is the caller's
responsibility to ensure this condition is met when using `transaction_async` with a
cluster connection.

For more details on Redis transactions, see the [Redis documentation](https://redis.io/topics/transactions)"""
async def transaction_async(connection: C, keys: object, func: F) -> T: ...

def get_push_kind(kind: str) -> PushKind: ...

"""Parses a redis value asynchronously."""
async def parse_redis_value_async(decoder: object, read: R) -> object: ...

"""Parses bytes into a redis value.

This is the most straightforward way to parse something into a low
level redis value instead of having to use a whole parser."""
def parse_redis_value(bytes: object) -> object: ...

"""Creates a new Redis error with the `Extension` kind.

This function is used to create Redis errors for extension error codes
that are not directly understood by the library.

# Arguments

* `code` - The error code string returned by the Redis server
* `detail` - Optional detailed error message. If None, a default message is used.

# Returns

A `RedisError` with the `Extension` kind."""
def make_extension_error(code: str, detail: str | None) -> RedisError: ...

"""A shortcut function to invoke `FromRedisValue::from_redis_value_ref`
to make the API slightly nicer."""
def from_redis_value_ref(v: Value) -> T: ...

"""A shortcut function to invoke `FromRedisValue::from_redis_value`
to make the API slightly nicer."""
def from_redis_value(v: Value) -> T: ...

"""Calculates a digest/hash of the given value for use with Redis value comparison operations.
This function uses the XXH3 algorithm, which is the same algorithm used by Redis for its DIGEST command.
The resulting digest can be used with `ValueComparison::IFDEQ` and `ValueComparison::IFDNE`.

# Example
```rust
use redis::{calculate_value_digest, ValueComparison, SetOptions};

let value = "my_value";
let digest = calculate_value_digest(value);

// Use the digest in a value comparison
let opts = SetOptions::default()
.value_comparison(ValueComparison::ifdeq(&digest));
```"""
def calculate_value_digest(value: T) -> str: ...

"""Validates that the given string is a valid 16-byte hex digest."""
def is_valid_16_bytes_hex_digest(s: str) -> bool: ...

"""Shortcut for creating a new cluster pipeline."""
def cluster_pipe() -> ClusterPipeline: ...

"""Shortcut function to creating a command with a single argument.

The first argument of a redis command is always the name of the command
which needs to be a string.  This is the recommended way to start a
command pipe.

```rust
redis::cmd("PING");
```"""
def cmd(name: str) -> Cmd: ...

"""Packs a bunch of commands into a request.

This is generally a quite useless function as this functionality is
nicely wrapped through the `Cmd` object, but in some cases it can be
useful.  The return value of this can then be send to the low level
`ConnectionLike` methods.

Example:

```rust
# use redis::ToRedisArgs;
let mut args = vec![];
args.extend("SET".to_redis_args());
args.extend("my_key".to_redis_args());
args.extend(42.to_redis_args());
let cmd = redis::pack_command(&args);
assert_eq!(cmd, b"*3\\r\\n$3\\r\\nSET\\r\\n$6\\r\\nmy_key\\r\\n$2\\r\\n42\\r\\n".to_vec());
```"""
def pack_command(args: object) -> list[int]: ...

"""Shortcut for creating a new pipeline."""
def pipe() -> Pipeline: ...

"""This function takes a redis URL string and parses it into a URL
as used by rust-url.

This is necessary as the default parser does not understand how redis URLs function."""
def parse_redis_url(input: str) -> Url | None: ...

def connect(connection_info: ConnectionInfo, timeout: Duration | None) -> object: ...

"""This function simplifies transaction management slightly.  What it
does is automatically watching keys and then going into a transaction
loop util it succeeds.  Once it goes through the results are
returned.

To use the transaction two pieces of information are needed: a list
of all the keys that need to be watched for modifications and a
closure with the code that should be execute in the context of the
transaction.  The closure is invoked with a fresh pipeline in atomic
mode.  To use the transaction the function needs to return the result
from querying the pipeline with the connection.

The end result of the transaction is then available as the return
value from the function call.

Example:

```rust,no_run
use redis::Commands;
# fn do_something() -> redis::RedisResult<()> {
# let client = redis::Client::open("redis://127.0.0.1/").unwrap();
# let mut con = client.get_connection().unwrap();
let key = "the_key";
let (new_val,) : (isize,) = redis::transaction(&mut con, &[key], |con, pipe| {
let old_val : isize = con.get(key)?;
pipe
.set(key, old_val + 1).ignore()
.get(key).query(con)
})?;
println!("The incremented number is: {}", new_val);
# Ok(()) }
```"""
def transaction(con: C, keys: object, func: F) -> object: ...

"""Common logic for clearing subscriptions in RESP2 async/sync"""
def resp2_is_pub_sub_state_cleared(received_unsub: mutbool, received_punsub: mutbool, kind: object, num: int) -> bool: ...

"""Common logic for clearing subscriptions in RESP3 async/sync"""
def resp3_is_pub_sub_state_cleared(received_unsub: mutbool, received_punsub: mutbool, kind: PushKind, num: int) -> bool: ...

def no_sub_err_is_pub_sub_state_cleared(received_unsub: mutbool, received_punsub: mutbool, err: ServerError) -> bool: ...

"""Common logic for checking real cause of hello3 command error"""
def get_resp3_hello_command_error(err: RedisError) -> RedisError: ...

"""Assures that the given [`RedisConnectionInfo`] sets the given expected library name and version"""
def assert_lib_name_in_connection_setup_pipeline(redis_connection_info: RedisConnectionInfo, expected_lib_name: str, expected_lib_ver: str) -> None: ...

"""Creates HELLO command for RESP3 with RedisConnectionInfo
[Redis Docs](https://redis.io/commands/HELLO)"""
def resp3_hello(connection_info: RedisConnectionInfo) -> Cmd: ...

__all__: list[str] = ["prefer_smol", "prefer_tokio", "transaction_async", "get_push_kind", "parse_redis_value_async", "parse_redis_value", "make_extension_error", "from_redis_value_ref", "from_redis_value", "calculate_value_digest", "is_valid_16_bytes_hex_digest", "cluster_pipe", "cmd", "pack_command", "pipe", "parse_redis_url", "connect", "transaction", "resp2_is_pub_sub_state_cleared", "resp3_is_pub_sub_state_cleared", "no_sub_err_is_pub_sub_state_cleared", "get_resp3_hello_command_error", "assert_lib_name_in_connection_setup_pipeline", "resp3_hello", "SendError", "Monitor", "PubSubSink", "PubSub", "ConnectionManagerConfig", "ConnectionManager", "MultiplexedConnection", "ValueCodec", "Parser", "ServerError", "RedisError", "ParsingError", "ClientCertificate", "EntraIdCredentialsProvider", "Sentinel", "SentinelNodeConnectionInfo", "LockedSentinelClient", "AsyncLockedSentinelClient", "SentinelClient", "SentinelClientBuilder", "InfoDict", "ReplicaInfo", "PushInfo", "Client", "AsyncConnectionConfig", "NodeAddress", "ClusterConfig", "ClusterConnection", "ClusterPipeline", "ClusterClientBuilder", "ClusterClient", "ClusterConnection", "Route", "Slot", "RandomReplicaStrategy", "Shard", "ClusterTopology", "Replicas", "AnyNodeCandidates", "ReplicasOnlyCandidates", "RoundRobinReplicaStrategy", "CommandCacheConfig", "Cmd", "Iter", "AsyncIter", "TcpSettings", "TokenRefreshConfig", "RetryConfig", "Pipeline", "BloomFilterInfoTypeResponse", "BloomFilterInsertOptions", "BloomFilterDumpChunk", "BloomFilterDumpIterator", "TlsConnParams", "ConnectionInfo", "RedisConnectionInfo", "Connection", "PubSub", "Msg", "CacheConfig", "CacheStatistics", "Script", "ScriptInvocation", "BasicAuth", "ClientTlsConfig", "TlsCertificates", "ClientTlsParams", "StreamTrimOptions", "StreamConfigOptions", "StreamAddOptions", "StreamAutoClaimOptions", "StreamClaimOptions", "StreamReadOptions", "StreamAutoClaimReply", "StreamReadReply", "StreamRangeReply", "StreamClaimReply", "StreamPendingData", "StreamPendingCountReply", "StreamInfoStreamReply", "StreamInfoStreamReplyWithIdempotency", "StreamInfoConsumersReply", "StreamInfoGroupsReply", "StreamInfoConsumer", "StreamInfoGroup", "StreamPendingId", "StreamKey", "StreamId", "ScanOptions", "LposOptions", "CopyOptions", "SetOptions", "MSetOptions", "FlushAllOptions", "HashFieldExpirationOptions", "SortedSetAddOptions", "AclInfo", "Coord", "RadiusOptions", "RadiusSearchResult", "VSimOptions", "VAddOptions", "VEmbOptions", "HotkeysOptions", "HotKeyEntry", "SlotRange", "HotkeysResponse", "ServerErrorKind", "ErrorKind", "RetryMethod", "SentinelServerType", "Expiry", "SetExpiry", "ExistenceCheck", "FieldExistenceCheck", "NumericBehavior", "Value", "ValueComparison", "VerbatimFormat", "PushKind", "MapIter", "OwnedMapIter", "Role", "ProtocolVersion", "ExpireOption", "ValueType", "IntegerReplyOrNoOp", "LogicalAggregateOp", "AggregateOp", "ResponsePolicy", "RoutingInfo", "SingleNodeRoutingInfo", "MultipleNodeRoutingInfo", "MultiSlotArgPattern", "SlotAddr", "ReadCandidates", "Arg", "BloomFilterInfoType", "BloomFilterScalingOptions", "TlsMode", "ConnectionAddr", "CacheMode", "StreamMaxlen", "StreamTrimmingMode", "StreamTrimStrategy", "StreamIdempotencyMode", "StreamPendingReply", "StreamDeletionPolicy", "XDelExStatusCode", "XAckDelStatusCode", "ControlFlow", "Direction", "UpdateCheck", "Rule", "Unit", "RadiusOrder", "EmbeddingInput", "VectorAddInput", "VectorQuantization", "VectorSimilaritySearchInput"]
