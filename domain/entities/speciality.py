from pydantic import BaseModel


class ISpeciality(BaseModel):
    name: str
    description: str
