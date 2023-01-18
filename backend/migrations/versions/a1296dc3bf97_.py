"""empty message

Revision ID: a1296dc3bf97
Revises: 35a086878af8
Create Date: 2023-01-18 18:02:45.450183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1296dc3bf97'
down_revision = '35a086878af8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')

    # ### end Alembic commands ###
