from typing import List

from domain.entities.doctor import IDoctor
from domain.use_cases.factories.find_doctors_factory import FindDoctorsFactory


class DoctorController:
    def find(self) -> List[IDoctor]:
        find_doctors_use_case = FindDoctorsFactory()

        return find_doctors_use_case.execute()
