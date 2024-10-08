"""Rename table to question_answer

Revision ID: c4ede7c8dc0c
Revises: a0dd87391957
Create Date: 2024-10-08 17:22:57.690502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = 'c4ede7c8dc0c'
down_revision: Union[str, None] = 'a0dd87391957'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
 
    op.create_table('question_answer',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('question', sa.String(), nullable=False),
        sa.Column('answer', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    
    op.drop_table('chatdb')


def downgrade() -> None:

    op.create_table('chatdb',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('question', sa.String(), nullable=False),
        sa.Column('answer', sa.String(), nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id', name='chatdb_pkey')
    )
    
    
    op.drop_table('question_answer')
