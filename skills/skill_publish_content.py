"""Publish content skill contract (spec-only)."""

from __future__ import annotations

from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field


class PublishPlatform(str, Enum):
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"


class PublishStatus(str, Enum):
    SCHEDULED = "scheduled"
    POSTED = "posted"
    FAILED = "failed"


class PublishContentInput(BaseModel):
    content_id: str = Field(..., description="Approved content identifier.")
    platform: PublishPlatform = Field(..., description="Target platform.")
    schedule_at: datetime | None = Field(
        None, description="Optional schedule time for publishing."
    )


class PublishContentOutput(BaseModel):
    success: bool = Field(..., description="Whether publishing succeeded.")
    publish_id: str | None = Field(None, description="Publish action identifier.")
    status: PublishStatus | None = Field(None, description="Publish status.")
    platform: PublishPlatform | None = Field(None, description="Target platform.")
    error_code: str | None = Field(None, description="Error code if failed.")
    error_message: str | None = Field(None, description="Error description if failed.")


def execute_publish_content(_: PublishContentInput) -> PublishContentOutput:
    raise NotImplementedError("Publishing is not implemented yet.")
