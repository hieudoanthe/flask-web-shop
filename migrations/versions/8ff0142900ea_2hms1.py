"""2HMS1

Revision ID: 8ff0142900ea
Revises: 6849d5af4e5f
Create Date: 2024-03-14 00:20:01.842366

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8ff0142900ea'
down_revision = '6849d5af4e5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('warehouse', schema=None) as batch_op:
        batch_op.alter_column('product_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('warehouse', schema=None) as batch_op:
        batch_op.alter_column('product_id',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
