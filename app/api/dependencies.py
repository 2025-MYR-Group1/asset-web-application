from app.repositories.asset_repository import AssetRepository
from app.services.asset_service import AssetService
from app.repositories.movement_repository import MovementRepository
from app.services.movement_service import MovementService
from app.repositories.notification_repository import NotificationRepository
from app.services.notification_service import NotificationService


def get_asset_service() -> AssetService:
	repository = AssetRepository()
	service = AssetService(repository)
	return service


def get_movement_service() -> MovementService:
	repository = MovementRepository()
	service = MovementService(repository)
	return service


def get_notification_service() -> NotificationService:
	repository = NotificationRepository()
	service = NotificationService(repository)
	return service