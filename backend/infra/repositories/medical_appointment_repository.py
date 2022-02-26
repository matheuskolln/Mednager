from datetime import date
from domain.entities.medical_appointment import IMedicalAppointment
from domain.repositories.medical_appointment_repository import (
    IMedicalAppointmentRepository,
)
from sqlalchemy.orm.session import Session

from infra.entities.medical_appointment import MedicalAppointment


class MedicalAppointmentRepository(IMedicalAppointmentRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self, date: date, patient_id: int, problem_id: int, employee_id: int
    ) -> IMedicalAppointment:
        medical_appointment = MedicalAppointment(
            date=date,
            patient_id=patient_id,
            problem_id=problem_id,
            employee_id=employee_id,
        )

        self.session.add(medical_appointment)
        self.session.commit()

        return medical_appointment
