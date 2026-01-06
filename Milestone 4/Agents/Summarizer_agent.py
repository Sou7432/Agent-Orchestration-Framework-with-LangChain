import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def create_summarizer():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    def run(text):
        final_prompt = f"Summarize this clearly and concisely:\n\n{text}"
        return llm.invoke(final_prompt).content

    return run
