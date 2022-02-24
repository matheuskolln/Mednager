from abc import ABC, abstractmethod
from datetime import date
from domain.entities.employee import IEmployee
from domain.entities.medical_appointment import IMedicalAppointment

from domain.entities.patient import IPatient
from domain.entities.problem import IProblem


class IMedicalAppointmentRepository(ABC):
    @abstractmethod
    def create(
        self, date: date, patient: IPatient, problem: IProblem, employee: IEmployee
    ) -> IMedicalAppointment:
        pass
