"""add plan_id on patients

Revision ID: 018b28b7193a
Revises: 1971389a662c
Create Date: 2022-02-26 01:13:14.640975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "018b28b7193a"
down_revision = "1971389a662c"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "patients",
        sa.Column("plan_id", sa.Integer, sa.ForeignKey("plans.id"), nullable=True),
    )


def downgrade():
    op.drop_column("patients", "plan_id")
