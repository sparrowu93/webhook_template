from pydantic import BaseModel, Field


class GeneralRequest(BaseModel):
    payload: dict = Field(..., title="payload")