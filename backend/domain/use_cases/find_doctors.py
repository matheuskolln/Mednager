from typing import List
from domain.entities.doctor import IDoctor
from domain.repositories.doctor_repository import IDoctorRepository


class FindDoctors:
    def __init__(self, doctor_repository: IDoctorRepository):
        self.doctor_repository = doctor_repository

    def execute(self) -> List[IDoctor]:
        return self.doctor_repository.find()
