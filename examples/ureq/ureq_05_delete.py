"""DELETE request example.

Demonstrates:
- Sending a DELETE request
- Inspecting and returning the response
"""

from spicycrab_ureq import RequestBuilder, Response, WithoutBody, delete


def delete_resource(url: str) -> str:
    """DELETE *url* and return httpbin's response body."""
    request: RequestBuilder[WithoutBody] = delete(url).header("Accept", "application/json")
    response: Response = request.call()

    print(f"DELETE status: {response.status()}")
    print(f"Response headers: {response.headers_debug()}")

    body: str = response.into_body().read_to_string()
    return body


def main() -> None:
    """DELETE against httpbin and display its returned JSON document."""
    body: str = delete_resource("https://httpbin.org/delete")
    print(f"Returned body: {body}")
