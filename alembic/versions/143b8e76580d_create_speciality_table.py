"""create speciality table

Revision ID: 143b8e76580d
Revises: 3ab1cae2fcb9
Create Date: 2022-02-28 11:05:55.986850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "143b8e76580d"
down_revision = "3ab1cae2fcb9"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "specialities",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("description", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table("specialities")
