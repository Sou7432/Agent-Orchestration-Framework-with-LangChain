from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools import tools
from memory import memory
from prompts import SYSTEM_PROMPT       
import os
from dotenv import load_dotenv

load_dotenv()

def create_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,

        
        system_message=SYSTEM_PROMPT
        
    )

    return agent
