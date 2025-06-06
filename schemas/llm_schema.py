from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class LLMModelBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    model_type: str = Field(..., min_length=1, max_length=100)
    model_name: str = Field(..., min_length=1, max_length=255)
    api_key: Optional[str] = None
    temperature: str = Field(default="0.7")
    max_tokens: int = Field(default=1000, ge=1, le=4000)
    description: Optional[str] = None
    is_active: bool = Field(default=True)


class LLMModelCreate(LLMModelBase):
    pass


class LLMModelUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    model_type: Optional[str] = Field(None, min_length=1, max_length=100)
    model_name: Optional[str] = Field(None, min_length=1, max_length=255)
    api_key: Optional[str] = None
    temperature: Optional[str] = None
    max_tokens: Optional[int] = Field(None, ge=1, le=4000)
    description: Optional[str] = None
    is_active: Optional[bool] = None


class LLMModelResponse(LLMModelBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
