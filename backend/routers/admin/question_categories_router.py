from http.client import HTTPException
from fastapi import APIRouter, Depends
from typing import List, Optional
from backend.models.admin_schemas import SetQuestionCategoriesBody, SetQuestionCategoryDB
from backend.models.admin_models_dals import QuestionCategoriesDAL
from backend.models.db.connections import get_db
from databases import Database


question_category_router = APIRouter()

@question_category_router.post("/question_category", response_model= SetQuestionCategoryDB)
async def create_question_category(payload: SetQuestionCategoriesBody, session: Database = Depends(get_db)):
    #question_category_dal = QuestionCategoriesDAL(session)
    question_category_id = await QuestionCategoriesDAL.create_question_category(payload)
    
    response_obj = {
        "id": question_category_id,
        "question_id": payload.question_id,
        "category_id": payload.category_id,
    }
    return response_obj

@question_category_router.get("/question_category", response_model= SetQuestionCategoryDB)
async def get_all_question_categories(session: Database = Depends(get_db)):
    #question_category_dal = QuestionCategoriesDAL(session)
    question_category = await QuestionCategoriesDAL.get_all_question_categories()
    if not question_category:
        raise HTTPException(status_code=404, detail="No question categories was found")
    return question_category

@question_category_router.put("/question_category/{id}", response_model= SetQuestionCategoryDB)
async def update_question_category(id: int, payload: SetQuestionCategoriesBody, session: Database = Depends(get_db)):
    #question_category_dal = QuestionCategoriesDAL(session)
    question_category_id = await QuestionCategoriesDAL.update_question_category(id, payload)

    response_obj = {
        "id": question_category_id,
        "question_id": payload.question_id,
        "category_id": payload.category_id,
    }
    return response_obj

@question_category_router.delete("/question_category/{id}")
async def delete_question_category(id: int, session: Database = Depends(get_db)):
    #question_category_dal = QuestionCategoriesDAL(session)
    return await QuestionCategoriesDAL.delete_question_category(id)