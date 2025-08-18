from datetime import date, datetime
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import create_engine
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Assets(SQLModel, table=True):
    __tablename__ = "assets"

    id: int | None = Field(default=None, primary_key=True)

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

    created_at: datetime | None = Field(default=datetime.now())
    updated_at: datetime | None = Field(default=datetime.now())
