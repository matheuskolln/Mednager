from domain.entities.patient import IPatient
from domain.entities.plan import IPlan
from domain.repositories.patient_repository import IPatientRepository


class SelectPlan:
    def __init__(self, patient_repository: IPatientRepository):
        self.patient_repository = patient_repository

    def execute(self, plan: IPlan, patient: IPatient) -> IPatient:
        patient = self.patient_repository.add_plan_to(patient, plan)
        return patient
