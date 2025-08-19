from app.repositories.asset_repository import InMemoryUserRepository
from app.services.asset_service import UserService


def get_user_service() -> UserService:
	# 간단한 데모: 요청마다 새로운 인메모리 저장소/서비스 인스턴스 제공
	repository = InMemoryUserRepository()
	service = UserService(repository)
	return service


