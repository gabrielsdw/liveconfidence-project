from langgraph.graph import StateGraph, END, START
from . import nodes, states


class ChatBotWorkflow:

    def __init__(self) -> None:
        self._workflow =  StateGraph(states.ChatbotState)

    def _add_nodes(self) -> None:
        self._workflow.add_node('chatbot', nodes.chatbot_node)
        self._workflow.add_node('response_splitter', nodes.response_splitter_node)

    def _add_edges(self) -> None:
        self._workflow.add_edge(START, 'chatbot'),
        self._workflow.add_edge('chatbot', END)
        
    def _create_workflow(self) -> None:
        self._add_nodes()
        self._add_edges()

    def _get_workflow(self) -> StateGraph:
        self._create_workflow()
        return self._workflow.compile()

    def run(self, data: dict) -> str:
        return self._get_workflow().invoke(data)
