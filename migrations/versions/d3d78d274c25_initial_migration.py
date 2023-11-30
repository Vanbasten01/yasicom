"""initial migration

Revision ID: d3d78d274c25
Revises: 
Create Date: 2023-11-23 00:35:55.891587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3d78d274c25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('cover', sa.String(length=255), nullable=False),
    sa.Column('photo1', sa.String(length=255), nullable=False),
    sa.Column('photo2', sa.String(length=255), nullable=False),
    sa.Column('photo3', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
