from domain.use_cases.find_medical_units import FindMedicalUnits
from infra.repositories.factories.medical_unit_repository_factory import (
    MedicalUnitRepositoryFactory,
)


def FindMedicalUnitsFactory() -> FindMedicalUnits:
    medical_units_repository = MedicalUnitRepositoryFactory()
    return FindMedicalUnits(medical_units_repository)
