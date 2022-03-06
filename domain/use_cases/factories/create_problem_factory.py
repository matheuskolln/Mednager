from domain.use_cases.create_problem import CreateProblem
from infra.repositories.factories.patient_repository_factory import (
    PatientRepositoryFactory,
)
from infra.repositories.factories.problem_repository_factory import (
    ProblemRepositoryFactory,
)


def CreateProblemFactory() -> CreateProblem:
    problem_repository = ProblemRepositoryFactory()
    patient_reporsitory = PatientRepositoryFactory()
    return CreateProblem(problem_repository, patient_reporsitory)
