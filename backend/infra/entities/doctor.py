from MySQLdb import Date
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.extensions import Base
from infra.entities.speciality import Speciality


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(255), nullable=False)
    birthdate = Column(Date, nullable=False)
    crm = Column(Integer, nullable=False)
    speciality_id = Column(Integer, ForeignKey(Speciality.id), nullable=False)

    speciality: relationship = relationship(Speciality)

    def to_dict(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "birthdate": self.birthdate,
            "crm": self.crm,
            "speciality_id": self.speciality_id,
            "speciality": self.speciality.to_dict(),
        }
