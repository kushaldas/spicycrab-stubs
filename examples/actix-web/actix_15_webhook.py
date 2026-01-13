"""Webhook endpoint example with actix-web.

Demonstrates:
- POST-only endpoints for webhooks
- Webhook acknowledgment responses
- Multiple webhook handlers
"""

from spicycrab_actix_web import App, HttpServer, HttpResponse, post


async def github_webhook() -> HttpResponse:
    """Handle GitHub webhook events."""
    json_body: str = '{"status": "received", "source": "github"}'
    return HttpResponse.Ok().content_type("application/json").insert_header(("X-Webhook-Processed", "true")).body(json_body)


async def stripe_webhook() -> HttpResponse:
    """Handle Stripe payment webhook events."""
    json_body: str = '{"status": "received", "source": "stripe"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def generic_webhook() -> HttpResponse:
    """Handle generic webhook events."""
    return HttpResponse.Ok().body("OK")


async def slack_webhook() -> HttpResponse:
    """Handle Slack webhook events."""
    json_body: str = '{"response_type": "in_channel", "text": "Webhook received!"}'
    return HttpResponse.Ok().content_type("application/json").body(json_body)


async def main() -> None:
    """Start the HTTP server with webhook endpoints."""
    HttpServer.new(App.new().route("/webhooks/github", post().to(github_webhook)).route("/webhooks/stripe", post().to(stripe_webhook)).route("/webhooks/generic", post().to(generic_webhook)).route("/webhooks/slack", post().to(slack_webhook))).bind("127.0.0.1:8080").run()
