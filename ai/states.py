from typing import Annotated, TypedDict


class State(TypedDict):
    model_physics_characteristics: Annotated[str, "Características físicas da pesssoa"]
    model_info: Annotated[str, "Características emocionais, de personalidade e comportamentais da pesssoa"]
    chat_history: Annotated[list, "Histórico de mensagens"]
    agent_response: Annotated[str, "Resposta do agente"]
    final_response: Annotated[str, "Resposta do agente com a devida escrita de acordo com as características emocionais da descrição da pessoa"]
