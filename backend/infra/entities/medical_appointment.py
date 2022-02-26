from typing import Any, Dict
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from config.extensions import Base
from infra.entities.patient import Patient
from infra.entities.problem import Problem
from infra.entities.employee import Employee


class MedicalAppointment(Base):
    __tablename__ = "medical_appointments"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)
    problem_id = Column(Integer, ForeignKey(Problem.id), nullable=False)
    employee_id = Column(Integer, ForeignKey(Employee.id), nullable=False)

    patient: relationship = relationship(Patient)
    problem: relationship = relationship(Problem)
    employee: relationship = relationship(Employee)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "date": self.date,
            "patient_id": self.patient_id,
            "problem_id": self.problem_id,
            "employee_id": self.employee_id,
            "patient": self.patient.to_dict(),
            "problem": self.problem.to_dict(),
            "employee": self.employee.to_dict(),
        }
