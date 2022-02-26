from domain.entities.problem import IProblem
from domain.use_cases.factories.create_problem_factory import CreateProblemFactory


class ProblemController:
    def create(self, patient_id: int, description: str) -> IProblem:
        create_problem_use_case = CreateProblemFactory()
        problem = create_problem_use_case.execute(patient_id, description)
        return problem
