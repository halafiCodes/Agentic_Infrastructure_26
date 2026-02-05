import re


class TrendPayload:
    """OOP-style payload builder for trend fetcher tests."""

    def __init__(self, source: str, region: str, limit: int) -> None:
        self.source = source
        self.region = region
        self.limit = limit

    def to_dict(self) -> dict:
        return {"source": self.source, "region": self.region, "limit": self.limit}


class TestTrendFetcher:
    """Contract tests for trend fetcher response structure."""

    def test_trend_fetcher_contract(self):
        """Contract test for trend fetcher response structure."""
        # NOTE: This intentionally fails until implementation exists.
        from chimera.trends import fetch_trends  # noqa: F401

        payload = TrendPayload(source="tiktok", region="US", limit=20)
        response = fetch_trends(payload.to_dict())

        assert response["source"] == payload.source
        assert response["region"] == payload.region
        assert re.match(r"\d{4}-\d{2}-\d{2}T", response["as_of"])
        assert isinstance(response["trends"], list)

        item = response["trends"][0]
        assert "trend_id" in item
        assert "title" in item
        assert "score" in item
        assert "metadata" in item
