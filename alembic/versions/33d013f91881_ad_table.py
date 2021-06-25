"""ad_table

Revision ID: 33d013f91881
Revises: 691de0eac04b
Create Date: 2021-06-25 16:26:02.262176

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33d013f91881'
down_revision = '691de0eac04b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ad',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(64), index=True, unique=True, nullable=False),
        sa.Column('description', sa.Text, index=True),
        sa.Column('creator_id', sa.Integer(), sa.ForeignKey('user.id')),
        sa.Column('created_on', sa.DateTime(), default=datetime.utcnow)
    )


def downgrade():
    op.drop_table('advertisement')
