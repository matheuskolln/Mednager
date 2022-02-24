from datetime import date
from domain.entities.employee import IEmployee
from domain.repositories.employee_repository import IEmployeeRepository


class CreateEmployee:
    def __init__(self, employee_repository: IEmployeeRepository):
        self.employee_repository = employee_repository

    def execute(
        self, fullname: str, birthdate: date, email: str, password: str
    ) -> IEmployee:
        employee_created = self.employee_repository.create(
            fullname, birthdate, email, password
        )
        return employee_created
