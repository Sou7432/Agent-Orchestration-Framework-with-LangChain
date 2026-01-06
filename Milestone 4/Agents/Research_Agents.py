import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def create_researcher():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    def run(prompt):
        final_prompt = f"Research this topic in detail:\n\n{prompt}"
        return llm.invoke(final_prompt).content

    return run
