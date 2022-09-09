from http.client import HTTPException
from fastapi import APIRouter, Depends
from typing import List, Optional
from backend.models.admin_schemas import SetAnswersBody, SetAnswerDB
from backend.models.model import Answers
from backend.models.admin_models_dals import AnswersDAL
from backend.models.db.connections import get_db
from databases import Database


answer_router = APIRouter()

@answer_router.post("/answer", response_model=SetAnswerDB)
async def create_answer(payload: SetAnswersBody, session: Database = Depends(get_db)):
    #answers_dal = AnswersDAL(session)
    answers_id = await AnswersDAL.create_answer(payload)
    
    response_obj = {
        "id": answers_id,
        "answer_text": payload.answer_text,
        "question_id": payload.question_id,
        "is_correct": payload.is_correct,
    }
    return response_obj

@answer_router.get("/answer", response_model=SetAnswerDB)
async def get_all_answers(session: Database = Depends(get_db)):
    #answers_dal = AnswersDAL(session)
    answers = await AnswersDAL.get_all_answers()
    if not answers:
        raise HTTPException(status_code=404, detail="No answers was found")
    return answers

@answer_router.put("/answer/{id}", response_model=SetAnswerDB)
async def update_answer(id: int, payload: SetAnswersBody, session: Database = Depends(get_db)):
    #answers_dal = AnswersDAL(session)
    answers_id =  await AnswersDAL.update_answer(id, payload)
    
    response_obj = {
        "id": answers_id,
        "answer_text": payload.answer_text,
        "question_id": payload.question_id,
        "is_correct": payload.is_correct,
    }
    return response_obj

@answer_router.delete("/answer/{id}")
async def delete_answer(id: int, session: Database = Depends(get_db)):
    #answers_dal = AnswersDAL(session)
    return await AnswersDAL.delete_answer(id)