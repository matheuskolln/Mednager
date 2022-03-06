from domain.repositories.doctor_repository import IDoctorRepository
from infra.repositories.doctor_repository import DoctorRepository
from config.extensions import db_session


def DoctorRepositoryFactory() -> IDoctorRepository:
    return DoctorRepository(db_session)
