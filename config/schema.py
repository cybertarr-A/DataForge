from datetime import datetime

from pydantic import BaseModel, HttpUrl


class BusinessRecord(BaseModel):
    name: str
    website: HttpUrl
    category: str | None = None

    city: str | None = None
    state: str | None = None
    country: str | None = None

    source_url: HttpUrl

    page_title: str | None = None
    description: str | None = None

    website_status: str = "unknown"

    collected_at: datetime

    data_quality_score: float = 0.0