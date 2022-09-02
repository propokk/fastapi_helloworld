from fastapi import APIRouter, Depends
from typing import List, Optional
from models.model import Question_categories
from models.admin_models_dals import QuestionCategoriesDAL
from models.db.connections import get_db
from databases import Database


question_category_router = APIRouter()

@question_category_router.post("/question_category")
async def create_question__category(question_id: int, category_id: int, session: Database = Depends(get_db)):
    question_category_dal = QuestionCategoriesDAL(session)
    return await question_category_dal.create_question_category(question_id, category_id)

@question_category_router.get("/question_category")
async def get_all_question_categories(session: Database = Depends(get_db)) -> List[QuestionCategoriesDAL]:
    question_category_dal = QuestionCategoriesDAL(session)
    return await question_category_dal.get_all_question_categories()

@question_category_router.put("/question_category/{question_category_id}")
async def update_question_category(question_category_id: int, question_id: Optional[int], category_id: Optional[int], session: Database = Depends(get_db)):
    question_category_dal = QuestionCategoriesDAL(session)
    return await question_category_dal.update_question_category(question_category_id, question_id, category_id)

@question_category_router.delete("/question_category/{question_category_id}")
async def delete_question_category(question_category_id: int, question_id: Optional[int], category_id: Optional[int], session: Database = Depends(get_db)):
    question_category_dal = QuestionCategoriesDAL(session)
    return await question_category_dal.delete_question_category(question_category_id, question_id, category_id)