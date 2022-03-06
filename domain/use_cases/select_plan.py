from domain.entities.patient import IPatient
from domain.repositories.patient_repository import IPatientRepository
from domain.repositories.plan_repository import IPlanRepository


class SelectPlan:
    def __init__(
        self, patient_repository: IPatientRepository, plan_repository: IPlanRepository
    ):
        self.patient_repository = patient_repository
        self.plan_repository = plan_repository

    def execute(self, patient_id: int, plan_id: int) -> IPatient:
        if not self.plan_exists(plan_id):
            raise Exception("Plan not found")

        patient = self.patient_repository.find_by_id(patient_id)
        if not patient:
            raise Exception("Patient not found")

        patient_with_plan = self.patient_repository.add_plan_to(patient_id, plan_id)

        return patient_with_plan

    def plan_exists(self, plan_id: int) -> bool:
        plans = self.plan_repository.find()
        for plan in plans:
            if plan.id == plan_id:
                return True
        return False
