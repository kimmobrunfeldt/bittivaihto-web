"""Add `round` and `layer` tables.

Revision ID: 54190942dc21
Revises: ceaffb36cd4
Create Date: 2013-09-07 00:18:23.146233

"""

# revision identifiers, used by Alembic.
revision = '54190942dc21'
down_revision = 'ceaffb36cd4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'round',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'layer',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('added_by_id', sa.Integer(), nullable=False),
        sa.Column('round_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('image', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ['added_by_id'],
            ['user.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['round_id'],
            ['round.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('round')
    op.drop_table('layer')
