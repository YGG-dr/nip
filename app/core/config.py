from pydantic import BaseSetting
from functools import lru_cache

class Settings(BaseSetting):
    APP_NAME: str = "nip"
    OPENAI_MODEL: str = "gpt-4o-mini"
    
    class Config:
        env file = ".env"
        
        
@lru_cache
def get_settings() -> Settings:
    return Settings()
    
