from pydantic import BaseModel, Field
from datetime import datetime


class SignUp_Request(BaseModel):
	id: int
	email: str = Field(min_length=1)
	name: str
	password: str = Field(min_length=1)


class User(SignUp_Request):
	id: int
	is_superuser: bool = Field(default_factory=False)
	created_at: datetime = Field(default_factory=datetime.now)


class SignIn_Request(SignUp_Request):
	id: int
	

class SetQuizzesBody(BaseModel):
	title: str
	description: str
	is_active: bool

class SetQuestionsBody(BaseModel):
	question_text: str
	quizz_id: int

class SetAnswersBody(BaseModel):
	answer_text: str
	questin_id: int
	is_correct: bool

class SetCategoriesBody(BaseModel):
	name: str
	description: str

class SetQuestionCategoriesBody(BaseModel):
	question_id: int
	category_id: int

