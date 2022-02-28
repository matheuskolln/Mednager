from domain.repositories.speciality_repository import ISpecialityRepository
from infra.repositories.speciality_repository import SpecialityRepository
from config.extensions import db_session


def SpecialityRepositoryFactory() -> ISpecialityRepository:
    return SpecialityRepository(db_session)
