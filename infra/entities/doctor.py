from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from config.extensions import Base
from infra.entities.speciality import Speciality


doctor_medical_unit = Table(
    "doctor_medical_unit",
    Base.metadata,
    Column("doctor_id", Integer, ForeignKey("doctors.id")),
    Column("medical_unit_id", Integer, ForeignKey("medical_units.id")),
)


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(255), nullable=False)
    birthdate = Column(Date, nullable=False)
    crm = Column(Integer, nullable=False)
    speciality_id = Column(Integer, ForeignKey(Speciality.id), nullable=False)
    medical_units = relationship(
        "MedicalUnit", secondary=doctor_medical_unit, back_populates="doctors"
    )

    speciality: relationship = relationship(Speciality)

    def to_dict(self, populate=True):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "birthdate": self.birthdate,
            "crm": self.crm,
            "speciality_id": self.speciality_id,
            "speciality": self.speciality.to_dict(),
            "medical_units": [
                medical_unit.to_dict(populate=False) if populate else medical_unit.id
                for medical_unit in self.medical_units
            ],
        }
