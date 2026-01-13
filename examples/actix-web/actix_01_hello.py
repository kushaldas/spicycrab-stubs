"""Basic hello world example with actix-web.

Demonstrates:
- Creating an App with App.new()
- Registering a route with get().to(handler)
- Starting HttpServer and binding to address
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def hello() -> HttpResponse:
    """Simple handler that returns Hello World."""
    return HttpResponse.Ok().body("Hello World!")


async def main() -> None:
    """Start the HTTP server."""
    HttpServer.new(App.new().route("/", get().to(hello))).bind("127.0.0.1:8080").run()
