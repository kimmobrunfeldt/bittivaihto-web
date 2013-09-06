"""Add `user`, `role` and `user_role` tables.

Revision ID: 3d40eb986e12
Revises: None
Create Date: 2013-09-06 18:21:32.870843

"""

# revision identifiers, used by Alembic.
revision = '3d40eb986e12'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=True),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('password', sa.String(length=255), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('confirmed_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_table(
        'user_role',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'role_id')
    )


def downgrade():
    op.drop_table('user_role')
    op.drop_table('user')
    op.drop_table('role')
