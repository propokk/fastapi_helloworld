from typing import List

import sqlalchemy as sa
from sqlalchemy import and_
from databases import Database
from redis import Redis

from backend.models.model import *
from backend.models.user_schemas import *

class UserQuizzDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def get_all_quizzes_for_user(self):

        query = sa.select([Quizzes])
        #[SetQuizzesBody(**data) for data in await self.db_session.fetch_all(query=query)]
        return await self.db_session.fetch_all(query=query)

    async def get_all_categories_for_user(self) -> List[Categories]:

        query = sa.select([Categories])
        #[SetCategoriesBody(**data) for data in await self.db_session.fetch_all(query=query)]
        return await self.db_session.fetch_all(query=query)

    async def get_questions_for_user(self, payload: SetChooseQuestionBody) -> List[Questions]:

        j = sa.join(Questions, Question_categories,
                Questions.id == Question_categories.question_id)
        
        query = sa.select([Questions]).select_from(j).where(and_(Questions.quizz_id == payload.quizz_id, Question_categories.category_id==payload.category_id))
        
        
        return [SetQuestionsBody(**data) for data in await self.db_session.fetch_all(query=query)]
    

