from typing import List, Optional

import sqlalchemy as sa
from sqlalchemy import and_
from databases import Database

from models.model import *
from models.user_schemas import *

class UserQuizzDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def get_all_quizzes(self) -> List[Quizzes]:

        query = sa.select([Quizzes])
        
        return [SetQuizzesBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def get_all_categories(self) -> List[Categories]:

        query = sa.select([Categories])
        
        return [SetCategoriesBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def get_questions(self, quizz_id: int, category_id: int) -> List[Questions]:

        j = sa.join(Questions, Question_categories,
                Questions.id == Question_categories.question_id)
        
        query = sa.select([Questions]).select_from(j).where(and_(Questions.quizz_id == quizz_id, Question_categories.category_id==category_id))

        return [SetQuestionsBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def send_answer(self, queston_id: int, answer_text: str):

        query = sa.select([Answers]).where(and_(Answers.question_id == queston_id, Answers.answer_text == answer_text))

        return [SetAnswerBody(**data) for data in await self.db_session.fetch_all(query=query)]