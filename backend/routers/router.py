from fastapi import APIRouter


router = APIRouter()

@router.get('/', tags=['home'])
async def home():
	return {"status": "Working"}