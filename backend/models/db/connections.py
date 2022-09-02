from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from starlette.requests import Request


app = FastAPI()

def get_db(request: Request) -> Database:
	return request.app.state.database

def get_redis(request: Request):
	return request.app.state.redis

Base = declarative_base()