from openai import OpenAI
from .settings import settings

openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)