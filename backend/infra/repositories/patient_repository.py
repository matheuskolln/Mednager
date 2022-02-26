from datetime import date
from domain.entities.patient import IPatient
from domain.entities.plan import IPlan
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

    def add_plan_to(self, patient: IPatient, plan: IPlan) -> IPatient:
        patient.plan = plan
        self.session.commit()
        return patient
