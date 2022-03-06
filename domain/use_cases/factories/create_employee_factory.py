from domain.use_cases.create_employee import CreateEmployee
from infra.repositories.factories.employee_repository_factory import (
    EmployeeRepositoryFactory,
)


def CreateEmployeeFactory() -> CreateEmployee:
    employee_repository = EmployeeRepositoryFactory()
    return CreateEmployee(employee_repository)
