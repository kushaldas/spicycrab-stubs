"""Health check endpoints example with actix-web.

Demonstrates:
- Common health check patterns for microservices
- Liveness and readiness probes
- Structured health responses
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, get


async def health() -> HttpResponse:
    """Simple health check endpoint."""
    return HttpResponse.Ok().body("OK")


async def liveness() -> HttpResponse:
    """Kubernetes-style liveness probe.

    Returns 200 if the service is alive.
    """
    json_body: str = '{"status": "alive"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def readiness() -> HttpResponse:
    """Kubernetes-style readiness probe.

    Returns 200 if the service is ready to accept traffic.
    """
    json_body: str = '{"status": "ready", "checks": {"database": "ok", "cache": "ok"}}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def detailed_health() -> HttpResponse:
    """Detailed health check with component status."""
    json_body: str = '{"status": "healthy", "components": {"api": "up", "database": "up", "cache": "up"}, "version": "1.0.0", "uptime_seconds": 3600}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def main() -> None:
    """Start the HTTP server with health check endpoints."""
    HttpServer.new(App.new().route("/health", get().to(health)).route("/healthz", get().to(liveness)).route("/ready", get().to(readiness)).route("/health/detailed", get().to(detailed_health))).bind("127.0.0.1:8080").run()
