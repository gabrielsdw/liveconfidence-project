from django.conf import settings
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

GPT4o = ChatOpenAI(model='gpt-4o', temperature=0.0, api_key=settings.OPENAI_API_KEY)

GPT4o_WITH_TEMPERATURE = ChatOpenAI(model='gpt-4o', temperature=0.2, api_key=settings.OPENAI_API_KEY)

GPT4o_MINI = ChatOpenAI(model='gpt-4o-mini', temperature=0.0, api_key=settings.OPENAI_API_KEY)