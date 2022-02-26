from domain.repositories.medical_unit_repository import IMedicalUnitRepository
from infra.repositories.medical_unit_repository import MedicalUnitRepository
from config.extensions import db_session


def MedicalUnitRepositoryFactory() -> IMedicalUnitRepository:
    return MedicalUnitRepository(db_session)
