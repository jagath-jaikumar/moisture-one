from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    postgres_user: str
    postgres_host: str
    postgres_database: str
    postgres_password: str
    postgres_port: int

    sentry_dsn: str | None = None


settings = Settings()
