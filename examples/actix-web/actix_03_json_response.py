"""JSON response example with actix-web.

Demonstrates:
- Setting Content-Type header for JSON
- Building JSON response with body()
- Using HttpResponseBuilder methods
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def json_hello() -> HttpResponse:
    """Return a JSON response with a greeting."""
    json_body: str = '{"message": "Hello, JSON!", "status": "success"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def json_user() -> HttpResponse:
    """Return a JSON response with user data."""
    json_body: str = '{"id": 1, "name": "John Doe", "email": "john@example.com"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def json_list() -> HttpResponse:
    """Return a JSON array response."""
    json_body: str = '[{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def main() -> None:
    """Start the HTTP server with JSON endpoints."""
    HttpServer.new(App.new().route("/hello", get().to(json_hello)).route("/user", get().to(json_user)).route("/items", get().to(json_list))).bind("127.0.0.1:8080").run()
