from abc import ABC, abstractmethod
from datetime import date
from typing import Optional
from domain.entities.medical_appointment import IMedicalAppointment


class IMedicalAppointmentRepository(ABC):
    @abstractmethod
    def create(
        self, date: date, patient_id: int, problem_id: int, employee_id: int
    ) -> IMedicalAppointment:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[IMedicalAppointment]:
        pass
