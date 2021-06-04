"""create repository table

Revision ID: 07a671e63b63
Revises: 7bbdd18eda0f
Create Date: 2021-06-04 23:01:47.242104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07a671e63b63'
down_revision = '7bbdd18eda0f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'repository',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
    )


def downgrade():
    op.drop_table('repository')
