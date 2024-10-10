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

def upgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'question_answer' not in inspector.get_table_names():
        op.create_table(
            'question_answer',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('question', sa.String, nullable=False),
            sa.Column('answer', sa.String, nullable=False),
        )

def downgrade():
    op.drop_table('question_answer')
