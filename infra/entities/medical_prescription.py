from sqlalchemy import Column, Date, ForeignKey, Integer, String
from infra.entities.doctor import Doctor
from infra.entities.patient import Patient
from sqlalchemy.orm import relationship
from config.extensions import Base


class MedicalPrescription(Base):
    __tablename__ = "medical_prescriptions"

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)
    doctor_id = Column(Integer, ForeignKey(Doctor.id), nullable=False)
    patient: relationship = relationship(Patient)
    doctor: relationship = relationship(Doctor)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "date": self.date,
            "patient_id": self.patient_id,
            "patient": self.patient.to_dict(),
            "doctor_id": self.doctor_id,
            "doctor": self.doctor.to_dict(),
        }
