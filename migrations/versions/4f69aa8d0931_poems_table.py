"""poems table

Revision ID: 4f69aa8d0931
Revises: b6dff5751433
Create Date: 2020-02-05 01:34:09.222909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f69aa8d0931'
down_revision = 'b6dff5751433'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poem', sa.Column('numWords', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poem', 'numWords')
    # ### end Alembic commands ###
