from datetime import date
from typing import Optional
from pydantic import BaseModel

from domain.entities.plan import IPlan


class IPatient(BaseModel):
    id: int
    fullname: str
    birthdate: date
    document: int  # CPF
    plan: Optional[IPlan]
