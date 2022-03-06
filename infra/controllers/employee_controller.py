from datetime import date
from typing import List
from domain.entities.employee import IEmployee
from domain.repositories.employee_repository import IEmployeeRepository

from domain.use_cases.factories.create_employee_factory import CreateEmployeeFactory
from infra.repositories.factories.employee_repository_factory import (
    EmployeeRepositoryFactory,
)


class EmployeeController:
    employee_repository: IEmployeeRepository

    def __init__(self) -> None:
        self.employee_repository = EmployeeRepositoryFactory()

    def create(
        self, fullname: str, birthdate: date, email: str, password: str
    ) -> IEmployee:
        use_case = CreateEmployeeFactory()
        employee = use_case.execute(fullname, birthdate, email, password)
        return employee

    def find(self) -> List[IEmployee]:
        return self.employee_repository.find()
