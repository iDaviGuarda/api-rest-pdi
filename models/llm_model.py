from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from config.database import Base


class LLMModel(Base):
    __tablename__ = "llm_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    model_type = Column(String(100), nullable=False)
    model_name = Column(String(255), nullable=False)
    api_key = Column(Text, nullable=True)
    temperature = Column(String(10), default="0.7")
    max_tokens = Column(Integer, default=1000)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())