"""add content

Revision ID: e99e0dbe1b9c
Revises: 4c14677f39e9
Create Date: 2025-10-01 12:31:56.027789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e99e0dbe1b9c'
down_revision: Union[str, Sequence[str], None] = '4c14677f39e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('Content',sa.String(),nullable=False))

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
