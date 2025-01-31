from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from . import llms, prompts

characteristic_parser_chain = llms.GPT4o | StrOutputParser()

agent_prompt_template = prompts.AGENT_PROMPT
agent_chain = llms.GPT4o | agent_prompt_template | StrOutputParser()
