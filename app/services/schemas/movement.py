from datetime import datetime

from sqlmodel import SQLModel


class CheckoutRequest(SQLModel):
    renter_id: int
    purpose: str
    return_due_date: datetime


class MovementRead(SQLModel):
    id: int
    asset_id: int
    renter_id: int
    purpose: str
    rental_date: datetime | None
    return_date: datetime | None
    return_due_date: datetime
    approval_status: str
    status: str
