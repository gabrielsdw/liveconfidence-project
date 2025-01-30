from typing import Annotated, TypedDict


class State(TypedDict):
    characteristics_emotionals: Annotated[str, "Características emocionais, de personalidade e comportamentais da pesssoa"]
    characteristics_fisics: Annotated[str, "Características físicas da pesssoa"]
    chat_history: Annotated[list, "Histórico de mensagens"]
    agent_response: Annotated[str, "Resposta do agente"]
    final_response: Annotated[str, "Resposta do agente com a devida escrita de acordo com as características emocionais e físicas"]
