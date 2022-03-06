from datetime import date
from typing import Optional

from domain.entities.medical_prescription import IMedicalPrescription
from domain.use_cases.factories.create_medical_prescription_factory import (
    CreateMedicalPrescriptionFactory,
)
from infra.repositories.factories.medical_prescription_repository_factory import (
    MedicalPrescriptionRepositoryFactory,
)


class MedicalPrescriptionController:
    def create(
        self, description: str, date: date, patient_id: int, doctor_id: int
    ) -> Optional[IMedicalPrescription]:
        create_medical_prescription_use_case = CreateMedicalPrescriptionFactory()
        return create_medical_prescription_use_case.execute(
            description=description,
            date=date,
            patient_id=patient_id,
            doctor_id=doctor_id,
        )

    def find(self) -> list:
        repository = MedicalPrescriptionRepositoryFactory()
        return repository.find()
