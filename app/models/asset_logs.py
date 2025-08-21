from datetime import datetime
from pydantic import BaseModel, Field


class AssetLogs(BaseModel, table=True):
    __tablename__ = "asset_logs"

    id: int | None = Field(default=None, primary_key=True)
    asset_id: int = Field(foreign_key="assets.id")
    modifier_id: int = Field(foreign_key="users.id")

    field_name: str = Field(max_length=255)
    old_value: str = Field(max_length=255)
    new_value: str = Field(max_length=255)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))