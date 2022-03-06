from typing import List
from pydantic import BaseModel
from domain.entities.doctor import IDoctor


class IMedicalUnit(BaseModel):
    name: str
    address: str
    employee_id: int
    doctors: List[IDoctor] = []
