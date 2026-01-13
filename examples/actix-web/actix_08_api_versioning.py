"""API versioning example with actix-web.

Demonstrates:
- Multiple API versions with different routes
- Version headers in responses
- Organizing routes by API version
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def v1_users() -> HttpResponse:
    """API v1 - Get users list (simple format)."""
    json_body: str = '{"version": "1.0", "users": ["alice", "bob"]}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-API-Version", "1.0")).body(json_body)


async def v2_users() -> HttpResponse:
    """API v2 - Get users list (detailed format)."""
    json_body: str = '{"version": "2.0", "users": [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}], "total": 2}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-API-Version", "2.0")).body(json_body)


async def v1_status() -> HttpResponse:
    """API v1 - Get status."""
    json_body: str = '{"status": "ok"}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-API-Version", "1.0")).body(json_body)


async def v2_status() -> HttpResponse:
    """API v2 - Get detailed status."""
    json_body: str = '{"status": "healthy", "uptime": 12345, "version": "2.0"}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-API-Version", "2.0")).body(json_body)


async def main() -> None:
    """Start the HTTP server with versioned API endpoints."""
    HttpServer.new(App.new().route("/api/v1/users", get().to(v1_users)).route("/api/v2/users", get().to(v2_users)).route("/api/v1/status", get().to(v1_status)).route("/api/v2/status", get().to(v2_status))).bind("127.0.0.1:8080").run()
