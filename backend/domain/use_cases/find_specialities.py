from typing import List
from domain.entities.speciality import ISpeciality
from domain.repositories.speciality_repository import ISpecialityRepository


class FindSpecialities:
    def __init__(self, speciality_repository: ISpecialityRepository):
        self.speciality_repository = speciality_repository

    def execute(self) -> List[ISpeciality]:
        return self.speciality_repository.find()
