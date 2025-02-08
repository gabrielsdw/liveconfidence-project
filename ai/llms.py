from django.conf import settings
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

GPT4o = ChatOpenAI(model='gpt-4o', temperature=0.0, api_key=settings.OPENAI_API_KEY)

GPT4o_WITH_TEMPERATURE = ChatOpenAI(model='gpt-4o', temperature=0.4, api_key=settings.OPENAI_API_KEY)
