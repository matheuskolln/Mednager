from datetime import date
from pydantic import BaseModel


class IEmployee(BaseModel):
    id: int
    fullname: str
    birthdate: date
    email: str
    password: str
