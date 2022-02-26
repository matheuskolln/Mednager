"""create patients table

Revision ID: 2a2e9b76f2f7
Revises: bf160a54cf14
Create Date: 2022-02-26 00:25:33.392498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2a2e9b76f2f7"
down_revision = "bf160a54cf14"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "patients",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("fullname", sa.String(100), nullable=False),
        sa.Column("birthdate", sa.Date, nullable=False),
        sa.Column("document", sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table("patients")
