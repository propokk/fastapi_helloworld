from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import FileResponse

from databases import Database
from redis import Redis
import sqlalchemy as sa

from authorization.auth import verify_token

import os
import asyncio
from models.admin_models_dals import QuizResultsDAL
from core.config import settings
from models.db.connections import get_db, get_redis
from models.model import Categories, Questions, Quizzes, Quizz_results, User, Answers
from models.user_models_dal import UserQuizzDAL


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


counter_lock = asyncio.Lock()
counter1 = 0
counter2 = 0

@router.post("/quizzes/categories/questions/answer")
async def send_answer(response: Response,
					question_id: int, answer_text: str,
					session: Database = Depends(get_db),
					additional: Redis = Depends(get_redis),
					token: HTTPAuthorizationCredentials = Depends(security)) -> List[Questions]:

	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)
	users_sub = result.get("sub")
	additional.set(question_id, answer_text)

	
	global counter1, counter2
	score = sa.select(Answers.is_correct).where(Answers.question_id==question_id)
	async with counter_lock:
		if score == 1:
			counter1 += 1
			counter2 += 1
		else:
			counter2 += 1


	query = sa.update(Quizz_results).where(Quizz_results.user==users_sub).values(user_score=counter1, max_score=counter2)
	await session.fetch_one(query=query)

	file_path = "my_csv.csv"
	with open(file_path, "w") as f:
		f.write(f"{users_sub}, {counter1}/{counter2}{os.linesep}")

	user_quizz_dal = UserQuizzDAL(session)
	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	return await user_quizz_dal.send_answer(question_id, answer_text)


@router.get("/download")
async def download():
	
	file_path = "my_csv.csv"
                
	return FileResponse(path=file_path, filename=file_path, media_type='text/csv')