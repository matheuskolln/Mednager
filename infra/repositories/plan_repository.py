from typing import List
from domain.entities.plan import IPlan
from domain.repositories.plan_repository import IPlanRepository
from sqlalchemy.orm.session import Session

from infra.entities.plan import Plan


class PlanRepository(IPlanRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def find(self) -> List[IPlan]:
        plans = self.session.query(Plan).all()
        return plans
