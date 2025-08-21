# app/core/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    db_url: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 3600
    access_token_expires_minutes: int = 15
    refresh_token_expires_days: int = 14

    cookie_domain: str | None = None
    cookie_secure: bool = False
    cookie_samesite: Literal["lax", "strict", "none"] = "lax"
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        case_sensitive=False,
        extra="ignore",
    )
