"""empty message

Revision ID: c657c8d28692
Revises: a4dac4dcd78c
Create Date: 2023-04-18 19:37:10.973095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c657c8d28692'
down_revision = 'a4dac4dcd78c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('request', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.drop_column('request')

    # ### end Alembic commands ###
