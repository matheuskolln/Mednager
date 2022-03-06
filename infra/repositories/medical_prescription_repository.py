from datetime import date
from sqlalchemy.orm.session import Session
from domain.entities.medical_prescription import IMedicalPrescription
from domain.repositories.medical_prescription_repository import (
    IMedicalPrescriptionRepository,
)
from infra.entities.medical_prescription import MedicalPrescription


class MedicalPrescriptionRepository(IMedicalPrescriptionRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def create(
        self, description: str, date: date, patient_id: int, doctor_id: int
    ) -> IMedicalPrescription:
        medical_prescription = MedicalPrescription(
            description=description,
            date=date,
            patient_id=patient_id,
            doctor_id=doctor_id,
        )

        self.session.add(medical_prescription)
        self.session.commit()

        return medical_prescription

    def find(self) -> list:
        return self.session.query(MedicalPrescription).all()
