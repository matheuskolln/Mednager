from datetime import date
from domain.entities.patient import IPatient
from domain.repositories.patient_repository import IPatientRepository


class CreatePatient:
    def __init__(self, patient_repository: IPatientRepository):
        self.patient_repository = patient_repository

    def execute(self, fullname: str, birthdate: date, document: str) -> IPatient:
        patient_created = self.patient_repository.create(fullname, birthdate, document)
        return patient_created
