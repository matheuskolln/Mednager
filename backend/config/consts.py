from domain.entities.medical_unit import IMedicalUnit
from domain.entities.plan import IPlan
from domain.entities.speciality import ISpeciality

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
