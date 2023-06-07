"""added tips and schedules tables

Revision ID: 9c4f265e1047
Revises: b7c5c5974fc4
Create Date: 2023-06-07 13:29:37.722234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c4f265e1047'
down_revision = 'b7c5c5974fc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('event_type', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.Column('arrival_time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('tipout_amount', sa.Integer(), nullable=True),
    sa.Column('check_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('events', sa.Column('type', sa.String(), nullable=True))
    op.drop_column('events', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_column('events', 'type')
    op.drop_table('tips')
    op.drop_table('schedules')
    # ### end Alembic commands ###
