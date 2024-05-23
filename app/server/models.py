from pydantic import BaseModel, Field
from typing import List

class GenerateAnswer(BaseModel):
    answer: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "answer": "This is an example",
            }
        }

class ChatBotModel(BaseModel):
    id:str
    answer: str
    response: str
   
def ResponseModel(data: List[ChatBotModel], message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
