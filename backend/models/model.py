from sqlalchemy import Float, DateTime, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey

from backend.models.db.connections import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, unique=True)
    password_id = Column(ForeignKey("passwords.id"))
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Passwords(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True)
    hashed_password = Column(String, nullable=False)


class Quizz_results(Base):
    __tablename__ = "quizz_results"

    id = Column(Integer, primary_key=True)
    user_score = Column(Float, default=0, nullable=False)
    max_score = Column(Float, default=0, nullable=False)
    finished_at = Column(DateTime(timezone=True), server_default=func.now())
    user = Column(String)


class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(Text, nullable=False)
    quizz_id = Column(ForeignKey("quizzes.id"))

class Quizzes(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    is_active = Column(Boolean)


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)


class Answers(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    answer_text = Column(Text, nullable=False)
    question_id = Column(ForeignKey("questions.id"))
    is_correct = Column(Boolean)


class Question_categories(Base):
    __tablename__ = "question_categories"

    id = Column(Integer, primary_key=True)
    question_id = Column(ForeignKey("questions.id"))
    category_id = Column(ForeignKey("categories.id"))