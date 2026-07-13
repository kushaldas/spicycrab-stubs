"""Reuse a ureq agent to make an HTTP request.

Demonstrates:
- Creating a ureq agent
- Adding a request header
- Inspecting and returning the response
"""

from spicycrab_ureq import Agent, RequestBuilder, Response, WithoutBody, agent


def fetch_with_agent(url: str) -> str:
    """Fetch *url* with an agent and return its response body."""
    http_agent: Agent = agent()
    request: RequestBuilder[WithoutBody] = http_agent.get(url).header("X-Spicycrab-Example", "agent")
    response: Response = request.call()

    print(f"Agent GET status: {response.status()}")
    print(f"Response headers: {response.headers_debug()}")

    body: str = response.into_body().read_to_string()
    return body


def main() -> None:
    """Show the headers httpbin received from the agent request."""
    body: str = fetch_with_agent("https://httpbin.org/headers")
    print(f"Returned body: {body}")
