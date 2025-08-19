from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_asset_service
from app.models.assets import Assets
from app.schemas.asset import AssetCreate, AssetDelete, AssetRead, AssetUpdate
from app.schemas.response import ApiResponse
from app.services import asset_service
from app.services.asset_service import AssetService

router = APIRouter()


# TODO: 자산 목록 조회
@router.get("/", response_model=ApiResponse[List[Assets]])
def list_assets(
    asset_service: AssetService = Depends(get_asset_service),
) -> ApiResponse[List[Assets]]:
    assets = asset_service.list_assets()
    if not assets:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    message = "Asset list retrieved successfully"
    return ApiResponse(success=True, data=assets, message=message)


# TODO: 신규 자산 등록
@router.post("/add", response_model=ApiResponse[AssetCreate])
def create_asset(
    payload: AssetCreate, asset_service: AssetService = Depends(get_asset_service)
) -> ApiResponse[AssetCreate]:
    created = asset_service.create_asset(payload)
    if not created:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Asset not created"
        )
    message = "Asset created successfully"
    return ApiResponse(success=True, data=created, message=message)


# TODO 자산 정보 수정
@router.patch("/{asset_id}")
def update_asset(
    asset_id: int,
    payload: AssetUpdate,
    asset_service: AssetService = Depends(get_asset_service),
) -> ApiResponse[AssetUpdate]:
    updated = asset_service.update_asset(asset_id, payload)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    message = "Asset updated successfully"
    return ApiResponse(success=True, data=updated, message=message)


# TODO: 자산 정보 삭제
@router.delete("/{asset_id}")
def delete_asset(asset_id: int) -> ApiResponse[None]:
    deleted = asset_service.delete_asset(asset_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    message = "Asset deleted successfully"
    return ApiResponse(success=True, data=deleted, message=message)


# TODO: 자산 정보 조회
@router.get("/{asset_id}", response_model=ApiResponse[AssetDelete])
def get_asset(asset_id: int) -> ApiResponse[AssetRead]:
    asset = asset_service.get_asset(asset_id)
    if not asset:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    message = "Asset retrieved successfully"
    return ApiResponse(success=True, data=asset, message=message)
