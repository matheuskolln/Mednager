from abc import ABC, abstractmethod
from datetime import date
from domain.entities.doctor import IDoctor

from domain.entities.medical_prescription import IMedicalPrescription
from domain.entities.patient import IPatient


class MedicalPrescriptionRepository(ABC):
    @abstractmethod
    def create(
        self,
        description: str,
        date: date,
        patient: IPatient,
        doctor: IDoctor,
    ) -> IMedicalPrescription:
        pass
