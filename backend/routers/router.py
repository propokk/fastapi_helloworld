<<<<<<< HEAD
from starlette.routing import Route

async def home():
	return {"status": "Working"}

routes = [
	Route("/", endpoint=home)
]
=======
from fastapi import APIRouter


router = APIRouter()

@router.get('/', tags=['home'])
async def home():
	return {"status": "Working"}
>>>>>>> origin/main
