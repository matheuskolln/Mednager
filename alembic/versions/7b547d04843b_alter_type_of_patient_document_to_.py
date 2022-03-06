"""alter type of patient document to string4

Revision ID: 7b547d04843b
Revises: 19918f3a31ee
Create Date: 2022-03-06 20:03:28.753118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7b547d04843b"
down_revision = "19918f3a31ee"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("patients", "document", type_=sa.String(11))


def downgrade():
    op.drop_column("patients", "document")
