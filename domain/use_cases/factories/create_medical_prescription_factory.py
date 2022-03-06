from domain.use_cases.create_medical_prescription import CreateMedicalPrescription
from infra.repositories.factories.medical_prescription_repository_factory import (
    MedicalPrescriptionRepositoryFactory,
)
from infra.repositories.factories.doctor_repository_factory import (
    DoctorRepositoryFactory,
)
from infra.repositories.factories.patient_repository_factory import (
    PatientRepositoryFactory,
)


def CreateMedicalPrescriptionFactory() -> CreateMedicalPrescription:
    medical_prescription_repository = MedicalPrescriptionRepositoryFactory()
    patient_repository = PatientRepositoryFactory()
    doctor_repository = DoctorRepositoryFactory()
    return CreateMedicalPrescription(
        medical_prescription_repository=medical_prescription_repository,
        patient_repository=patient_repository,
        doctor_repository=doctor_repository,
    )
