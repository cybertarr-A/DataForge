from __future__ import annotations

import requests


def fetch_url(url: str, timeout: int = 15) -> str:
    response = requests.get(
        url,
        timeout=timeout,
        headers={
            "User-Agent": "DataForge/0.1"
        },
    )

    response.raise_for_status()

    return response.text

