from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Notifications(SQLModel, table=True):
    __tablename__ = "notifications"

    id: int | None = Field(default=None, primary_key=True)
    recipient_id: int = Field(foreign_key="users.id")
    movement_id: int = Field(foreign_key="movements.id")
    asset_id: int = Field(foreign_key="assets.id")

    type: str = Field(max_length=255)  # overdue_return, warranty_expiry
    content: str = Field(max_length=255)
    status: str = Field(max_length=255)  # unread, read

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
