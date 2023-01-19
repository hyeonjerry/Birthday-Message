"""empty message

Revision ID: 7c9b27fecacd
Revises: 
Create Date: 2023-01-19 22:51:25.879111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c9b27fecacd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('birthday',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('bdate', sa.Date(), nullable=False),
    sa.Column('introduce', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_birthday_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_birthday'))
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('birthday_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['birthday_id'], ['birthday.id'], name=op.f('fk_message_birthday_id_birthday')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_message'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('birthday')
    op.drop_table('user')
    # ### end Alembic commands ###
