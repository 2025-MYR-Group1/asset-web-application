from datetime import date, datetime, timezone
from decimal import Decimal

from sqlmodel import Field, SQLModel
from sqlalchemy import Column
from sqlalchemy.types import Numeric


class Assets(SQLModel, table=True):
    __tablename__ = "assets"

    id: int | None = Field(default=None, primary_key=True)

    category: str = Field(max_length=255)
    type: str = Field(max_length=255)
    brand: str = Field(max_length=255)
    name: str = Field(max_length=255)
    supplier: str = Field(max_length=255)

    serial_no: str = Field(max_length=255)
    invoice_no: str = Field(max_length=255)

    purchase_date: date
    warranty_start_date: date
    warranty_end_date: date

    location: str = Field(max_length=255)
    assigned_campus: str = Field(max_length=255)
    assigned_department: str = Field(max_length=255)

    manager_name: str = Field(max_length=255)
    status: str = Field(max_length=255)
    depreciation: Decimal = Field(
        default=Decimal("0.00"),
        sa_column=Column(Numeric(12, 2), nullable=False, server_default="0")
    )

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
