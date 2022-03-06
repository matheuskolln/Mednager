"""create exam table

Revision ID: f9f9565d9a8e
Revises: a00e3ab82d0d
Create Date: 2022-02-28 12:00:53.167417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f9f9565d9a8e"
down_revision = "a00e3ab82d0d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "exams",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column(
            "employee_id", sa.Integer, sa.ForeignKey("employees.id"), nullable=False
        ),
        sa.Column(
            "previous_medical_appointment_id",
            sa.Integer,
            sa.ForeignKey("medical_appointments.id"),
            nullable=False,
        ),
        sa.Column(
            "patient_id", sa.Integer, sa.ForeignKey("patients.id"), nullable=False
        ),
        sa.Column("doctor_id", sa.Integer, sa.ForeignKey("doctors.id"), nullable=False),
    )


def downgrade():
    op.drop_table("exams")
