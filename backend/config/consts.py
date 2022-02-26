from domain.entities.medical_unit import IMedicalUnit
from domain.entities.plan import IPlan


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
