from abc import ABC, abstractmethod
from datetime import date
from domain.entities.exam import IExam


class IExamRepository(ABC):
    @abstractmethod
    def create(
        self,
        date: date,
        employee_id: int,
        previous_medical_appointment_id: int,
        patient_id: int,
        doctor_id: int,
    ) -> IExam:
        pass
