"""create plans table

Revision ID: 1971389a662c
Revises: 2a2e9b76f2f7
Create Date: 2022-02-26 00:26:35.192407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1971389a662c"
down_revision = "2a2e9b76f2f7"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "plans",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("description", sa.String(255), nullable=False),
        sa.Column("price", sa.Float, nullable=False),
    )


def downgrade():
    op.drop_table("plans")
