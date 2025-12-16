from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field("FastAPI Service", env="APP_NAME")
    environment: str = Field("development", env="ENVIRONMENT")
    debug: bool = Field(True, env="DEBUG")
    version: str = "0.1.0"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
