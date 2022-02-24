from datetime import date
from pydantic import BaseModel


class IDoctor(BaseModel):
    id: int
    fullname: str
    birthdate: date
    crm: int
    speciality: int
