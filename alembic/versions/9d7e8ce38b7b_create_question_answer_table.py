"""create question_answer table

Revision ID: 9d7e8ce38b7b
Revises: c4ede7c8dc0c
Create Date: 2024-10-09 13:38:08.064574

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '9d7e8ce38b7b'
down_revision: Union[str, None] = 'c4ede7c8dc0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'question_answer',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('question', sa.String(length=255), nullable=False),
        sa.Column('answer', sa.String(length=255), nullable=False),
        
    )

def downgrade() -> None:
    op.drop_table('question_answer')
