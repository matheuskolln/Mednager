"""create doctor_medical_unit table

Revision ID: 8bf157162217
Revises: 5e94b2076a15
Create Date: 2022-03-06 14:51:08.503209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8bf157162217"
down_revision = "5e94b2076a15"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "doctor_medical_unit",
        sa.Column("doctor_id", sa.Integer, sa.ForeignKey("doctors.id")),
        sa.Column("medical_unit_id", sa.Integer, sa.ForeignKey("medical_units.id")),
    )


def downgrade():
    op.drop_table("doctor_medical_unit")
