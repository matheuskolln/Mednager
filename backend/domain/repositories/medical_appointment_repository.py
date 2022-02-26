from abc import ABC, abstractmethod
from datetime import date
from domain.entities.medical_appointment import IMedicalAppointment


class IMedicalAppointmentRepository(ABC):
    @abstractmethod
    def create(
        self, date: date, patient_id: int, problem_id: int, employee_id: int
    ) -> IMedicalAppointment:
        pass
