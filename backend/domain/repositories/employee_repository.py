from abc import ABC, abstractmethod
from datetime import date

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
