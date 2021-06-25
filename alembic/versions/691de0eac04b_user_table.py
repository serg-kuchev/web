"""user_table

Revision ID: 691de0eac04b
Revises: 
Create Date: 2021-06-25 16:25:52.456517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '691de0eac04b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(64), index=True, unique=True, nullable=False),
        sa.Column('email', sa.String(120), index=True, unique=True),
        sa.Column('password', sa.String(128)),
    )


def downgrade():
    op.drop_table('user')
