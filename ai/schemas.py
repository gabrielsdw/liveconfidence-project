from langchain_core.pydantic_v1 import BaseModel, Field


class MostMessagesResponse(BaseModel):
    messages: list =  Field(description="Lista de mensagens separadas")
