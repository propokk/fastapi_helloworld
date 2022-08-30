from fastapi import FastAPI
from databases import Database
from routers import router as hw_router
from core.config import settings

app = FastAPI()

#db connection
DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)

async def inject_db(app: FastAPI, db: Database):
	app.state.database = db
	for route in app.router.routes:
		if isinstance(route, hw_router.routes):
			route.app.state.database = db


@app.on_event("startup")
async def startup():
	await database.connect()
	await inject_db(app, database)


app.include_router(hw_router.router)
