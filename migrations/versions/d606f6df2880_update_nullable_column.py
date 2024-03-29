"""update nullable column

Revision ID: d606f6df2880
Revises: 918070daea7e
Create Date: 2021-09-07 15:18:47.952733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd606f6df2880'
down_revision = '918070daea7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recipe', 'user_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('recipe', 'chef_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recipe', 'chef_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('recipe', 'user_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
