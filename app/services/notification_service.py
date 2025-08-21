from typing import List

from sqlmodel import Session

from app.models.notifications import Notifications
from app.repositories.notification_repository import NotificationRepository
from app.schemas.notification import NotificationCreate


class NotificationService:
    def __init__(self, repository: NotificationRepository) -> None:
        self._repository = repository

    def notify(
        self, session: Session, payload: NotificationCreate, asset_id: int
    ) -> Notifications:
        notification = Notifications(
            recipient_id=payload.recipient_id,
            movement_id=payload.movement_id,
            asset_id=asset_id,
            type=payload.type,
            content=payload.content,
            status="unread",
        )
        return self._repository.create_notification(session, notification)

    def list_all_notifications(self, session: Session) -> List[Notifications]:
        return self._repository.list_notifications(session)
