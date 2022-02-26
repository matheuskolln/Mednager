from infra.repositories.employee_repository import EmployeeRepository
from config.extensions import db_session


def EmployeeRepositoryFactory() -> EmployeeRepository:
    return EmployeeRepository(session=db_session)
