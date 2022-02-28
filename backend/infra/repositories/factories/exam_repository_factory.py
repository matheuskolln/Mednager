from domain.repositories.exam_repository import IExamRepository
from infra.repositories.exam_repository import ExamRepository
from config.extensions import db_session


def ExamRepositoryFactory() -> IExamRepository:
    return ExamRepository(db_session)
