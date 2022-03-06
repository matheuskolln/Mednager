from domain.use_cases.find_plans import FindPlans
from infra.repositories.factories.plan_repository_factory import PlanRepositoryFactory


def FindPlansFactory() -> FindPlans:
    plans_repository = PlanRepositoryFactory()
    return FindPlans(plans_repository)
