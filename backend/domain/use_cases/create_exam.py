from datetime import date
from domain.entities.doctor import IDoctor
from domain.entities.employee import IEmployee
from domain.entities.exam import IExam
from domain.entities.medical_appointment import IMedicalAppointment
from domain.entities.patient import IPatient
from domain.repositories.exam_repository import IExamRepository


class CreateExam:
    def __init__(self, exam_repository: IExamRepository):
        self.exam_repository = exam_repository

    def execute(
        self,
        date: date,
        employee: IEmployee,
        previous_medical_appointment: IMedicalAppointment,
        patient: IPatient,
        doctor: IDoctor,
    ) -> IExam:
        exam_created = self.exam_repository.create(
            date, employee, previous_medical_appointment, patient, doctor
        )
        return exam_created
