"""Create a baseline migrations

Revision ID: 0a3ff7409731
Revises: da86c529c3ae
Create Date: 2024-06-11 23:25:53.941930

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0a3ff7409731"
down_revision: Union[str, None] = "da86c529c3ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "monitor",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "plant",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("species_name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("image", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "sensor",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    op.drop_table("sensor")
    op.drop_table("plant")
    op.drop_table("monitor")
    # ### end Alembic commands ###
