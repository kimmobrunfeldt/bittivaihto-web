"""Add unique constraint `layer_added_by_id_round_id_key` to `layer` table.

Revision ID: 6ed330a299
Revises: 54190942dc21
Create Date: 2013-09-07 11:43:05.532779

"""

# revision identifiers, used by Alembic.
revision = '6ed330a299'
down_revision = '54190942dc21'

from alembic import op


def upgrade():
    op.execute(
        "ALTER TABLE layer ADD CONSTRAINT layer_added_by_id_round_id_key "
        "UNIQUE (added_by_id, round_id)"
    )


def downgrade():
    op.execute(
        "ALTER TABLE layer DROP CONSTRAINT layer_added_by_id_round_id_key"
    )
