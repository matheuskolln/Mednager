from domain.repositories.patient_repository import IPatientRepository
from infra.repositories.patient_repository import PatientRepository
from config.extensions import db_session


def PatientRepositoryFactory() -> IPatientRepository:
    return PatientRepository(db_session)
