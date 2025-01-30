from langgraph.graph import StateGraph, END, START
from . import nodes, states

class ChatBotWorkflow:

    def __init__(self) -> None:
        self._workflow =  StateGraph(states.State)
   
    def _create_workflow(self) -> None:
        self._workflow.add_node('agent', nodes.agent_node)
        self._workflow.add_node('characteristic_parser', nodes.characteristics_parser_node)
        
        self._workflow.add_edge(START, 'agent')
        self._workflow.add_edge('agent', 'characteristic_parser')
        self._workflow.add_edge('characteristic_parser', END)
        
        # self._workflow.set_entry_point('agent')
        
    def _get_workflow(self) -> StateGraph:
        self._create_workflow()
        return self._workflow.compile()

    def run(self, data: dict) -> str:
        return self._get_workflow().invoke(data)
    

if __name__ == '__main__':

    workflow = ChatBotWorkflow()

    chat_history = ["Modelo: Olá, tudo bem?", "Cliente: Olá, quero fazer uma chamada. Como posso pagar?"]

    characteristics_emotionals = """
    Oi, meu nome é Clarice, tenho 24 anos e sou de Balneario camburiu. Tenho 167 de altura, meu corpo é magrinho como de uma modelo. Meus cabelos são morenos, meus olhos são verdes e meu olhar é cativante. Minha pele é branquinha, meus lábios são carnudos e meu sorriso é lindo. Tenho um jeito brincalona e meio ciumenta, sempre alegre.
    No meu tempo livre, adoro ler, principalmente estudar. Gosto de me vestir no jeito classico e sempre escolho vestidos.
    Se tem algo que me define, é meu corpo. Sou do tipo que gosta de ajudar todo mundo, e adoro carinho e um pouquinho de safadesa haha. Estou aqui para te satisfazer e prometo que, depois de me conhecer, você não vai me esquecer tão cedo. Quer saber mais sobre mim?
    """ 

    characteristics_fisics = """
        Olho azul
        Cabelo Rosa
    """

    response = workflow.run({
        "chat_history": chat_history,
        "characteristics_emotionals": characteristics_emotionals,
        "characteristics_fisics": characteristics_fisics,
    })
    print("FINAL RESPONSE\n")
    # print(response['final_response'])
    """  messages = [msg for msg in response['final_response'].split("\n")]
    for message in messages:
        print(message)
    """
