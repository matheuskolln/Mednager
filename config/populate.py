from config.consts import (
    DEFAULT_DOCTORS,
    DEFAULT_EMPLOYEES,
    DEFAULT_MEDICAL_UNITS,
    DEFAULT_PATIENTS,
    DEFAULT_PLANS,
    DEFAULT_SPECIALITIES,
)
from infra.entities.doctor import Doctor
from infra.entities.employee import Employee
from infra.entities.medical_unit import MedicalUnit
from infra.entities.patient import Patient
from infra.entities.plan import Plan
from infra.entities.speciality import Speciality


def populate_plans(db_session) -> None:
    for plan in DEFAULT_PLANS:
        possible_existing_plan = (
            db_session.query(Plan).filter_by(name=plan.name).first()
        )
        if not possible_existing_plan:
            db_session.add(Plan(**plan.dict()))
    db_session.commit()


def populate_medical_units(db_session) -> None:
    for medical_unit in DEFAULT_MEDICAL_UNITS:
        possible_existing_medical_unit = (
            db_session.query(MedicalUnit).filter_by(name=medical_unit.name).first()
        )
        if not possible_existing_medical_unit:
            doctors_name = [doctor.fullname for doctor in medical_unit.doctors]
            doctors = (
                db_session.query(Doctor).filter(Doctor.fullname.in_(doctors_name)).all()
            )
            db_session.add(
                MedicalUnit(
                    name=medical_unit.name,
                    address=medical_unit.address,
                    employee_id=medical_unit.employee_id,
                    doctors=doctors,
                )
            )
    db_session.commit()


def populate_specialities(db_session) -> None:
    for speciality in DEFAULT_SPECIALITIES:
        possible_existing_speciality = (
            db_session.query(Speciality).filter_by(name=speciality.name).first()
        )
        if not possible_existing_speciality:
            db_session.add(Speciality(**speciality.dict()))
    db_session.commit()


def populate_doctors(db_session) -> None:
    for doctor in DEFAULT_DOCTORS:
        possible_existing_doctor = (
            db_session.query(Doctor).filter_by(fullname=doctor.fullname).first()
        )
        if not possible_existing_doctor:
            db_session.add(Doctor(**doctor.dict()))
    db_session.commit()


def populate_employees(db_session) -> None:
    for employee in DEFAULT_EMPLOYEES:
        possible_existing_employee = (
            db_session.query(Employee).filter_by(fullname=employee.fullname).first()
        )
        if not possible_existing_employee:
            db_session.add(Employee(**employee.dict()))
    db_session.commit()


def populate_patients(db_session) -> None:
    for patient in DEFAULT_PATIENTS:
        possible_existing_patient = (
            db_session.query(Patient).filter_by(fullname=patient.fullname).first()
        )
        if not possible_existing_patient:
            db_session.add(Patient(**patient.dict()))
    db_session.commit()


def populate(db_session) -> None:

    populate_specialities(db_session)
    populate_doctors(db_session)
    populate_employees(db_session)
    populate_plans(db_session)
    populate_medical_units(db_session)
    populate_patients(db_session)
