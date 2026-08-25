"""configuración de la aplicación, cargada desde variables de entorno o .env."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ajustes de la aplicación."""

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    # base de datos: sin default, deben venir de .env o del entorno
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    # jwt: sin default, debe venir de .env o del entorno
    jwt_secret_key: str
    jwt_algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30

    # api
    api_v1_prefix: str = '/api/v1'
    project_name: str = 'Northwind API'

    @property
    def database_url(self) -> str:
        """construimos la url de conexión asíncrona a postgresql."""
        return (
            f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}'
            f'@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}'
        )


@lru_cache
def get_settings() -> Settings:
    """devolvemos una instancia cacheada de la configuración."""
    return Settings()


settings = get_settings()
