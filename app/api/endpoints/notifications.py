from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_notification_service
from app.db.session import SessionDep
from app.schemas.notification import NotificationCreate, NotificationRead
from app.schemas.response import ApiResponse
from app.services.notification_service import NotificationService

router = APIRouter()


@router.post("/checkout/{asset_id}", response_model=ApiResponse[NotificationRead])
def notify_return_overdue(
    asset_id: int,
    payload: NotificationCreate,
    session: SessionDep,
    notification_service: NotificationService = Depends(get_notification_service),
) -> ApiResponse[NotificationRead]:

    notification = notification_service.notify(session, payload, asset_id)
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found"
        )
    message = "Notification created successfully"
    return ApiResponse(success=True, data=notification, message=message)


@router.post("/warranty/{asset_id}", response_model=ApiResponse[NotificationRead])
def notify_warranty_expiry(
    asset_id: int,
    payload: NotificationCreate,
    session: SessionDep,
    notification_service: NotificationService = Depends(get_notification_service),
) -> ApiResponse[NotificationRead]:
    notification = notification_service.notify(session, payload, asset_id)
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found"
        )
    message = "Notification created successfully"
    return ApiResponse(success=True, data=notification, message=message)


@router.get("/history", response_model=ApiResponse[List[NotificationRead]])
def get_notification_history(
    session: SessionDep,
    notification_service: NotificationService = Depends(get_notification_service),
) -> ApiResponse[List[NotificationRead]]:
    notifications = notification_service.list_all_notifications(session)
    if not notifications:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found"
        )
    message = "Notification list retrieved successfully"
    return ApiResponse(success=True, data=notifications, message=message)


@router.get("/{notification_id}", response_model=ApiResponse[NotificationRead])
def get_notification_detail(
    notification_id: int,
    session: SessionDep,
    notification_service: NotificationService = Depends(get_notification_service),
) -> ApiResponse[NotificationRead]:
    notification = notification_service.get_notification(session, notification_id)
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found"
        )
    message = "Notification retrieved successfully"
    return ApiResponse(success=True, data=notification, message=message)
