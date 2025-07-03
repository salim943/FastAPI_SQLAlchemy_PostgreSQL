from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import Optional

load_dotenv()  # Explicitly load the .env file


class Settings(BaseSettings):
    POSTGRES_HOSTNAME: str
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "fastapi"
    DATABASE_PORT: int = 5432
    API_KEY: Optional[str] = None  

    class Config:
        env_file = ".env"


settings = Settings()
