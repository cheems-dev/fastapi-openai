from fastapi import APIRouter, HTTPException
from app.server.models import GenerateAnswer,ResponseModel
from app.config.open_ai import openai_client
from app.config.database import chatbox_collection
import json

router = APIRouter()

def chatbot_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "answer": student["answer"],
        "question": student["question"],
    }

@router.post("/chatbot", response_model=ResponseModel, summary="Generate an answer using OpenAI")
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
        chatbot_find = await chatbox_collection.find_one({"_id": response.inserted_id})
        return ResponseModel(chatbot_helper(chatbot_find), "Create new collection")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/chatbot", response_model=ResponseModel, summary="Get all conversation messages")
async def get_all_answers():
    try:
        chatbot_array = []
        async for item in chatbox_collection.find():
            chatbot_array.append(chatbot_helper(item))

        if chatbot_array: 
            return ResponseModel(chatbot_array, "Get all collections")
        else: 
            return ResponseModel(chatbot_array, "Collections is empty.")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))