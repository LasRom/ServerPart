from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


env_path = Path(__file__).resolve().parent.parent / '.env'


class Settings(BaseSettings):
    DEBUG: str = 'T'

    DATABASE_USER: str
    DATABASE_PASSWORD: SecretStr
    DATABASE_NAME: str
    DATABASE_URI: str
    DATABASE_PORT: int = 5432

    model_config = SettingsConfigDict(env_file=str(env_path), env_file_encoding='utf-8')


settings = Settings()
