# spicycrab-tunnelbana-core

Python type stubs for the local `tunnelbana-core` Rust crate.

Use these stubs for the tunnelbana microservice codegen pilot. During local
development the generated Cargo project depends on the tunnelbana checkout by
path.

## MicroService Trait

The `MicroService` stub intentionally models Tunnelbana's async trait hooks:

- `async def process_request(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]`
- `async def process_response(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]`
- `async def handle_endpoint(self, ctx: Context, route_id: str) -> Result[Response, Error]`

The synchronous trait methods are also represented:

- `def name(self) -> str`
- `def register_endpoints(self) -> list[Route]`

When a Python class subclasses `MicroService`, spicycrab emits an
`#[async_trait::async_trait] impl tunnelbana_core::MicroService` block and uses
the Tunnelbana trait signatures for the async hooks.
