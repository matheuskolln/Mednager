from datetime import date
from typing import List, Optional
from domain.entities.employee import IEmployee
from domain.repositories.employee_repository import IEmployeeRepository
from sqlalchemy.orm.session import Session

from infra.entities.employee import Employee


class EmployeeRepository(IEmployeeRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self, fullname: str, birthdate: date, email: str, password: str
    ) -> IEmployee:
        employee = Employee(
            fullname=fullname, birthdate=birthdate, email=email, password=password
        )
        self.session.add(employee)
        self.session.commit()
        return employee

    def find_by(self, email: str) -> IEmployee:
        return self.session.query(Employee).filter(Employee.email == email).first()

    def find_by_id(self, employee_id) -> Optional[IEmployee]:
        return self.session.query(Employee).filter(Employee.id == employee_id).first()

    def find(self) -> List[IEmployee]:
        return self.session.query(Employee).all()
