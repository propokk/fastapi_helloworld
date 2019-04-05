from typing import List, Optional

import sqlalchemy as sa
from databases import Database


from backend.models.model import *
from backend.models.admin_schemas import (
    SetQuizzDB,
    SetQuizzesBody, 
    SetQuestionsBody, 
    SetAnswersBody, 
    SetCategoriesBody,
    SetQuestionCategoriesBody)



class QuizzesDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_quizz(self, payload: SetQuizzesBody):
         
        new_quizz = sa.insert(Quizzes).values(title=payload.title, description=payload.description, is_active=payload.is_active)

        return await self.db_session.fetch_one(query=new_quizz)
        

    async def get_all_quizzes(self):

        query = sa.select([Quizzes])
        # [SetQuizzDB(**data) for data in await self.db_session.fetch_all(query=query)]
        return await self.db_session.fetch_all(query=query)

    async def update_quizz(self, id: int, payload: SetQuizzesBody):
        q = sa.update(Quizzes).where(Quizzes.id == id)
        
        if payload.title:
            q = q.values(title=payload.title)
        if payload.description:
            q = q.values(description=payload.description)
        
        return await self.db_session.fetch_one(query=q)

    async def delete_quizz(self, id: int):
        delete_quiz = sa.delete(Quizzes).where(Quizzes.id == id)

        await self.db_session.fetch_one(query=delete_quiz)



class QuestionsDAL():

    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_question(self, payload: SetQuestionsBody):

        new_question = sa.insert(Questions).values(question_text=payload.question_text, quizz_id=payload.quizz_id)

        return await self.db_session.fetch_one(query=new_question)
        

    async def get_all_questions(self):

        query = sa.select([Questions])
        # [SetQuestionsBody(**data) for data in await self.db_session.fetch_all(query=query)]
        return await self.db_session.fetch_all(query=query)

    async def update_question(self, id: int, payload: SetQuestionsBody):
        q = sa.update(Questions).where(Questions.id == payload.question_id)
        
        if payload.question_text:
            q = q.values(question_text=payload.question_text)
        if payload.quizz_id:
            q = q.values(quizz_id=payload.quizz_id)
        
        return await self.db_session.fetch_one(query=q)

    async def delete_question(self, id: int):
        delete_question = sa.delete(Questions).where(Questions.id == id)

        await self.db_session.fetch_one(query=delete_question)

 
class CategoriesDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_category(self, payload: SetCategoriesBody):
         
        new_category = sa.insert(Categories).values(name=payload.name, description=payload.description)

        return await self.db_session.fetch_one(query=new_category)
        

    async def get_all_categories(self) -> List[Categories]:

        query = sa.select([Categories])
        #[SetCategoriesBody(**data) for data in await self.db_session.fetch_all(query=query)]
        return await self.db_session.fetch_all(query=query)

    async def update_category(self, id: int, payload: SetCategoriesBody):
        q = sa.update(Categories).where(Categories.id == id)
        
        if payload.name:
            q = q.values(name=payload.name)
        if payload.description:
            q = q.values(description=payload.description)
        
        return await self.db_session.fetch_one(query=q)

    async def delete_category(self, id: int):
        delete_category = sa.delete(Categories).where(Categories.id == id)

        await self.db_session.fetch_one(query=delete_category)   


class QuestionCategoriesDAL():

    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_question_category(self, payload: SetQuestionCategoriesBody):
         
        new_question_category = sa.insert(Question_categories).values(question_id=payload.question_id, category_id=payload.category_id)

        return await self.db_session.fetch_one(query=new_question_category)
        

    async def get_all_question_categories(self) -> List[Question_categories]:

        query = sa.select([Question_categories])
        #[SetQuestionCategoriesBody(**data) for data in await self.db_session.fetch_all(query=query)]
        return await self.db_session.fetch_all(query=query)

    async def update_question_category(self, id: int, payload: SetQuestionCategoriesBody):
        q = sa.update(Question_categories).where(Question_categories.id == id)
        
        if payload.question_id:
            q = q.values(question_id=payload.question_id)
        if payload.category_id:
            q = q.values(category_id=payload.category_id)
        
        return await self.db_session.fetch_one(query=q)

    async def delete_question_category(self, id: int):
        delete_question_category = sa.delete(Question_categories).where(Question_categories.id == id)

        await self.db_session.fetch_one(query=delete_question_category) 



class AnswersDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_answer(self, payload: SetAnswersBody):
         
        new_answer = sa.insert(Answers).values(answer_text=payload.answer_text, question_id=payload.question_id, is_correct=payload.is_correct)

        return await self.db_session.fetch_one(query=new_answer)
        

    async def get_all_answers(self):

        query = sa.select([Answers])
        #[SetAnswersBody(**data) for data in await self.db_session.fetch_all(query=query)]
        return await self.db_session.fetch_all(query=query)

    async def update_answer(self, id: int, payload: SetAnswersBody):
        q = sa.update(Answers).where(Answers.id == id)
        
        if payload.answer_text:
            q = q.values(answer_text=payload.answer_text)
        if payload.question_id:
            q = q.values(question_id=payload.question_id)
        if payload.is_correct:
            q = q.values(is_correct=payload.is_correct)
        
        return await self.db_session.fetch_one(query=q)

    async def delete_answer(self, id: int):
        delete_answer = sa.delete(Answers).where(Answers.id == id)

        await self.db_session.fetch_one(query=delete_answer)

