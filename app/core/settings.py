# app/core/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_url: str
    model_config = SettingsConfigDict(env_file=".env", env_prefix="", case_sensitive=False)