from typing import Any, Dict
from sqlalchemy import Column, Integer, String
from config.extensions import Base


class MedicalUnit(Base):
    __tablename__ = "medical_units"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(50), nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
        }
