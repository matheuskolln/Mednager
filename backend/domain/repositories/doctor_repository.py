from abc import ABC, abstractmethod
from typing import List

from domain.entities.doctor import IDoctor


class IDoctorRepository(ABC):
    @abstractmethod
    def find(self) -> List[IDoctor]:
        pass
