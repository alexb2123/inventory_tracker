"""empty message

Revision ID: 0231d3e61d29
Revises: c6499a8424d5
Create Date: 2022-09-03 17:34:59.934687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0231d3e61d29'
down_revision = 'c6499a8424d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_sequence')
    op.add_column('Inventory', sa.Column('AmazonAsin', sa.String(length=100), nullable=True))
    op.add_column('Inventory', sa.Column('RetailerAsin', sa.String(length=100), nullable=True))
    op.add_column('Inventory', sa.Column('price_min', sa.Float(), nullable=True))
    op.add_column('Inventory', sa.Column('price_max', sa.Float(), nullable=True))
    op.alter_column('Inventory', 'ID',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('Inventory', 'ItemName',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_column('Inventory', 'AmazonASIN')
    op.drop_column('Inventory', 'RetailerASIN')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Inventory', sa.Column('RetailerASIN', sa.TEXT(), nullable=True))
    op.add_column('Inventory', sa.Column('AmazonASIN', sa.TEXT(), nullable=True))
    op.alter_column('Inventory', 'ItemName',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Inventory', 'ID',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_column('Inventory', 'price_max')
    op.drop_column('Inventory', 'price_min')
    op.drop_column('Inventory', 'RetailerAsin')
    op.drop_column('Inventory', 'AmazonAsin')
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    # ### end Alembic commands ###
