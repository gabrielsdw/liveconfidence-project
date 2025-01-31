from langchain.agents import AgentExecutor, create_react_agent
from .states import ChatbotState
from .utils import get_tools
from . import llms, prompts, chains

def agent_node(state: ChatbotState) -> dict:
    tools = get_tools()

    agent = create_react_agent(llms.GPT4o, tools, prompts.AGENT_PROMPT)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    chat_history = state["chat_history"]
    
    input = chat_history.pop()

    response = agent_executor.invoke({
        "chat_history": chat_history,
        "input": input,
    })
    return {"agent_response": response.get('output')}

def characteristics_parser_node(state: ChatbotState) -> dict:
    chain = chains.characteristic_parser_chain

    formatted_prompt = prompts.CHARACTERISCT_PARSER_PROMPT.format(
        response=state['agent_response'],
        model_info=state['model_info'],
        model_physics_characteristics=state['model_physics_characteristics']
    )
    print("------------------------------ PROMPT FORMATADO ------------------------------")
    print(formatted_prompt)
    print("------------------------------ END PROMPT ------------------------------")
    print('\n'*5)

    response = chain.invoke(formatted_prompt)
    return {"final_response": response}
