from domain.use_cases.find_specialities import FindSpecialities
from infra.repositories.factories.speciality_repository_factory import (
    SpecialityRepositoryFactory,
)


def FindSpecialitiesFactory() -> FindSpecialities:
    speciality_repository = SpecialityRepositoryFactory()
    return FindSpecialities(speciality_repository)
