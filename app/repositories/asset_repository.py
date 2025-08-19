from typing import List, Optional

from sqlmodel import Session, select

from app.models.assets import Assets
from app.schemas.asset import AssetCreate, AssetUpdate


class AssetRepository:

    def list_assets(self, session: Session) -> List[Assets]:
        query = select(Assets)
        return list(session.exec(query).all())

    def create_asset(self, session: Session, payload: AssetCreate) -> Assets:
        asset = Assets(**payload.model_dump())
        session.add(asset)
        session.commit()
        session.refresh(asset)
        return asset

    def update_asset(
        self, session: Session, asset_id: int, payload: AssetUpdate
    ) -> Optional[Assets]:
        asset = session.get(Assets, asset_id)
        if asset is None:
            return None

        update_data = payload.model_dump(exclude_unset=True)
        for field_name, field_value in update_data.items():
            setattr(asset, field_name, field_value)
        session.add(asset)
        session.commit()
        session.refresh(asset)
        return asset

    def delete_asset(self, session: Session, asset_id: int) -> bool:
        asset = session.get(Assets, asset_id)
        if asset is None:
            return False
        session.delete(asset)
        session.commit()
        return True

    def get_asset(self, session: Session, asset_id: int) -> Optional[Assets]:
        return session.get(Assets, asset_id)

				