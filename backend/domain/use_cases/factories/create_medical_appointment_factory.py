from domain.use_cases.create_medical_appointment import CreateMedicalAppointment
from infra.repositories.factories.employee_repository_factory import (
    EmployeeRepositoryFactory,
)
from infra.repositories.factories.patient_repository_factory import (
    PatientRepositoryFactory,
)
from infra.repositories.factories.medical_appointment_repository_factory import (
    MedicalAppointmentRepositoryFactory,
)
from infra.repositories.factories.problem_repository_factory import (
    ProblemRepositoryFactory,
)


def CreateMedicalAppointmentFactory() -> CreateMedicalAppointment:
    appointment_repository = MedicalAppointmentRepositoryFactory()
    patient_repository = PatientRepositoryFactory()
    problem_repository = ProblemRepositoryFactory()
    employee_repository = EmployeeRepositoryFactory()
    return CreateMedicalAppointment(
        appointment_repository,
        patient_repository,
        problem_repository,
        employee_repository,
    )
