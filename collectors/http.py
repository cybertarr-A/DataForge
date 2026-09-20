from __future__ import annotations

import requests


DEFAULT_HEADERS = {
    "User-Agent": "DataForge/0.1 (+https://example.com/dataforge)"
}


def fetch_url(
    url: str,
    timeout: int = 15,
) -> str:
    response = requests.get(
        url,
        timeout=timeout,
        headers=DEFAULT_HEADERS,
    )

    response.raise_for_status()

    content_type = response.headers.get(
        "content-type",
        "",
    )

    if "text/html" not in content_type:
        raise ValueError(
            f"Expected HTML but received: {content_type}"
        )

    return response.text