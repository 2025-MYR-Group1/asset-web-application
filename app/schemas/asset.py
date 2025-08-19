from datetime import date, datetime

from sqlmodel import Field, SQLModel


class AssetCreate(SQLModel):
    status: bool = Field(default=True)

    category: str = Field(max_length=255)
    type: str = Field(max_length=255)
    brand: str = Field(max_length=255)
    model: str = Field(max_length=255)
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
    depreciation: int = Field(default=0)


class AssetRead(SQLModel):
    id: int

    category: str
    type: str
    brand: str
    model: str
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
    depreciation: int

    created_at: datetime | None
    updated_at: datetime | None


class AssetUpdate(SQLModel):
    category: str | None = None
    type: str | None = None
    brand: str | None = None
    model: str | None = None
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
    depreciation: int | None = None


class AssetDelete(SQLModel):
    id: int
    deleted: bool = False