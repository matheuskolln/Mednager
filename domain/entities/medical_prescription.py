from pydantic import BaseModel
from datetime import date
from domain.entities.doctor import IDoctor

from domain.entities.patient import IPatient


class IMedicalPrescription(BaseModel):
    id: int
    description: str
    date: date
    patient: IPatient
    doctor: IDoctor
