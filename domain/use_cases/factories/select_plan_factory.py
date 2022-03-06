from domain.use_cases.select_plan import SelectPlan
from infra.repositories.factories.patient_repository_factory import (
    PatientRepositoryFactory,
)
from infra.repositories.factories.plan_repository_factory import PlanRepositoryFactory


def SelectPlanFactory() -> SelectPlan:
    patient_repository = PatientRepositoryFactory()
    plan_repository = PlanRepositoryFactory()
    return SelectPlan(patient_repository, plan_repository)
