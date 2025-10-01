"""add user table

Revision ID: 5ab3b16c42e9
Revises: e99e0dbe1b9c
Create Date: 2025-10-01 12:43:44.074237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ab3b16c42e9'
down_revision: Union[str, Sequence[str], None] = 'e99e0dbe1b9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
