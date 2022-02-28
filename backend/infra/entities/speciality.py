from sqlalchemy import Column, Integer, String
from config.extensions import Base


class Speciality(Base):
    __tablename__ = "specialities"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}
