from langchain import hub

AGENT_PROMPT = hub.pull("x-05/react-chat-history")

CHARACTERISCT_PARSER_PROMPT = """
De acordo com a resposta recebida, refaça a mensagem com as mesmas informações, no entanto, escreva ela de acordo com as características fornecidas.

Resposta:

<resposta>
{response}
</resposta>

Características:

<características>
{characteristics}
</características>
"""