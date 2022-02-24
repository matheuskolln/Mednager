from domain.entities.patient import IPatient
from domain.entities.problem import IProblem
from domain.repositories.problem_repository import IProblemRepository


class CreateProblem:
    def __init__(self, problem_repository: IProblemRepository):
        self.problem_repository = problem_repository

    def execute(self, patient: IPatient, description: str) -> IProblem:
        problem_created = self.problem_repository.create(patient, description)
        return problem_created
