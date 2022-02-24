from abc import ABC, abstractmethod
from datetime import date
from domain.entities.doctor import IDoctor
from domain.entities.employee import IEmployee
from domain.entities.exam import IExam
from domain.entities.medical_appointment import IMedicalAppointment

from domain.entities.patient import IPatient


class IExamRepository(ABC):
    @abstractmethod
    def create(
        self,
        date: date,
        employee: IEmployee,
        previous_medical_appointment: IMedicalAppointment,
        patient: IPatient,
        doctor: IDoctor,
    ) -> IExam:
        pass
