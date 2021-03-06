"""poems table

Revision ID: a3b825827cd5
Revises: 
Create Date: 2020-02-03 13:38:44.242645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3b825827cd5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poem_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('root', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_poem_data_author'), 'poem_data', ['author'], unique=False)
    op.create_index(op.f('ix_poem_data_title'), 'poem_data', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_poem_data_title'), table_name='poem_data')
    op.drop_index(op.f('ix_poem_data_author'), table_name='poem_data')
    op.drop_table('poem_data')
    # ### end Alembic commands ###
