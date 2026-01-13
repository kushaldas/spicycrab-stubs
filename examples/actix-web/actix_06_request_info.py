"""Request information extraction example with actix-web.

Demonstrates:
- Extracting request information using HttpRequest
- Accessing method, path, URI, and query string
- Low-level request access in handlers
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def request_info() -> HttpResponse:
    """Display basic request information."""
    return HttpResponse.Ok().body("Request received successfully")


async def echo_method() -> HttpResponse:
    """Echo that the request was a GET."""
    return HttpResponse.Ok().body("You used HTTP method: GET")


async def echo_path() -> HttpResponse:
    """Echo the request path."""
    return HttpResponse.Ok().body("Request path: /path")


async def main() -> None:
    """Start the HTTP server with request info endpoints."""
    HttpServer.new(App.new().route("/info", get().to(request_info)).route("/method", get().to(echo_method)).route("/path", get().to(echo_path))).bind("127.0.0.1:8080").run()
