from typing import List

from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import FileResponse

from databases import Database
from redis import Redis
import sqlalchemy as sa
from sqlalchemy import and_

from authorization.auth import verify_token

import os
import pandas as pd
from models.user_schemas import SetFinalAnswerBody
from core.config import settings
from models.db.connections import get_db, get_redis
from models.model import Categories, Questions, Quizzes, Quizz_results, Answers, Question_categories
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
	users_sub = result.get("sub")

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	user_quizz_dal = UserQuizzDAL(session)

	j = sa.join(Questions, Question_categories, Questions.id == Question_categories.question_id)
	max_score = sa.select(sa.func.count(Questions.quizz_id)).select_from(j).where(and_(Questions.quizz_id == quizz_id, Question_categories.category_id==category_id))
	count_q = list((dict(await session.fetch_one(query=max_score))).items())

	query = sa.insert(Quizz_results).values(user=users_sub, user_score=0, max_score=count_q[0][1])
	await session.fetch_one(query=query)


	return await user_quizz_dal.get_questions(quizz_id, category_id)



@router.post("/quizzes/categories/questions/answer")
async def send_answer(response: Response,
					data: SetFinalAnswerBody,
					session: Database = Depends(get_db),
					additional: Redis = Depends(get_redis),
					token: HTTPAuthorizationCredentials = Depends(security)) -> List[Questions]:

	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)
	users_sub = result.get("sub")
	file_path = "users_csv.csv"

	max_score = sa.select(Quizz_results.max_score).where(Quizz_results.user==users_sub)
	max_score_list = list((dict(await session.fetch_one(query=max_score))).items())

	correct_check_list = []
	for i in range(int(max_score_list[0][1])):
		additional.append(users_sub,str({'question_id':(list(data.answers[i]))[0][1], 'answer_text':(list(data.answers[i]))[1][1]}))
		correct_check = sa.select(Answers.is_correct).where(Answers.answer_text==(list(data.answers[i]))[1][1])
		l = list((dict(await session.fetch_one(query=correct_check))).items())
		if l[0][1] == True:
			correct_check_list.append(l)
	
	additional.expire(users_sub, 172800)
	query = sa.update(Quizz_results).where(Quizz_results.user==users_sub).values(user_score=len(correct_check_list))
	await session.fetch_one(query=query)


	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result


	if additional.exists(users_sub) == 1:
		query = additional.get(users_sub)
		with open('users_csv.csv', 'w', newline='') as fp:
			fp.write(f"{query}{os.linesep}")

	res = "{}/{}".format(len(correct_check_list), int(max_score_list[0][1]))

	return res


@router.put("/quizzes/categories/questions/answer")
async def update_answer(response: Response,
					data: SetFinalAnswerBody,
					session: Database = Depends(get_db),
					additional: Redis = Depends(get_redis),
					token: HTTPAuthorizationCredentials = Depends(security)):
	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)
	users_sub = result.get("sub")
	file_path = "users_csv.csv"


	max_score = sa.select(Quizz_results.max_score).where(Quizz_results.user==users_sub)
	max_score_list = list((dict(await session.fetch_one(query=max_score))).items())

	correct_check_list = []
	for i in range(int(max_score_list[0][1])):
		additional.append(users_sub,str({'question_id':(list(data.answers[i]))[0][1], 'answer_text':(list(data.answers[i]))[1][1]}))
		correct_check = sa.select(Answers.is_correct).where(Answers.answer_text==(list(data.answers[i]))[1][1])
		l = list((dict(await session.fetch_one(query=correct_check))).items())
		if l[0][1] == True:
			correct_check_list.append(l)
	
	query = sa.update(Quizz_results).where(Quizz_results.user==users_sub).values(user_score=len(correct_check_list))
	await session.fetch_one(query=query)

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	if additional.exists(users_sub) == 1:
		query = additional.get(users_sub)
		with open('users_csv.csv', 'w', newline='') as fp:
			fp.write(f"{query}{os.linesep}")

	res = "{}/{}".format(len(correct_check_list), int(max_score_list[0][1]))
	return res

	

@router.get("/quizzes/quizz_results/download")
async def download(response: Response, token: HTTPAuthorizationCredentials = Depends(security)):
	file_path = "users_csv.csv"
	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	return FileResponse(path=file_path, filename=file_path, media_type='text/csv')


@router.get("/download")
async def download(user_id:int, session: Database = Depends(get_db)):
	
	file_path = "my_csv.csv"

	if user_id == 0:
		user = sa.select(Quizz_results)
		res = list((dict(await session.fetch_one(query=user))).items())
	else:
		user = sa.select(Quizz_results).where(Quizz_results.id==user_id)
		res = list((dict(await session.fetch_one(query=user))).items())


	df = pd.DataFrame(res)
	df.to_csv(file_path, index=False)
	
	return FileResponse(path=file_path, filename=file_path, media_type='text/csv')