from pydantic import BaseModel

from domain.entities.patient import IPatient


class IProblem(BaseModel):
    patient_id: int
    description: str
    patient: IPatient
