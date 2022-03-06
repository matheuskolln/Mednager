from datetime import date
from domain.entities.patient import IPatient
from domain.entities.plan import IPlan
from domain.use_cases.factories.create_patient_factory import CreatePatientFactory
from domain.use_cases.factories.select_plan_factory import SelectPlanFactory


class PatientController:
    def create(self, fullname: str, birthdate: date, document: int) -> IPatient:
        create_patient_use_case = CreatePatientFactory()
        patient = create_patient_use_case.execute(fullname, birthdate, document)
        return patient

    def add_plan_to(self, patient_id: int, plan_id: int) -> IPatient:
        select_plan_use_case = SelectPlanFactory()
        patient = select_plan_use_case.execute(
            patient_id,
            plan_id,
        )
        return patient
