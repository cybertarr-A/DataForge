from datetime import datetime, timezone

from collectors.base import Collector
from collectors.http import fetch_url


class WebsiteCollector(Collector):

    def collect(self, source: str) -> list[dict]:
        html = fetch_url(source)

        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")

        title = None

        if soup.title:
            title = soup.title.get_text(strip=True)

        description = None

        meta = soup.find(
            "meta",
            attrs={"name": "description"},
        )

        if meta:
            description = meta.get("content")

        return [
            {
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
                "collected_at": datetime.now(timezone.utc),
                "data_quality_score": 0.0,
            }
        ]