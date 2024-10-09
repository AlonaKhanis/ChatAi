"""Create chatdb table

Revision ID: a0dd87391957
Revises: 
Create Date: 2024-10-08 16:28:19.060675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a0dd87391957'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table('chatdb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:

    op.drop_table('chatdb')

