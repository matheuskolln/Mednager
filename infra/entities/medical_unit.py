from typing import Any, Dict
from sqlalchemy import Column, Integer, String, ForeignKey
from config.extensions import Base
from infra.entities.doctor import Doctor, doctor_medical_unit
from sqlalchemy.orm import relationship

from infra.entities.employee import Employee


class MedicalUnit(Base):
    __tablename__ = "medical_units"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(50), nullable=False)

    doctors: relationship = relationship(
        Doctor, secondary=doctor_medical_unit, back_populates="medical_units"
    )
    employee_id = Column(Integer, ForeignKey(Employee.id), nullable=False)
    employee: relationship = relationship(Employee)

    def to_dict(self, populate=True) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "doctors": [
                doctor.to_dict(populate=False)
                if populate
                else {
                    "id": doctor.id,
                    "fullname": doctor.fullname,
                }
                for doctor in self.doctors
            ],
            "employee_id": self.employee_id,
            "employee": self.employee.to_dict(),
        }
