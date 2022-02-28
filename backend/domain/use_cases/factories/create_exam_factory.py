from domain.use_cases.create_exam import CreateExam
from infra.repositories.factories.doctor_repository_factory import (
    DoctorRepositoryFactory,
)
from infra.repositories.factories.employee_repository_factory import (
    EmployeeRepositoryFactory,
)
from infra.repositories.factories.exam_repository_factory import ExamRepositoryFactory
from infra.repositories.factories.medical_appointment_repository_factory import (
    MedicalAppointmentRepositoryFactory,
)
from infra.repositories.factories.patient_repository_factory import (
    PatientRepositoryFactory,
)


def CreateExamFactory() -> CreateExam:
    exam_repository = ExamRepositoryFactory()
    employee_repository = EmployeeRepositoryFactory()
    medical_appointment_repository = MedicalAppointmentRepositoryFactory()
    patient_repository = PatientRepositoryFactory()
    doctor_repository = DoctorRepositoryFactory()

    return CreateExam(
        exam_repository=exam_repository,
        employee_repository=employee_repository,
        medical_appointment_repository=medical_appointment_repository,
        patient_repository=patient_repository,
        doctor_repository=doctor_repository,
    )
