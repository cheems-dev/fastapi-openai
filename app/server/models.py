from pydantic import BaseModel, Field

class GenerateAnswer(BaseModel):
    """
    Container for a single value.
    """
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
   
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
