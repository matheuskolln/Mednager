from pydantic import BaseModel

from domain.entities.patient import IPatient


class IProblem(BaseModel):
    id: int
    description: str
    patient: IPatient
