from langchain_core.messages import HumanMessage, SystemMessage
from .schemas import MostMessagesResponse
from .states import ChatbotState
from .utils import format_chat_history, format_dict
from . import llms, prompts, chains

def chatbot_node(state: ChatbotState) -> dict:
    chain = chains.chatbot_chain

    chat_history = f"""
    <Histórico de conversas>
    {format_chat_history(state['chat_history'])}
    </Histórico de conversas>    
    """

    system_prompt = prompts.CHATBOT_PROMPT_2.format(
        model_physics_characteristics=state['model_physics_characteristics'],
        model_info=state['model_info']
    )
    print(system_prompt)
    print(chat_history)
    messages = [
        SystemMessage(
            content=system_prompt
        ),
        HumanMessage(
            content=chat_history
        )
    ]
    response = chain.invoke(messages)
    return {'final_response': response}

def response_splitter_node(state: ChatbotState) -> dict:
    structured_llm = llms.GPT4o.with_structured_output(MostMessagesResponse)

    human_message = f"""
    <mensagem>
    f{state['final_response']}
    </mensagem>
    """

    messages = [
        SystemMessage(
            content="""
                Responda SEMPRE no formato JSON.  
                Sua resposta deve conter apenas um objeto JSON com a chave `"ai_splitted_response"`, que deve ser uma lista simples de strings.  

                Formato esperado:  
                ```json
                {
                    "ai_splitted_response": [
                        "Mensagem 1",
                        "Mensagem 2",
                        "Mensagem 3"
                    ]
                }

                Regras:
                - Se a mensagem for curta e clara, mantenha-a como está.
                - Se a mensagem for muito longa, divida-a em partes menores para melhorar a legibilidade, sem modificar o conteúdo.
                - Preserve o sentido original das frases ao dividir.
                - Não adicione outras chaves ou estruturas aninhadas.
                - Apenas devolva um JSON válido seguindo esse formato.
            """
        ),
        HumanMessage(
            content= human_message
        )
    ]
    response = structured_llm.invoke(messages)
    return {'splitted_response': response}
