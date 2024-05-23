import os
from dotenv import load_dotenv
from pathlib import Path

# Carga las variables de entorno desde el archivo .env en el directorio actual
env_patch= Path(".")/ ".env"
load_dotenv(dotenv_path=env_patch)

class Settings: 
    """
    Clase que contiene las configuraciones del sistema.
    """

    MONGODB_URL:str = os.getenv("MONGODB_URL")
    """
    URL de conexión a la base de datos MongoDB obtenida desde las variables de entorno.
    """

    OPENAI_API_KEY:str = os.getenv("OPENAI_API_KEY")
    """
    Clave de API de OpenAI obtenida desde las variables de entorno.
    """
    
settings = Settings()