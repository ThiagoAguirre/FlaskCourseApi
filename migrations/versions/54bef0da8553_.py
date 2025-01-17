"""empty message

Revision ID: 54bef0da8553
Revises: 391b63321784
Create Date: 2024-04-25 17:46:29.230988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54bef0da8553'
down_revision = '391b63321784'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('formation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('formation')
    # ### end Alembic commands ###
