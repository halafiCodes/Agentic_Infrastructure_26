import re


def test_trend_fetcher_contract():
    """Contract test for trend fetcher response structure."""
    # NOTE: This intentionally fails until implementation exists.
    from chimera.trends import fetch_trends  # noqa: F401

    payload = {"source": "tiktok", "region": "US", "limit": 20}
    response = fetch_trends(payload)

    assert response["source"] == payload["source"]
    assert response["region"] == payload["region"]
    assert re.match(r"\d{4}-\d{2}-\d{2}T", response["as_of"])
    assert isinstance(response["trends"], list)

    item = response["trends"][0]
    assert "trend_id" in item
    assert "title" in item
    assert "score" in item
    assert "metadata" in item
