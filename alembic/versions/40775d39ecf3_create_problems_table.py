"""create problems table

Revision ID: 40775d39ecf3
Revises: 4759cfe84568
Create Date: 2022-02-26 02:03:53.333890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "40775d39ecf3"
down_revision = "4759cfe84568"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "problems",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.String(500), nullable=False),
        sa.Column(
            "patient_id", sa.Integer, sa.ForeignKey("patients.id"), nullable=False
        ),
    )


def downgrade():
    op.drop_table("problems")
