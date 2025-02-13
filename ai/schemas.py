from pydantic import BaseModel, Field


class MostMessagesResponse(BaseModel):
    messages: list =  Field(description="Lista de mensagens separadas")
