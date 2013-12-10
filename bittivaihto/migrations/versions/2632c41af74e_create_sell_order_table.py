"""Create `sell_order` table.

Revision ID: 2632c41af74e
Revises: None
Create Date: 2013-12-10 14:19:00.948665

"""

# revision identifiers, used by Alembic.
revision = '2632c41af74e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'sell_order',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column(
            'status',
            sa.Unicode(length=255),
            server_default=u'pending',
            nullable=False
        ),
        sa.Column('ordered_at', sa.DateTime(), nullable=False),
        sa.Column('name', sa.Unicode(length=255), nullable=False),
        sa.Column('email', sa.Unicode(length=255), nullable=False),
        sa.Column('bank_account', sa.Unicode(length=255), nullable=False),
        sa.Column('sell_amount', sa.Integer(), nullable=False),
        sa.Column(
            'currency',
            sa.Unicode(length=10),
            server_default=u'BTC',
            nullable=False
        ),
        sa.Column(
            'deposit_address',
            sa.Unicode(length=255),
            nullable=False
        ),
        sa.Column('minimum_price', sa.Integer(), nullable=True),
        sa.Column('maximum_time', sa.Integer(), nullable=True),
        sa.Column('return_address', sa.Unicode(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('sell_order')
