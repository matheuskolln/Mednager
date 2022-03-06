from datetime import date
from typing import Optional
from pydantic import BaseModel


class IPatient(BaseModel):
    fullname: str
    birthdate: date
    document: str  # CPF
    plan_id: Optional[int]
