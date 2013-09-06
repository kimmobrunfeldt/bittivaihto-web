"""Add column `winner_layer_id` to `round` table.

Revision ID: 4e8f532c1a26
Revises: 54190942dc21
Create Date: 2013-09-07 00:56:16.843112

"""

# revision identifiers, used by Alembic.
revision = '4e8f532c1a26'
down_revision = '54190942dc21'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'round',
        sa.Column('winner_layer_id', sa.Integer(), nullable=True)
    )


def downgrade():
    op.drop_column('round', 'winner_layer_id')
