from config.consts import DEFAULT_PLANS
from infra.entities.plan import Plan


def populate_plans(db_session):
    for plan in DEFAULT_PLANS:
        possible_existing_plan = (
            db_session.query(Plan).filter_by(name=plan.name).first()
        )
        if not possible_existing_plan:
            db_session.add(Plan(**plan.dict()))
    db_session.commit()
