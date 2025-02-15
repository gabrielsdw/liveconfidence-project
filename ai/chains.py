from langchain_core.output_parsers import StrOutputParser
from . import llms

chatbot_chain = llms.GPT4o | StrOutputParser()

message_splitter_chain = llms.GPT4o_MINI | StrOutputParser()