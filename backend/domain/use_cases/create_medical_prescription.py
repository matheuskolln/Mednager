from datetime import date
from domain.entities.doctor import IDoctor
from domain.entities.medical_prescription import IMedicalPrescription
from domain.entities.patient import IPatient
from domain.repositories.medical_prescription_repository import (
    MedicalPrescriptionRepository,
)


class CreateMedicalPrescription:
    def __init__(self, medical_prescription_repository: MedicalPrescriptionRepository):
        self.medical_prescription_repository = medical_prescription_repository

    def execute(
        self,
        description: str,
        date: date,
        patient: IPatient,
        doctor: IDoctor,
    ) -> IMedicalPrescription:
        medical_prescription_created = self.medical_prescription_repository.create(
            description, date, patient, doctor
        )
        return medical_prescription_created
