from typing import Any, Dict
from sqlalchemy import Column, Date, Integer, String
from config.extensions import Base

MAX_CHAR_FOR_PASSWORD = 24


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(MAX_CHAR_FOR_PASSWORD), nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "fullname": self.fullname,
            "birthdate": self.birthdate,
            "email": self.email,
            "password": self.password,
        }
