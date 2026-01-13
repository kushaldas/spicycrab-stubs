"""Security headers example with actix-web.

Demonstrates:
- Common security headers for web applications
- Content Security Policy (CSP)
- XSS protection and other security measures
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def secure_page() -> HttpResponse:
    """Page with comprehensive security headers."""
    html: str = "<!DOCTYPE html><html><head><title>Secure Page</title></head><body><h1>This page has security headers</h1></body></html>"
    return HttpResponse.Ok().content_type("text/html").insert_header(("X-Content-Type-Options", "nosniff")).insert_header(("X-Frame-Options", "DENY")).insert_header(("X-XSS-Protection", "1; mode=block")).insert_header(("Strict-Transport-Security", "max-age=31536000; includeSubDomains")).insert_header(("Content-Security-Policy", "default-src 'self'")).body(html)


async def api_secure() -> HttpResponse:
    """API endpoint with security headers."""
    json_body: str = '{"message": "Secure API response"}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-Content-Type-Options", "nosniff")).insert_header(("Cache-Control", "no-store")).insert_header(("Pragma", "no-cache")).body(json_body)


async def referrer_policy() -> HttpResponse:
    """Page demonstrating Referrer-Policy header."""
    html: str = "<!DOCTYPE html><html><body><p>This page controls referrer information</p></body></html>"
    return HttpResponse.Ok().content_type("text/html").insert_header(("Referrer-Policy", "strict-origin-when-cross-origin")).body(html)


async def permissions_policy() -> HttpResponse:
    """Page with Permissions-Policy header."""
    html: str = "<!DOCTYPE html><html><body><p>This page restricts browser features</p></body></html>"
    return HttpResponse.Ok().content_type("text/html").insert_header(("Permissions-Policy", "geolocation=(), microphone=(), camera=()")).body(html)


async def main() -> None:
    """Start the HTTP server with security header examples."""
    HttpServer.new(App.new().route("/secure", get().to(secure_page)).route("/api/secure", get().to(api_secure)).route("/referrer", get().to(referrer_policy)).route("/permissions", get().to(permissions_policy))).bind("127.0.0.1:8080").run()
