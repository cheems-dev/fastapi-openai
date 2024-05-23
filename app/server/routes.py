from fastapi import APIRouter, HTTPException
from app.server.models import GenerateAnswer,ResponseModel
from app.config.open_ai import openai_client
from app.config.database import chatbox_collection

router = APIRouter()

def chatbot_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "answer": student["answer"],
        "question": student["question"],
    }

@router.post("/chatbot", summary="Generate an answer using OpenAI")
async def create_answer(chatbot: GenerateAnswer):
    """
    Crea una respuesta utilizando OpenAI y la almacena en la base de datos.

    Parameters:
    - chatbot: Objeto de tipo GenerateAnswer que contiene la pregunta para generar una respuesta.

    Returns:
    - Respuesta: Objeto de tipo ResponseModel que contiene la respuesta generada y la pregunta asociada.
    """
    try:
        # Genera una respuesta utilizando OpenAI
        response =  openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": chatbot.answer},
            ]
        )
        
         # Obtiene el contenido de la respuesta generada
        answer_content = response.choices[0].message.content
        
        payload = {
            "answer":  answer_content,
            "question": chatbot.answer
        }

        # Inserta los datos en la colección de la base de datos
        response = await chatbox_collection.insert_one(payload)
        # Busca la respuesta recién insertada en la base de datos
        chatbot_find = await chatbox_collection.find_one({"_id": response.inserted_id})
        # Devuelve la respuesta
        return ResponseModel(chatbot_helper(chatbot_find), "Create new collection")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/chatbot", summary="Get all conversation messages")
async def get_all_answers():
    """
    Obtiene todos los mensajes de la conversación almacenados en la base de datos.

    Returns:
    - Respuesta: Objeto de tipo ResponseModel que contiene todos los mensajes de la conversación.
    """

    try:
        chatbot_array = []
        # Itera sobre todos los documentos en la colección de la base de datos
        async for item in chatbox_collection.find():
            chatbot_array.append(chatbot_helper(item))

        if chatbot_array:
            # Devuelve todos los mensajes de la conversación
            return ResponseModel(chatbot_array, "Get all collections")
        else: 
            return ResponseModel(chatbot_array, "Collections is empty.")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))