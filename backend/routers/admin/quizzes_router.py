from http.client import HTTPException
from fastapi import APIRouter, Depends
from typing import List, Optional
from backend.models.admin_schemas import SetQuizzesBody, SetQuizzDB
from backend.models.model import Quizzes
from backend.models.admin_models_dals import QuizzesDAL
from backend.models.db.connections import get_db
from databases import Database


quizz_router = APIRouter()

@quizz_router.post("/quizz", response_model=SetQuizzDB)
async def create_quizz(payload: SetQuizzesBody, session: Database = Depends(get_db)):
    #quizz_dal = QuizzesDAL(session)
    quizz_id = await QuizzesDAL.create_quizz(payload)

    response_obj = {
        "id": quizz_id,
        "title": payload.title,
        "description": payload.description,
        "is_active": payload.is_active,
    }

    return response_obj

@quizz_router.get("/quizz", response_model=SetQuizzDB)
async def get_all_quizzes(session: Database = Depends(get_db)):
    #quizz_dal = QuizzesDAL(session)
    quizz = await QuizzesDAL.get_all_quizzes()
    if not quizz:
        raise HTTPException(status_code=404, detail="No quizzes was found")
    return quizz

@quizz_router.put("/quizz/{id}", response_model=SetQuizzDB)
async def update_quizz(id: int, payload: SetQuizzesBody, session: Database = Depends(get_db)):
    #quizz_dal = QuizzesDAL(session)

    quizz_id = await QuizzesDAL.update_quizz(id, payload)

    response_obj = {
        "id": quizz_id,
        "title": payload.title,
        "description": payload.description,
        "is_active": payload.is_active,
    }

    return response_obj

@quizz_router.delete("/quizz/{id}")
async def delete_quizz(id: int, session: Database = Depends(get_db)):
    #quizz_dal = QuizzesDAL(session)
    return await QuizzesDAL.delete_quizz(id)