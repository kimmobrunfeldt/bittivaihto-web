"""Change column nullability of `role` and `user` tables.

Revision ID: ceaffb36cd4
Revises: 3d40eb986e12
Create Date: 2013-09-06 23:56:20.014680

"""

# revision identifiers, used by Alembic.
revision = 'ceaffb36cd4'
down_revision = '3d40eb986e12'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column(
        u'role',
        'description',
        existing_type=sa.VARCHAR(length=255),
        nullable=False
    )
    op.alter_column(
        u'role',
        'name',
        existing_type=sa.VARCHAR(length=80),
        nullable=False
    )
    op.alter_column(
        u'user',
        'active',
        existing_type=sa.BOOLEAN(),
        nullable=False
    )
    op.alter_column(
        u'user',
        'email',
        existing_type=sa.VARCHAR(length=255),
        nullable=False
    )
    op.alter_column(
        u'user',
        'password',
        existing_type=sa.VARCHAR(length=255),
        nullable=False
    )


def downgrade():
    op.alter_column(
        u'user',
        'password',
        existing_type=sa.VARCHAR(length=255),
        nullable=True
    )
    op.alter_column(
        u'user',
        'email',
        existing_type=sa.VARCHAR(length=255),
        nullable=True
    )
    op.alter_column(
        u'user',
        'active',
        existing_type=sa.BOOLEAN(),
        nullable=True
    )
    op.alter_column(
        u'role',
        'name',
        existing_type=sa.VARCHAR(length=80),
        nullable=True
    )
    op.alter_column(
        u'role',
        'description',
        existing_type=sa.VARCHAR(length=255),
        nullable=True
    )
