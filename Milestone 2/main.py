# main.py

from agents import create_agent

agent = create_agent()

print("LangChain Agent is ready!")
print("Type 'exit' to quit.")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    response = agent.run(query)
    print("Agent:", response)
