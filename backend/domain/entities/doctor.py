from datetime import date
from pydantic import BaseModel

from domain.entities.speciality import ISpeciality


class IDoctor(BaseModel):
    fullname: str
    birthdate: date
    crm: int
    speciality_id: int
    speciality: ISpeciality
