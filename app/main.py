from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.v1.routers import api_v1_router


def create_app() -> FastAPI:
	app = FastAPI(title="Asset Web Application", version="0.1.0")

	@app.get("/health", tags=["health"])  # 간단 헬스체크
	def health_check() -> dict:
		return {"status": "ok"}

	# 예외 핸들링: 서비스 계층에서 발생한 ValueError를 400으로 변환
	@app.exception_handler(ValueError)
	def value_error_handler(_, exc: ValueError):
		return JSONResponse(status_code=400, content={"detail": str(exc)})

	# API v1 라우터 마운트
	app.include_router(api_v1_router, prefix="/api/v1")

	return app


app = create_app()


