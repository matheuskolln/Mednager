from domain.entities.patient import IPatient
from domain.entities.problem import IProblem
from domain.repositories.patient_repository import IPatientRepository
from domain.repositories.problem_repository import IProblemRepository


class CreateProblem:
    def __init__(
        self,
        problem_repository: IProblemRepository,
        patient_repository: IPatientRepository,
    ) -> None:
        self.problem_repository = problem_repository
        self.patient_repository = patient_repository

    def execute(self, patient_id: int, description: str) -> IProblem:
        patient = self.patient_repository.find_by_id(patient_id)
        if not patient:
            raise Exception("Patient not found")

        problem_created = self.problem_repository.create(patient_id, description)
        return problem_created
