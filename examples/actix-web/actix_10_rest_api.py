"""RESTful API example with actix-web.

Demonstrates:
- Complete REST API pattern for a resource
- CRUD operations (Create, Read, Update, Delete)
- Proper HTTP methods and status codes
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get, post, put, delete


async def list_items() -> HttpResponse:
    """GET /items - List all items."""
    json_body: str = '{"items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def get_item() -> HttpResponse:
    """GET /items/{id} - Get a single item."""
    json_body: str = '{"id": 1, "name": "Item 1", "description": "First item"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def create_item() -> HttpResponse:
    """POST /items - Create a new item."""
    json_body: str = '{"id": 3, "name": "New Item", "created": true}'
    return HttpResponse.Created().content_type("application/json").body(json_body)


async def update_item() -> HttpResponse:
    """PUT /items/{id} - Update an existing item."""
    json_body: str = '{"id": 1, "name": "Updated Item", "updated": true}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def delete_item() -> HttpResponse:
    """DELETE /items/{id} - Delete an item."""
    return HttpResponse.NoContent().finish()


async def main() -> None:
    """Start the HTTP server with REST API endpoints."""
    HttpServer.new(App.new().route("/items", get().to(list_items)).route("/items/1", get().to(get_item)).route("/items", post().to(create_item)).route("/items/1", put().to(update_item)).route("/items/1", delete().to(delete_item))).bind("127.0.0.1:8080").run()
