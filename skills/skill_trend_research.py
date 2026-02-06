"""Trend research skill contract (spec-only)."""

from __future__ import annotations

from enum import Enum
from datetime import datetime
from typing import List, Dict

from pydantic import BaseModel, Field


class Platform(str, Enum):
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"


class TrendResearchInput(BaseModel):
    platforms: List[Platform] = Field(
        ..., description="Target platforms to scan for trends."
    )
    keywords: List[str] = Field(
        ..., description="Keywords to seed trend discovery."
    )
    time_range_hours: int = Field(
        ..., description="Lookback window in hours."
    )
    min_volume: int | None = Field(
        None, description="Minimum volume threshold to include a trend."
    )


class TrendResearchOutput(BaseModel):
    success: bool = Field(
        ..., description="Whether the trend research completed successfully."
    )
    trends_found: int = Field(
        ..., description="Number of trends discovered."
    )
    trends: List[Dict[str, object]] = Field(
        ..., description="Trend items matching the technical spec schema."
    )
    analysis_summary: str = Field(
        ..., description="Short natural language summary of findings."
    )
    confidence_score: float = Field(
        ..., ge=0.0, le=1.0, description="Confidence score between 0.0 and 1.0."
    )
    platform_breakdown: Dict[str, int] = Field(
        ..., description="Counts of trends per platform."
    )
    timestamp: datetime = Field(
        ..., description="UTC timestamp for the analysis run."
    )
    execution_time_ms: int = Field(
        ..., description="Total execution time in milliseconds."
    )


def execute_trend_research(_: TrendResearchInput) -> TrendResearchOutput:
    raise NotImplementedError("Trend research is not implemented yet.")
