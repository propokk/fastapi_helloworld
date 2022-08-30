from fastapi import APIRouter, Depends
from authorization.auth import has_access

router = APIRouter()

@router.get("/", dependencies=[Depends(has_access)])
async def home():
	return {"status": "Working"}

