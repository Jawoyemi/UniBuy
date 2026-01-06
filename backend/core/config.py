from pydantic_settings import BaseSettings
from typing import Optional
import os
from pathlib import Path

# BASE_DIR is .../unibuy/backend/core -> .../unibuy
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = str(BASE_DIR / ".env")

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:Tomiwa2006@localhost/unibuy_db"
    SECRET_KEY: str = "4d44a5726f355c7173d6c4a027b7325d221ba67c82305d9abbde069ed14ed61a"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Email settings
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = 587
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None
    EMAILS_FROM_NAME: Optional[str] = "Unibuy"
    
    # Redis Configuration
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ENV_FILE
        extra = "ignore"

settings = Settings()