from abc import ABC, abstractmethod
from datetime import date

from domain.entities.patient import IPatient
from domain.entities.plan import IPlan


class IPatientRepository(ABC):
    @abstractmethod
    def create(self, fullname: str, birthdate: date, document: int) -> IPatient:
        pass

    @abstractmethod
    def add_plan_to(self, patient: IPatient, plan: IPlan) -> IPatient:
        pass
