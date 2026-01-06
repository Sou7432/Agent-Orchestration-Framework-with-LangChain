from agents.researcher_agent import create_researcher
from agents.summarizer_agent import create_summarizer
from agents.email_agent import create_email_agent


def run_workflow(topic, recipient):
    researcher = create_researcher()
    summarizer = create_summarizer()
    email_agent = create_email_agent()

    research = researcher(topic)
    summary = summarizer(research)
    email = email_agent(summary, recipient)

    return research, summary, email
