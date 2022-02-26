from datetime import date
from domain.entities.medical_appointment import IMedicalAppointment
from domain.repositories.employee_repository import IEmployeeRepository
from domain.repositories.medical_appointment_repository import (
    IMedicalAppointmentRepository,
)
from domain.repositories.patient_repository import IPatientRepository
from domain.repositories.problem_repository import IProblemRepository


class CreateMedicalAppointment:
    def __init__(
        self,
        medical_appointment_repository: IMedicalAppointmentRepository,
        patient_repository: IPatientRepository,
        problem_repository: IProblemRepository,
        employee_repository: IEmployeeRepository,
    ):
        self.medical_appointment_repository = medical_appointment_repository
        self.patient_repository = patient_repository
        self.problem_repository = problem_repository
        self.employee_repository = employee_repository

    def execute(
        self, date: date, patient_id: int, problem_id: int, employee_id: int
    ) -> IMedicalAppointment:
        patient = self.patient_repository.find_by_id(patient_id=patient_id)
        if not patient:
            raise Exception("Patient not found")

        problem = self.problem_repository.find_by_id(problem_id)
        if not problem:
            raise Exception("Problem not found")

        employee = self.employee_repository.find_by_id(employee_id)
        if not employee:
            raise Exception("Employee not found")

        medical_appointment_created = self.medical_appointment_repository.create(
            date, patient_id, problem_id, employee_id
        )
        return medical_appointment_created
