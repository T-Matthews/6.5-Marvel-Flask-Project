"""empty message

Revision ID: 5c05c4b77cdf
Revises: 
Create Date: 2022-05-30 17:25:46.025489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c05c4b77cdf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hero', sa.Column('userid', sa.String(length=80), nullable=True))
    op.create_foreign_key(None, 'hero', 'user', ['userid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hero', type_='foreignkey')
    op.drop_column('hero', 'userid')
    # ### end Alembic commands ###
