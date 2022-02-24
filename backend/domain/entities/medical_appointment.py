from datetime import date
from pydantic import BaseModel
from domain.entities.employee import IEmployee

from domain.entities.patient import IPatient
from domain.entities.problem import IProblem


class IMedicalAppointment(BaseModel):
    id: int
    date: date
    patient: IPatient
    problem: IProblem
    employee: IEmployee
