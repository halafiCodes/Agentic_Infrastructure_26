"""Content generation skill contract (spec-only)."""

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Tone(str, Enum):
    PLAYFUL = "playful"
    SERIOUS = "serious"
    INFORMATIVE = "informative"


class Length(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


class AssetType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"


class ContentAsset(BaseModel):
    type: AssetType = Field(..., description="Asset type for the draft.")
    uri: str = Field(..., description="URI for the generated asset.")


class ContentGenerateInput(BaseModel):
    trend_id: str = Field(..., description="Trend identifier to draft against.")
    tone: Tone = Field(..., description="Desired tone for the draft.")
    length: Length = Field(..., description="Desired length category for the draft.")


class ContentGenerateOutput(BaseModel):
    success: bool = Field(..., description="Whether content generation succeeded.")
    content_id: str | None = Field(None, description="Identifier for the draft.")
    caption: str | None = Field(None, description="Draft caption text.")
    hashtags: List[str] = Field(default_factory=list, description="Hashtags.")
    assets: List[ContentAsset] = Field(
        default_factory=list, description="Generated assets for the draft."
    )
    error_code: str | None = Field(None, description="Error code if failed.")
    error_message: str | None = Field(None, description="Error description if failed.")


def execute_generate_content(_: ContentGenerateInput) -> ContentGenerateOutput:
    raise NotImplementedError("Content generation is not implemented yet.")
