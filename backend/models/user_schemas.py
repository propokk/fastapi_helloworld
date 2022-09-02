from pydantic import BaseModel

class SetQuizzesBody(BaseModel):
    id: int
    title: str
    description: str
    is_active: bool

class SetCategoriesBody(BaseModel):
    id: int
    name: str
    description: str

class SetQuestionsBody(BaseModel):
    id: int
    question_text: str

class SetAnswerBody(BaseModel):
    answer_text: str
    is_correct: bool

class SetResponseBody(SetAnswerBody):
    sub: str
