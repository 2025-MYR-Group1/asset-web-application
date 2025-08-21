from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)

    username: str = Field(max_length=255)
    role: str = Field(max_length=255, default="user")
    email: str = Field(max_length=255)
    password: str = Field(max_length=255)
    token_version: int = Field(default=0, nullable=False)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
