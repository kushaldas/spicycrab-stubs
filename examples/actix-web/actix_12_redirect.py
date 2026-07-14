"""HTTP redirects example with actix-web.

Demonstrates:
- Setting Location headers for redirects
- Common redirect patterns
- Redirect with different destinations
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def redirect_home() -> HttpResponse:
    """Redirect to home page."""
    return HttpResponse.Found().insert_header(("Location", "/")).finish()


async def redirect_docs() -> HttpResponse:
    """Redirect to documentation."""
    return HttpResponse.TemporaryRedirect().insert_header(("Location", "/docs")).finish()


async def redirect_login() -> HttpResponse:
    """Redirect to login page."""
    return HttpResponse.SeeOther().insert_header(("Location", "/login")).finish()


async def redirect_dashboard() -> HttpResponse:
    """Redirect to dashboard after successful action."""
    return HttpResponse.SeeOther().insert_header(("Location", "/dashboard")).finish()


async def main() -> None:
    """Start the HTTP server with redirect examples."""
    HttpServer.new(App.new().route("/old-page", get().to(redirect_home)).route("/api-docs", get().to(redirect_docs)).route("/auth", get().to(redirect_login)).route("/success", get().to(redirect_dashboard))).bind("127.0.0.1:8080").run()
