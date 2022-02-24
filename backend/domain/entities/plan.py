from pydantic import BaseModel


class IPlan(BaseModel):
    id: int
    name: str
    description: str
    price: float
