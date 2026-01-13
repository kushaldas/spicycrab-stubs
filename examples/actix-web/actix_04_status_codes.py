"""HTTP status codes example with actix-web.

Demonstrates:
- Different HTTP status codes (200, 201, 204, 400, 401, 403, 404, 500)
- HttpResponse builder methods for various status codes
- Appropriate use cases for each status code
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def success() -> HttpResponse:
    """200 OK - Standard successful response."""
    return HttpResponse.Ok().body("Request was successful")


async def created() -> HttpResponse:
    """201 Created - Resource was created."""
    return HttpResponse.Created().body("Resource has been created")


async def no_content() -> HttpResponse:
    """204 No Content - Success with no response body."""
    return HttpResponse.NoContent().finish()


async def bad_request() -> HttpResponse:
    """400 Bad Request - Invalid request from client."""
    return HttpResponse.BadRequest().body("Invalid request parameters")


async def unauthorized() -> HttpResponse:
    """401 Unauthorized - Authentication required."""
    return HttpResponse.Unauthorized().body("Authentication required")


async def forbidden() -> HttpResponse:
    """403 Forbidden - Not allowed to access resource."""
    return HttpResponse.Forbidden().body("Access denied")


async def not_found() -> HttpResponse:
    """404 Not Found - Resource does not exist."""
    return HttpResponse.NotFound().body("Resource not found")


async def server_error() -> HttpResponse:
    """500 Internal Server Error - Server-side error."""
    return HttpResponse.InternalServerError().body("Internal server error")


async def main() -> None:
    """Start the HTTP server with various status code endpoints."""
    HttpServer.new(App.new().route("/success", get().to(success)).route("/created", get().to(created)).route("/no-content", get().to(no_content)).route("/bad-request", get().to(bad_request)).route("/unauthorized", get().to(unauthorized)).route("/forbidden", get().to(forbidden)).route("/not-found", get().to(not_found)).route("/error", get().to(server_error))).bind("127.0.0.1:8080").run()
