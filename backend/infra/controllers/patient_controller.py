from datetime import date
from domain.entities.patient import IPatient
from domain.use_cases.factories.create_patient_factory import CreatePatientFactory


class PatientController:
    def create(self, fullname: str, birthdate: date, document: int) -> IPatient:
        create_patient_use_case = CreatePatientFactory()
        patient = create_patient_use_case.execute(fullname, birthdate, document)
        return patient
