"""Request information extraction example with actix-web.

Demonstrates:
- Extracting request information using HttpRequest
- Accessing method, path, URI, and query string
- Low-level request access in handlers
"""

from spicycrab_actix_web import App, HttpRequest, HttpResponse, HttpServer, get


async def request_info(request: HttpRequest) -> HttpResponse:
    """Display basic request information."""
    body: str = f"Method: {request.method()}\nPath: {request.path()}\nQuery: {request.query_string()}"
    return HttpResponse.Ok().content_type("text/plain").body(body)


async def echo_method(request: HttpRequest) -> HttpResponse:
    """Echo the actual request method."""
    return HttpResponse.Ok().body(f"You used HTTP method: {request.method()}")


async def echo_path(request: HttpRequest) -> HttpResponse:
    """Echo the actual request path."""
    return HttpResponse.Ok().body(f"Request path: {request.path()}")


async def main() -> None:
    """Start the HTTP server with request info endpoints."""
    HttpServer.new(App.new().route("/info", get().to(request_info)).route("/method", get().to(echo_method)).route("/path", get().to(echo_path))).bind("127.0.0.1:8080").run()
