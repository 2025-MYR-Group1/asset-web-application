from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_movement_service
from app.db.session import SessionDep
from app.schemas.movement import CheckoutRequest, MovementRead
from app.schemas.response import ApiResponse
from app.services.movement_service import MovementService

router = APIRouter()


@router.post("/check-out/{asset_id}", response_model=ApiResponse[MovementRead])
def check_out_movement(
    asset_id: int,
    payload: CheckoutRequest,
    session: SessionDep,
    movement_service: MovementService = Depends(get_movement_service),
) -> ApiResponse[MovementRead]:

    created = movement_service.checkout_asset(session, asset_id, payload)
    if not created:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Movement not created"
        )
    message = "Asset checked out successfully"
    return ApiResponse(success=True, data=created, message=message)


@router.patch("/check-in/{asset_id}", response_model=ApiResponse[MovementRead])
def check_in_movement(
    asset_id: int,
    session: SessionDep,
    movement_service: MovementService = Depends(get_movement_service),
) -> ApiResponse[MovementRead]:

    updated = movement_service.checkin_asset(session, asset_id)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Movement not updated"
        )
    message = "Asset checked in successfully"
    return ApiResponse(success=True, data=updated, message=message)


@router.get("/{asset_id}", response_model=ApiResponse[List[MovementRead]])
def list_asset_movements(
    asset_id: int,
    session: SessionDep,
    movement_service: MovementService = Depends(get_movement_service),
) -> ApiResponse[List[MovementRead]]:
    movements = movement_service.list_asset_movements(session, asset_id)
    if not movements:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movements not found"
        )
    message = f"Movements found successfully for asset {asset_id}"
    return ApiResponse(success=True, data=movements, message=message)


@router.get("/{user_id}", response_model=ApiResponse[List[MovementRead]])
def list_user_movements(
    user_id: int,
    session: SessionDep,
    movement_service: MovementService = Depends(get_movement_service),
) -> ApiResponse[List[MovementRead]]:
    movements = movement_service.list_user_movements(session, user_id)
    if not movements:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movements not found"
        )
    message = f"Movements found successfully for user {user_id}"
    return ApiResponse(success=True, data=movements, message=message)

@router.get("/", response_model=ApiResponse[List[MovementRead]])
def list_all_movements(
    session: SessionDep,
    movement_service: MovementService = Depends(get_movement_service),
) -> ApiResponse[List[MovementRead]]:
    movements = movement_service.list_all_movements(session)
    if not movements:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movements not found"
        )
    message = "Movements found successfully"
    return ApiResponse(success=True, data=movements, message=message)