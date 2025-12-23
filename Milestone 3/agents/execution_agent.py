from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from memory.individual_memory import create_memory
import os
from dotenv import load_dotenv

load_dotenv()

def create_execution_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = PromptTemplate(
        input_variables=["plan"],
        template="Execute the following plan step by step:\n{plan}"
    )

    memory = create_memory()

    return LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=True
    )
