from __future__ import annotations

from datetime import datetime, timezone
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from collectors.base import Collector
from collectors.http import fetch_url


class WebsiteCollector(Collector):

    def collect(self, source: str) -> list[dict]:
        parsed = urlparse(source)

        if parsed.scheme not in {"http", "https"}:
            raise ValueError(
                f"Unsupported URL scheme: {parsed.scheme}"
            )

        html = fetch_url(source)

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        title = None

        if soup.title:
            title = soup.title.get_text(
                " ",
                strip=True,
            )

        description = None

        meta = soup.find(
            "meta",
            attrs={"name": "description"},
        )

        if meta:
            description = meta.get(
                "content"
            )

        record = {
            "name": title or "Unknown",
            "website": source,
            "category": None,
            "city": None,
            "state": None,
            "country": None,
            "source_url": source,
            "page_title": title,
            "description": description,
            "website_status": "active",
            "collected_at": datetime.now(
                timezone.utc,
            ),
            "data_quality_score": 0.0,
        }

        return [record]