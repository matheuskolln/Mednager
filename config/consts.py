from datetime import date
from domain.entities.employee import IEmployee
from domain.entities.medical_unit import IMedicalUnit
from domain.entities.plan import IPlan
from domain.entities.speciality import ISpeciality
from domain.entities.doctor import IDoctor

DEFAULT_PLANS = [
    IPlan(
        name="Best Plan Ever",
        description="The best plan ever",
        price=12.34,
    )
]


DEFAULT_SPECIALITIES = [
    ISpeciality(
        name="Speciality - UFSC",
        description="The best speciality ever",
    )
]

DEFAULT_DOCTORS = [
    IDoctor(
        fullname="Doctor - UFSC",
        birthdate=date(2000, 1, 1),
        crm=12345,
        speciality_id=1,
    )
]

DEFAULT_MEDICAL_UNITS = [
    IMedicalUnit(
        name="Medical Unit - UFSC",
        address="Araranguá, SC, Brazil",
        employee_id=1,
        doctors=DEFAULT_DOCTORS,
    )
]

DEFAULT_EMPLOYEES = [
    IEmployee(
        fullname="Employee - UFSC",
        birthdate=date(2000, 1, 1),
        email="employee@ufsc.br",
        password="12345",
    )
]
