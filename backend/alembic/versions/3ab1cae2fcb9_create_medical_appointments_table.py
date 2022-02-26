"""create medical appointments table

Revision ID: 3ab1cae2fcb9
Revises: 40775d39ecf3
Create Date: 2022-02-26 20:08:50.363868

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision = "3ab1cae2fcb9"
down_revision = "40775d39ecf3"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "medical_appointments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column("patient_id", sa.Integer, ForeignKey("patients.id"), nullable=False),
        sa.Column("problem_id", sa.Integer, ForeignKey("problems.id"), nullable=False),
        sa.Column(
            "employee_id", sa.Integer, ForeignKey("employees.id"), nullable=False
        ),
    )


def downgrade():
    op.drop_table("medical_appointments")
