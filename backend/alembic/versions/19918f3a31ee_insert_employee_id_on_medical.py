"""insert employee id on medical

Revision ID: 19918f3a31ee
Revises: 8bf157162217
Create Date: 2022-03-06 15:00:32.504298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "19918f3a31ee"
down_revision = "8bf157162217"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "medical_units",
        sa.Column(
            "employee_id", sa.Integer, sa.ForeignKey("employees.id"), nullable=False
        ),
    )


def downgrade():
    op.drop_column("medical_units", "employee_id")
