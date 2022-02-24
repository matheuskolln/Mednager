from pydantic import BaseModel


class IMedicalUnit(BaseModel):
    id: int
    name: str
    address: str
