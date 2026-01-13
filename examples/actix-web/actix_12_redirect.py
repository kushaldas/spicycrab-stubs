"""HTTP redirects example with actix-web.

Demonstrates:
- Setting Location headers for redirects
- Common redirect patterns
- Redirect with different destinations
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def redirect_home() -> HttpResponse:
    """Redirect to home page."""
    return HttpResponse.Ok().insert_header(("Location", "/")).body("Redirecting to home")


async def redirect_docs() -> HttpResponse:
    """Redirect to documentation."""
    return HttpResponse.Ok().insert_header(("Location", "/docs")).body("Redirecting to docs")


async def redirect_login() -> HttpResponse:
    """Redirect to login page."""
    return HttpResponse.Ok().insert_header(("Location", "/login")).body("Please login")


async def redirect_dashboard() -> HttpResponse:
    """Redirect to dashboard after successful action."""
    return HttpResponse.Ok().insert_header(("Location", "/dashboard")).body("Action successful, redirecting")


async def main() -> None:
    """Start the HTTP server with redirect examples."""
    HttpServer.new(App.new().route("/old-page", get().to(redirect_home)).route("/api-docs", get().to(redirect_docs)).route("/auth", get().to(redirect_login)).route("/success", get().to(redirect_dashboard))).bind("127.0.0.1:8080").run()
