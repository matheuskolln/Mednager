
from datetime import date
from pydantic import BaseModel
from domain.entities.doctor import IDoctor

from domain.entities.employee import IEmployee
from domain.entities.medical_appointment import IMedicalAppointment
from domain.entities.patient import IPatient


class IExam(BaseModel):
    id: int
    date: date
    employee: IEmployee
    previous_medical_appointment: IMedicalAppointment
    patient: IPatient
    doctor: IDoctor
