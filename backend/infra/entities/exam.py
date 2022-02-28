from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship
from config.extensions import Base
from infra.entities.employee import Employee
from infra.entities.medical_appointment import MedicalAppointment
from infra.entities.patient import Patient
from infra.entities.doctor import Doctor


class Exam(Base):
    __tablename__ = "exams"

    id = Column("id", Integer, primary_key=True)
    date = Column("date", Date, nullable=False)
    employee_id = Column(
        "employee_id", Integer, ForeignKey(Employee.id), nullable=False
    )
    previous_medical_appointment_id = Column(
        "previous_medical_appointment_id",
        Integer,
        ForeignKey(MedicalAppointment.id),
        nullable=False,
    )
    patient_id = Column("patient_id", Integer, ForeignKey(Patient.id), nullable=False)
    doctor_id = Column("doctor_id", Integer, ForeignKey(Doctor.id), nullable=False)

    employee: relationship = relationship(Employee)
    previous_medical_appointment: relationship = relationship(MedicalAppointment)
    patient: relationship = relationship(Patient)
    doctor: relationship = relationship(Doctor)

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "employee_id": self.employee_id,
            "employee": self.employee.to_dict(),
            "previous_medical_appointment_id": self.previous_medical_appointment_id,
            "previous_medical_appointment": self.previous_medical_appointment.to_dict(),
            "patient_id": self.patient_id,
            "patient": self.patient.to_dict(),
            "doctor_id": self.doctor_id,
            "doctor": self.doctor.to_dict(),
        }
