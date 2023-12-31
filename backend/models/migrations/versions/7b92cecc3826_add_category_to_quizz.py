"""Add category to quizz

Revision ID: 7b92cecc3826
Revises: d51df09b38e0
Create Date: 2022-09-20 15:00:55.553766

"""
from alembic import op
import sqlalchemy as sa
from db.connections import Base
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b92cecc3826'
down_revision = 'd51df09b38e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('test_question_categories')
    # op.drop_table('test_questions')
    # op.drop_table('test_quizzes')
    # op.drop_table('test_answers')
    # op.drop_table('test_quizz_results')
    # op.drop_table('test_categories')
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_categories',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('test_categories_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_categories_pkey'),
    sa.UniqueConstraint('name', name='test_categories_name_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('test_quizz_results',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_score', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('max_score', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('finished_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('user', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_quizz_results_pkey')
    )
    op.create_table('test_answers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('answer_text', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('question_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_correct', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], name='test_answers_question_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='test_answers_pkey')
    )
    op.create_table('test_quizzes',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('test_quizzes_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_quizzes_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('test_questions',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('test_questions_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('question_text', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('quizz_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['quizz_id'], ['test_quizzes.id'], name='test_questions_quizz_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='test_questions_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('test_question_categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['test_categories.id'], name='test_question_categories_category_id_fkey'),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], name='test_question_categories_question_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='test_question_categories_pkey')
    )
    # ### end Alembic commands ###
