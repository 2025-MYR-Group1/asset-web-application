from fastapi import APIRouter
from app.api.endpoints import assets


api_router = APIRouter()

# 서브 라우터 마운트
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])


