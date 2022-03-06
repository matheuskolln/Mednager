from datetime import date
from domain.entities.exam import IExam
from infra.entities.exam import Exam
from domain.repositories.exam_repository import IExamRepository
from sqlalchemy.orm.session import Session


class ExamRepository(IExamRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        date: date,
        employee_id: int,
        previous_medical_appointment_id: int,
        patient_id: int,
        doctor_id: int,
    ) -> IExam:
        exam = Exam(
            date=date,
            employee_id=employee_id,
            previous_medical_appointment_id=previous_medical_appointment_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
        )
        self.session.add(exam)
        self.session.commit()
        return exam

    def find(self) -> list:
        return self.session.query(Exam).all()
