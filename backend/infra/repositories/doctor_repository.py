from typing import List
from sqlalchemy.orm import Session
from domain.entities.doctor import IDoctor
from domain.repositories.doctor_repository import IDoctorRepository
from infra.entities.doctor import Doctor


class DoctorRepository(IDoctorRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def find(self) -> List[IDoctor]:
        return self.session.query(Doctor).all()
