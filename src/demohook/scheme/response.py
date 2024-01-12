from typing import Any

from pydantic import BaseModel, Field


class WebHookResponse(BaseModel):
    code: int = Field(..., alias="code")
    label: str = Field(..., alias="label")
    data: Any = Field(default={}, alias="data")