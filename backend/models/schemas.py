from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
	id: int
	email: Optional[SignUp_Request.email]
	name: Optional[SignUp_Request.name]
	is_superuser: bool = Field(default_factory=False)
	password_id: Optional[SignUp_Request.password]
	created_at: datetime = Field(default_factory=datetime.now)

class SignUp_Request(BaseModel):
	id: int
	email: str = Field(min_length=1)
	name: str
	password: str = Field(min_length=1)

class SignIn_Request(BaseModel):
	id:
	email: Optional[SignUp_Request.email]
	password: Optional[SignUp_Request.email]