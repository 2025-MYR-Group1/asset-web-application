from datetime import datetime, timedelta
from typing import Optional, Tuple

from jose import jwt
from passlib.context import CryptContext
from sqlmodel import Session

from app.core.settings import Settings
from app.models.users import Users
from app.repositories.user_repository import UserRepository


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, user_repository: UserRepository, settings: Settings) -> None:
        self._user_repository = user_repository
        self._settings = settings

    def hash_password(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, *, subject: str, token_version: int) -> str:
        expire = datetime.utcnow() + timedelta(minutes=self._settings.access_token_expires_minutes)
        payload = {
            "sub": subject,
            "exp": expire,
            "tv": token_version,
            "type": "access",
        }
        return jwt.encode(payload, self._settings.jwt_secret, algorithm=self._settings.jwt_algorithm)

    def create_refresh_token(self, *, subject: str, token_version: int) -> str:
        expire = datetime.utcnow() + timedelta(days=self._settings.refresh_token_expires_days)
        payload = {
            "sub": subject,
            "exp": expire,
            "tv": token_version,
            "type": "refresh",
        }
        return jwt.encode(payload, self._settings.jwt_secret, algorithm=self._settings.jwt_algorithm)

    def decode_token(self, token: str) -> dict:
        return jwt.decode(token, self._settings.jwt_secret, algorithms=[self._settings.jwt_algorithm])

    def signup(self, session: Session, username: str, email: str, password: str) -> Users:
        existing = self._user_repository.get_by_username(session, username) or self._user_repository.get_by_email(session, email)
        if existing:
            raise ValueError("User already exists")
        user = Users(username=username, email=email, password=self.hash_password(password))
        return self._user_repository.create_user(session, user)

    def login(self, session: Session, username: str, password: str) -> Tuple[Users, str, str]:
        user = self._user_repository.get_by_username(session, username)
        if not user or not self.verify_password(password, user.password):
            raise ValueError("Invalid credentials")
        access = self.create_access_token(subject=str(user.id), token_version=user.token_version)
        refresh = self.create_refresh_token(subject=str(user.id), token_version=user.token_version)
        return user, access, refresh

    def logout(self, session: Session, user: Users) -> Users:
        # token_version 증가로 기존 refresh 토큰 무효화
        return self._user_repository.increment_token_version(session, user)

    def get_user_from_refresh(self, session: Session, refresh_token: str) -> Optional[Users]:
        payload = self.decode_token(refresh_token)
        if payload.get("type") != "refresh":
            return None
        user_id = int(payload["sub"])
        user = session.get(Users, user_id)
        if not user:
            return None
        if user.token_version != payload.get("tv"):
            return None
        return user

