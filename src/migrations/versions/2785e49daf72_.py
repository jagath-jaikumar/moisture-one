"""

Revision ID: 2785e49daf72
Revises: 8b45460766cc
Create Date: 2024-06-12 10:08:33.783395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2785e49daf72'
down_revision: Union[str, None] = '8b45460766cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_key', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('fleetship', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('plant', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('sensor', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('sensor_reading', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    op.drop_column('sensor_reading', 'created_at')
    op.drop_column('sensor', 'created_at')
    op.drop_column('plant', 'created_at')
    op.drop_column('fleetship', 'created_at')
    op.drop_column('api_key', 'created_at')
    # ### end Alembic commands ###
