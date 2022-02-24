from abc import ABC, abstractmethod
from typing import List

from domain.entities.plan import IPlan


class IPlanRepository(ABC):
    @abstractmethod
    def find(self) -> List[IPlan]:
        pass
