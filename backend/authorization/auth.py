from typing import Any

import jwt
from fastapi import HTTPException


def verify_token(token: str, domain: str, audience: str) -> dict[str, Any]:
    """
    Use the pyjwt jwkclient to get a signing key, then decode the supplied token
    """
    jwks_client = jwt.PyJWKClient(f"https://{domain}/.well-known/jwks.json")
    signing_key = jwks_client.get_signing_key_from_jwt(token).key

    try: 
        decoded = jwt.decode(
            token,
            signing_key,
            algorithms=["RS256"],
            audience=audience,
            issuer=f"https://{domain}/",
        )
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=401, detail=str(e))

    return decoded