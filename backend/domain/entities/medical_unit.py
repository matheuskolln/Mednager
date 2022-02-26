from pydantic import BaseModel


class IMedicalUnit(BaseModel):
    name: str
    address: str
