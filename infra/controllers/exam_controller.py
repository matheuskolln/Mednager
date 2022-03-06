from datetime import date
from typing import Optional
from domain.entities.exam import IExam
from domain.use_cases.factories.create_exam_factory import CreateExamFactory
from infra.repositories.factories.exam_repository_factory import ExamRepositoryFactory


class ExamController:
    def create(
        self,
        date: date,
        employee_id: int,
        previous_medical_appointment_id: int,
        patient_id: int,
        doctor_id: int,
    ) -> Optional[IExam]:
        create_exam_use_case = CreateExamFactory()
        exam = create_exam_use_case.execute(
            date=date,
            employee_id=employee_id,
            previous_medical_appointment_id=previous_medical_appointment_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
        )
        return exam

    def find(self) -> list:
        exam_repository = ExamRepositoryFactory()
        return exam_repository.find()
