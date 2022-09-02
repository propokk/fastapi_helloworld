from typing import List, Optional
from unittest import result
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from databases import Database
from redis import Redis
import sqlalchemy as sa
import os
from authorization.auth import verify_token
from core.config import settings
from models.db.connections import get_db, get_redis
from models.model import Categories, Questions, Quizzes, Quizz_results, User
from models.user_models_dal import UserQuizzDAL
from models.user_schemas import SetResponseBody
from fastapi.responses import FileResponse


router = APIRouter()
security = HTTPBearer()

AUTH0_DOMAIN = settings.AUTH0_DOMAIN
AUTH0_AUDIENCE = settings.AUTH0_AUDIENCE

@router.get("/quizzes")
async def get_all_quizzes(response: Response,
					session: Database = Depends(get_db), 
					token: HTTPAuthorizationCredentials = Depends(security)) -> List[Quizzes]:

	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	user_quizz_dal = UserQuizzDAL(session)



	return await user_quizz_dal.get_all_quizzes()

@router.get("/quizzes/categories")
async def get_all_categories(response: Response,
					session: Database = Depends(get_db), 
					token: HTTPAuthorizationCredentials = Depends(security)) -> List[Categories]:

	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	user_quizz_dal = UserQuizzDAL(session)

	return await user_quizz_dal.get_all_categories()

@router.post("/quizzes/categories/questions")
async def get_all_questions(response: Response,
					quizz_id: int, category_id: int,
					session: Database = Depends(get_db), 
					token: HTTPAuthorizationCredentials = Depends(security)) -> List[Questions]:

	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	user_quizz_dal = UserQuizzDAL(session)

	return await user_quizz_dal.get_questions(quizz_id, category_id)



@router.post("/quizzes/categories/questions/answer")
async def send_answer(response: Response,
					question_id: int, answer_text: str,
					session: Database = Depends(get_db),
					additional: Redis = Depends(get_redis),
					token: HTTPAuthorizationCredentials = Depends(security)) -> List[Questions]:

	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)
	users_sub = result.get("sub")
	additional.set(question_id, answer_text)

	query = sa.insert(Quizz_results).values(user=users_sub, user_score=1, max_score=1)
	await session.fetch_one(query=query)


	with open("my_csv.csv", "a") as f:
		f.write(f"{users_sub},1,1{os.linesep}")

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	user_quizz_dal = UserQuizzDAL(session)

	return await user_quizz_dal.send_answer(question_id, answer_text)

file_path = "my_csv.csv"
@router.get("/download")
async def download():
	return FileResponse(path=file_path, filename=file_path, media_type='text/csv')