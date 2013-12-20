"""change currency units to Decimal

Revision ID: 1134da570f7d
Revises: 2632c41af74e
Create Date: 2013-12-20 23:47:31.435892

"""

# revision identifiers, used by Alembic.
revision = '1134da570f7d'
down_revision = '2632c41af74e'

from alembic import op
import sqlalchemy as sa



def upgrade():
    op.alter_column('sell_order', 'sell_amount', type_=sa.Numeric)
    op.alter_column('sell_order', 'minimum_price', type_=sa.Numeric)


def downgrade():
    op.alter_column('sell_order', 'sell_amount', type_=sa.Integer)
    op.alter_column('sell_order', 'minimum_price', type_=sa.Integer)
