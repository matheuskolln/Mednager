from domain.use_cases.create_patient import CreatePatient
from infra.repositories.factories.patient_repository_factory import (
    PatientRepositoryFactory,
)


def CreatePatientFactory() -> CreatePatient:
    patient_repository = PatientRepositoryFactory()
    return CreatePatient(patient_repository)
