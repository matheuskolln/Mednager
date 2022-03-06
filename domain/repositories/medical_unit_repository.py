from abc import ABC, abstractmethod
from typing import List

from domain.entities.medical_unit import IMedicalUnit


class IMedicalUnitRepository(ABC):
    @abstractmethod
    def find(self) -> List[IMedicalUnit]:
        pass
