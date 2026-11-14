from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "MaintX API"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"
    ENVIRONMENT: str = "development"
    
    # Supabase credentials (from environment)
    SUPABASE_URL: str = "https://zbvlzsxlxjbmqqlbdhed.supabase.co"
    DATABASE_URL: str = "postgresql://postgres:Deepak8431%2A%2A%23%23%40%40@db.zbvlzsxlxjbmqqlbdhed.supabase.co:5432/postgres"
    SUPABASE_SECRET_KEY: str = ""
    SUPABASE_JWT_SECRET: str = ""
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()

