from typing import List
from domain.entities.medical_unit import IMedicalUnit
from domain.use_cases.factories.find_medical_units_factory import (
    FindMedicalUnitsFactory,
)


class MedicalUnitController:
    def find(self) -> List[IMedicalUnit]:
        find_medical_units_use_case = FindMedicalUnitsFactory()
        return find_medical_units_use_case.execute()
