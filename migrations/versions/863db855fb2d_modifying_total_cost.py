"""modifying 'total_cost'

Revision ID: 863db855fb2d
Revises: 4a7b25c0d854
Create Date: 2023-11-28 14:44:56.378416

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '863db855fb2d'
down_revision = '4a7b25c0d854'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_cost', sa.DECIMAL(precision=10, scale=2), nullable=False))
        batch_op.add_column(sa.Column('total_cost', sa.DECIMAL(precision=10, scale=2), nullable=False))
        batch_op.drop_column('cost')
        batch_op.drop_column('total')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total', mysql.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('cost', mysql.DECIMAL(precision=10, scale=2), nullable=False))
        batch_op.drop_column('total_cost')
        batch_op.drop_column('product_cost')

    # ### end Alembic commands ###