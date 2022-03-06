from typing import List
from domain.repositories.speciality_repository import ISpecialityRepository
from sqlalchemy.orm import Session

from infra.entities.speciality import Speciality
from domain.entities.speciality import ISpeciality


class SpecialityRepository(ISpecialityRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def find(self) -> List[ISpeciality]:
        return self.session.query(Speciality).all()
