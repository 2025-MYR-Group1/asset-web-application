from datetime import datetime
from pydantic import BaseModel, Field


class Movements(BaseModel, table=True):
    __tablename__ = "asset_logs"

    id: int | None = Field(default=None, primary_key=True)
    asset_id: int = Field(foreign_key="assets.id")
    renter_id: int = Field(foreign_key="users.id")

    purpose: str = Field(max_length=255)

    rental_date: datetime | None = Field(default=datetime.now())
    return_date: datetime
    return_due_date: datetime

    # enum 검토 필요
    approval_status: str = Field(max_length=255, default="pending")
    status: str = Field(max_length=255, default="pending")