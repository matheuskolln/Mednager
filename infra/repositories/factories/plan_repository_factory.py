from domain.repositories.plan_repository import IPlanRepository
from infra.repositories.plan_repository import PlanRepository
from config.extensions import db_session


def PlanRepositoryFactory() -> IPlanRepository:
    return PlanRepository(db_session)
