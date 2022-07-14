"""events table

Revision ID: 9d009cb8aff0
Revises: 
Create Date: 2022-07-14 18:49:29.321767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d009cb8aff0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('value', sa.String(length=120), nullable=True),
    sa.Column('event', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_timestamp'), 'event', ['timestamp'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_timestamp'), table_name='event')
    op.drop_table('event')
    # ### end Alembic commands ###
