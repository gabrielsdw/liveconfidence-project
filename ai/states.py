from typing import Annotated, TypedDict


class ChatbotState(TypedDict):
    model_physics_characteristics: Annotated[str, "Características físicas de uma pessoa"]
    model_info: Annotated[str, "Características emocionais, de personalidade e comportamentais de uma pesssoa"]
    chat_history: Annotated[list, "Histórico de mensagens"]
    final_response: Annotated[str, "Resposta final"]
    splitted_final_response: Annotated[list[str], "Resposta final quebrada em mensagens se necessário"]
    