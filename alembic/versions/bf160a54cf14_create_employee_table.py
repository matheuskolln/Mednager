"""create employee table

Revision ID: bf160a54cf14
Revises:
Create Date: 2022-02-25 11:44:35.706946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bf160a54cf14"
down_revision = None
branch_labels = None
depends_on = None

MAX_CHAR_FOR_PASSWORD = 24


def upgrade():
    op.create_table(
        "employees",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("fullname", sa.String(100), nullable=False),
        sa.Column("birthdate", sa.Date, nullable=False),
        sa.Column("email", sa.String(100), nullable=False),
        sa.Column("password", sa.String(MAX_CHAR_FOR_PASSWORD), nullable=False),
    )


def downgrade():
    op.drop_table("employees")
