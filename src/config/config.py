from pydantic_settings import BaseSettings


class Config(BaseSettings):
    db_uri: str
    logfire_token: str
    api_version: str = "v1"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    class Config:
        env_file = ".env"
