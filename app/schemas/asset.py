from datetime import date, datetime
from decimal import Decimal

from sqlmodel import SQLModel


class AssetCreate(SQLModel):
    category: str
    type: str
    brand: str
    name: str
    supplier: str

    serial_no: str
    invoice_no: str

    purchase_date: date
    warranty_start_date: date
    warranty_end_date: date

    location: str
    assigned_campus: str
    assigned_department: str

    manager_name: str
    status: str
    depreciation: Decimal


class AssetRead(SQLModel):
    id: int

    category: str
    type: str
    brand: str
    name: str
    supplier: str

    serial_no: str
    invoice_no: str

    purchase_date: date
    warranty_start_date: date
    warranty_end_date: date

    location: str
    assigned_campus: str
    assigned_department: str

    manager_name: str
    status: str
    depreciation: Decimal

    created_at: datetime | None
    updated_at: datetime | None


class AssetUpdate(SQLModel):
    category: str | None = None
    type: str | None = None
    brand: str | None = None
    name: str | None = None
    supplier: str | None = None

    serial_no: str | None = None
    invoice_no: str | None = None

    purchase_date: date | None = None
    warranty_start_date: date | None = None
    warranty_end_date: date | None = None

    location: str | None = None
    assigned_campus: str | None = None
    assigned_department: str | None = None

    manager_name: str | None = None
    status: str | None = None
    depreciation: Decimal | None = None


class AssetDelete(SQLModel):
    id: int
    deleted: bool = False