"""create medical prescription table

Revision ID: 5e94b2076a15
Revises: f9f9565d9a8e
Create Date: 2022-02-28 12:21:03.610832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5e94b2076a15"
down_revision = "f9f9565d9a8e"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "medical_prescriptions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column(
            "patient_id", sa.Integer(), sa.ForeignKey("patients.id"), nullable=False
        ),
        sa.Column(
            "doctor_id", sa.Integer(), sa.ForeignKey("doctors.id"), nullable=False
        ),
    )


def downgrade():
    op.drop_table("medical_prescriptions")
