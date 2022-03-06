from typing import List
from domain.entities.plan import IPlan
from domain.repositories.plan_repository import IPlanRepository


class FindPlans:
    def __init__(self, plan_repository: IPlanRepository):
        self.plan_repository = plan_repository

    def execute(self) -> List[IPlan]:
        return self.plan_repository.find()
