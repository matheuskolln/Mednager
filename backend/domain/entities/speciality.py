from pydantic import BaseModel


class ISpeciality(BaseModel):
    id: int
    name: str
    description: str
