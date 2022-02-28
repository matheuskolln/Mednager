from config.consts import DEFAULT_MEDICAL_UNITS, DEFAULT_PLANS, DEFAULT_SPECIALITIES
from infra.entities.medical_unit import MedicalUnit
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
            db_session.add(MedicalUnit(**medical_unit.dict()))
    db_session.commit()


def populate_specialities(db_session) -> None:
    for speciality in DEFAULT_SPECIALITIES:
        possible_existing_speciality = (
            db_session.query(Speciality).filter_by(name=speciality.name).first()
        )
        if not possible_existing_speciality:
            db_session.add(Speciality(**speciality.dict()))
    db_session.commit()


def populate(db_session) -> None:
    populate_plans(db_session)
    populate_medical_units(db_session)
    populate_specialities(db_session)
