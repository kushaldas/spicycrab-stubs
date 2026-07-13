"""Perform a GET request and inspect the response.

Demonstrates:
- Sending a GET request
- Printing the status and response headers
- Reading and returning the response body
"""

from spicycrab_ureq import RequestBuilder, Response, WithoutBody, get


def fetch(url: str) -> str:
    """Fetch *url* and return its response body."""
    request: RequestBuilder[WithoutBody] = get(url).header("Accept", "application/json")
    response: Response = request.call()

    print(f"GET status: {response.status()}")
    print(f"Response headers: {response.headers_debug()}")

    body: str = response.into_body().read_to_string()
    return body


def main() -> None:
    """Fetch httpbin and display the returned JSON document."""
    body: str = fetch("https://httpbin.org/get?source=spicycrab")
    print(f"Returned body: {body}")
