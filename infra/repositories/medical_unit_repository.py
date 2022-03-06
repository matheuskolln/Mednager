from typing import List
from sqlalchemy.orm.session import Session
from domain.entities.medical_unit import IMedicalUnit
from domain.repositories.medical_unit_repository import IMedicalUnitRepository
from infra.entities.medical_unit import MedicalUnit


class MedicalUnitRepository(IMedicalUnitRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def find(self) -> List[IMedicalUnit]:
        return self.session.query(MedicalUnit).all()
