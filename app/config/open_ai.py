from openai import OpenAI
from .settings import settings

# Inicializa un cliente de OpenAI utilizando la clave de API obtenida de las configuraciones
openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)