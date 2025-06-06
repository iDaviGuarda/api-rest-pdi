from typing import List, Optional

from sqlalchemy.orm import Session

from models.llm_model import LLMModel
from schemas.llm_schema import LLMModelCreate, LLMModelUpdate


class LLMService:

    @staticmethod
    def criar_llm_model(db: Session, llm_model: LLMModelCreate) -> LLMModel:
        db_llm_model = LLMModel(**llm_model.model_dump())
        db.add(db_llm_model)
        db.commit()
        db.refresh(db_llm_model)
        return db_llm_model

    @staticmethod
    def get_llm_model_por_id(db: Session, model_id: int) -> Optional[LLMModel]:
        return db.query(LLMModel).filter(LLMModel.id == model_id).first()

    @staticmethod
    def get_llm_models(db: Session, skip: int = 0, limit: int = 100) -> List[LLMModel]:
        return db.query(LLMModel).offset(skip).limit(limit).all()

    @staticmethod
    def atualizar_llm_model(db: Session, model_id: int, llm_model: LLMModelUpdate) -> Optional[LLMModel]:
        db_llm_model = db.query(LLMModel).filter(LLMModel.id == model_id).first()
        if db_llm_model:
            update_data = llm_model.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_llm_model, field, value)
            db.commit()
            db.refresh(db_llm_model)
        return db_llm_model

    @staticmethod
    def deletar_llm_model_por_id(db: Session, model_id: int) -> bool:
        db_llm_model = db.query(LLMModel).filter(LLMModel.id == model_id).first()
        if db_llm_model:
            db.delete(db_llm_model)
            db.commit()
            return True
        return False
