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


def test_all_skills_have_input_output_models():
    """Test that each skill module has input and output models"""
    skill_modules = [
        ("skill_trend_research", TrendResearchInput, TrendResearchOutput),
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
    ]

    for module_name, execute_func in skill_functions:
        assert callable(execute_func), f"{module_name} missing execute function"
        assert (
            execute_func.__name__ == f"execute_{module_name.replace('skill_', '')}"
        ), f"Function name should follow pattern: execute_[skill_name]"


def test_input_models_have_field_descriptions():
    """Test that all input model fields have descriptions (for AI clarity)"""
    input_models = [TrendResearchInput]

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
    # Trend research skill
    trend_input = TrendResearchInput(
        platforms=["twitter"], keywords=["test"], time_range_hours=1
    )

    with pytest.raises(NotImplementedError):
        execute_trend_research(trend_input)


def test_skill_output_includes_confidence_score():
    """Test that all skill outputs include confidence scores"""
    output_models = [TrendResearchOutput]

    for model in output_models:
        assert (
            "confidence_score" in model.model_fields
        ), f"{model.__name__} missing confidence_score field"

        field = model.model_fields["confidence_score"]
        # FIX: Use isinstance for type comparison
        assert (
            isinstance(field.annotation, type) and field.annotation == float
        ), "confidence_score must be float"

        # Check for ge/le constraints if they exist
        if hasattr(field, "ge"):
            assert field.ge == 0.0, "confidence_score minimum should be 0.0"
        if hasattr(field, "le"):
            assert field.le == 1.0, "confidence_score maximum should be 1.0"


def test_skill_output_includes_timestamp():
    """Test that all skill outputs include timestamps"""
    output_models = [TrendResearchOutput]

    for model in output_models:
        assert (
            "timestamp" in model.model_fields
        ), f"{model.__name__} missing timestamp field"
        # FIX: Check the annotation properly
        field = model.model_fields["timestamp"]
        assert field.annotation == datetime, "timestamp must be datetime"


if __name__ == "__main__":
    print("Running skills interface tests...")
    print("These tests should FAIL - they define contracts for AI implementation.")
    pytest.main([__file__, "-v"])