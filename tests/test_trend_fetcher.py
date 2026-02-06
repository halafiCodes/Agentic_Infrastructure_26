"""
Test: Trend Fetcher Contract Validation
Purpose: Define the expected data structure for trend analysis
These tests MUST FAIL initially - they define what AI agents need to build.
"""

import pytest
from datetime import datetime, timezone
from skills.skill_trend_research import (
    TrendResearchInput,
    TrendResearchOutput,
    Platform,
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
    actual_result = None  # Will be implemented by AI agents

    # These assertions will fail (as expected in TDD)
    assert actual_result is not None, "AI agents must implement trend fetching"

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
    # This test will fail until implementation exists
    output = TrendResearchOutput(
        success=False,
        trends_found=0,
        trends=[],
        analysis_summary="",
        confidence_score=-0.1,  # Invalid - should fail validation
        platform_breakdown={},
        timestamp=datetime.now(timezone.utc),
        execution_time_ms=0,
    )

    # Pydantic should validate this, but test will fail as expected
    assert 0.0 <= output.confidence_score <= 1.0


if __name__ == "__main__":
    print("Running trend fetcher tests...")
    print("These tests should FAIL - they define what AI agents need to build.")
    pytest.main([__file__, "-v"])