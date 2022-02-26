from abc import ABC, abstractmethod

from domain.entities.problem import IProblem


class IProblemRepository(ABC):
    @abstractmethod
    def create(self, patient_id: int, description: str) -> IProblem:
        pass
