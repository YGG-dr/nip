from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "nip"
    OPENAI_MODEL: str = "gpt-4o-mini"
    
    class Config:
        env_file = ".env"
        
        
@lru_cache
def get_settings() -> Settings:
    return Settings()