from domain.repositories.problem_repository import IProblemRepository
from infra.repositories.problem_repository import ProblemRepository
from config.extensions import db_session


def ProblemRepositoryFactory() -> IProblemRepository:
    return ProblemRepository(db_session)
