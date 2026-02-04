"""Trend fetching contract implementation (spec-aligned placeholder)."""

from datetime import datetime, timezone


def fetch_trends(payload: dict) -> dict:
    """Return a spec-compliant trend payload using the provided request.

    This is a minimal contract implementation to satisfy tests; replace with
    real MCP-backed data ingestion after full ratification.
    """
    source = payload.get("source", "unknown")
    region = payload.get("region", "unknown")
    return {
        "source": source,
        "region": region,
        "as_of": datetime.now(timezone.utc).isoformat(),
        "trends": [
            {
                "trend_id": "stub-001",
                "title": "Placeholder Trend",
                "score": 0.0,
                "metadata": {"language": "en", "tags": []},
            }
        ],
    }
