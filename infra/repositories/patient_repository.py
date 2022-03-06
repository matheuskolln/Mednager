from datetime import date
from typing import Optional
from domain.entities.patient import IPatient
from domain.repositories.patient_repository import IPatientRepository
from sqlalchemy.orm.session import Session

from infra.entities.patient import Patient


class PatientRepository(IPatientRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, fullname: str, birthdate: date, document: int) -> IPatient:
        patient = Patient(fullname=fullname, birthdate=birthdate, document=document)
        self.session.add(patient)
        self.session.commit()
        return patient

    def add_plan_to(self, patient_id: int, plan_id: int) -> IPatient:
        patient = self.session.query(Patient).filter(Patient.id == patient_id).one()

        patient.plan_id = plan_id
        self.session.commit()

        return patient

    def find_by_id(self, patient_id: int) -> Optional[IPatient]:
        patient = (
            self.session.query(Patient).filter(Patient.id == patient_id).one_or_none()
        )
        return patient
