import os
from dotenv import load_dotenv
from pathlib import Path

env_patch= Path(".")/ ".env"
load_dotenv(dotenv_path=env_patch)

class Settings: 
    MONGODB_URL:str = os.getenv("MONGODB_URL")
    OPENAI_API_KEY:str = os.getenv("OPENAI_API_KEY")

settings = Settings()