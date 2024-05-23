import motor.motor_asyncio
from .settings import settings

# Obtiene la URL de conexión a MongoDB desde las configuraciones
mongodb_url = settings.MONGODB_URL

# Comprueba si la URL de MongoDB está definida en las variables de entorno
if not mongodb_url:
    raise ValueError("MONGODB_URL environment variable not set")

# Crea un cliente motor asíncrono de MongoDB utilizando la URL de conexión
client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url)

# Obtiene la base de datos y la colección del cliente MongoDB
database = client.get_database("test")
chatbox_collection = database.get_collection("store-chatbot")


