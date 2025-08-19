from typing import List, Optional

from sqlmodel import Session

from app.models.assets import Assets
from app.repositories.asset_repository import AssetRepository
from app.schemas.asset import AssetCreate, AssetUpdate


class AssetService:
    def __init__(self, repository: AssetRepository) -> None:
        self._repository = repository

    def list_assets(self, session: Session) -> List[Assets]:
        return self._repository.list_assets(session)

    def create_asset(self, session: Session, payload: AssetCreate) -> Assets:
        return self._repository.create_asset(session, payload)

    def update_asset(self, session: Session, asset_id: int, payload: AssetUpdate) -> Optional[Assets]:
        return self._repository.update_asset(session, asset_id, payload)

    def delete_asset(self, session: Session, asset_id: int) -> bool:
        return self._repository.delete_asset(session, asset_id)

    def get_asset(self, session: Session, asset_id: int) -> Optional[Assets]:
        return self._repository.get_asset(session, asset_id)
