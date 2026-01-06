import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def create_email_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    def run(summary, recipient):
        final_prompt = f"""
Write a professional email to {recipient}
based on the following information:

{summary}
"""
        return llm.invoke(final_prompt).content

    return run
