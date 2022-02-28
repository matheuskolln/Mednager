from datetime import date
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

DEFAULT_MEDICAL_UNITS = [
    IMedicalUnit(
        name="Medical Unit - UFSC",
        address="Araranguá, SC, Brazil",
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
