from app.repositories.asset_repository import AssetRepository
from app.services.asset_service import AssetService


def get_asset_service() -> AssetService:
	repository = AssetRepository()
	service = AssetService(repository)
	return service


