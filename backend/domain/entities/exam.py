from datetime import date
from pydantic import BaseModel
from domain.entities.doctor import IDoctor

from domain.entities.employee import IEmployee
from domain.entities.medical_appointment import IMedicalAppointment
from domain.entities.patient import IPatient


class IExam(BaseModel):
    date: date
    employee_id: int
    employee: IEmployee
    previous_medical_appointment_id: int
    previous_medical_appointment: IMedicalAppointment
    patient_id: int
    patient: IPatient
    doctor_id: int
    doctor: IDoctor
