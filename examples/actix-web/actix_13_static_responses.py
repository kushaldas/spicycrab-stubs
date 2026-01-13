"""Static file-like responses example with actix-web.

Demonstrates:
- Serving static content directly from handlers
- Setting appropriate MIME types
- Caching headers for static content
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def robots_txt() -> HttpResponse:
    """Serve robots.txt file."""
    content: str = "User-agent: *\nDisallow: /admin/\nDisallow: /private/\nAllow: /\n\nSitemap: https://example.com/sitemap.xml"
    return HttpResponse.Ok().content_type("text/plain").insert_header(("Cache-Control", "public, max-age=86400")).body(content)


async def favicon() -> HttpResponse:
    """Return a placeholder for favicon."""
    return HttpResponse.NoContent().content_type("image/x-icon").finish()


async def sitemap_xml() -> HttpResponse:
    """Serve sitemap.xml file."""
    content: str = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://example.com/</loc><lastmod>2024-01-01</lastmod></url></urlset>'
    return HttpResponse.Ok().content_type("application/xml").insert_header(("Cache-Control", "public, max-age=3600")).body(content)


async def manifest_json() -> HttpResponse:
    """Serve web app manifest."""
    content: str = '{"name": "My App", "short_name": "App", "start_url": "/", "display": "standalone", "theme_color": "#ffffff"}'
    return HttpResponse.Ok().content_type("application/manifest+json").insert_header(("Cache-Control", "public, max-age=86400")).body(content)


async def main() -> None:
    """Start the HTTP server with static content endpoints."""
    HttpServer.new(App.new().route("/robots.txt", get().to(robots_txt)).route("/favicon.ico", get().to(favicon)).route("/sitemap.xml", get().to(sitemap_xml)).route("/manifest.json", get().to(manifest_json))).bind("127.0.0.1:8080").run()
