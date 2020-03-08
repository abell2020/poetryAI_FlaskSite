"""empty message

Revision ID: b8896e508db0
Revises: 4f69aa8d0931
Create Date: 2020-02-10 17:19:31.652502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8896e508db0'
down_revision = '4f69aa8d0931'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poem', sa.Column('seed', sa.String(), nullable=True))
    op.drop_column('poem', 'root')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poem', sa.Column('root', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('poem', 'seed')
    # ### end Alembic commands ###
