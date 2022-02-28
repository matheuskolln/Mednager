from domain.use_cases.find_doctors import FindDoctors
from infra.repositories.factories.doctor_repository_factory import (
    DoctorRepositoryFactory,
)


def FindDoctorsFactory() -> FindDoctors:
    doctor_repository = DoctorRepositoryFactory()
    return FindDoctors(doctor_repository)
