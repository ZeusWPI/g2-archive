"""empty message

Revision ID: 56a55eab991b
Revises: 1d565be91098
Create Date: 2018-02-23 15:56:54.346446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56a55eab991b'
down_revision = '1d565be91098'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.add_column('project', sa.Column('stop_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'stop_time')
    op.drop_column('project', 'start_time')
    # ### end Alembic commands ###
