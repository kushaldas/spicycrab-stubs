"""Error response patterns example with actix-web.

Demonstrates:
- Structured error responses
- Different error formats for different scenarios
- Proper error status codes with meaningful bodies
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def validation_error() -> HttpResponse:
    """Return a validation error with details."""
    json_body: str = '{"error": "validation_failed", "message": "Invalid input data", "fields": {"email": "Invalid email format", "age": "Must be positive"}}'
    return HttpResponse.BadRequest().content_type("application/json").body(json_body)


async def auth_error() -> HttpResponse:
    """Return an authentication error."""
    json_body: str = '{"error": "unauthorized", "message": "Invalid or expired token"}'
    return HttpResponse.Unauthorized().content_type("application/json").insert_header(("WWW-Authenticate", "Bearer")).body(json_body)


async def permission_error() -> HttpResponse:
    """Return a permission denied error."""
    json_body: str = '{"error": "forbidden", "message": "You do not have permission to access this resource"}'
    return HttpResponse.Forbidden().content_type("application/json").body(json_body)


async def not_found_error() -> HttpResponse:
    """Return a resource not found error."""
    json_body: str = '{"error": "not_found", "message": "The requested resource was not found", "resource": "user", "id": "12345"}'
    return HttpResponse.NotFound().content_type("application/json").body(json_body)


async def server_error() -> HttpResponse:
    """Return an internal server error."""
    json_body: str = '{"error": "internal_error", "message": "An unexpected error occurred", "request_id": "abc-123"}'
    return HttpResponse.InternalServerError().content_type("application/json").body(json_body)


async def main() -> None:
    """Start the HTTP server with error response examples."""
    HttpServer.new(App.new().route("/error/validation", get().to(validation_error)).route("/error/auth", get().to(auth_error)).route("/error/permission", get().to(permission_error)).route("/error/not-found", get().to(not_found_error)).route("/error/server", get().to(server_error))).bind("127.0.0.1:8080").run()
