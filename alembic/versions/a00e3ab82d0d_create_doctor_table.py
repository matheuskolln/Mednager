"""create doctor  table

Revision ID: a00e3ab82d0d
Revises: 143b8e76580d
Create Date: 2022-02-28 11:25:33.840816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a00e3ab82d0d"
down_revision = "143b8e76580d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "doctors",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("fullname", sa.String(255), nullable=False),
        sa.Column("birthdate", sa.Date, nullable=False),
        sa.Column("crm", sa.Integer, nullable=False),
        sa.Column(
            "speciality_id",
            sa.Integer,
            sa.ForeignKey("specialities.id"),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("doctors")
