from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

from domain.entities.employee import IEmployee


class IEmployeeRepository(ABC):
    @abstractmethod
    def create(
        self, fullname: str, birthdate: date, email: str, password: str
    ) -> IEmployee:
        pass

    @abstractmethod
    def find_by(self, email: str) -> IEmployee:
        pass

    @abstractmethod
    def find_by_id(self, employee_id) -> Optional[IEmployee]:
        pass
