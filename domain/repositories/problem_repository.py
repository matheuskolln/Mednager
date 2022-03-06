from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.problem import IProblem


class IProblemRepository(ABC):
    @abstractmethod
    def create(self, patient_id: int, description: str) -> IProblem:
        pass

    @abstractmethod
    def find_by_id(self, problem_id: int) -> Optional[IProblem]:
        pass

    @abstractmethod
    def find(self) -> list:
        pass
