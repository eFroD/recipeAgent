"""Input models for video related uses."""

from pydantic import BaseModel


class VideoUrl(BaseModel):
    url: str
