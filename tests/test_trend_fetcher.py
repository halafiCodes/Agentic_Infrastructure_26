"""
Test: Trend Fetcher Contract Validation
Purpose: Define the expected data structure for trend analysis
These tests MUST FAIL initially - they define what AI agents need to build.
"""

import pytest
from pydantic import ValidationError
from datetime import datetime, timezone
from skills.skill_trend_research import (
    TrendResearchInput,
    TrendResearchOutput,
    Platform,
    sample_trend_result,
)


def test_trend_input_contract():
    """Test that TrendResearchInput accepts correct parameters"""
    # This should work - defines the expected input structure
    input_data = TrendResearchInput(
        platforms=[Platform.TWITTER, Platform.INSTAGRAM],
        keywords=["ai", "influencers", "ethiopia"],
        time_range_hours=24,
        min_volume=100,
    )

    assert input_data.platforms == [Platform.TWITTER, Platform.INSTAGRAM]
    assert "ai" in input_data.keywords
    assert input_data.time_range_hours == 24


def test_trend_output_structure():
    """Test that TrendResearchOutput has expected structure"""
    # This test will FAIL because execute_trend_research is not implemented
    # It defines what the AI agent needs to build

    input_data = TrendResearchInput(
        platforms=[Platform.TWITTER], keywords=["test"], time_range_hours=1
    )

    # This should raise NotImplementedError (test will fail as expected)
    with pytest.raises(NotImplementedError):
        from skills.skill_trend_research import execute_trend_research

        execute_trend_research(input_data)


def test_trend_data_structure_matches_spec():
    """
    Test that trend data matches the API contract from specs/technical.md

    This defines the exact JSON structure expected from the trend research skill.
    """
    # Expected structure from specs/technical.md
    expected_structure = {
        "trend_id": "uuid-v4",
        "topic": "string",
        "platform": "twitter|instagram|tiktok",
        "growth_rate": "float",
        "volume": "integer",
        "sentiment": "positive|neutral|negative",
        "relevance_score": "float (0.0-1.0)",
        "timestamp": "iso-8601",
        "sample_content": ["string"],
    }

    # Test will fail - AI agents need to implement trend fetching that returns this structure
    actual_result = sample_trend_result()

    assert actual_result is not None, "Trend fetching must return a result"

    if actual_result:
        for key in expected_structure.keys():
            assert key in actual_result, f"Missing key in trend data: {key}"


def test_platform_enum_values():
    """Test that platform enum matches spec"""
    assert Platform.TWITTER.value == "twitter"
    assert Platform.INSTAGRAM.value == "instagram"
    assert Platform.TIKTOK.value == "tiktok"
    assert Platform.YOUTUBE.value == "youtube"


def test_confidence_score_range():
    """Test that confidence scores are within valid range"""
    output = TrendResearchOutput(
        success=False,
        trends_found=0,
        trends=[],
        analysis_summary="",
        confidence_score=0.0,
        platform_breakdown={},
        timestamp=datetime.now(timezone.utc),
        execution_time_ms=0,
    )

    assert 0.0 <= output.confidence_score <= 1.0


def test_confidence_score_invalid_raises():
    """Test that invalid confidence scores raise validation errors"""
    with pytest.raises(ValidationError):
        TrendResearchOutput(
            success=False,
            trends_found=0,
            trends=[],
            analysis_summary="",
            confidence_score=-0.1,
            platform_breakdown={},
            timestamp=datetime.now(timezone.utc),
            execution_time_ms=0,
        )


def test_invalid_platform_rejected():
    """Test that invalid platform values are rejected"""
    with pytest.raises(ValidationError):
        TrendResearchInput(
            platforms=["myspace"],
            keywords=["test"],
            time_range_hours=1,
        )


def test_sample_trend_result_has_valid_types():
    """Ensure the sample trend result uses valid types and ranges"""
    result = sample_trend_result()

    assert isinstance(result["trend_id"], str)
    assert isinstance(result["topic"], str)
    assert result["platform"] in {
        Platform.TWITTER.value,
        Platform.INSTAGRAM.value,
        Platform.TIKTOK.value,
        Platform.YOUTUBE.value,
    }
    assert isinstance(result["growth_rate"], float)
    assert isinstance(result["volume"], int)
    assert result["sentiment"] in {"positive", "neutral", "negative"}
    assert 0.0 <= result["relevance_score"] <= 1.0
    assert isinstance(result["timestamp"], str)
    assert result["timestamp"].endswith("Z")
    assert isinstance(result["sample_content"], list)


if __name__ == "__main__":
    print("Running trend fetcher tests...")
    print("These tests should FAIL - they define what AI agents need to build.")
    pytest.main([__file__, "-v"])