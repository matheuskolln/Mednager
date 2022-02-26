from typing import Any, Dict
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.extensions import Base
from infra.entities.plan import Plan

MAX_CHAR_FOR_PASSWORD = 24


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    document = Column(Integer, nullable=False)
    plan_id = Column(Integer, ForeignKey(Plan.id), nullable=True)
    plan: relationship = relationship(Plan)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "fullname": self.fullname,
            "birthdate": self.birthdate,
            "document": self.document,
            "plan_id": self.plan_id,
            "plan": self.plan.to_dict() if self.plan else None,
        }
