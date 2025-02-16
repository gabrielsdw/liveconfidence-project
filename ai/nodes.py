from langchain_core.messages import HumanMessage, SystemMessage
from .states import ChatbotState
from .utils import format_chat_history
from . import prompts, chains
import json

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

def message_splitter_node(state: ChatbotState) -> dict:
    chain = chains.message_splitter_chain

    message = f"""
    <Mensagem>
    {str(state['final_response'])}
    </Mensagem>
    """

    messages = [
        SystemMessage(
            content=prompts.MESSAGE_SPLITTER_PROMPT
        ),
        HumanMessage(
            content=message
        )
    ]
    response = chain.invoke(messages)
    print(response)
    try:
        json_response = json.loads(str(response))
        return {'splitted_final_response': json_response.get('messages')}
    except:
        return {'splitted_final_response': {'messages': []}}
