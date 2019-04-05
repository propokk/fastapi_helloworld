from http.client import HTTPException
from fastapi import APIRouter, Depends
from typing import List, Optional
from backend.models.admin_schemas import SetQuestionsBody, SetQuestionDB
from backend.models.model import Questions
from backend.models.admin_models_dals import QuestionsDAL
from backend.models.db.connections import get_db
from databases import Database


questions_router = APIRouter()

@questions_router.post("/question", response_model=SetQuestionDB)
async def create_question(payload: SetQuestionsBody, session: Database = Depends(get_db)):
    #question_dal = QuestionsDAL(session)
    question_id =  await QuestionsDAL.create_question(payload)

    response_obj = {
        "id": question_id,
        "question_text": payload.question_text,
        "quizz_id": payload.quizz_id,
    }
    return response_obj

@questions_router.get("/question", response_model=SetQuestionDB)
async def get_all_questions(session: Database = Depends(get_db)):
    #question_dal = QuestionsDAL(session)
    questions = await QuestionsDAL.get_all_questions()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions was found")
    return questions

@questions_router.put("/question/{id}", response_model=SetQuestionDB)
async def update_question(id: int, payload: SetQuestionsBody, session: Database = Depends(get_db)):
    #question_dal = QuestionsDAL(session)
    question_id = await QuestionsDAL.update_question(id, payload)

    response_obj = {
        "id": question_id,
        "question_text": payload.question_text,
        "quizz_id": payload.quizz_id,
    }

    return response_obj

@questions_router.delete("/question/{id}")
async def delete_question(id: int, session: Database = Depends(get_db)):
    #question_dal = QuestionsDAL(session)
    return await QuestionsDAL.delete_question(id)