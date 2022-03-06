from typing import Any, Dict
from sqlalchemy import Column, ForeignKey, Integer, String
from config.extensions import Base
from infra.entities.patient import Patient
from sqlalchemy.orm import relationship


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True)
    description = Column(String(500), nullable=False)
    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)

    patient: relationship = relationship(Patient)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "description": self.description,
            "patient_id": self.patient_id,
            "patient": self.patient.to_dict(),
        }
