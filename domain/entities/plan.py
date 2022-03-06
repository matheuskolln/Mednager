from pydantic import BaseModel


class IPlan(BaseModel):
    name: str
    description: str
    price: float
