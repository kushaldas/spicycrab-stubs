"""Combined application example with actix-web.

Demonstrates:
- Complete web application with multiple endpoints
- API routes, health checks, and static content
- Production-ready patterns combined
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get, post


async def index() -> HttpResponse:
    """Home page."""
    html: str = "<!DOCTYPE html><html><head><title>Welcome</title></head><body><h1>Welcome to Actix Web!</h1><p>A fast web framework for Rust.</p></body></html>"
    return HttpResponse.Ok().content_type("text/html").body(html)


async def health() -> HttpResponse:
    """Health check endpoint."""
    json_body: str = '{"status": "healthy"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def api_info() -> HttpResponse:
    """API information endpoint."""
    json_body: str = '{"name": "My API", "version": "1.0.0", "endpoints": ["/api/users", "/api/items"]}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-API-Version", "1.0.0")).body(json_body)


async def list_users() -> HttpResponse:
    """List all users."""
    json_body: str = '{"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def create_user() -> HttpResponse:
    """Create a new user."""
    json_body: str = '{"id": 3, "name": "Charlie", "created": true}'
    return HttpResponse.Created().content_type("application/json").body(json_body)


async def list_items() -> HttpResponse:
    """List all items."""
    json_body: str = '{"items": [{"id": 1, "name": "Widget"}, {"id": 2, "name": "Gadget"}]}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def main() -> None:
    """Start the complete web application."""
    HttpServer.new(App.new().route("/", get().to(index)).route("/health", get().to(health)).route("/api", get().to(api_info)).route("/api/users", get().to(list_users)).route("/api/users", post().to(create_user)).route("/api/items", get().to(list_items))).bind("127.0.0.1:8080").run()
