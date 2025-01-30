from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from decouple import config
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_FILE = os.path.join(BASE_DIR, ".env")

GPT = ChatOpenAI(model='gpt-4o', temperature=0.0, api_key=config("OPENAI_API_KEY"))


if __name__ == "__main__":
    chain = GPT | StrOutputParser()
    print(chain.invoke("Opa, eae fi bão?"))
