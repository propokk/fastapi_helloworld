from sqlalchemy import Float, DateTime, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey
from backend.models.db.test_connections import TestBase

class Quizz_results(TestBase):
    __tablename__ = "test_quizz_results"

    id = Column(Integer, primary_key=True)
    user_score = Column(Float, default=0, nullable=False)
    max_score = Column(Float, default=0, nullable=False)
    finished_at = Column(DateTime(timezone=True), server_default=func.now())
    user = Column(String)


class Questions(TestBase):
    __tablename__ = "test_questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(Text, nullable=False)
    quizz_id = Column(ForeignKey("test_quizzes.id"))

class Quizzes(TestBase):
    __tablename__ = "test_quizzes"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    is_active = Column(Boolean)


class Categories(TestBase):
    __tablename__ = "test_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)


class Answers(TestBase):
    __tablename__ = "test_answers"

    id = Column(Integer, primary_key=True)
    answer_text = Column(Text, nullable=False)
    question_id = Column(ForeignKey("test_questions.id"))
    is_correct = Column(Boolean)


class Question_categories(TestBase):
    __tablename__ = "test_question_categories"

    id = Column(Integer, primary_key=True)
    question_id = Column(ForeignKey("test_questions.id"))
    category_id = Column(ForeignKey("test_categories.id"))