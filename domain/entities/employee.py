from datetime import date
from pydantic import BaseModel


class IEmployee(BaseModel):
    fullname: str
    birthdate: date
    email: str
    password: str
