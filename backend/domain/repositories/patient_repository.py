from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

from domain.entities.patient import IPatient
from domain.entities.plan import IPlan


class IPatientRepository(ABC):
    @abstractmethod
    def create(self, fullname: str, birthdate: date, document: int) -> IPatient:
        pass

    @abstractmethod
    def add_plan_to(self, patient_id: int, plan_id: int) -> IPatient:
        pass

    @abstractmethod
    def find_by_id(self, patient_id: int) -> Optional[IPatient]:
        pass
