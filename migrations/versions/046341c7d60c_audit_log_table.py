"""audit log table

Revision ID: 046341c7d60c
Revises: d606f6df2880
Create Date: 2021-09-21 09:24:12.107197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046341c7d60c'
down_revision = 'd606f6df2880'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audit_log',
    sa.Column('id', sa.String(), autoincrement=False, nullable=False),
    sa.Column('action', sa.String(), nullable=True),
    sa.Column('object_id', sa.String(), nullable=True),
    sa.Column('object_name', sa.String(), nullable=True),
    sa.Column('object_type', sa.String(), nullable=True),
    sa.Column('done_by', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('audit_log')
    # ### end Alembic commands ###