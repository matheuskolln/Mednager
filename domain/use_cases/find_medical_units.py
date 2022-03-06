from typing import List
from domain.entities.medical_unit import IMedicalUnit
from domain.repositories.medical_unit_repository import IMedicalUnitRepository


class FindMedicalUnits:
    def __init__(self, medical_unit_repository: IMedicalUnitRepository):
        self.medical_unit_repository = medical_unit_repository

    def execute(self) -> List[IMedicalUnit]:
        return self.medical_unit_repository.find()
