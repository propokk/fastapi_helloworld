from backend.main import app
from backend.models.db.connections import get_db, get_redis
from backend.core.config import settings

from databases import Database
from redis import Redis 
from sqlalchemy.ext.declarative import declarative_base

database_test = Database(settings.TEST_DATABASE_URL)
redis = Redis(host="redis-17761.c239.us-east-1-2.ec2.cloud.redislabs.com", port=17761, db="test_db",password="userpass")

async def override_get_db():
    return await database_test.connect()

def override_get_redis():
    return redis


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_redis] = override_get_redis

TestBase = declarative_base()