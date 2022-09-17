from pydantic import BaseModel
	

class SetQuizzesBody(BaseModel):
	title: str
	description: str
	is_active: bool

class SetQuizzDB(SetQuizzesBody):
	id: int

class SetQuestionsBody(BaseModel):
	question_text: str
	quizz_id: int

class SetQuestionDB(SetQuestionsBody):
	id: int

class SetQuestionCategoriesBody(BaseModel):
	question_id: int
	category_id: int

class SetQuestionCategoryDB(SetQuestionCategoriesBody):
	id: int


class SetCategoriesBody(BaseModel):
	name: str
	description: str

class SetCategoryDB(SetCategoriesBody):
	id: int

class SetAnswersBody(BaseModel):
	answer_text: str
	question_id: int
	is_correct: bool

class SetAnswerDB(SetAnswersBody):
	id: int

