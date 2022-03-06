from typing import Optional
from sqlalchemy.orm.session import Session
from domain.entities.problem import IProblem
from domain.repositories.problem_repository import IProblemRepository
from infra.entities.problem import Problem


class ProblemRepository(IProblemRepository):
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, patient_id: int, description: str) -> IProblem:
        problem = Problem(patient_id=patient_id, description=description)
        self.session.add(problem)
        self.session.commit()
        return problem

    def find_by_id(self, problem_id: int) -> Optional[IProblem]:
        patient = self.session.query(Problem).filter(Problem.id == problem_id).first()
        return patient
