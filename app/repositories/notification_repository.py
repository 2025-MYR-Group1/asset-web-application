from typing import List

from sqlmodel import Session, select

from app.models.notifications import Notifications


class NotificationRepository:

    def list_notifications(self, session: Session) -> List[Notifications]:
        query = select(Notifications)
        return list(session.exec(query).all())

    def create_notification(
        self, session: Session, notification: Notifications
    ) -> Notifications:
        session.add(notification)
        session.commit()
        session.refresh(notification)
        return notification