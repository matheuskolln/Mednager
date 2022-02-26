from typing import List
from domain.entities.plan import IPlan
from domain.use_cases.factories.find_plans_factory import FindPlansFactory


class PlanController:
    def find(self) -> List[IPlan]:
        find_plans_use_case = FindPlansFactory()
        plans = find_plans_use_case.execute()
        return plans
