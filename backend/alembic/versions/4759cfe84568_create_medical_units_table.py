"""create medical_units table

Revision ID: 4759cfe84568
Revises: 018b28b7193a
Create Date: 2022-02-26 01:42:26.705834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4759cfe84568"
down_revision = "018b28b7193a"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "medical_units",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("address", sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table("medical_units")
