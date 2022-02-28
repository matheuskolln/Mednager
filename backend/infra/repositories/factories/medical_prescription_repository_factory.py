from domain.repositories.medical_prescription_repository import (
    IMedicalPrescriptionRepository,
)
from infra.repositories.medical_prescription_repository import (
    MedicalPrescriptionRepository,
)
from config.extensions import db_session


def MedicalPrescriptionRepositoryFactory() -> IMedicalPrescriptionRepository:
    return MedicalPrescriptionRepository(db_session)
