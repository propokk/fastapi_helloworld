from fastapi import APIRouter, Depends
from typing import List, Optional
from models.model import Answers
from models.admin_models_dals import AnswersDAL
from models.db.connections import get_db
from databases import Database


answer_router = APIRouter()

@answer_router.post("/answer")
async def create_answer(answer_text: str, question_id: int, is_correct: bool, session: Database = Depends(get_db)):
    answers_dal = AnswersDAL(session)
    return await answers_dal.create_answer(answer_text, question_id, is_correct)

@answer_router.get("/answer")
async def get_all_answers(session: Database = Depends(get_db)) -> List[Answers]:
    answers_dal = AnswersDAL(session)
    return await answers_dal.get_all_answers()

@answer_router.put("/answer/{answer_id}")
async def update_answer(answer_id: int, answer_text: Optional[str], question_id: Optional[int], is_correct: Optional[bool], session: Database = Depends(get_db)):
    answers_dal = AnswersDAL(session)
    return await answers_dal.update_answer(answer_id, answer_text, question_id, is_correct)

@answer_router.delete("/answer/{answer_id}")
async def delete_answer(answer_id: int, answer_text: Optional[str], question_id: Optional[int], is_correct: Optional[bool], session: Database = Depends(get_db)):
    answers_dal = AnswersDAL(session)
    return await answers_dal.delete_answer(answer_id, answer_text, question_id, is_correct)