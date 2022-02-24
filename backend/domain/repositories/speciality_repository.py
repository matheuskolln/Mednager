from abc import ABC, abstractmethod
from typing import List

from domain.entities.speciality import ISpeciality


class ISpecialityRepository(ABC):
    @abstractmethod
    def find(self) -> List[ISpeciality]:
        pass
