from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field
from typing import Optional

class DataBaseSettings(BaseModel):
    db_url: str = "postgresql+asyncpg://postgres:12345@localhost:5432/market"
    echo: bool = False  

class JWTSettings(BaseModel):
    secret: str = "hnpWHTGBYiOSIhXcJhArlhbe69rjyonjLfj5FaNXl3Y"
    algorithm: str = "HS256"
    access_token_minutes: int = 60
    auth_cookie_name: str = "access_token"
    auth_cookie_path: str = "/"
    auth_cookie_secure: bool = False
    auth_cookie_samesite: str = "lax"

class ApiSettings(BaseModel):
    api_prefix: str = "/api/v1"

class Settings(BaseSettings):
   
    db: DataBaseSettings = Field(default_factory=DataBaseSettings)
    jwt: JWTSettings = Field(default_factory=JWTSettings)
    api: ApiSettings = Field(default_factory=ApiSettings)
    
    class Config:
        env_nested_delimiter = '__'

settings = Settings()

