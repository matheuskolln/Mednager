from datetime import date
from pydantic import BaseModel


class IDoctor(BaseModel):
    fullname: str
    birthdate: date
    crm: int
    speciality_id: int
