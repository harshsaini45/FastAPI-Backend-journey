# settings.py
# Purpose:
# .env ki values ko Python/FastAPI me safely access karne ke liye Settings banate hain.
# BaseSettings → .env ki settings ko Python mein lane ke liye
# SettingsConfigDict → batane ke liye ki .env file kahan hai aur uske saath kya behavior rakhna hai.
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
      # Pydantic ko bataya ki settings .env file se leni hain
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
       # .env se DB_CONNECTION ki value read hogi
    DB_CONNECTION:str
    SECRET_KEY:str
    ALGORITHM:str
    EXP_TIME:int
    
    
    
settings=Settings()