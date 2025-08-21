from datetime import datetime

from sqlmodel import SQLModel


class NotificationCreate(SQLModel):
    recipient_id: int
    movement_id: int
    type: str
    content: str


class NotificationRead(SQLModel):
    id: int
    recipient_id: int
    movement_id: int
    asset_id: int
    type: str
    content: str
    status: str
    created_at: datetime