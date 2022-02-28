from typing import List

from domain.entities.speciality import ISpeciality
from domain.use_cases.factories.find_specialities_factory import FindSpecialitiesFactory


class SpecialityController:
    def find(self) -> List[ISpeciality]:
        find_specialities_use_case = FindSpecialitiesFactory()
        return find_specialities_use_case.execute()
