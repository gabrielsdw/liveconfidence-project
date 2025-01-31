from langgraph.graph import StateGraph, END, START
from . import nodes, states


class ChatBotWorkflow:

    def __init__(self) -> None:
        self._workflow =  StateGraph(states.ChatbotState)
   
    def _create_workflow(self) -> None:
        self._workflow.add_node('agent', nodes.agent_node)
        self._workflow.add_node('characteristic_parser', nodes.characteristics_parser_node)
        
        self._workflow.add_edge(START, 'agent')
        self._workflow.add_edge('agent', 'characteristic_parser')
        self._workflow.add_edge('characteristic_parser', END)
        
    def _get_workflow(self) -> StateGraph:
        self._create_workflow()
        return self._workflow.compile()

    def run(self, data: dict) -> str:
        return self._get_workflow().invoke(data)
