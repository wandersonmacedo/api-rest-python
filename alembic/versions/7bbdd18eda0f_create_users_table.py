"""create users table

Revision ID: 7bbdd18eda0f
Revises: 
Create Date: 2021-06-04 23:01:31.634212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bbdd18eda0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.INTEGER, primary_key=True),
        sa.Column('username', sa.String(100), nullable=False)
    )


def downgrade():
    op.drop_table('users')
