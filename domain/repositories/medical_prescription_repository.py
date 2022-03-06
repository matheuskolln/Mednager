from abc import ABC, abstractmethod
from datetime import date
from domain.entities.medical_prescription import IMedicalPrescription


class IMedicalPrescriptionRepository(ABC):
    @abstractmethod
    def create(
        self,
        description: str,
        date: date,
        patient_id: int,
        doctor_id: int,
    ) -> IMedicalPrescription:
        pass
