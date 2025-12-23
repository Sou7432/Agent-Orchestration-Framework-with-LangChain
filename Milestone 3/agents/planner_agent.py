from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from memory.individual_memory import create_memory
import os
from dotenv import load_dotenv

load_dotenv()

def create_planner_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = PromptTemplate(
        input_variables=["task"],
        template="Create a clear step-by-step plan for the following task:\n{task}"
    )

    memory = create_memory()

    return LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=True
    )
