from pydantic import BaseModel
from typing import List

class SetQuizzesBody(BaseModel):
    id: int
    title: str
    description: str
    is_active: bool

class SetCategoriesBody(BaseModel):
    id: int
    name: str
    description: str

class SetChooseQuestionBody(BaseModel):
    quizz_id: int
    category_id: int

class SetQuestionsBody(BaseModel):
    id: int
    question_text: str

class Answer(BaseModel):
    question_id: int
    answer_text: str

class SetFinalAnswerBody(BaseModel):
    answers: List[Answer]