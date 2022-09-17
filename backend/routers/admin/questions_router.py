from fastapi import APIRouter, Depends
from typing import List, Optional
from models.model import Questions
from models.admin_models_dals import QuestionsDAL
from models.db.connections import get_db
from databases import Database


questions_router = APIRouter()

@questions_router.post("/question")
async def create_question(question_text: str, quizz_id: int, session: Database = Depends(get_db)):
    question_dal = QuestionsDAL(session)
    return await question_dal.create_question(question_text, quizz_id)

@questions_router.get("/question")
async def get_all_questions(session: Database = Depends(get_db)) -> List[Questions]:
    question_dal = QuestionsDAL(session)
    return await question_dal.get_all_questions()

@questions_router.put("/question/{question_id}")
async def update_question(question_id: int, question_text: Optional[str] = None, quizz_id: Optional[int] = None, session: Database = Depends(get_db)):
    question_dal = QuestionsDAL(session)
    return await question_dal.update_question(question_id, question_text, quizz_id)

@questions_router.delete("/question/{question_id}")
async def delete_question(question_id: int, question_text: Optional[str] = None, quizz_id: Optional[int] = None, session: Database = Depends(get_db)):
    question_dal = QuestionsDAL(session)
    return await question_dal.delete_question(question_id, question_text, quizz_id)