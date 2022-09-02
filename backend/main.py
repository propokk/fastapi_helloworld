from fastapi import FastAPI
from databases import Database
from routers import router as hw_router
from routers.admin import answers_router, categories_router, question_categories_router, questions_router, quizzes_router
from core.config import settings
from starlette.routing import Mount
from redis import Redis 

app = FastAPI()

#db connection
DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)


def inject_db(app: FastAPI, db: Database, db_r: Redis):
	app.state.database = db
	app.state.redis = db_r
	for route in app.router.routes:
		if isinstance(route, Mount):
			route.app.state.database = db
			route.app.state.redis = db_r


@app.on_event("startup")
async def startup():
	await database.connect()
	r = Redis(host="localhost", port=6379, db=0, password=None, socket_timeout=None)
	inject_db(app, database, r)


app.include_router(hw_router.router)
app.include_router(answers_router.answer_router)
app.include_router(categories_router.category_router)
app.include_router(question_categories_router.question_category_router)
app.include_router(questions_router.questions_router)
app.include_router(quizzes_router.quizz_router)