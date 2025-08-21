from pydantic import BaseModel, EmailStr
from typing import Optional

from app.schemas.user import UserRead


class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: Optional[UserRead] = None


