"""Content types example with actix-web.

Demonstrates:
- Different content types (text/plain, text/html, application/json, application/xml)
- Setting Content-Type header appropriately
- Returning different formats from handlers
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def plain_text() -> HttpResponse:
    """Return plain text response."""
    return HttpResponse.Ok().content_type("text/plain").body("This is plain text content.")


async def html_page() -> HttpResponse:
    """Return an HTML page."""
    html: str = "<!DOCTYPE html><html><head><title>Hello</title></head><body><h1>Hello, World!</h1><p>This is an HTML page.</p></body></html>"
    return HttpResponse.Ok().content_type("text/html").body(html)


async def json_data() -> HttpResponse:
    """Return JSON data."""
    json_body: str = '{"type": "json", "message": "This is JSON data"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def xml_data() -> HttpResponse:
    """Return XML data."""
    xml: str = '<?xml version="1.0"?><response><type>xml</type><message>This is XML data</message></response>'
    return HttpResponse.Ok().content_type("application/xml").body(xml)


async def css_style() -> HttpResponse:
    """Return CSS stylesheet."""
    css: str = "body { font-family: Arial, sans-serif; margin: 20px; } h1 { color: #333; }"
    return HttpResponse.Ok().content_type("text/css").body(css)


async def main() -> None:
    """Start the HTTP server with content type examples."""
    HttpServer.new(App.new().route("/text", get().to(plain_text)).route("/html", get().to(html_page)).route("/json", get().to(json_data)).route("/xml", get().to(xml_data)).route("/style.css", get().to(css_style))).bind("127.0.0.1:8080").run()
