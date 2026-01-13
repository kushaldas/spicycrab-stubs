"""Multiple HTTP methods example with actix-web.

Demonstrates:
- GET, POST, PUT, DELETE routes
- Different HTTP methods with get(), post(), put(), delete()
- Multiple routes in a single application
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get, post, put, delete


async def get_resource() -> HttpResponse:
    """Handle GET request - retrieve a resource."""
    return HttpResponse.Ok().body("GET: Retrieved resource")


async def create_resource() -> HttpResponse:
    """Handle POST request - create a resource."""
    return HttpResponse.Created().body("POST: Resource created")


async def update_resource() -> HttpResponse:
    """Handle PUT request - update a resource."""
    return HttpResponse.Ok().body("PUT: Resource updated")


async def delete_resource() -> HttpResponse:
    """Handle DELETE request - delete a resource."""
    return HttpResponse.Ok().body("DELETE: Resource deleted")


async def main() -> None:
    """Start the HTTP server with multiple routes."""
    HttpServer.new(App.new().route("/resource", get().to(get_resource)).route("/resource", post().to(create_resource)).route("/resource", put().to(update_resource)).route("/resource", delete().to(delete_resource))).bind("127.0.0.1:8080").run()
