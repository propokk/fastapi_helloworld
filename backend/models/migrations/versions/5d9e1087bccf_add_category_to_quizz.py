"""Add category to quizz

Revision ID: 5d9e1087bccf
Revises: 2c3c4edea2df
Create Date: 2022-09-20 16:31:30.304708

"""
from alembic import op
import sqlalchemy as sa
from db.connections import Base
from sqlalchemy.orm import relationship


# revision identifiers, used by Alembic.
revision = '5d9e1087bccf'
down_revision = '2c3c4edea2df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
