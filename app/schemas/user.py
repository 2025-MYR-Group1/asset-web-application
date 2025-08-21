from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime | None


