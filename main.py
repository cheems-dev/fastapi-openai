from fastapi import FastAPI
from app.server.routes import router as chatbot_router

app = FastAPI()

app.include_router(chatbot_router, tags=["Chatbot"], prefix="/api")