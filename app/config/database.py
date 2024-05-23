import motor.motor_asyncio
from .settings import settings


mongodb_url = settings.MONGODB_URL
print(mongodb_url)
if not mongodb_url:
    raise ValueError("MONGODB_URL environment variable not set")

client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url)
database = client.get_database("test")
chatbox_collection = database.get_collection("store-chatbot")


