
from pathlib import Path

from pydantic import (
    Field,
)
from pydantic_settings import BaseSettings

PROJECT_DIR = Path(__file__).parent.parent

CONF_DIR = PROJECT_DIR / "conf"
DB_DIR = PROJECT_DIR / "db"


class Settings(BaseSettings):
    db_name: str = Field(alias='DB_NAME')

    api_key: str = Field(alias='API_KEY')
    redis_host: str = Field(default="", alias='REDIS_HOST')
    redis_port: str = Field(default="", validate_default=False, alias='REDIS_PORT')

    @property
    def db_url(self):
        return f"sqlite:///{DB_DIR}/{self.db_name}.db"

    class Config:
        env_file = CONF_DIR / ".env"
        env_file_encoding = "utf-8"

settings = Settings() # type: ignore

