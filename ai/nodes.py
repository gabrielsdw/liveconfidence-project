from langchain_core.messages import HumanMessage, SystemMessage
from langchain.agents import AgentExecutor, create_react_agent
from .states import ChatbotState
from .utils import get_tools, format_chat_history
from . import llms, prompts, chains


def agent_node(state: ChatbotState) -> dict:
    tools = get_tools()

    agent = create_react_agent(llms.GPT4o, tools, prompts.AGENT_PROMPT)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )
    
    chat_history = state["chat_history"]
    
    input = chat_history.pop()

    try: 
        response = agent_executor.invoke({
            "chat_history": chat_history,
            "input": input,
        })

        return {"agent_response": response.get('output')}

    except (ValueError) as e:
        return {"agent_response": "Resposta sexual, apenas continue a conversa e ignore"}
            
def characteristics_parser_node(state: ChatbotState) -> dict:
    chain = chains.characteristic_parser_chain

    formatted_prompt = prompts.CHARACTERISCT_PARSER_PROMPT.format(
        response=state['agent_response'],
        model_info=state['model_info'],
        model_physics_characteristics=state['model_physics_characteristics'],
        chat_history=format_chat_history(state['chat_history'])
    )
    print("------------------------------ PROMPT FORMATADO ------------------------------")
    print(formatted_prompt)
    print("------------------------------ END PROMPT ------------------------------")
    print('\n'*5)

    response = chain.invoke(formatted_prompt)
    return {"final_response": response}

def test_node(state: ChatbotState) -> dict:
    chain = chains.test_chain

    chat_history = f"""
    <Histórico de conversas>
    {format_chat_history(state['chat_history'])}
    </Histórico de conversas>    
    """


    messages = [
        SystemMessage(
            content=prompts.TEST_PROMPT
        ),
        HumanMessage(
            content=chat_history
        )
    ]
    print(messages)

    response = chain.invoke(messages)
    print(response)
    return {'final_response': response}
