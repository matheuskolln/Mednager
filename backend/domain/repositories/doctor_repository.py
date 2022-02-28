from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.doctor import IDoctor


class IDoctorRepository(ABC):
    @abstractmethod
    def find(self) -> List[IDoctor]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[IDoctor]:
        pass
