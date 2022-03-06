from datetime import date
from domain.entities.employee import IEmployee

from domain.use_cases.factories.create_employee_factory import CreateEmployeeFactory


class EmployeeController:
    def create(
        self, fullname: str, birthdate: date, email: str, password: str
    ) -> IEmployee:
        use_case = CreateEmployeeFactory()
        employee = use_case.execute(fullname, birthdate, email, password)
        return employee
