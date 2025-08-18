from datetime import datetime
from pydantic import BaseModel, Field


class Users(BaseModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    
    username: str = Field(max_length=255)
    role: str = Field(max_length=255)
    email: str = Field(max_length=255)
    password: str = Field(max_length=255)

    created_at: datetime | None = Field(default=datetime.now())