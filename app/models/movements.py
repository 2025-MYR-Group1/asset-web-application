from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Movements(SQLModel, table=True):
    __tablename__ = "movements"

    id: int | None = Field(default=None, primary_key=True)
    asset_id: int = Field(foreign_key="assets.id")
    renter_id: int = Field(foreign_key="users.id")

    purpose: str = Field(max_length=255)

    rental_date: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    return_date: datetime | None = Field(default=None)
    return_due_date: datetime

    approval_status: str = Field(max_length=255, default="pending")
    status: str = Field(max_length=255, default="pending")
