from datetime import date
from domain.entities.medical_appointment import IMedicalAppointment
from domain.use_cases.factories.create_medical_appointment_factory import (
    CreateMedicalAppointmentFactory,
)
from infra.repositories.factories.medical_appointment_repository_factory import (
    MedicalAppointmentRepositoryFactory,
)


class MedicalAppointmentController:
    def create(
        self, date: date, patient_id: int, problem_id: int, employee_id: int
    ) -> IMedicalAppointment:
        create_medical_appointment_use_case = CreateMedicalAppointmentFactory()
        medical_appointment_created = create_medical_appointment_use_case.execute(
            date, patient_id, problem_id, employee_id
        )
        return medical_appointment_created

    def find(self) -> list:
        repository = MedicalAppointmentRepositoryFactory()
        return repository.find()
