"""create_home

Revision ID: ea778f58a013
Revises: 
Create Date: 2022-01-20 10:44:35.481918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea778f58a013'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'house',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('street', sa.String(250)),
        sa.Column('number', sa.Integer())
    )


def downgrade():
    op.drop_table('house')
