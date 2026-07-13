"""POST request example.

Demonstrates:
- Sending a JSON request body
- Inspecting and returning the response
"""

from spicycrab_ureq import RequestBuilder, Response, WithBody, post


def post_json(url: str, payload: str) -> str:
    """POST *payload* as JSON and return httpbin's response body."""
    request: RequestBuilder[WithBody] = post(url).header("Content-Type", "application/json")
    response: Response = request.send(payload)

    print(f"POST status: {response.status()}")
    print(f"Response headers: {response.headers_debug()}")

    body: str = response.into_body().read_to_string()
    return body


def main() -> None:
    """POST JSON to httpbin and display its echoed return value."""
    payload: str = '{"name":"spicycrab","operation":"post"}'
    body: str = post_json("https://httpbin.org/post", payload)
    print(f"Returned body: {body}")
