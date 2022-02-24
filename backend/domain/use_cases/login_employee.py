from domain.entities.employee import IEmployee
from domain.repositories.employee_repository import IEmployeeRepository


class LoginEmployee:
    def __init__(self, employee_repository: IEmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self, email: str, password: str) -> IEmployee:
        employee = self.employee_repository.find_by(email)
        if employee.password == password:
            return employee
        else:
            raise ValueError("Invalid email or password")
