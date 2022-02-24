from abc import ABC, abstractmethod

from domain.entities.problem import IProblem
from domain.entities.patient import IPatient


class IProblemRepository(ABC):
    @abstractmethod
    def create(self, patient: IPatient, description: str) -> IProblem:
        pass
