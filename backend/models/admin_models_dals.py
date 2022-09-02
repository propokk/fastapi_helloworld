from typing import List, Optional

import sqlalchemy as sa
from databases import Database

from models.model import *
from models.admin_schemas import (
    SetQuizzesBody, 
    SetQuestionsBody, 
    SetAnswersBody, 
    SetCategoriesBody,
    SetQuestionCategoriesBody)



class QuizzesDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_quizz(self, title: str, description: str, is_active: bool):
         
        new_quizz = sa.insert(Quizzes).values(title=title, description=description, is_active=is_active)

        await self.db_session.fetch_one(query=new_quizz)
        

    async def get_all_quizzes(self) -> List[Quizzes]:

        query = sa.select([Quizzes])
        
        return [SetQuizzesBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def update_quizz(self, quizz_id: int, title: Optional[str], description: Optional[str]):
        q = sa.update(Quizzes).where(Quizzes.id == quizz_id)
        
        if title:
            q = q.values(title=title)
        if description:
            q = q.values(description=description)
        
        await self.db_session.fetch_one(query=q)

    async def delete_quizz(self, quiz_id: int, title: Optional[str], description: Optional[str]):
        delete_quiz = sa.delete(Quizzes).where(Quizzes.id == quiz_id)

        await self.db_session.fetch_one(query=delete_quiz)



class QuestionsDAL():

    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_question(self, question_text: str, quizz_id: int):
         
        new_question = sa.insert(Questions).values(question_text=question_text, quizz_id=quizz_id)

        await self.db_session.fetch_one(query=new_question)
        

    async def get_all_questions(self) -> List[Questions]:

        query = sa.select([Questions])
        
        return [SetQuestionsBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def update_question(self, question_id: int, question_text: Optional[str], quizz_id: Optional[int]):
        q = sa.update(Questions).where(Questions.id == question_id)
        
        if question_text:
            q = q.values(question_text=question_text)
        if quizz_id:
            q = q.values(quizz_id=quizz_id)
        
        await self.db_session.fetch_one(query=q)

    async def delete_question(self, question_id: int, question_text: Optional[str], quizz_id: Optional[int]):
        delete_question = sa.delete(Questions).where(Questions.id == question_id)

        await self.db_session.fetch_one(query=delete_question)



class AnswersDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_answer(self, answer_text: str, question_id: int, is_correct: bool):
         
        new_answer = sa.insert(Answers).values(answer_text=answer_text, question_id=question_id, is_correct=is_correct)

        await self.db_session.fetch_one(query=new_answer)
        

    async def get_all_answers(self) -> List[Answers]:

        query = sa.select([Answers])
        
        return [SetAnswersBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def update_answer(self, answer_id: int, answer_text: Optional[str], question_id: Optional[int], is_correct: Optional[bool]):
        q = sa.update(Answers).where(Answers.id == answer_id)
        
        if answer_text:
            q = q.values(answer_text=answer_text)
        if question_id:
            q = q.values(question_id=question_id)
        if is_correct:
            q = q.values(is_correct=is_correct)
        
        await self.db_session.fetch_one(query=q)

    async def delete_answer(self, answer_id: int, answer_text: Optional[str], question_id: Optional[int], is_correct: Optional[bool]):
        delete_answer = sa.delete(Answers).where(Answers.id == answer_id)

        await self.db_session.fetch_one(query=delete_answer)


 
class CategoriesDAL():
    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_category(self, name: str, description: str):
         
        new_category = sa.insert(Categories).values(name=name, description=description)

        await self.db_session.fetch_one(query=new_category)
        

    async def get_all_categories(self) -> List[Categories]:

        query = sa.select([Categories])
        
        return [SetCategoriesBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def update_category(self, category_id: int, name: Optional[str], description: Optional[str]):
        q = sa.update(Categories).where(Categories.id == category_id)
        
        if name:
            q = q.values(name=name)
        if description:
            q = q.values(description=description)
        
        await self.db_session.fetch_one(query=q)

    async def delete_category(self, category_id: int, name: Optional[str], description: Optional[str]):
        delete_category = sa.delete(Categories).where(Categories.id == category_id)

        await self.db_session.fetch_one(query=delete_category)   



class QuestionCategoriesDAL():

    def __init__(self, db_session: Database):
        self.db_session = db_session

    async def create_question_category(self, question_id: int, category_id: int):
         
        new_question_category = sa.insert(Question_categories).values(question_id=question_id, category_id=category_id)

        await self.db_session.fetch_one(query=new_question_category)
        

    async def get_all_question_categories(self) -> List[Question_categories]:

        query = sa.select([Question_categories])
        
        return [SetQuestionCategoriesBody(**data) for data in await self.db_session.fetch_all(query=query)]

    async def update_question_category(self, question_category_id: int, question_id: Optional[int], category_id: Optional[int]):
        q = sa.update(Question_categories).where(Question_categories.id == question_category_id)
        
        if question_id:
            q = q.values(question_id=question_id)
        if category_id:
            q = q.values(category_id=category_id)
        
        await self.db_session.fetch_one(query=q)

    async def delete_question_category(self, question_category_id: int, question_id: Optional[int], category_id: Optional[int]):
        delete_question_category = sa.delete(Question_categories).where(Question_categories.id == question_category_id)

        await self.db_session.fetch_one(query=delete_question_category)   