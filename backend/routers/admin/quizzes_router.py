from fastapi import APIRouter, Depends
from typing import List, Optional
from models.model import Quizzes
from models.admin_models_dals import QuizzesDAL
from models.db.connections import get_db
from databases import Database


quizz_router = APIRouter()

@quizz_router.post("/quizz")
async def create_quizz(title: str, description: str, is_active:bool, session: Database = Depends(get_db)):
    quizz_dal = QuizzesDAL(session)
    return await quizz_dal.create_quizz(title, description, is_active)

@quizz_router.get("/quizz")
async def get_all_quizzes(session: Database = Depends(get_db)) -> List[Quizzes]:
    quizz_dal = QuizzesDAL(session)
    return await quizz_dal.get_all_quizzes()

@quizz_router.put("/quizz/{quizz_id}")
async def update_quizz(quizz_id: int, title: Optional[str] = None, description: Optional[str] = None, session: Database = Depends(get_db)):
    quizz_dal = QuizzesDAL(session)
    return await quizz_dal.update_quizz(quizz_id, title, description)

@quizz_router.delete("/quizz/{quizz_id}")
async def delete_quizz(quizz_id: int, title: Optional[str] = None, description: Optional[str] = None, session: Database = Depends(get_db)):
    quizz_dal = QuizzesDAL(session)
    return await quizz_dal.delete_quizz(quizz_id, title, description)