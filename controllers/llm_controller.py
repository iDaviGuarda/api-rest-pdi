from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from services.llm_service import LLMService
from schemas.llm_schema import (
    LLMModelCreate,
    LLMModelUpdate,
    LLMModelResponse,
)
from typing import List

router = APIRouter(prefix="/api/llm-models", tags=["LLM Models"])

@router.post("/", response_model=LLMModelResponse, status_code=status.HTTP_201_CREATED)
def criar_llm_model(
    llm_model: LLMModelCreate,
    db: Session = Depends(get_db)
):
    return LLMService.criar_llm_model(db=db, llm_model=llm_model)

@router.get("/", response_model=List[LLMModelResponse])
def get_llm_models(
    page: int = 0,
    size: int = 100,
    db: Session = Depends(get_db)
):
    return LLMService.get_llm_models(db=db, skip=page, limit=size)

@router.get("/{model_id}", response_model=LLMModelResponse)
def get_llm_model_por_id(
    model_id: int,
    db: Session = Depends(get_db)
):
    db_llm_model = LLMService.get_llm_model_por_id(db=db, model_id=model_id)
    if db_llm_model is None:
        raise HTTPException(status_code=404, detail="LLM Model não encontrado.")
    return db_llm_model

@router.put("/{model_id}", response_model=LLMModelResponse)
def atualizar_llm_model(
    model_id: int,
    llm_model: LLMModelUpdate,
    db: Session = Depends(get_db)
):
    db_llm_model = LLMService.atualizar_llm_model(db=db, model_id=model_id, llm_model=llm_model)
    if db_llm_model is None:
        raise HTTPException(status_code=404, detail="LLM Model não encontrado.")
    return db_llm_model

@router.delete("/{model_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_llm_model_por_id(
    model_id: int,
    db: Session = Depends(get_db)
):
    success = LLMService.deletar_llm_model_por_id(db=db, model_id=model_id)
    if not success:
        raise HTTPException(status_code=404, detail="LLM Model não encontrado.")