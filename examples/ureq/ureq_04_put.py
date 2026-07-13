"""PUT request example.

Demonstrates:
- Sending a text request body
- Inspecting and returning the response
"""

from spicycrab_ureq import RequestBuilder, Response, WithBody, put


def put_text(url: str, payload: str) -> str:
    """PUT *payload* as text and return httpbin's response body."""
    request: RequestBuilder[WithBody] = put(url).header("Content-Type", "text/plain")
    response: Response = request.send(payload)

    print(f"PUT status: {response.status()}")
    print(f"Response headers: {response.headers_debug()}")

    body: str = response.into_body().read_to_string()
    return body


def main() -> None:
    """PUT text to httpbin and display its echoed return value."""
    body: str = put_text("https://httpbin.org/put", "updated by spicycrab")
    print(f"Returned body: {body}")
