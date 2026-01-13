"""Custom headers example with actix-web.

Demonstrates:
- Setting custom response headers with insert_header()
- Multiple headers on a single response
- Common header patterns (Content-Type, Cache-Control, etc.)
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def with_cache_headers() -> HttpResponse:
    """Response with cache control headers."""
    return HttpResponse.Ok().insert_header(("Cache-Control", "max-age=3600")).insert_header(("Vary", "Accept-Encoding")).body("This response is cacheable for 1 hour")


async def with_cors_headers() -> HttpResponse:
    """Response with CORS headers for cross-origin requests."""
    return HttpResponse.Ok().insert_header(("Access-Control-Allow-Origin", "*")).insert_header(("Access-Control-Allow-Methods", "GET, POST, OPTIONS")).body("CORS-enabled response")


async def with_custom_header() -> HttpResponse:
    """Response with a custom application header."""
    return HttpResponse.Ok().insert_header(("X-Custom-Header", "CustomValue")).insert_header(("X-Request-Id", "12345")).body("Response with custom headers")


async def json_with_headers() -> HttpResponse:
    """JSON response with appropriate headers."""
    json_body: str = '{"status": "ok"}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-API-Version", "1.0")).body(json_body)


async def main() -> None:
    """Start the HTTP server with header examples."""
    HttpServer.new(App.new().route("/cache", get().to(with_cache_headers)).route("/cors", get().to(with_cors_headers)).route("/custom", get().to(with_custom_header)).route("/api", get().to(json_with_headers))).bind("127.0.0.1:8080").run()
