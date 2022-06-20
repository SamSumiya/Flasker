"""create user table

Revision ID: 84ef3e6d4d77
Revises: 
Create Date: 2022-06-20 08:51:29.052682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84ef3e6d4d77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False), 
                    sa.Column('email', sa.String(), nullable=False), 
                    sa.Column('created_at', sa.DateTime, nullable=True)
                    )


def downgrade() -> None:
    op.drop_table('users')
