from datetime import date
from domain.entities.medical_prescription import IMedicalPrescription
from domain.repositories.medical_prescription_repository import (
    IMedicalPrescriptionRepository,
)
from domain.repositories.doctor_repository import IDoctorRepository
from domain.repositories.patient_repository import IPatientRepository


class CreateMedicalPrescription:
    def __init__(
        self,
        medical_prescription_repository: IMedicalPrescriptionRepository,
        patient_repository: IPatientRepository,
        doctor_repository: IDoctorRepository,
    ):
        self.medical_prescription_repository = medical_prescription_repository
        self.patient_repository = patient_repository
        self.doctor_repository = doctor_repository

    def execute(
        self,
        description: str,
        date: date,
        patient_id: int,
        doctor_id: int,
    ) -> IMedicalPrescription:
        doctor = self.doctor_repository.find_by_id(doctor_id)
        if not doctor:
            raise Exception("Doctor not found")

        patient = self.patient_repository.find_by_id(patient_id)
        if not patient:
            raise Exception("Patient not found")

        medical_prescription_created = self.medical_prescription_repository.create(
            description, date, patient_id, doctor_id
        )
        return medical_prescription_created
