# Fix the test_skills_interface.py file

"""
Test: Skills Interface Contracts
Purpose: Validate that all skills follow the required input/output pattern
These tests MUST FAIL initially - they define the contracts for AI implementation.
"""

import pytest
import inspect
from pydantic import BaseModel
from datetime import datetime
from skills.skill_trend_research import (
    TrendResearchInput,
    TrendResearchOutput,
    execute_trend_research,
)
from skills.skill_generate_content import (
    ContentGenerateInput,
    ContentGenerateOutput,
    execute_generate_content,
)
from skills.skill_publish_content import (
    PublishContentInput,
    PublishContentOutput,
    execute_publish_content,
)


def test_all_skills_have_input_output_models():
    """Test that each skill module has input and output models"""
    skill_modules = [
        ("skill_trend_research", TrendResearchInput, TrendResearchOutput),
        ("skill_generate_content", ContentGenerateInput, ContentGenerateOutput),
        ("skill_publish_content", PublishContentInput, PublishContentOutput),
    ]

    for module_name, input_model, output_model in skill_modules:
        assert inspect.isclass(input_model), f"{module_name} missing Input model"
        assert inspect.isclass(output_model), f"{module_name} missing Output model"
        assert issubclass(
            input_model, BaseModel
        ), f"{module_name} Input must be Pydantic model"
        assert issubclass(
            output_model, BaseModel
        ), f"{module_name} Output must be Pydantic model"


def test_all_skills_have_execute_function():
    """Test that each skill has an execute function"""
    skill_functions = [
        ("skill_trend_research", execute_trend_research),
        ("skill_generate_content", execute_generate_content),
        ("skill_publish_content", execute_publish_content),
    ]

    for module_name, execute_func in skill_functions:
        assert callable(execute_func), f"{module_name} missing execute function"
        assert (
            execute_func.__name__ == f"execute_{module_name.replace('skill_', '')}"
        ), f"Function name should follow pattern: execute_[skill_name]"


def test_input_models_have_field_descriptions():
    """Test that all input model fields have descriptions (for AI clarity)"""
    input_models = [TrendResearchInput, ContentGenerateInput, PublishContentInput]

    for model in input_models:
        for field_name, field in model.model_fields.items():
            assert (
                field.description is not None
            ), f"Field '{field_name}' in {model.__name__} missing description"
            assert (
                len(field.description) > 0
            ), f"Field '{field_name}' in {model.__name__} has empty description"


def test_skill_execution_raises_not_implemented():
    """Test that skills raise NotImplementedError (they should be implemented by AI)"""
    trend_input = TrendResearchInput(
        platforms=["twitter"], keywords=["test"], time_range_hours=1
    )

    with pytest.raises(NotImplementedError):
        execute_trend_research(trend_input)

    content_input = ContentGenerateInput(
        trend_id="trend-1", tone="playful", length="short"
    )

    with pytest.raises(NotImplementedError):
        execute_generate_content(content_input)

    publish_input = PublishContentInput(content_id="content-1", platform="tiktok")

    with pytest.raises(NotImplementedError):
        execute_publish_content(publish_input)


def test_skill_output_includes_confidence_score():
    """Test that trend output includes confidence score"""
    field = TrendResearchOutput.model_fields["confidence_score"]
    assert isinstance(field.annotation, type) and field.annotation == float

    if hasattr(field, "ge"):
        assert field.ge == 0.0, "confidence_score minimum should be 0.0"
    if hasattr(field, "le"):
        assert field.le == 1.0, "confidence_score maximum should be 1.0"


def test_skill_output_includes_timestamp():
    """Test that trend output includes timestamps"""
    assert "timestamp" in TrendResearchOutput.model_fields
    field = TrendResearchOutput.model_fields["timestamp"]
    assert field.annotation == datetime, "timestamp must be datetime"


if __name__ == "__main__":
    print("Running skills interface tests...")
    print("These tests should FAIL - they define contracts for AI implementation.")
    pytest.main([__file__, "-v"])