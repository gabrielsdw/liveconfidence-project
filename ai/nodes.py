from langchain.agents import AgentExecutor, create_react_agent
from .states import State
from .utils import get_tools
from . import llms, prompts, chains

def agent_node(state: State) -> dict:
    tools = get_tools()

    agent = create_react_agent(llms.GPT, tools, prompts.AGENT_PROMPT)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    chat_history = state["chat_history"]
    
    input = chat_history.pop()

    response = agent_executor.invoke({
        "chat_history": chat_history,
        "input": input,
    })
    return {"agent_response": response.get('output')}

def characteristics_parser_node(state: State) -> dict:
    chain = chains.characteristic_parser_chain

    formatted_prompt = prompts.CHARACTERISCT_PARSER_PROMPT.format(
        response=state['agent_response'],
        characteristics=state['characteristics_emotionals']
    )
    response = chain.invoke(formatted_prompt)
    return {"final_response": response}
    


if __name__ == "__main__":

    chat_history = [
        "Modelo: Olá, tudo bem?",
        "Cliente: Sim, gata"
    ]
    """chat_history = [
        "Modelo: Olá, tudo bem?",
        "Cliente: Olá, quero fazer uma chamada. Como posso pagar?",
        "Modelo: Você pode pagar através deste link: www.mercadopago/payment/sdw123.",
        "Sistema: Pagamento efetuado com sucesso.",
    ]
    """
    characteristics = """
    Oi, meu nome é Clarice, tenho 24 anos e sou de Balneario camburiu. Tenho 167 de altura, meu corpo é magrinho como de uma modelo. Meus cabelos são morenos, meus olhos são verdes e meu olhar é cativante. Minha pele é branquinha, meus lábios são carnudos e meu sorriso é lindo. Tenho um jeito brincalona e meio ciumenta, sempre alegre.
    No meu tempo livre, adoro ler, principalmente estudar. Gosto de me vestir no jeito classico e sempre escolho vestidos.
    Se tem algo que me define, é meu corpo. Sou do tipo que gosta de ajudar todo mundo, e adoro carinho e um pouquinho de safadesa haha. Estou aqui para te satisfazer e prometo que, depois de me conhecer, você não vai me esquecer tão cedo. Quer saber mais sobre mim?
    """

    state = State(chat_history=chat_history, characteristics_emotionals=characteristics)
