"""empty message

Revision ID: 547ae59353cf
Revises: 
Create Date: 2019-02-14 13:03:25.131307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '547ae59353cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tweet', sa.String(length=140), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###