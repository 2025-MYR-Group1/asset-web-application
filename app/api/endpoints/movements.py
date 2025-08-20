from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_asset_service
from app.db.session import SessionDep
from app.models.assets import Assets
from app.schemas.asset import AssetCreate, AssetDelete, AssetRead, AssetUpdate
from app.schemas.response import ApiResponse
from app.services.asset_service import AssetService

router = APIRouter()


# TODO: 자산 대출
@router.get("/", response_model=ApiResponse[List[AssetRead]])
def list_assets(
    session: SessionDep,
    asset_service: AssetService = Depends(get_asset_service),
) -> ApiResponse[List[AssetRead]]:
    assets = asset_service.list_assets(session)
    if not assets:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    message = "Asset list retrieved successfully"
    return ApiResponse(success=True, data=assets, message=message)


# TODO: 자산 반납
@router.post("/add", response_model=ApiResponse[AssetRead])
def create_asset(
    payload: AssetCreate,
    session: SessionDep,
    asset_service: AssetService = Depends(get_asset_service),
) -> ApiResponse[AssetRead]:
    created = asset_service.create_asset(session, payload)
    if not created:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Asset not created"
        )
    message = "Asset created successfully"
    return ApiResponse(success=True, data=created, message=message)

# TODO: 자산 이동 이력 조회회