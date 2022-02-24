from datetime import date
from domain.entities.employee import IEmployee
from domain.entities.medical_appointment import IMedicalAppointment
from domain.entities.patient import IPatient
from domain.entities.problem import IProblem
from domain.repositories.medical_appointment_repository import (
    IMedicalAppointmentRepository,
)


class CreateMedicalAppointment:
    def __init__(self, medical_appointment_repository: IMedicalAppointmentRepository):
        self.medical_appointment_repository = medical_appointment_repository

    def execute(
        self, date: date, patient: IPatient, problem: IProblem, employee: IEmployee
    ) -> IMedicalAppointment:
        medical_appointment_created = self.medical_appointment_repository.create(
            date, patient, problem, employee
        )
        return medical_appointment_created
