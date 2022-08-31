from pydantic import BaseModel, Field
from datetime import datetime

class SignUp_Request(BaseModel):
	id: int
	email: str = Field(min_length=1)
	name: str
	password: str = Field(min_length=1)

class User(SignUp_Request):
	id: int
	is_superuser: bool = Field(default_factory=False)
	created_at: datetime = Field(default_factory=datetime.now)

class SignIn_Request(SignUp_Request):
	id: int