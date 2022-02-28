from datetime import date
from domain.entities.exam import IExam
from domain.repositories.exam_repository import IExamRepository
from domain.repositories.employee_repository import IEmployeeRepository
from domain.repositories.medical_appointment_repository import (
    IMedicalAppointmentRepository,
)
from domain.repositories.patient_repository import IPatientRepository
from domain.repositories.doctor_repository import IDoctorRepository


class CreateExam:
    def __init__(
        self,
        exam_repository: IExamRepository,
        employee_repository: IEmployeeRepository,
        medical_appointment_repository: IMedicalAppointmentRepository,
        patient_repository: IPatientRepository,
        doctor_repository: IDoctorRepository,
    ):
        self.exam_repository = exam_repository
        self.employee_repository = employee_repository
        self.medical_appointment_repository = medical_appointment_repository
        self.patient_repository = patient_repository
        self.doctor_repository = doctor_repository

    def execute(
        self,
        date: date,
        employee_id: int,
        previous_medical_appointment_id: int,
        patient_id: int,
        doctor_id: int,
    ) -> IExam:
        employee = self.employee_repository.find_by_id(employee_id)
        if not employee:
            raise Exception("Employee not found")

        previous_medical_appointment = self.medical_appointment_repository.find_by_id(
            previous_medical_appointment_id
        )
        if not previous_medical_appointment:
            raise Exception("Previous medical appointment not found")

        patient = self.patient_repository.find_by_id(patient_id)
        if not patient:
            raise Exception("Patient not found")

        doctor = self.doctor_repository.find_by_id(doctor_id)
        if not doctor:
            raise Exception("Doctor not found")

        exam_created = self.exam_repository.create(
            date, employee_id, previous_medical_appointment_id, patient_id, doctor_id
        )
        return exam_created
