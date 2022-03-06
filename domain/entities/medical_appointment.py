from datetime import date
from pydantic import BaseModel
from domain.entities.employee import IEmployee

from domain.entities.patient import IPatient
from domain.entities.problem import IProblem


class IMedicalAppointment(BaseModel):
    id: int
    date: date
    patient_id: int
    patient: IPatient
    problem_id: int
    problem: IProblem
    employee_id: int
    employee: IEmployee
