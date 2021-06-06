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
        sa.Column('name', sa.String(100), nullable=False, unique=True),
        sa.Column('url', sa.String(200), nullable=True),
        sa.Column('access_type', sa.Boolean, nullable=True),
        sa.Column('size', sa.String(50), nullable=True),
        sa.Column('stars', sa.String(100), nullable=True),
        sa.Column('watchers', sa.Integer, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
    )


def downgrade():
    op.drop_table('repository')
