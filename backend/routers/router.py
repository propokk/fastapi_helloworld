from unittest import result
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from authorization.auth import verify_token
from core.config import settings

router = APIRouter()
security = HTTPBearer()

AUTH0_DOMAIN = settings.AUTH0_DOMAIN
AUTH0_AUDIENCE = settings.AUTH0_AUDIENCE

@router.get("/")
async def private(response: Response, token: HTTPAuthorizationCredentials = Depends(security)):

	result = verify_token(token.credentials, AUTH0_DOMAIN, AUTH0_AUDIENCE)

	if result.get("status"):
		response.status_code = status.HTTP_400_BAD_REQUEST
		return result

	return result

