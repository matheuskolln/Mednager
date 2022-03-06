from infra.repositories.medical_appointment_repository import (
    MedicalAppointmentRepository,
)
from config.extensions import db_session


def MedicalAppointmentRepositoryFactory():
    return MedicalAppointmentRepository(db_session)
