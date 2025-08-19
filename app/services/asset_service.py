from typing import List

from app.db import session
from app.models.assets import Assets
from app.repositories.asset_repository import AssetRepository
from app.schemas.asset import AssetCreate, AssetDelete, AssetRead, AssetUpdate


class AssetService:
    def __init__(self, repository: AssetRepository) -> None:
        self._repository = repository

    def list_assets(self) -> List[Assets]:
        return self._repository.list_assets(session)

    def create_asset(self, payload: AssetCreate) -> AssetCreate:
        return self._repository.create_asset(payload)

    def update_asset(self, asset_id: int, payLoad: AssetUpdate) -> AssetUpdate:
        return self._repository.update_asset(asset_id, payLoad)

    def delete_asset(self, asset_id: int) -> AssetDelete:
        return self._repository.delete_asset(asset_id)

    def get_asset(self, asset_id: int) -> AssetRead:
        return self._repository.get_asset(asset_id)
