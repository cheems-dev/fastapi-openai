from fastapi import APIRouter, HTTPException
from app.server.models import GenerateAnswer,ResponseModel
from app.config.open_ai import openai_client
from app.config.database import chatbox_collection
import json

router = APIRouter()

@router.post("/chatbot")
async def create_answer(chatbot: GenerateAnswer):
    try:
        response =  openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": chatbot.answer},
            ]
        )
        
        answer_content = response.choices[0].message.content
        
        payload = {
            "answer":  answer_content,
            "question": chatbot.answer
        }

        response = await chatbox_collection.insert_one(payload)
        return response["inserted_id"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def chatbot_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "answer": student["answer"],
        "question": student["question"],
    }

@router.get("/chatbot")
async def get_all_answers():
    try:
        chatbot_array = []
        async for item in chatbox_collection.find():
            chatbot_array.append(chatbot_helper(item))
        return ResponseModel(chatbot_array, "Historial get all answers!")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))